"""Configuration module for Jira API interactions."""

import logging
import os
from dataclasses import dataclass
from typing import Literal

from ..utils.env import get_custom_headers, is_env_ssl_verify
from ..utils.oauth import (
    BYOAccessTokenOAuthConfig,
    OAuthConfig,
    get_oauth_config_from_env,
)
from ..utils.urls import is_atlassian_cloud_url


@dataclass
class JiraConfig:
    """Jira API configuration.

    Handles authentication for Jira Cloud and Server/Data Center:
    - Cloud: username/API token (basic auth) or OAuth 2.0 (3LO)
    - Server/DC: personal access token or basic auth
    """

    url: str  # Base URL for Jira
    auth_type: Literal["basic", "pat", "oauth"]  # Authentication type
    username: str | None = None  # Email or username (Cloud)
    api_token: str | None = None  # API token (Cloud)
    personal_token: str | None = None  # Personal access token (Server/DC)
    oauth_config: OAuthConfig | BYOAccessTokenOAuthConfig | None = None
    ssl_verify: bool = True  # Whether to verify SSL certificates
    projects_filter: str | None = None  # List of project keys to filter searches
    http_proxy: str | None = None  # HTTP proxy URL
    https_proxy: str | None = None  # HTTPS proxy URL
    no_proxy: str | None = None  # Comma-separated list of hosts to bypass proxy
    socks_proxy: str | None = None  # SOCKS proxy URL (optional)
    custom_headers: dict[str, str] | None = None  # Custom HTTP headers

    @property
    def is_cloud(self) -> bool:
        """Check if this is a cloud instance.

        Returns:
            True if this is a cloud instance (atlassian.net), False otherwise.
            Localhost URLs are always considered non-cloud (Server/Data Center).
        """
        # Multi-Cloud OAuth mode: URL might be None, but we use api.atlassian.com
        if (
            self.auth_type == "oauth"
            and self.oauth_config
            and self.oauth_config.cloud_id
        ):
            # OAuth with cloud_id uses api.atlassian.com which is always Cloud
            return True

        # For other auth types, check the URL
        return is_atlassian_cloud_url(self.url) if self.url else False

    @property
    def verify_ssl(self) -> bool:
        """Compatibility property for old code.

        Returns:
            The ssl_verify value
        """
        return self.ssl_verify

    @classmethod
    def from_env(cls, prefix: str | None = None) -> "JiraConfig":
        """Create configuration from environment variables.

        Args:
            prefix: Optional prefix for environment variables (e.g., "suppathletik" for
                JIRA_URL_suppathletik, JIRA_USERNAME_suppathletik, etc.).
                If None, uses default JIRA_* variables.

        Returns:
            JiraConfig with values from environment variables

        Raises:
            ValueError: If required environment variables are missing or invalid
        """

        # Build environment variable names with optional prefix
        def env_name(base: str) -> str:
            return f"{base}_{prefix}" if prefix else base

        url = os.getenv(env_name("JIRA_URL"))
        oauth_enable = os.getenv(env_name("ATLASSIAN_OAUTH_ENABLE"))
        if not url and not oauth_enable:
            var_name = env_name("JIRA_URL")
            error_msg = f"Missing required {var_name} environment variable"
            raise ValueError(error_msg)

        # url is required for non-OAuth configs
        if not url:
            url = ""  # Will be handled by OAuth flow

        # Determine authentication type based on available environment variables
        username = os.getenv(env_name("JIRA_USERNAME"))
        api_token = os.getenv(env_name("JIRA_API_TOKEN"))
        personal_token = os.getenv(env_name("JIRA_PERSONAL_TOKEN"))

        # Check for OAuth configuration (OAuth doesn't support prefixes yet)
        # For now, OAuth uses default env vars regardless of prefix
        oauth_config = get_oauth_config_from_env() if not prefix else None
        auth_type: Literal["basic", "pat", "oauth"] | None = None

        # Use the shared utility function directly
        is_cloud = is_atlassian_cloud_url(url) if url else False

        if oauth_config:
            # OAuth is available - could be full config or minimal config
            auth_type = "oauth"
        elif is_cloud:
            if username and api_token:
                auth_type = "basic"
            else:
                username_var = env_name("JIRA_USERNAME")
                token_var = env_name("JIRA_API_TOKEN")
                error_msg = (
                    f"Cloud authentication requires {username_var} and "
                    f"{token_var}, or OAuth configuration "
                    "(set ATLASSIAN_OAUTH_ENABLE=true for user-provided tokens)"
                )
                raise ValueError(error_msg)
        else:  # Server/Data Center
            if personal_token:
                auth_type = "pat"
            elif username and api_token:
                # Allow basic auth for Server/DC too
                auth_type = "basic"
            else:
                pat_var = env_name("JIRA_PERSONAL_TOKEN")
                username_var = env_name("JIRA_USERNAME")
                token_var = env_name("JIRA_API_TOKEN")
                error_msg = (
                    f"Server/Data Center authentication requires "
                    f"{pat_var} or {username_var} and {token_var}"
                )
                raise ValueError(error_msg)

        # SSL verification (for Server/DC)
        ssl_verify = is_env_ssl_verify(env_name("JIRA_SSL_VERIFY"))

        # Get the projects filter if provided
        projects_filter = os.getenv(env_name("JIRA_PROJECTS_FILTER"))

        # Proxy settings (with fallback to unprefixed)
        http_proxy = os.getenv(
            env_name("JIRA_HTTP_PROXY"),
            os.getenv("JIRA_HTTP_PROXY", os.getenv("HTTP_PROXY")),
        )
        https_proxy = os.getenv(
            env_name("JIRA_HTTPS_PROXY"),
            os.getenv("JIRA_HTTPS_PROXY", os.getenv("HTTPS_PROXY")),
        )
        no_proxy = os.getenv(
            env_name("JIRA_NO_PROXY"),
            os.getenv("JIRA_NO_PROXY", os.getenv("NO_PROXY")),
        )
        socks_proxy = os.getenv(
            env_name("JIRA_SOCKS_PROXY"),
            os.getenv("JIRA_SOCKS_PROXY", os.getenv("SOCKS_PROXY")),
        )

        # Custom headers - service-specific only
        custom_headers = get_custom_headers(env_name("JIRA_CUSTOM_HEADERS"))

        # url is required for non-OAuth configs
        if not url and auth_type != "oauth":
            var_name = env_name("JIRA_URL")
            error_msg = f"Missing required {var_name} environment variable"
            raise ValueError(error_msg)

        return cls(
            url=url or "",  # Empty string for OAuth-only configs
            auth_type=auth_type,
            username=username,
            api_token=api_token,
            personal_token=personal_token,
            oauth_config=oauth_config,
            ssl_verify=ssl_verify,
            projects_filter=projects_filter,
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            no_proxy=no_proxy,
            socks_proxy=socks_proxy,
            custom_headers=custom_headers,
        )

    def is_auth_configured(self) -> bool:
        """Check if authentication configuration is complete and valid.

        Returns:
            bool: True if authentication is fully configured, False otherwise.
        """
        logger = logging.getLogger("mcp-atlassian.jira.config")
        if self.auth_type == "oauth":
            # Handle different OAuth configuration types
            if self.oauth_config:
                # Full OAuth configuration (traditional mode)
                if isinstance(self.oauth_config, OAuthConfig):
                    if (
                        self.oauth_config.client_id
                        and self.oauth_config.client_secret
                        and self.oauth_config.redirect_uri
                        and self.oauth_config.scope
                        and self.oauth_config.cloud_id
                    ):
                        return True
                    # Minimal OAuth configuration (user-provided tokens mode)
                    # This is valid if we have oauth_config but missing client
                    # credentials. In this case, we expect authentication to come
                    # from user-provided headers
                    elif (
                        not self.oauth_config.client_id
                        and not self.oauth_config.client_secret
                    ):
                        logger.debug(
                            "Minimal OAuth config detected - expecting "
                            "user-provided tokens via headers"
                        )
                        return True
                # Bring Your Own Access Token mode
                elif isinstance(self.oauth_config, BYOAccessTokenOAuthConfig):
                    if self.oauth_config.cloud_id and self.oauth_config.access_token:
                        return True

            # Partial configuration is invalid
            logger.warning("Incomplete OAuth configuration detected")
            return False
        elif self.auth_type == "pat":
            return bool(self.personal_token)
        elif self.auth_type == "basic":
            return bool(self.username and self.api_token)
        # Defensive fallback (unreachable in practice due to Literal type)
        logger.warning(
            f"Unknown or unsupported auth_type: " f"{self.auth_type} in JiraConfig"
        )
        return False  # noqa: RET503
