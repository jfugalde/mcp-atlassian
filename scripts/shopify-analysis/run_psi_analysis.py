"""Run PageSpeed Insights analysis on selected URLs."""

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional

from performance_analysis import analyze_page_performance, extract_metrics, get_pagespeed_api_key


def analyze_urls_from_set(
    url_set_path: Path, api_key: Optional[str] = None
) -> Dict:
    """
    Analyze all URLs from the selected URL set.
    
    Args:
        url_set_path: Path to JSON file with selected URLs.
        api_key: PageSpeed Insights API key.
    
    Returns:
        Dictionary containing analysis results for all URLs.
    """
    if not url_set_path.exists():
        raise FileNotFoundError(f"URL set file not found: {url_set_path}")
    
    with open(url_set_path, "r", encoding="utf-8") as f:
        selected_urls = json.load(f)
    
    api_key = api_key or get_pagespeed_api_key()
    if not api_key:
        raise ValueError("PageSpeed Insights API key is required")
    
    results = {}
    perf_runs_dir = url_set_path.parent / "perf_runs"
    perf_runs_dir.mkdir(parents=True, exist_ok=True)
    
    total = len(selected_urls)
    print(f"\n🔍 Analyzing {total} URLs with PageSpeed Insights...\n")
    
    for i, item in enumerate(selected_urls, 1):
        url = item["url"]
        category = item.get("category", "unknown")
        
        print(f"[{i}/{total}] Analyzing: {url} ({category})")
        
        url_results = {"url": url, "category": category, "error": None}
        
        # Analyze mobile
        try:
            print("  📱 Mobile analysis...")
            mobile_data = analyze_page_performance(url, api_key, strategy="mobile")
            mobile_metrics = extract_metrics(mobile_data)
            url_results["mobile"] = mobile_metrics
            
            # Save raw data
            safe_filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
            mobile_file = perf_runs_dir / f"{safe_filename}_mobile.json"
            with open(mobile_file, "w", encoding="utf-8") as f:
                json.dump(mobile_data, f, indent=2)
            
            print(f"    Performance: {mobile_metrics.get('performance_score', 'N/A')}")
            print(f"    LCP: {mobile_metrics.get('lcp', 'N/A')}s")
            print(f"    CLS: {mobile_metrics.get('cls', 'N/A')}")
            
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            error_msg = str(e)
            print(f"    ❌ Error: {error_msg}")
            url_results["mobile"] = {"error": error_msg}
            if not url_results.get("error"):
                url_results["error"] = error_msg
        
        # Analyze desktop
        try:
            print("  💻 Desktop analysis...")
            desktop_data = analyze_page_performance(url, api_key, strategy="desktop")
            desktop_metrics = extract_metrics(desktop_data)
            url_results["desktop"] = desktop_metrics
            
            # Save raw data
            safe_filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
            desktop_file = perf_runs_dir / f"{safe_filename}_desktop.json"
            with open(desktop_file, "w", encoding="utf-8") as f:
                json.dump(desktop_data, f, indent=2)
            
            print(f"    Performance: {desktop_metrics.get('performance_score', 'N/A')}")
            print(f"    LCP: {desktop_metrics.get('lcp', 'N/A')}s")
            print(f"    CLS: {desktop_metrics.get('cls', 'N/A')}")
            
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            error_msg = str(e)
            print(f"    ❌ Error: {error_msg}")
            url_results["desktop"] = {"error": error_msg}
            if not url_results.get("error"):
                url_results["error"] = error_msg
        
        results[url] = url_results
        print()
    
    # Save summary
    summary_path = perf_runs_dir / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Analysis complete!")
    print(f"✓ Results saved to: {summary_path}")
    print(f"✓ Raw data saved to: {perf_runs_dir}")
    
    return results


def main():
    """Main function to run PSI analysis."""
    url_set_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "shopify-analysis"
        / "url_set.json"
    )
    
    try:
        results = analyze_urls_from_set(url_set_path)
        return results
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()

