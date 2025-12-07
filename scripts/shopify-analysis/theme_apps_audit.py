"""Audit theme, apps, and scripts for performance impact."""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional

import httpx

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

from auth import create_graphql_client, execute_graphql_query
from query_apps import query_installed_apps, format_apps_data
from query_theme import query_theme_info, format_theme_data


def load_query(query_name: str) -> str:
    """Load a GraphQL query from the queries directory."""
    script_dir = Path(__file__).parent
    query_path = script_dir / "queries" / f"{query_name}.graphql"
    
    if not query_path.exists():
        raise FileNotFoundError(f"Query file not found: {query_path}")
    
    return query_path.read_text()


def analyze_page_scripts(url: str) -> Dict:
    """
    Analyze scripts loaded on a page using regex (no BeautifulSoup required).
    
    Args:
        url: URL to analyze.
    
    Returns:
        Dictionary containing script analysis.
    """
    try:
        response = httpx.get(url, timeout=30.0, follow_redirects=True)
        response.raise_for_status()
        html_content = response.text
        
        # Find head section
        head_match = re.search(r'<head[^>]*>(.*?)</head>', html_content, re.IGNORECASE | re.DOTALL)
        head_content = head_match.group(1) if head_match else ""
        head_end_pos = head_match.end() if head_match else 0
        
        scripts_in_head = []
        scripts_in_body = []
        blocking_scripts = []
        async_scripts = []
        defer_scripts = []
        external_scripts = []
        inline_scripts = []
        
        # Find all script tags
        script_pattern = r'<script([^>]*)>(.*?)</script>|<script([^>]*)/>'
        for script_match in re.finditer(script_pattern, html_content, re.IGNORECASE | re.DOTALL):
            script_attrs = script_match.group(1) or script_match.group(3) or ""
            script_content = script_match.group(2) or ""
            script_pos = script_match.start()
            
            # Parse attributes
            src_match = re.search(r'src=["\']([^"\']+)["\']', script_attrs, re.IGNORECASE)
            src = src_match.group(1) if src_match else ""
            is_async = "async" in script_attrs.lower()
            is_defer = "defer" in script_attrs.lower()
            is_inline = not src and script_content.strip()
            type_match = re.search(r'type=["\']([^"\']+)["\']', script_attrs, re.IGNORECASE)
            script_type = type_match.group(1) if type_match else "text/javascript"
            
            script_info = {
                "src": src or "inline",
                "async": is_async,
                "defer": is_defer,
                "type": script_type,
                "inline": is_inline,
                "size": len(script_content) if script_content else 0,
            }
            
            # Determine location
            in_head = script_pos < head_end_pos
            if in_head:
                scripts_in_head.append(script_info)
            else:
                scripts_in_body.append(script_info)
            
            # Categorize
            if is_inline:
                inline_scripts.append(script_info)
            else:
                external_scripts.append(script_info)
            
            if is_async:
                async_scripts.append(script_info)
            elif is_defer:
                defer_scripts.append(script_info)
            else:
                # Blocking script (no async, no defer)
                blocking_scripts.append(script_info)
        
        # Find all link tags
        stylesheets = []
        preloads = []
        fonts = []
        
        link_pattern = r'<link([^>]*)/?>'
        for link_match in re.finditer(link_pattern, html_content, re.IGNORECASE):
            link_attrs = link_match.group(1)
            
            rel_match = re.search(r'rel=["\']([^"\']+)["\']', link_attrs, re.IGNORECASE)
            rel = rel_match.group(1).lower() if rel_match else ""
            href_match = re.search(r'href=["\']([^"\']+)["\']', link_attrs, re.IGNORECASE)
            href = href_match.group(1) if href_match else ""
            media_match = re.search(r'media=["\']([^"\']+)["\']', link_attrs, re.IGNORECASE)
            media = media_match.group(1) if media_match else "all"
            as_match = re.search(r'as=["\']([^"\']+)["\']', link_attrs, re.IGNORECASE)
            link_as = as_match.group(1) if as_match else ""
            type_match = re.search(r'type=["\']([^"\']+)["\']', link_attrs, re.IGNORECASE)
            link_type = type_match.group(1) if type_match else ""
            
            if "stylesheet" in rel:
                stylesheets.append({"href": href, "media": media})
            elif "preload" in rel:
                preloads.append({"href": href, "as": link_as, "type": link_type})
            elif "preconnect" in rel or "dns-prefetch" in rel:
                if "fonts" in href or "gstatic" in href:
                    fonts.append({"href": href, "rel": rel})
        
        return {
            "total_scripts": len(scripts_in_head) + len(scripts_in_body),
            "scripts_in_head": len(scripts_in_head),
            "scripts_in_body": len(scripts_in_body),
            "blocking_scripts": len(blocking_scripts),
            "async_scripts": len(async_scripts),
            "defer_scripts": len(defer_scripts),
            "external_scripts": len(external_scripts),
            "inline_scripts": len(inline_scripts),
            "blocking_scripts_detail": blocking_scripts[:10],
            "stylesheets": len(stylesheets),
            "preloads": len(preloads),
            "font_preconnects": len(fonts),
            "script_details": {
                "head": scripts_in_head[:20],
                "body": scripts_in_body[:20],
            },
        }
    except Exception as e:
        return {"error": str(e)}


