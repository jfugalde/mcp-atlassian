"""Generate comprehensive analysis report from all collected data."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def load_json_data(filename: str) -> Optional[Dict]:
    """Load JSON data from the analysis output directory."""
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent.parent / "docs" / "shopify-analysis"
    file_path = data_dir / filename
    
    if not file_path.exists():
        return None
    
    with open(file_path) as f:
        return json.load(f)


def generate_apps_section(apps_data: List[Dict]) -> str:
    """Generate markdown section for installed apps."""
    if not apps_data:
        return "## Installed Apps\n\nNo apps found or data not available.\n"
    
    section = "## Installed Apps\n\n"
    section += f"**Total Apps Installed:** {len(apps_data)}\n\n"
    section += "| App Name | Developer | Category | Pricing | Scopes |\n"
    section += "|----------|-----------|----------|---------|--------|\n"
    
    for app in apps_data:
        name = app.get("name", "Unknown")
        developer = app.get("developer", "Unknown")
        category = app.get("category", "N/A")
        pricing = app.get("pricing", "Free")
        scopes_count = len(app.get("granted_scopes", []))
        
        section += f"| {name} | {developer} | {category} | {pricing} | {scopes_count} |\n"
    
    section += "\n### App Details\n\n"
    for app in apps_data:
        section += f"#### {app.get('name', 'Unknown')}\n\n"
        section += f"- **Developer:** {app.get('developer', 'Unknown')}\n"
        section += f"- **Category:** {app.get('category', 'N/A')}\n"
        section += f"- **Pricing:** {app.get('pricing', 'Free')}\n"
        section += f"- **Published:** {app.get('published', False)}\n"
        section += f"- **Embedded:** {app.get('embedded', False)}\n"
        
        scopes = app.get("granted_scopes", [])
        if scopes:
            section += f"- **Granted Scopes:** {', '.join(scopes[:5])}"
            if len(scopes) > 5:
                section += f" (+{len(scopes) - 5} more)"
            section += "\n"
        
        subscriptions = app.get("subscriptions", [])
        if subscriptions:
            section += f"- **Active Subscriptions:** {len(subscriptions)}\n"
            for sub in subscriptions:
                section += f"  - {sub.get('name')} ({sub.get('status')})\n"
        
        section += "\n"
    
    return section


def generate_theme_section(theme_data: Dict) -> str:
    """Generate markdown section for theme information."""
    if not theme_data:
        return "## Theme Information\n\nTheme data not available.\n"
    
    section = "## Theme Information\n\n"
    
    shop = theme_data.get("shop", {})
    section += f"**Shop:** {shop.get('name', 'Unknown')}\n"
    section += f"**Domain:** {shop.get('primary_domain', 'N/A')}\n\n"
    
    published = theme_data.get("published_theme", {})
    if published.get("name"):
        section += f"**Published Theme:** {published.get('name')}\n"
        section += f"**Theme ID:** {published.get('id', 'N/A')}\n"
        if published.get("theme_store_id"):
            section += f"**Theme Store ID:** {published.get('theme_store_id')}\n"
        section += f"**Last Updated:** {published.get('updated_at', 'N/A')}\n"
    else:
        section += "**Published Theme:** None found\n"
    
    section += f"\n**Total Themes:** {theme_data.get('total_themes', 0)}\n"
    
    all_themes = theme_data.get("all_themes", [])
    if all_themes:
        section += "\n### All Themes\n\n"
        for theme in all_themes:
            section += f"- **{theme.get('name')}** ({theme.get('role')})\n"
    
    section += "\n"
    return section


def generate_store_config_section(store_data: Dict) -> str:
    """Generate markdown section for store configuration."""
    if not store_data:
        return "## Store Configuration\n\nStore configuration data not available.\n"
    
    section = "## Store Configuration\n\n"
    
    basic = store_data.get("basic_info", {})
    section += f"**Store Name:** {basic.get('name', 'Unknown')}\n"
    section += f"**Email:** {basic.get('email', 'N/A')}\n"
    section += f"**Domain:** {basic.get('primary_domain', 'N/A')}\n"
    section += f"**SSL Enabled:** {basic.get('ssl_enabled', False)}\n\n"
    
    plan = store_data.get("plan", {})
    section += f"**Plan:** {plan.get('display_name', 'Unknown')}\n"
    section += f"**Shopify Plus:** {plan.get('shopify_plus', False)}\n"
    section += f"**Partner Development:** {plan.get('partner_development', False)}\n\n"
    
    currency = store_data.get("currency", {})
    section += f"**Currency:** {currency.get('code', 'N/A')}\n"
    enabled_currencies = currency.get("enabled_presentment_currencies", [])
    if enabled_currencies:
        section += f"**Enabled Currencies:** {', '.join(enabled_currencies)}\n"
    section += "\n"
    
    features = store_data.get("features", {})
    section += "### Features\n\n"
    section += f"- **Storefront:** {features.get('storefront', False)}\n"
    section += f"- **Gift Cards:** {features.get('gift_cards', False)}\n"
    section += f"- **Captcha:** {features.get('captcha', False)}\n"
    section += f"- **Reports:** {features.get('reports', False)}\n"
    section += f"- **Live View:** {features.get('live_view', False)}\n"
    section += f"- **Avalara AvaTax:** {features.get('avalara_avatax', False)}\n"
    section += f"- **Branding:** {features.get('branding', 'N/A')}\n\n"
    
    timezone = store_data.get("timezone", {})
    section += f"**Timezone:** {timezone.get('iana', 'N/A')} ({timezone.get('abbreviation', 'N/A')})\n\n"
    
    return section


def generate_performance_section(perf_data: Dict) -> str:
    """Generate markdown section for performance analysis."""
    if not perf_data:
        return "## Performance Analysis\n\nPerformance data not available.\n"
    
    section = "## Performance Analysis\n\n"
    
    weighted_score = perf_data.get("weighted_average_score")
    if weighted_score:
        section += f"**Weighted Average Performance Score:** {weighted_score}/100\n\n"
        if weighted_score >= 90:
            section += "✅ **Excellent** - Performance is optimal.\n\n"
        elif weighted_score >= 75:
            section += "⚠️ **Good** - Performance is acceptable but could be improved.\n\n"
        elif weighted_score >= 50:
            section += "⚠️ **Needs Improvement** - Performance should be optimized.\n\n"
        else:
            section += "❌ **Poor** - Performance requires immediate attention.\n\n"
    
    for page_name, page_data in perf_data.items():
        if page_name == "weighted_average_score" or "error" in page_data:
            continue
        
        section += f"### {page_name.capitalize()} Page\n\n"
        section += f"**URL:** {page_data.get('url', 'N/A')}\n"
        section += f"**Weight:** {page_data.get('weight', 0) * 100}%\n\n"
        
        mobile = page_data.get("mobile", {})
        desktop = page_data.get("desktop", {})
        
        section += "#### Mobile Metrics\n\n"
        section += f"- **Performance Score:** {mobile.get('performance_score', 'N/A')}/100\n"
        section += f"- **LCP (Largest Contentful Paint):** {mobile.get('lcp', 'N/A'):.2f}s\n"
        section += f"- **CLS (Cumulative Layout Shift):** {mobile.get('cls', 'N/A'):.3f}\n"
        section += f"- **FCP (First Contentful Paint):** {mobile.get('fcp', 'N/A'):.2f}s\n"
        section += f"- **TTI (Time to Interactive):** {mobile.get('tti', 'N/A'):.2f}s\n"
        section += f"- **Speed Index:** {mobile.get('speed_index', 'N/A'):.2f}s\n\n"
        
        section += "#### Desktop Metrics\n\n"
        section += f"- **Performance Score:** {desktop.get('performance_score', 'N/A')}/100\n"
        section += f"- **LCP:** {desktop.get('lcp', 'N/A'):.2f}s\n"
        section += f"- **CLS:** {desktop.get('cls', 'N/A'):.3f}\n"
        section += f"- **FCP:** {desktop.get('fcp', 'N/A'):.2f}s\n\n"
    
    return section


def generate_recommendations(
    apps_data: List[Dict],
    perf_data: Dict,
    theme_data: Dict,
) -> str:
    """Generate recommendations based on analysis."""
    section = "## Recommendations\n\n"
    
    recommendations = []
    
    # Performance recommendations
    weighted_score = perf_data.get("weighted_average_score") if perf_data else None
    if weighted_score:
        if weighted_score < 75:
            recommendations.append(
                "**Performance Optimization:** Storefront performance is below optimal. "
                "Consider optimizing images, reducing JavaScript bundle sizes, and using "
                "theme app extensions instead of theme modifications."
            )
    
    # App recommendations
    if apps_data:
        app_count = len(apps_data)
        if app_count > 20:
            recommendations.append(
                f"**App Audit:** {app_count} apps are installed. Review and remove "
                "unused apps to improve performance and reduce complexity."
            )
        
        # Check for apps with many scopes
        high_scope_apps = [
            app for app in apps_data if len(app.get("granted_scopes", [])) > 10
        ]
        if high_scope_apps:
            recommendations.append(
                f"**Scope Review:** {len(high_scope_apps)} app(s) have extensive permissions. "
                "Review if all scopes are necessary for functionality."
            )
    
    # Theme recommendations
    if theme_data:
        total_themes = theme_data.get("total_themes", 0)
        if total_themes > 5:
            recommendations.append(
                f"**Theme Cleanup:** {total_themes} themes found. Consider removing "
                "unused themes to reduce clutter."
            )
    
    if not recommendations:
        section += "✅ No immediate recommendations. Store appears to be well-optimized.\n"
    else:
        for i, rec in enumerate(recommendations, 1):
            section += f"{i}. {rec}\n\n"
    
    return section


def generate_report(
    shop_name: str = "Macross Pharma",
    output_path: Optional[Path] = None,
) -> str:
    """
    Generate comprehensive analysis report.
    
    Args:
        shop_name: Name of the shop.
        output_path: Path to save the report. If None, saves to docs/shopify-analysis.
    
    Returns:
        Path to the generated report file.
    """
    # Load all data
    apps_data = load_json_data("installed_apps.json") or []
    theme_data = load_json_data("theme_info.json")
    store_data = load_json_data("store_config.json")
    perf_data = load_json_data("performance_analysis.json")
    
    # Generate report
    report = f"# Shopify Storefront Analysis Report\n\n"
    report += f"**Store:** {shop_name}\n"
    report += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "---\n\n"
    
    # Executive Summary
    report += "## Executive Summary\n\n"
    report += "This report provides a comprehensive analysis of the Shopify storefront, "
    report += "including installed apps, theme configuration, store settings, and performance metrics.\n\n"
    report += "---\n\n"
    
    # Add sections
    report += generate_store_config_section(store_data)
    report += "---\n\n"
    report += generate_theme_section(theme_data)
    report += "---\n\n"
    report += generate_apps_section(apps_data)
    report += "---\n\n"
    report += generate_performance_section(perf_data)
    report += "---\n\n"
    report += generate_recommendations(apps_data, perf_data or {}, theme_data or {})
    
    # Save report
    if output_path is None:
        script_dir = Path(__file__).parent
        output_path = script_dir.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
    
    report_file = output_path / "macross-pharma-analysis.md"
    report_file.write_text(report)
    
    print(f"Report generated: {report_file}")
    return str(report_file)


def main():
    """Main function to generate the analysis report."""
    try:
        report_path = generate_report()
        print(f"\n✅ Analysis report generated successfully!")
        print(f"📄 Report location: {report_path}")
    except Exception as e:
        print(f"Error generating report: {e}")
        raise


if __name__ == "__main__":
    main()


