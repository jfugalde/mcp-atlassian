"""Select representative URLs from crawl results for deep analysis."""

import json
from pathlib import Path
from typing import Dict, List


def select_representative_urls(
    categorized_urls: Dict[str, List[str]], target_count: int = 15
) -> List[Dict[str, str]]:
    """
    Select representative URLs for deep analysis.
    
    Args:
        categorized_urls: Dictionary mapping categories to URL lists.
        target_count: Target number of URLs to select.
    
    Returns:
        List of dictionaries with 'url' and 'category' keys.
    """
    selected: List[Dict[str, str]] = []
    
    # Priority order for selection
    priority_categories = [
        "home",
        "category",
        "product",
        "legal",
        "cart",
        "checkout",
        "search",
        "account",
        "other",
    ]
    
    # Select from each category
    for category in priority_categories:
        urls = categorized_urls.get(category, [])
        
        if not urls:
            continue
        
        # Select up to a certain number from each category
        if category == "home":
            # Always include home
            for url in urls[:1]:
                selected.append({"url": url, "category": category})
        elif category == "category":
            # Select 3-4 category pages
            for url in urls[:4]:
                if len(selected) < target_count:
                    selected.append({"url": url, "category": category})
        elif category == "product":
            # Select 3-4 product pages
            for url in urls[:4]:
                if len(selected) < target_count:
                    selected.append({"url": url, "category": category})
        elif category in ["legal", "cart", "checkout"]:
            # Select 1-2 from each
            for url in urls[:2]:
                if len(selected) < target_count:
                    selected.append({"url": url, "category": category})
        elif category == "search":
            # Select 1 search page
            for url in urls[:1]:
                if len(selected) < target_count:
                    selected.append({"url": url, "category": category})
        else:
            # Select 1-2 from other categories
            for url in urls[:2]:
                if len(selected) < target_count:
                    selected.append({"url": url, "category": category})
        
        if len(selected) >= target_count:
            break
    
    return selected[:target_count]


def save_url_set(selected_urls: List[Dict[str, str]], output_path: Path):
    """
    Save selected URL set to markdown file.
    
    Args:
        selected_urls: List of selected URLs with categories.
        output_path: Path to save markdown file.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    lines = [
        "# Selected URLs for Deep Analysis",
        "",
        f"Total URLs selected: {len(selected_urls)}",
        "",
        "## URLs by Category",
        "",
    ]
    
    # Group by category
    by_category: Dict[str, List[str]] = {}
    for item in selected_urls:
        category = item["category"]
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(item["url"])
    
    for category in sorted(by_category.keys()):
        lines.append(f"### {category.title()} ({len(by_category[category])})")
        lines.append("")
        for url in by_category[category]:
            lines.append(f"- {url}")
        lines.append("")
    
    lines.append("## All URLs")
    lines.append("")
    for i, item in enumerate(selected_urls, 1):
        lines.append(f"{i}. [{item['url']}]({item['url']}) ({item['category']})")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"✓ URL set saved to: {output_path}")


def main():
    """Main function to select URLs from crawl results."""
    crawl_results_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "shopify-analysis"
        / "crawl_results.json"
    )
    
    if not crawl_results_path.exists():
        print(f"Error: Crawl results not found at {crawl_results_path}")
        print("Please run url_crawler.py first.")
        return
    
    with open(crawl_results_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    categorized_urls = data.get("categories", {})
    selected_urls = select_representative_urls(categorized_urls, target_count=15)
    
    # Save to markdown
    output_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "shopify-analysis"
        / "url_set.md"
    )
    save_url_set(selected_urls, output_path)
    
    # Also save as JSON for easy access
    json_output = output_path.with_suffix(".json")
    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(selected_urls, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Selected {len(selected_urls)} URLs for analysis")
    print(f"✓ JSON saved to: {json_output}")
    
    return selected_urls


if __name__ == "__main__":
    main()