def identify_app_scripts(apps: List[Dict], script_analysis: Dict) -> Dict:
    """
    Identify which scripts belong to which apps.
    
    Args:
        apps: List of installed apps.
        script_analysis: Script analysis from page.
    
    Returns:
        Dictionary mapping apps to their scripts.
    """
    app_scripts = {}
    
    # Common app patterns
    app_patterns = {
        "google-analytics": ["google-analytics", "gtag", "ga.js", "analytics.js"],
        "facebook-pixel": ["facebook", "fbq", "connect.facebook.net"],
        "shopify-analytics": ["trekkie", "shopify", "analytics.shopify"],
        "reputon": ["reputon", "reviews"],
    }
    
    # Match apps by name/handle
    for app in apps:
        app_name = app.get("name", "").lower()
        app_handle = app.get("handle", "").lower()
        
        scripts_found = []
        
        # Check blocking scripts
        for script in script_analysis.get("blocking_scripts_detail", []):
            src = script.get("src", "").lower()
            
            # Check if script matches app name or handle
            if app_name in src or app_handle in src:
                scripts_found.append(script)
            
            # Check common patterns
            for pattern_name, patterns in app_patterns.items():
                if any(pattern in src for pattern in patterns):
                    if pattern_name not in app_scripts:
                        app_scripts[pattern_name] = []
                    app_scripts[pattern_name].append(script)
        
        if scripts_found:
            app_scripts[app.get("name", "Unknown")] = scripts_found
    
    return app_scripts


