"""Query store configuration from Shopify store."""

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


def query_store_config(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Dict:
    """
    Query store configuration from the Shopify store.
    
    Args:
        shop_domain: Shop domain. If None, reads from environment.
        access_token: Access token. If None, reads from environment.
    
    Returns:
        Dictionary containing store configuration data.
    """
    client = create_graphql_client(shop_domain, access_token)
    
    try:
        query = load_query("store_settings")
        data = execute_graphql_query(client, query)
        
        return data.get("shop", {})
    finally:
        client.close()


def format_store_config(shop_data: Dict) -> Dict:
    """
    Format store configuration data into a structured dictionary.
    
    Args:
        shop_data: Raw shop data from GraphQL query.
    
    Returns:
        Formatted store configuration dictionary.
    """
    plan = shop_data.get("plan", {})
    features = shop_data.get("features", {})
    payment_settings = shop_data.get("paymentSettings", {})
    primary_domain = shop_data.get("primaryDomain", {})
    
    return {
        "basic_info": {
            "id": shop_data.get("id"),
            "name": shop_data.get("name"),
            "email": shop_data.get("email"),
            "myshopify_domain": shop_data.get("myshopifyDomain"),
            "primary_domain": primary_domain.get("host"),
            "ssl_enabled": primary_domain.get("sslEnabled"),
        },
        "plan": {
            "display_name": plan.get("publicDisplayName"),
            "shopify_plus": plan.get("shopifyPlus", False),
            "partner_development": plan.get("partnerDevelopment", False),
        },
        "currency": {
            "code": shop_data.get("currencyCode"),
            "enabled_presentment_currencies": shop_data.get(
                "enabledPresentmentCurrencies", []
            ),
        },
        "features": {
            "avalara_avatax": features.get("avalaraAvatax", False),
            "branding": features.get("branding"),
            "captcha": features.get("captcha", False),
            "gift_cards": features.get("giftCards", False),
            "storefront": features.get("storefront", False),
            "reports": features.get("reports", False),
            "live_view": features.get("liveView", False),
            "show_metrics": features.get("showMetrics", False),
        },
        "payment_settings": {
            "supported_digital_wallets": payment_settings.get(
                "supportedDigitalWallets", []
            ),
        },
        "timezone": {
            "abbreviation": shop_data.get("timezoneAbbreviation"),
            "iana": shop_data.get("ianaTimezone"),
        },
        "timestamps": {
            "created_at": shop_data.get("createdAt"),
            "updated_at": shop_data.get("updatedAt"),
        },
    }


def main():
    """Main function to query and display store configuration."""
    try:
        print("Querying store configuration...")
        shop_data = query_store_config()
        formatted = format_store_config(shop_data)
        
        print(f"\nStore: {formatted['basic_info']['name']}")
        print(f"Plan: {formatted['plan']['display_name']}")
        print(f"Shopify Plus: {formatted['plan']['shopify_plus']}")
        print(f"Currency: {formatted['currency']['code']}")
        print(f"Storefront Enabled: {formatted['features']['storefront']}")
        
        # Save to JSON file
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "store_config.json"
        
        with open(output_file, "w") as f:
            json.dump(formatted, f, indent=2)
        
        print(f"\nData saved to: {output_file}")
        
        return formatted
    except Exception as e:
        print(f"Error querying store config: {e}")
        raise


if __name__ == "__main__":
    main()

