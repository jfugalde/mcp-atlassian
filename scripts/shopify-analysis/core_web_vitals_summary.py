"""Consolidate Core Web Vitals analysis from existing PageSpeed Insights data."""

import json
from pathlib import Path
from typing import Dict, List, Optional


def extract_ttfb_from_raw(raw_data: Dict) -> Optional[float]:
    """
    Extract TTFB from raw PageSpeed Insights data.
    
    Args:
        raw_data: Raw PageSpeed Insights API response.
    
    Returns:
        TTFB in seconds or None if not found.
    """
    lighthouse_result = raw_data.get("lighthouseResult", {})
    audits = lighthouse_result.get("audits", {})
    
    # Try different audit keys for TTFB
    ttfb_audit = audits.get("server-response-time", {})
    if ttfb_audit:
        numeric_value = ttfb_audit.get("numericValue")
        if numeric_value:
            return numeric_value / 1000  # Convert to seconds
    
    # Try loading experience metrics
    loading_experience = raw_data.get("loadingExperience", {})
    if loading_experience:
        metrics = loading_experience.get("metrics", {})
        ttfb_metric = metrics.get("EXPERIMENTAL_TIME_TO_FIRST_BYTE", {})
        if ttfb_metric:
            percentile = ttfb_metric.get("percentile")
            if percentile:
                return percentile / 1000  # Convert to seconds
    
    return None


def consolidate_core_web_vitals(
    summary_path: Path,
    perf_runs_dir: Path,
) -> Dict:
    """
    Consolidate Core Web Vitals from summary and raw data files.
    
    Args:
        summary_path: Path to summary.json file.
        perf_runs_dir: Directory containing raw PageSpeed Insights data.
    
    Returns:
        Dictionary containing consolidated Core Web Vitals analysis.
    """
    with open(summary_path, "r", encoding="utf-8") as f:
        summary_data = json.load(f)
    
    # Organize by category
    by_category = {
        "home": [],
        "category": [],
        "product": [],
        "other": [],
    }
    
    # Process each URL
    for url, data in summary_data.items():
        if data.get("error"):
            continue
        
        category = data.get("category", "other")
        mobile_data = data.get("mobile", {})
        desktop_data = data.get("desktop", {})
        
        # Try to get TTFB from raw files
        ttfb_mobile = None
        ttfb_desktop = None
        
        # Construct filename
        safe_filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
        mobile_file = perf_runs_dir / f"{safe_filename}_mobile.json"
        desktop_file = perf_runs_dir / f"{safe_filename}_desktop.json"
        
        if mobile_file.exists():
            try:
                with open(mobile_file, "r", encoding="utf-8") as f:
                    mobile_raw = json.load(f)
                    ttfb_mobile = extract_ttfb_from_raw(mobile_raw)
            except Exception:
                pass
        
        if desktop_file.exists():
            try:
                with open(desktop_file, "r", encoding="utf-8") as f:
                    desktop_raw = json.load(f)
                    ttfb_desktop = extract_ttfb_from_raw(desktop_raw)
            except Exception:
                pass
        
        page_metrics = {
            "url": url,
            "category": category,
            "mobile": {
                **mobile_data,
                "ttfb": ttfb_mobile,
            },
            "desktop": {
                **desktop_data,
                "ttfb": ttfb_desktop,
            },
        }
        
        if category in by_category:
            by_category[category].append(page_metrics)
        else:
            by_category["other"].append(page_metrics)
    
    # Calculate averages by category
    averages = {}
    for category, pages in by_category.items():
        if not pages:
            continue
        
        mobile_metrics = {
            "performance_score": [],
            "lcp": [],
            "cls": [],
            "fcp": [],
            "tti": [],
            "ttfb": [],
            "speed_index": [],
        }
        
        desktop_metrics = {
            "performance_score": [],
            "lcp": [],
            "cls": [],
            "fcp": [],
            "tti": [],
            "ttfb": [],
            "speed_index": [],
        }
        
        for page in pages:
            mobile = page.get("mobile", {})
            desktop = page.get("desktop", {})
            
            for metric in mobile_metrics.keys():
                value = mobile.get(metric)
                if value is not None:
                    mobile_metrics[metric].append(value)
                
                value = desktop.get(metric)
                if value is not None:
                    desktop_metrics[metric].append(value)
        
        # Calculate averages
        def avg(values):
            return sum(values) / len(values) if values else None
        
        averages[category] = {
            "mobile": {k: avg(v) for k, v in mobile_metrics.items()},
            "desktop": {k: avg(v) for k, v in desktop_metrics.items()},
            "page_count": len(pages),
        }
    
    # Identify worst performing pages
    worst_pages = {
        "mobile": {
            "lcp": None,
            "fcp": None,
            "tti": None,
            "cls": None,
        },
        "desktop": {
            "lcp": None,
            "fcp": None,
            "tti": None,
            "cls": None,
        },
    }
    
    for url, data in summary_data.items():
        if data.get("error"):
            continue
        
        mobile = data.get("mobile", {})
        desktop = data.get("desktop", {})
        
        # Mobile worst performers
        for metric in ["lcp", "fcp", "tti", "cls"]:
            value = mobile.get(metric)
            if value is not None:
                worst = worst_pages["mobile"][metric]
                if worst is None or value > worst["value"]:
                    worst_pages["mobile"][metric] = {
                        "url": url,
                        "value": value,
                        "category": data.get("category", "other"),
                    }
        
        # Desktop worst performers
        for metric in ["lcp", "fcp", "tti", "cls"]:
            value = desktop.get(metric)
            if value is not None:
                worst = worst_pages["desktop"][metric]
                if worst is None or value > worst["value"]:
                    worst_pages["desktop"][metric] = {
                        "url": url,
                        "value": value,
                        "category": data.get("category", "other"),
                    }
    
    # Google's recommended thresholds
    thresholds = {
        "lcp": {"good": 2.5, "needs_improvement": 4.0},
        "fcp": {"good": 1.8, "needs_improvement": 3.0},
        "cls": {"good": 0.1, "needs_improvement": 0.25},
        "tti": {"good": 3.8, "needs_improvement": 7.3},
        "ttfb": {"good": 0.8, "needs_improvement": 1.8},
    }
    
    # Evaluate compliance
    compliance = {}
    for category, pages in by_category.items():
        if not pages:
            continue
        
        mobile_compliance = {}
        desktop_compliance = {}
        
        for page in pages:
            mobile = page.get("mobile", {})
            desktop = page.get("desktop", {})
            
            for metric, threshold in thresholds.items():
                mobile_value = mobile.get(metric)
                desktop_value = desktop.get(metric)
                
                if mobile_value is not None:
                    if metric not in mobile_compliance:
                        mobile_compliance[metric] = {"good": 0, "needs_improvement": 0, "poor": 0}
                    
                    if mobile_value <= threshold["good"]:
                        mobile_compliance[metric]["good"] += 1
                    elif mobile_value <= threshold["needs_improvement"]:
                        mobile_compliance[metric]["needs_improvement"] += 1
                    else:
                        mobile_compliance[metric]["poor"] += 1
                
                if desktop_value is not None:
                    if metric not in desktop_compliance:
                        desktop_compliance[metric] = {"good": 0, "needs_improvement": 0, "poor": 0}
                    
                    if desktop_value <= threshold["good"]:
                        desktop_compliance[metric]["good"] += 1
                    elif desktop_value <= threshold["needs_improvement"]:
                        desktop_compliance[metric]["needs_improvement"] += 1
                    else:
                        desktop_compliance[metric]["poor"] += 1
        
        compliance[category] = {
            "mobile": mobile_compliance,
            "desktop": desktop_compliance,
        }
    
    return {
        "summary": {
            "total_pages_analyzed": len([u for u in summary_data.keys() if not summary_data[u].get("error")]),
            "categories": list(by_category.keys()),
        },
        "averages_by_category": averages,
        "worst_performing_pages": worst_pages,
        "compliance_with_thresholds": compliance,
        "thresholds": thresholds,
        "pages_by_category": {
            category: [
                {
                    "url": p["url"],
                    "mobile": {k: v for k, v in p["mobile"].items() if v is not None},
                    "desktop": {k: v for k, v in p["desktop"].items() if v is not None},
                }
                for p in pages
            ]
            for category, pages in by_category.items()
        },
    }