def audit_theme_apps_scripts(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
    storefront_url: str = "https://farmaciasmacross.com.mx",
) -> Dict:
    """
    Perform comprehensive audit of theme, apps, and scripts.
    
    Args:
        shop_domain: Shop domain. If None, reads from environment.
        access_token: Access token. If None, reads from environment.
        storefront_url: Public storefront URL to analyze.
    
    Returns:
        Dictionary containing comprehensive audit results.
    """
    print("🔍 Auditing theme, apps, and scripts...")
    
    # Try to query theme and apps, but continue if API access is not available
    theme_formatted = None
    apps = []
    
    try:
        print("  Querying theme information...")
        theme_data = query_theme_info(shop_domain, access_token)
        theme_formatted = format_theme_data(theme_data)
    except Exception as e:
        print(f"  ⚠️  Could not query theme (API access required): {e}")
        theme_formatted = {
            "published_theme": {
                "name": "Unknown (API access required)",
                "id": None,
            },
        }
    
    try:
        print("  Querying installed apps...")
        apps_data = query_installed_apps(shop_domain, access_token)
        apps = format_apps_data(apps_data)
    except Exception as e:
        print(f"  ⚠️  Could not query apps (API access required): {e}")
        apps = []
    
    # Analyze scripts on homepage
    print("  Analyzing scripts on homepage...")
    script_analysis = analyze_page_scripts(storefront_url)
    
    # Identify app scripts
    print("  Identifying app scripts...")
    app_scripts = identify_app_scripts(apps, script_analysis)
    
    # Calculate performance impact
    performance_impact = {
        "blocking_scripts_count": script_analysis.get("blocking_scripts", 0),
        "total_scripts": script_analysis.get("total_scripts", 0),
        "blocking_ratio": (
            script_analysis.get("blocking_scripts", 0)
            / script_analysis.get("total_scripts", 1)
            if script_analysis.get("total_scripts", 0) > 0
            else 0
        ),
        "recommendation": (
            "Critical"
            if script_analysis.get("blocking_scripts", 0) > 10
            else "High"
            if script_analysis.get("blocking_scripts", 0) > 5
            else "Medium"
            if script_analysis.get("blocking_scripts", 0) > 2
            else "Low"
        ),
    }
    
    # Identify potential conflicts
    conflicts = []
    
    # Check for multiple analytics tools
    analytics_apps = [
        app for app in apps
        if any(
            keyword in app.get("name", "").lower()
            for keyword in ["analytics", "tracking", "pixel", "tag manager"]
        )
    ]
    
    if len(analytics_apps) > 1:
        conflicts.append({
            "type": "multiple_analytics",
            "severity": "medium",
            "description": f"Multiple analytics tools detected: {', '.join([a['name'] for a in analytics_apps])}",
            "apps": [a["name"] for a in analytics_apps],
        })
    
    # Check for apps with many scopes
    high_scope_apps = [
        app for app in apps if len(app.get("granted_scopes", [])) > 10
    ]
    
    if high_scope_apps:
        conflicts.append({
            "type": "high_permissions",
            "severity": "low",
            "description": "Apps with high number of permissions detected",
            "apps": [
                {
                    "name": app["name"],
                    "scopes_count": len(app.get("granted_scopes", [])),
                }
                for app in high_scope_apps
            ],
        })
    
    theme_info = theme_formatted.get("published_theme", {}) if theme_formatted else {}
    
    return {
        "audit_date": theme_formatted.get("shop", {}).get("name") if theme_formatted else None,
        "theme": {
            "name": theme_info.get("name", "Unknown (API access required)"),
            "id": theme_info.get("id"),
            "created_at": theme_info.get("created_at"),
            "updated_at": theme_info.get("updated_at"),
            "theme_store_id": theme_info.get("theme_store_id"),
        },
        "apps": {
            "total": len(apps),
            "list": apps,
            "by_category": {},
            "total_monthly_cost": sum(
                float(re.findall(r"[\d.]+", app.get("pricing", "0"))[0])
                if re.findall(r"[\d.]+", app.get("pricing", "0"))
                else 0
                for app in apps
            ),
        },
        "scripts": script_analysis,
        "app_scripts_mapping": app_scripts,
        "performance_impact": performance_impact,
        "conflicts": conflicts,
        "recommendations": [
            {
                "priority": "high",
                "action": "Convert blocking scripts to async/defer",
                "impact": "Reduce Time to Interactive (TTI)",
                "scripts_count": script_analysis.get("blocking_scripts", 0),
            },
            {
                "priority": "medium",
                "action": "Consolidate analytics tools",
                "impact": "Reduce script overhead",
                "apps_affected": len(analytics_apps),
            },
            {
                "priority": "low",
                "action": "Review app permissions",
                "impact": "Security and performance",
                "apps_affected": len(high_scope_apps),
            },
        ],
    }


def main():
    """Main function to run theme/apps/scripts audit."""
    try:
        storefront_url = "https://farmaciasmacross.com.mx"
        
        audit_results = audit_theme_apps_scripts(storefront_url=storefront_url)
        
        # Save to JSON
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "theme_apps_analysis.json"
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(audit_results, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Audit complete!")
        print(f"✓ Results saved to: {output_file}")
        print(f"\nSummary:")
        print(f"  Theme: {audit_results['theme']['name']}")
        print(f"  Total Apps: {audit_results['apps']['total']}")
        print(f"  Total Scripts: {audit_results['scripts'].get('total_scripts', 0)}")
        print(f"  Blocking Scripts: {audit_results['scripts'].get('blocking_scripts', 0)}")
        print(f"  Performance Impact: {audit_results['performance_impact']['recommendation']}")
        
        if audit_results.get("conflicts"):
            print(f"\n⚠️  Conflicts detected: {len(audit_results['conflicts'])}")
            for conflict in audit_results["conflicts"]:
                print(f"  - {conflict['type']}: {conflict['description']}")
        
        return audit_results
    except Exception as e:
        print(f"❌ Error during audit: {e}")
        raise


if __name__ == "__main__":
    main()

