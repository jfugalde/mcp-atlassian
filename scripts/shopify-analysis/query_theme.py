"""Query theme information from Shopify store."""

import json
from pathlib import Path
from typing import Dict, Optional

from auth import create_graphql_client, execute_graphql_query


def load_query(query_name: str) -> str:
    """Load a GraphQL query from the queries directory."""
    script_dir = Path(__file__).parent
    query_path = script_dir / "queries" / f"{query_name}.graphql"
    
    if not query_path.exists():
        raise FileNotFoundError(f"Query file not found: {query_path}")
    
    return query_path.read_text()


def query_theme_info(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Dict:
    """
    Query theme information from the Shopify store.
    
    Args:
        shop_domain: Shop domain. If None, reads from environment.
        access_token: Access token. If None, reads from environment.
    
    Returns:
        Dictionary containing theme and shop data.
    """
    client = create_graphql_client(shop_domain, access_token)
    
    try:
        query = load_query("theme_info")
        data = execute_graphql_query(client, query)
        
        return data
    finally:
        client.close()


def format_theme_data(theme_data: Dict) -> Dict:
    """
    Format theme data into a structured dictionary.
    
    Args:
        theme_data: Raw theme data from GraphQL query.
    
    Returns:
        Formatted theme information dictionary.
    """
    themes = theme_data.get("themes", {}).get("nodes", [])
    shop = theme_data.get("shop", {})
    
    # Find published theme
    published_theme = None
    for theme in themes:
        if theme.get("role") == "MAIN":
            published_theme = theme
            break
    
    return {
        "shop": {
            "id": shop.get("id"),
            "name": shop.get("name"),
            "domain": shop.get("myshopifyDomain"),
            "primary_domain": shop.get("primaryDomain", {}).get("host"),
        },
        "published_theme": {
            "id": published_theme.get("id") if published_theme else None,
            "name": published_theme.get("name") if published_theme else None,
            "role": published_theme.get("role") if published_theme else None,
            "created_at": published_theme.get("createdAt") if published_theme else None,
            "updated_at": published_theme.get("updatedAt") if published_theme else None,
            "theme_store_id": published_theme.get("themeStoreId")
            if published_theme
            else None,
        },
        "all_themes": [
            {
                "id": theme.get("id"),
                "name": theme.get("name"),
                "role": theme.get("role"),
                "created_at": theme.get("createdAt"),
                "updated_at": theme.get("updatedAt"),
            }
            for theme in themes
        ],
        "total_themes": len(themes),
    }


def main():
    """Main function to query and display theme information."""
    try:
        print("Querying theme information...")
        theme_data = query_theme_info()
        formatted = format_theme_data(theme_data)
        
        print(f"\nShop: {formatted['shop']['name']}")
        print(f"Domain: {formatted['shop']['primary_domain']}")
        print(f"\nPublished Theme: {formatted['published_theme']['name']}")
        print(f"Total Themes: {formatted['total_themes']}")
        
        # Save to JSON file
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "theme_info.json"
        
        with open(output_file, "w") as f:
            json.dump(formatted, f, indent=2)
        
        print(f"\nData saved to: {output_file}")
        
        return formatted
    except Exception as e:
        print(f"Error querying theme info: {e}")
        raise


if __name__ == "__main__":
    main()

