#!/usr/bin/env python3
"""Local testing interface for Shopify storefront analysis."""

import json
import sys
from pathlib import Path
from typing import Optional

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth import get_access_token, get_shop_domain
from query_apps import query_installed_apps, format_apps_data
from query_theme import query_theme_info
from query_store_config import query_store_config
from performance_analysis import analyze_storefront_pages
from app_analyzer import deep_analyze_apps
from generate_report import generate_report


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 60)
    print("Shopify Storefront Analysis - Local Testing")
    print("=" * 60)
    print("1. Quick Analysis (Apps + Theme + Store Config)")
    print("2. Deep App Analysis (Security, Cost, Performance)")
    print("3. Performance Analysis (PageSpeed Insights)")
    print("4. Full Comprehensive Analysis")
    print("5. Test API Connection")
    print("6. View Saved Reports")
    print("0. Exit")
    print("=" * 60)


def test_connection():
    """Test API connection."""
    print("\n🔌 Testing API connection...")
    
    token = get_access_token()
    domain = get_shop_domain()
    
    if not token:
        print("❌ Error: SHOPIFY_ACCESS_TOKEN not set")
        print("   Set it in .env file or export it:")
        print("   export SHOPIFY_ACCESS_TOKEN='your_token'")
        return False
    
    if not domain:
        print("❌ Error: SHOPIFY_SHOP_DOMAIN not set")
        return False
    
    print(f"✅ Token found: {token[:10]}...")
    print(f"✅ Shop domain: {domain}")
    
    try:
        # Try a simple query
        from auth import create_graphql_client, execute_graphql_query
        
        client = create_graphql_client()
        query = "{ shop { name } }"
        result = execute_graphql_query(client, query)
        client.close()
        
        shop_name = result.get("shop", {}).get("name", "Unknown")
        print(f"✅ Connected successfully to: {shop_name}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False


def quick_analysis():
    """Run quick analysis of apps, theme, and store config."""
    print("\n🚀 Running quick analysis...")
    
    try:
        # Query apps
        print("  📱 Querying installed apps...")
        apps_data = query_installed_apps()
        apps = format_apps_data(apps_data)
        print(f"     Found {len(apps)} apps")
        
        # Query theme
        print("  🎨 Querying theme information...")
        theme_data = query_theme_info()
        themes = theme_data.get("themes", {}).get("nodes", [])
        print(f"     Found {len(themes)} themes")
        
        # Query store config
        print("  ⚙️  Querying store configuration...")
        store_data = query_store_config()
        shop = store_data.get("shop", {})
        print(f"     Store: {shop.get('name', 'Unknown')}")
        
        print("\n✅ Quick analysis complete!")
        print(f"   Check docs/shopify-analysis/ for detailed JSON files")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def deep_app_analysis():
    """Run deep app analysis."""
    print("\n🔍 Running deep app analysis...")
    
    try:
        from app_analyzer import deep_analyze_apps
        
        analysis = deep_analyze_apps()
        
        # Print summary
        summary = analysis["summary"]
        print("\n" + "=" * 60)
        print("DEEP APP ANALYSIS SUMMARY")
        print("=" * 60)
        print(f"Total Apps: {analysis['total_apps']}")
        print(f"Total Monthly Cost: ${summary['total_monthly_cost']:.2f}")
        print(f"High-Risk Apps: {summary['high_risk_apps']}")
        print(f"Performance Concerns: {summary['performance_concerns']}")
        print(f"Security Issues: {summary['security_issues']}")
        print("=" * 60)
        
        # Show top concerns
        print("\n⚠️  Top Concerns:")
        for app_analysis in analysis["apps"][:5]:  # Top 5 lowest scores
            app = app_analysis["app"]
            print(f"  - {app['name']}: Score {app_analysis['overall_score']:.1f}/100")
            if app_analysis["recommendations"]:
                print(f"    → {app_analysis['recommendations'][0]}")
        
        print("\n✅ Deep analysis complete!")
        print("   Check docs/shopify-analysis/deep_app_analysis_report.md")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def performance_analysis():
    """Run performance analysis."""
    print("\n⚡ Running performance analysis...")
    
    try:
        # Get store domain
        domain = get_shop_domain()
        if not domain:
            print("❌ Error: SHOPIFY_SHOP_DOMAIN not set")
            return
        
        print(f"  Analyzing: {domain}")
        print("  This may take a few minutes...")
        
        # Use analyze_storefront_pages which handles the URL construction
        results = analyze_storefront_pages(
            shop_domain=domain,
            product_path=None,  # Can be customized via env var
            collection_path=None,  # Can be customized via env var
        )
        
        if results:
            print("\n✅ Performance analysis complete!")
            if "weighted_average_score" in results:
                print(f"   Weighted Average Score: {results['weighted_average_score']}")
            print("   Check docs/shopify-analysis/performance_analysis.json")
        else:
            print("⚠️  Performance analysis requires PAGESPEED_INSIGHTS_API_KEY")
            print("   Get one at: https://developers.google.com/speed/docs/insights/v5/get-started")
        
    except ValueError as e:
        # This is raised when API key is missing
        print(f"⚠️  {e}")
        print("   Performance analysis is optional - other analyses will work without it")
    except Exception as e:
        print(f"❌ Error: {e}")


def full_analysis():
    """Run full comprehensive analysis."""
    print("\n🌟 Running full comprehensive analysis...")
    print("   This will take several minutes...\n")
    
    try:
        # Run all analyses
        quick_analysis()
        print()
        deep_app_analysis()
        print()
        performance_analysis()
        print()
        
        # Generate comprehensive report
        print("📄 Generating comprehensive report...")
        generate_report()
        
        print("\n✅ Full analysis complete!")
        print("   Check docs/shopify-analysis/ for all reports")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def view_reports():
    """View saved reports."""
    print("\n📄 Available Reports:\n")
    
    reports_dir = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
    
    if not reports_dir.exists():
        print("  No reports directory found. Run an analysis first.")
        return
    
    reports = {
        "installed_apps.json": "Installed Apps Data",
        "theme_info.json": "Theme Information",
        "store_config.json": "Store Configuration",
        "deep_app_analysis.json": "Deep App Analysis (JSON)",
        "deep_app_analysis_report.md": "Deep App Analysis (Report)",
        "performance_results.json": "Performance Results",
        "comprehensive_report.md": "Comprehensive Report",
    }
    
    for filename, description in reports.items():
        filepath = reports_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            print(f"  ✅ {filename}")
            print(f"     {description} ({size:,} bytes)")
        else:
            print(f"  ⏳ {filename} (not generated yet)")
    
    print(f"\n  Reports directory: {reports_dir}")


def main():
    """Main interactive loop."""
    print("Welcome to Shopify Storefront Analysis!")
    print("Make sure you've set up your .env file or environment variables.")
    
    # Test connection first
    if not test_connection():
        print("\n⚠️  Connection test failed. Please check your configuration.")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != "y":
            return
    
    while True:
        print_menu()
        choice = input("\nSelect an option: ").strip()
        
        if choice == "0":
            print("\n👋 Goodbye!")
            break
        elif choice == "1":
            quick_analysis()
        elif choice == "2":
            deep_app_analysis()
        elif choice == "3":
            performance_analysis()
        elif choice == "4":
            full_analysis()
        elif choice == "5":
            test_connection()
        elif choice == "6":
            view_reports()
        else:
            print("❌ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

