"""Web crawler for discovering URLs from farmaciasmacross.com.mx."""

import json
import time
from pathlib import Path
from typing import Dict, List, Set
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.robotparser import RobotFileParser

import httpx
from bs4 import BeautifulSoup


class SiteCrawler:
    """Crawler that respects robots.txt and discovers URLs."""

    def __init__(self, base_url: str, max_urls: int = 120):
        """
        Initialize crawler.
        
        Args:
            base_url: Base URL of the site (e.g., 'https://farmaciasmacross.com.mx').
            max_urls: Maximum number of URLs to collect.
        """
        self.base_url = base_url.rstrip("/")
        self.max_urls = max_urls
        self.discovered_urls: Set[str] = set()
        self.visited_urls: Set[str] = set()
        self.robots_parser = RobotFileParser()
        self.session = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            },
        )

    def _normalize_url(self, url: str) -> str:
        """
        Normalize URL by removing fragments and query params for deduplication.
        
        Args:
            url: URL to normalize.
        
        Returns:
            Normalized URL.
        """
        parsed = urlparse(url)
        # Keep query params but remove fragments
        normalized = urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                parsed.params,
                parsed.query,
                "",  # Remove fragment
            )
        )
        return normalized.rstrip("/") or normalized

    def _load_robots_txt(self) -> bool:
        """
        Load and parse robots.txt.
        
        Returns:
            True if robots.txt was loaded successfully.
        """
        robots_url = urljoin(self.base_url, "/robots.txt")
        try:
            response = self.session.get(robots_url, timeout=10.0)
            if response.status_code == 200:
                self.robots_parser.set_url(robots_url)
                self.robots_parser.read()
                print(f"✓ Loaded robots.txt from {robots_url}")
                return True
            else:
                print(f"⚠ robots.txt not found (status {response.status_code})")
                return False
        except Exception as e:
            print(f"⚠ Could not load robots.txt: {e}")
            return False

    def _can_fetch(self, url: str) -> bool:
        """
        Check if URL can be fetched according to robots.txt.
        
        Args:
            url: URL to check.
        
        Returns:
            True if URL can be fetched.
        """
        try:
            return self.robots_parser.can_fetch("*", url)
        except Exception:
            # If robots.txt parsing fails, allow by default
            return True

    def _extract_links(self, html: str, current_url: str) -> List[str]:
        """
        Extract links from HTML content.
        
        Args:
            html: HTML content.
            current_url: Current page URL.
        
        Returns:
            List of absolute URLs found in the page.
        """
        soup = BeautifulSoup(html, "html.parser")
        links = []
        
        # Find all <a> tags with href
        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            absolute_url = urljoin(current_url, href)
            
            # Only include URLs from the same domain
            parsed = urlparse(absolute_url)
            base_parsed = urlparse(self.base_url)
            
            if parsed.netloc == base_parsed.netloc:
                normalized = self._normalize_url(absolute_url)
                links.append(normalized)
        
        return links

    def _categorize_url(self, url: str) -> str:
        """
        Categorize URL by type.
        
        Args:
            url: URL to categorize.
        
        Returns:
            Category name.
        """
        url_lower = url.lower()
        path = urlparse(url).path.lower()
        
        if path == "/" or path == "":
            return "home"
        elif "/product" in path or "/producto" in path:
            return "product"
        elif "/category" in path or "/categoria" in path or "/collection" in path:
            return "category"
        elif "/cart" in path or "/carrito" in path:
            return "cart"
        elif "/checkout" in path or "/pago" in path:
            return "checkout"
        elif "/search" in path or "/buscar" in path:
            return "search"
        elif any(
            term in path
            for term in [
                "/privacy",
                "/privacidad",
                "/terms",
                "/terminos",
                "/legal",
                "/aviso",
            ]
        ):
            return "legal"
        elif "/account" in path or "/cuenta" in path or "/login" in path:
            return "account"
        else:
            return "other"

    def crawl(self) -> Dict[str, List[str]]:
        """
        Crawl the site and discover URLs.
        
        Returns:
            Dictionary mapping categories to lists of URLs.
        """
        print(f"\n🔍 Starting crawl of {self.base_url}")
        print(f"   Max URLs: {self.max_urls}\n")
        
        # Load robots.txt
        self._load_robots_txt()
        
        # Start with home page
        home_url = self.base_url
        normalized_home = self._normalize_url(home_url)
        self.discovered_urls.add(normalized_home)
        
        # Queue for BFS
        queue = [normalized_home]
        categorized_urls: Dict[str, List[str]] = {
            "home": [],
            "product": [],
            "category": [],
            "cart": [],
            "checkout": [],
            "search": [],
            "legal": [],
            "account": [],
            "other": [],
        }
        
        while queue and len(self.discovered_urls) < self.max_urls:
            current_url = queue.pop(0)
            
            if current_url in self.visited_urls:
                continue
            
            # Check robots.txt
            if not self._can_fetch(current_url):
                print(f"🚫 Skipped (robots.txt): {current_url}")
                continue
            
            # Visit URL
            try:
                print(f"📄 Fetching: {current_url}")
                response = self.session.get(current_url, timeout=15.0)
                
                if response.status_code != 200:
                    print(f"   ⚠ Status {response.status_code}")
                    self.visited_urls.add(current_url)
                    continue
                
                self.visited_urls.add(current_url)
                
                # Categorize and add to results
                category = self._categorize_url(current_url)
                if current_url not in categorized_urls[category]:
                    categorized_urls[category].append(current_url)
                
                # Extract links
                if len(self.discovered_urls) < self.max_urls:
                    links = self._extract_links(response.text, current_url)
                    
                    for link in links:
                        if link not in self.discovered_urls:
                            self.discovered_urls.add(link)
                            queue.append(link)
                
                # Rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                print(f"   ❌ Error: {e}")
                self.visited_urls.add(current_url)
                continue
        
        print(f"\n✓ Crawl complete: {len(self.discovered_urls)} URLs discovered")
        print(f"  Visited: {len(self.visited_urls)} URLs\n")
        
        # Print summary
        for category, urls in categorized_urls.items():
            if urls:
                print(f"  {category}: {len(urls)} URLs")
        
        return categorized_urls

    def save_results(self, output_path: Path, categorized_urls: Dict[str, List[str]]):
        """
        Save crawl results to JSON file.
        
        Args:
            output_path: Path to save JSON file.
            categorized_urls: Categorized URL dictionary.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            "base_url": self.base_url,
            "total_urls": len(self.discovered_urls),
            "visited_urls": len(self.visited_urls),
            "categories": categorized_urls,
            "all_urls": sorted(list(self.discovered_urls)),
        }
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Results saved to: {output_path}")


def main():
    """Main function to crawl farmaciasmacross.com.mx."""
    base_url = "https://farmaciasmacross.com.mx"
    
    crawler = SiteCrawler(base_url, max_urls=120)
    categorized_urls = crawler.crawl()
    
    # Save results
    output_dir = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
    output_path = output_dir / "crawl_results.json"
    crawler.save_results(output_path, categorized_urls)
    
    return categorized_urls


if __name__ == "__main__":
    main()

