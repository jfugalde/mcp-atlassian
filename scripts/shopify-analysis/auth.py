"""Authentication helper for Shopify Admin API."""

import os
from pathlib import Path
from typing import Optional

import httpx

# Try to load from .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    
    # Load .env file from the script directory or parent directories
    script_dir = Path(__file__).parent
    env_file = script_dir / ".env"
    if env_file.exists():
        load_dotenv(env_file)
    else:
        # Try parent directory
        parent_env = script_dir.parent / ".env"
        if parent_env.exists():
            load_dotenv(parent_env)
        else:
            # Try project root
            project_root = script_dir.parent.parent / ".env"
            if project_root.exists():
                load_dotenv(project_root)
except ImportError:
    # python-dotenv not installed, skip .env loading
    pass


def get_access_token() -> Optional[str]:
    """
    Get Shopify Admin API access token from environment variable.
    
    Returns:
        Access token string or None if not found.
    """
    return os.getenv("SHOPIFY_ACCESS_TOKEN")


def get_shop_domain() -> Optional[str]:
    """
    Get Shopify shop domain from environment variable.
    
    Returns:
        Shop domain (e.g., 'macross-pharma.myshopify.com') or None if not found.
    """
    return os.getenv("SHOPIFY_SHOP_DOMAIN", "macross-pharma.myshopify.com")


def get_api_version() -> str:
    """
    Get Shopify API version.
    
    Returns:
        API version string (default: '2025-01').
    """
    return os.getenv("SHOPIFY_API_VERSION", "2025-01")


def create_graphql_client(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
) -> httpx.Client:
    """
    Create an authenticated GraphQL client for Shopify Admin API.
    
    Args:
        shop_domain: Shop domain (e.g., 'macross-pharma.myshopify.com').
                    If None, reads from environment.
        access_token: Admin API access token. If None, reads from environment.
    
    Returns:
        Configured httpx.Client instance.
    
    Raises:
        ValueError: If shop_domain or access_token is missing.
    """
    shop = shop_domain or get_shop_domain()
    token = access_token or get_access_token()
    
    if not shop:
        raise ValueError("Shop domain is required. Set SHOPIFY_SHOP_DOMAIN env var.")
    if not token:
        raise ValueError(
            "Access token is required. Set SHOPIFY_ACCESS_TOKEN env var.\n"
            "You can get this by:\n"
            "1. Installing the admin-app on the store and using OAuth tokens, or\n"
            "2. Creating a private app in Shopify admin and generating an access token."
        )
    
    # Ensure shop domain has .myshopify.com suffix
    if not shop.endswith(".myshopify.com"):
        shop = f"{shop}.myshopify.com"
    
    api_version = get_api_version()
    base_url = f"https://{shop}/admin/api/{api_version}/graphql.json"
    
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": token,
    }
    
    return httpx.Client(base_url=base_url, headers=headers, timeout=30.0)


def execute_graphql_query(
    client: httpx.Client,
    query: str,
    variables: Optional[dict] = None,
) -> dict:
    """
    Execute a GraphQL query against Shopify Admin API.
    
    Args:
        client: Authenticated httpx.Client instance.
        query: GraphQL query string.
        variables: Optional query variables.
    
    Returns:
        JSON response data.
    
    Raises:
        httpx.HTTPStatusError: If the API request fails.
        ValueError: If the response contains GraphQL errors.
    """
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    
    response = client.post("", json=payload)
    response.raise_for_status()
    
    data = response.json()
    
    if "errors" in data:
        error_messages = [err.get("message", str(err)) for err in data["errors"]]
        raise ValueError(f"GraphQL errors: {'; '.join(error_messages)}")
    
    return data.get("data", {})

