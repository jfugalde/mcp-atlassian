"""On-page technical analysis: meta tags, headers, schema, security, etc."""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup


class OnPageAnalyzer:
    """Analyzer for on-page technical elements."""

    def __init__(self):
        """Initialize analyzer."""
        self.session = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            },
        )

    def analyze_url(self, url: str) -> Dict:
        """
        Analyze a single URL for on-page technical elements.
        
        Args:
            url: URL to analyze.
        
        Returns:
            Dictionary containing analysis results.
        """
        print(f"Analyzing: {url}")
        
        result = {
            "url": url,
            "error": None,
            "status_code": None,
            "meta_tags": {},
            "headings": {},
            "schema": [],
            "open_graph": {},
            "twitter_card": {},
            "canonical": None,
            "hreflang": [],
            "security_headers": {},
            "mixed_content": False,
            "https_redirect": False,
            "sitemap_reference": None,
            "robots_meta": None,
        }
        
        try:
            # Check HTTPS redirect
            if url.startswith("http://"):
                https_url = url.replace("http://", "https://")
                try:
                    response = self.session.get(https_url, timeout=10.0)
                    if response.status_code == 200:
                        result["https_redirect"] = True
                        url = https_url
                except Exception:
                    pass
            
            response = self.session.get(url, timeout=15.0)
            result["status_code"] = response.status_code
            
            if response.status_code != 200:
                result["error"] = f"HTTP {response.status_code}"
                return result
            
            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract meta tags
            result["meta_tags"] = self._extract_meta_tags(soup)
            
            # Extract headings
            result["headings"] = self._extract_headings(soup)
            
            # Extract schema
            result["schema"] = self._extract_schema(soup)
            
            # Extract Open Graph tags
            result["open_graph"] = self._extract_open_graph(soup)
            
            # Extract Twitter Card tags
            result["twitter_card"] = self._extract_twitter_card(soup)
            
            # Extract canonical
            canonical_tag = soup.find("link", rel="canonical")
            if canonical_tag and canonical_tag.get("href"):
                result["canonical"] = canonical_tag["href"]
            
            # Extract hreflang
            result["hreflang"] = self._extract_hreflang(soup)
            
            # Extract robots meta
            robots_meta = soup.find("meta", attrs={"name": "robots"})
            if robots_meta and robots_meta.get("content"):
                result["robots_meta"] = robots_meta["content"]
            
            # Check for sitemap reference
            sitemap_link = soup.find("link", attrs={"rel": "sitemap"})
            if sitemap_link and sitemap_link.get("href"):
                result["sitemap_reference"] = sitemap_link["href"]
            
            # Check for mixed content
            result["mixed_content"] = self._check_mixed_content(response.text, url)
            
            # Extract security headers from response
            result["security_headers"] = self._extract_security_headers(response.headers)
            
        except Exception as e:
            result["error"] = str(e)
            print(f"  ❌ Error: {e}")
        
        return result

    def _extract_meta_tags(self, soup: BeautifulSoup) -> Dict:
        """Extract meta tags from HTML."""
        meta_tags = {}
        
        # Standard meta tags
        for attr in ["name", "property"]:
            for tag in soup.find_all("meta", attrs={attr: True}):
                key = tag.get(attr)
                content = tag.get("content", "")
                if key and content:
                    meta_tags[key] = content
        
        # Special handling for charset
        charset_tag = soup.find("meta", attrs={"charset": True})
        if charset_tag:
            meta_tags["charset"] = charset_tag.get("charset")
        
        return meta_tags

    def _extract_headings(self, soup: BeautifulSoup) -> Dict[str, int]:
        """Extract heading structure."""
        headings = {"h1": 0, "h2": 0, "h3": 0, "h4": 0, "h5": 0, "h6": 0}
        
        for level in range(1, 7):
            tags = soup.find_all(f"h{level}")
            headings[f"h{level}"] = len(tags)
        
        return headings

    def _extract_schema(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract JSON-LD schema markup."""
        schemas = []
        
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                content = script.string
                if content:
                    schema_data = json.loads(content)
                    if isinstance(schema_data, list):
                        schemas.extend(schema_data)
                    else:
                        schemas.append(schema_data)
            except (json.JSONDecodeError, Exception):
                pass
        
        return schemas

    def _extract_open_graph(self, soup: BeautifulSoup) -> Dict:
        """Extract Open Graph meta tags."""
        og_tags = {}
        
        for tag in soup.find_all("meta", attrs={"property": re.compile(r"^og:")}):
            property_name = tag.get("property", "").replace("og:", "")
            content = tag.get("content", "")
            if property_name and content:
                og_tags[property_name] = content
        
        return og_tags

    def _extract_twitter_card(self, soup: BeautifulSoup) -> Dict:
        """Extract Twitter Card meta tags."""
        twitter_tags = {}
        
        for tag in soup.find_all("meta", attrs={"name": re.compile(r"^twitter:")}):
            name = tag.get("name", "").replace("twitter:", "")
            content = tag.get("content", "")
            if name and content:
                twitter_tags[name] = content
        
        return twitter_tags

    def _extract_hreflang(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract hreflang tags."""
        hreflangs = []
        
        for tag in soup.find_all("link", attrs={"rel": "alternate", "hreflang": True}):
            hreflangs.append(
                {
                    "lang": tag.get("hreflang"),
                    "href": tag.get("href"),
                }
            )
        
        return hreflangs

    def _check_mixed_content(self, html: str, base_url: str) -> bool:
        """Check for mixed content (HTTP resources on HTTPS page)."""
        if not base_url.startswith("https://"):
            return False
        
        # Look for HTTP URLs in src, href, action attributes
        http_pattern = re.compile(r'https?://[^\s"\'<>]+', re.IGNORECASE)
        matches = http_pattern.findall(html)
        
        for match in matches:
            if match.startswith("http://"):
                return True
        
        return False

    def _extract_security_headers(self, headers: httpx.Headers) -> Dict:
        """Extract security-related HTTP headers."""
        security_headers = {}
        
        security_header_names = [
            "strict-transport-security",
            "x-frame-options",
            "x-content-type-options",
            "x-xss-protection",
            "content-security-policy",
            "referrer-policy",
            "permissions-policy",
        ]
        
        for header_name in security_header_names:
            value = headers.get(header_name)
            if value:
                security_headers[header_name] = value
        
        return security_headers

    def analyze_urls(self, urls: List[Dict[str, str]]) -> Dict[str, Dict]:
        """
        Analyze multiple URLs.
        
        Args:
            urls: List of dictionaries with 'url' and optionally 'category' keys.
        
        Returns:
            Dictionary mapping URLs to analysis results.
        """
        results = {}
        
        total = len(urls)
        print(f"\n🔍 Analyzing {total} URLs for on-page elements...\n")
        
        for i, item in enumerate(urls, 1):
            url = item["url"]
            print(f"[{i}/{total}] ", end="")
            result = self.analyze_url(url)
            results[url] = result
        
        print(f"\n✓ On-page analysis complete for {len(results)} URLs")
        
        return results


def main():
    """Main function to run on-page analysis."""
    url_set_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "shopify-analysis"
        / "url_set.json"
    )
    
    if not url_set_path.exists():
        print(f"Error: URL set not found at {url_set_path}")
        print("Please run url_selector.py first.")
        return
    
    with open(url_set_path, "r", encoding="utf-8") as f:
        selected_urls = json.load(f)
    
    analyzer = OnPageAnalyzer()
    results = analyzer.analyze_urls(selected_urls)
    
    # Save results
    output_path = (
        Path(__file__).parent.parent.parent
        / "docs"
        / "shopify-analysis"
        / "onpage_analysis.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Results saved to: {output_path}")
    
    return results


if __name__ == "__main__":
    main()

