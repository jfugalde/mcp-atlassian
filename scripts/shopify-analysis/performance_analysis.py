"""Performance analysis using PageSpeed Insights API."""

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional

import httpx


def get_pagespeed_api_key() -> Optional[str]:
    """
    Get Google PageSpeed Insights API key from environment.
    
    Returns:
        API key string or None if not found.
    """
    return os.getenv("PAGESPEED_INSIGHTS_API_KEY")


def analyze_page_performance(
    url: str,
    api_key: Optional[str] = None,
    strategy: str = "mobile",
) -> Dict:
    """
    Analyze a single page using PageSpeed Insights API.
    
    Args:
        url: URL to analyze.
        api_key: PageSpeed Insights API key. If None, reads from environment.
        strategy: Analysis strategy ('mobile' or 'desktop').
    
    Returns:
        Dictionary containing performance metrics.
    
    Raises:
        ValueError: If API key is missing.
        httpx.HTTPStatusError: If the API request fails.
    """
    api_key = api_key or get_pagespeed_api_key()
    
    if not api_key:
        raise ValueError(
            "PageSpeed Insights API key is required.\n"
            "Set PAGESPEED_INSIGHTS_API_KEY environment variable.\n"
            "Get a free API key from: https://developers.google.com/speed/docs/insights/v5/get-started"
        )
    
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    
    params = {
        "url": url,
        "key": api_key,
        "strategy": strategy,
        "category": ["performance", "accessibility", "best-practices", "seo"],
    }
    
    with httpx.Client(timeout=60.0) as client:
        response = client.get(api_url, params=params)
        response.raise_for_status()
        return response.json()


def extract_metrics(data: Dict) -> Dict:
    """
    Extract key performance metrics from PageSpeed Insights response.
    
    Args:
        data: Raw PageSpeed Insights API response.
    
    Returns:
        Dictionary containing extracted metrics.
    """
    lighthouse_result = data.get("lighthouseResult", {})
    categories = lighthouse_result.get("categories", {})
    audits = lighthouse_result.get("audits", {})
    
    # Core Web Vitals
    lcp = audits.get("largest-contentful-paint", {}).get("numericValue")
    cls = audits.get("cumulative-layout-shift", {}).get("numericValue")
    fcp = audits.get("first-contentful-paint", {}).get("numericValue")
    tti = audits.get("interactive", {}).get("numericValue")
    speed_index = audits.get("speed-index", {}).get("numericValue")
    
    # Performance score
    performance_score = categories.get("performance", {}).get("score")
    if performance_score:
        performance_score = int(performance_score * 100)
    
    return {
        "performance_score": performance_score,
        "lcp": lcp / 1000 if lcp else None,  # Convert to seconds
        "cls": cls,
        "fcp": fcp / 1000 if fcp else None,  # Convert to seconds
        "tti": tti / 1000 if tti else None,  # Convert to seconds
        "speed_index": speed_index / 1000 if speed_index else None,  # Convert to seconds
        "accessibility_score": int(
            categories.get("accessibility", {}).get("score", 0) * 100
        ),
        "best_practices_score": int(
            categories.get("best-practices", {}).get("score", 0) * 100
        ),
        "seo_score": int(categories.get("seo", {}).get("score", 0) * 100),
    }


def analyze_storefront_pages(
    shop_domain: str,
    home_path: str = "/",
    product_path: Optional[str] = None,
    collection_path: Optional[str] = None,
    api_key: Optional[str] = None,
) -> Dict:
    """
    Analyze multiple storefront pages and calculate weighted performance score.
    
    Args:
        shop_domain: Shop domain (e.g., 'macross-pharma.myshopify.com').
        home_path: Path to home page (default: '/').
        product_path: Path to a product page (e.g., '/products/example').
        collection_path: Path to a collection page (e.g., '/collections/all').
        api_key: PageSpeed Insights API key.
    
    Returns:
        Dictionary containing analysis results for all pages.
    """
    if not shop_domain.startswith("http"):
        if not shop_domain.endswith(".myshopify.com"):
            shop_domain = f"{shop_domain}.myshopify.com"
        shop_domain = f"https://{shop_domain}"
    
    results = {}
    pages_to_analyze = [
        ("home", f"{shop_domain}{home_path}", 0.17),
        ("product", f"{shop_domain}{product_path}", 0.40) if product_path else None,
        ("collection", f"{shop_domain}{collection_path}", 0.43) if collection_path else None,
    ]
    
    # Filter out None values
    pages_to_analyze = [p for p in pages_to_analyze if p is not None]
    
    print("Analyzing storefront performance...")
    print("This may take a few minutes...\n")
    
    for page_name, url, weight in pages_to_analyze:
        print(f"Analyzing {page_name} page: {url}")
        try:
            # Analyze mobile first (as per Shopify's testing methodology)
            mobile_data = analyze_page_performance(url, api_key, strategy="mobile")
            mobile_metrics = extract_metrics(mobile_data)
            
            # Small delay to avoid rate limiting
            time.sleep(2)
            
            # Analyze desktop
            desktop_data = analyze_page_performance(url, api_key, strategy="desktop")
            desktop_metrics = extract_metrics(desktop_data)
            
            results[page_name] = {
                "url": url,
                "weight": weight,
                "mobile": mobile_metrics,
                "desktop": desktop_metrics,
            }
            
            print(f"  Mobile Performance: {mobile_metrics['performance_score']}")
            print(f"  Desktop Performance: {desktop_metrics['performance_score']}\n")
            
            # Rate limiting delay
            time.sleep(2)
        except Exception as e:
            print(f"  Error analyzing {page_name}: {e}\n")
            results[page_name] = {"error": str(e)}
    
    # Calculate weighted average
    if results:
        weighted_scores = []
        for page_name, page_data in results.items():
            if "error" not in page_data and "mobile" in page_data:
                weight = page_data.get("weight", 0)
                score = page_data["mobile"].get("performance_score", 0)
                if score:
                    weighted_scores.append((weight, score))
        
        if weighted_scores:
            total_weight = sum(w for w, _ in weighted_scores)
            weighted_avg = sum(w * s for w, s in weighted_scores) / total_weight if total_weight > 0 else 0
            results["weighted_average_score"] = round(weighted_avg, 1)
    
    return results


def main():
    """Main function to analyze storefront performance."""
    shop_domain = os.getenv("SHOPIFY_SHOP_DOMAIN", "macross-pharma.myshopify.com")
    
    # You can customize these paths based on your store
    product_path = os.getenv("SHOPIFY_PRODUCT_PATH")  # e.g., "/products/example"
    collection_path = os.getenv("SHOPIFY_COLLECTION_PATH")  # e.g., "/collections/all"
    
    try:
        results = analyze_storefront_pages(
            shop_domain,
            product_path=product_path,
            collection_path=collection_path,
        )
        
        # Save to JSON file
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "performance_analysis.json"
        
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\nPerformance analysis saved to: {output_file}")
        
        if "weighted_average_score" in results:
            print(f"\nWeighted Average Performance Score: {results['weighted_average_score']}")
        
        return results
    except Exception as e:
        print(f"Error analyzing performance: {e}")
        raise


if __name__ == "__main__":
    main()


