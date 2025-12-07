"""Query installed apps from Shopify store."""

import json
from pathlib import Path
from typing import Dict, List, Optional

from auth import create_graphql_client, execute_graphql_query


def load_query(query_name: str) -> str:
    """
    Load a GraphQL query from the queries directory.
    
    Args:
        query_name: Name of the query file (without .graphql extension).
    
    Returns:
        GraphQL query string.
    """
    script_dir = Path(__file__).parent
    query_path = script_dir / "queries" / f"{query_name}.graphql"
    
    if not query_path.exists():
        raise FileNotFoundError(f"Query file not found: {query_path}")
    
    return query_path.read_text()


def query_installed_apps(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Dict:
    """
    Query all installed apps from the Shopify store.
    
    Args:
        shop_domain: Shop domain. If None, reads from environment.
        access_token: Access token. If None, reads from environment.
    
    Returns:
        Dictionary containing app installation data.
    """
    client = create_graphql_client(shop_domain, access_token)
    
    try:
        query = load_query("installed_apps")
        data = execute_graphql_query(client, query)
        
        return data.get("appInstallations", {})
    finally:
        client.close()


def format_apps_data(apps_data: Dict) -> List[Dict]:
    """
    Format app installation data into a structured list.
    
    Args:
        apps_data: Raw app installations data from GraphQL query.
    
    Returns:
        List of formatted app dictionaries.
    """
    apps = []
    nodes = apps_data.get("nodes", [])
    
    for node in nodes:
        app_info = node.get("app", {})
        app = {
            "id": node.get("id"),
            "app_id": app_info.get("id"),
            "name": app_info.get("title", "Unknown"),
            "handle": app_info.get("handle"),
            "developer": app_info.get("developerName", "Unknown"),
            "developer_type": app_info.get("developerType"),
            "category": app_info.get("publicCategory"),
            "description": app_info.get("description"),
            "pricing": app_info.get("pricingDetailsSummary", "Free"),
            "published": app_info.get("published", False),
            "embedded": app_info.get("embedded", False),
            "requested_scopes": [
                scope.get("handle")
                for scope in app_info.get("requestedAccessScopes", [])
            ],
            "granted_scopes": [
                scope.get("handle") for scope in node.get("accessScopes", [])
            ],
            "subscriptions": [
                {
                    "name": sub.get("name"),
                    "status": sub.get("status"),
                    "period_end": sub.get("currentPeriodEnd"),
                }
                for sub in node.get("activeSubscriptions", [])
            ],
            "launch_url": node.get("launchUrl"),
        }
        apps.append(app)
    
    return apps


def main():
    """Main function to query and display installed apps."""
    try:
        print("Querying installed apps...")
        apps_data = query_installed_apps()
        apps = format_apps_data(apps_data)
        
        print(f"\nFound {len(apps)} installed apps:\n")
        for app in apps:
            print(f"- {app['name']} (by {app['developer']})")
            print(f"  Category: {app['category']}")
            print(f"  Pricing: {app['pricing']}")
            print(f"  Scopes: {len(app['granted_scopes'])} granted")
            if app["subscriptions"]:
                print(f"  Active Subscriptions: {len(app['subscriptions'])}")
            print()
        
        # Save to JSON file
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        output_file = output_path / "installed_apps.json"
        
        with open(output_file, "w") as f:
            json.dump(apps, f, indent=2)
        
        print(f"Data saved to: {output_file}")
        
        return apps
    except Exception as e:
        print(f"Error querying apps: {e}")
        raise


if __name__ == "__main__":
    main()