def main():
    """Main function to consolidate Core Web Vitals."""
    base_dir = Path(__file__).parent.parent.parent
    summary_path = base_dir / "docs" / "shopify-analysis" / "perf_runs" / "summary.json"
    perf_runs_dir = base_dir / "docs" / "shopify-analysis" / "perf_runs"
    output_path = base_dir / "docs" / "shopify-analysis" / "core_web_vitals_summary.json"
    
    if not summary_path.exists():
        print(f"Error: Summary file not found at {summary_path}")
        return
    
    print("Consolidating Core Web Vitals analysis...")
    print(f"Reading from: {summary_path}")
    
    consolidated = consolidate_core_web_vitals(summary_path, perf_runs_dir)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Core Web Vitals summary saved to: {output_path}")
    print(f"\nSummary:")
    print(f"  Total pages analyzed: {consolidated['summary']['total_pages_analyzed']}")
    print(f"  Categories: {', '.join(consolidated['summary']['categories'])}")
    
    # Print worst performers
    print("\nWorst performing pages (Mobile):")
    for metric, worst in consolidated["worst_performing_pages"]["mobile"].items():
        if worst:
            print(f"  {metric.upper()}: {worst['value']:.2f}s - {worst['url']}")
    
    print("\nWorst performing pages (Desktop):")
    for metric, worst in consolidated["worst_performing_pages"]["desktop"].items():
        if worst:
            print(f"  {metric.upper()}: {worst['value']:.2f}s - {worst['url']}")


if __name__ == "__main__":
    main()

