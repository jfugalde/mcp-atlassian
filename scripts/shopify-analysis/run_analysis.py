#!/usr/bin/env python3
"""Main script to run complete Shopify storefront analysis."""

import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from query_apps import main as query_apps
from query_theme import main as query_theme
from query_store_config import main as query_store_config
from performance_analysis import main as analyze_performance
from generate_report import main as generate_report


def main():
    """Run complete analysis pipeline."""
    print("=" * 60)
    print("Shopify Storefront Analysis")
    print("=" * 60)
    print()
    
    try:
        # Step 1: Query installed apps
        print("Step 1/5: Querying installed apps...")
        query_apps()
        print()
        
        # Step 2: Query theme information
        print("Step 2/5: Querying theme information...")
        query_theme()
        print()
        
        # Step 3: Query store configuration
        print("Step 3/5: Querying store configuration...")
        query_store_config()
        print()
        
        # Step 4: Performance analysis (optional - requires API key)
        print("Step 4/5: Analyzing performance...")
        try:
            analyze_performance()
        except ValueError as e:
            print(f"⚠️  Performance analysis skipped: {e}")
            print("   Set PAGESPEED_INSIGHTS_API_KEY to enable performance analysis.")
        print()
        
        # Step 5: Generate report
        print("Step 5/5: Generating comprehensive report...")
        generate_report()
        print()
        
        print("=" * 60)
        print("✅ Analysis complete!")
        print("=" * 60)
        print()
        print("📄 View the report at: docs/shopify-analysis/macross-pharma-analysis.md")
        
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

