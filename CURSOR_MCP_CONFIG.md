# Cursor MCP Configuration for mcp-atlassian

## Local Installation Configuration

Since you're running the server locally (not via Docker), use this configuration in Cursor:

1. Open Cursor Settings → MCP → + Add new global MCP server

2. Use this JSON configuration:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross",
        "mcp-atlassian"
      ],
      "env": {
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "your_jira_api_token",
        "CONFLUENCE_URL": "https://your-company.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_confluence_api_token"
      }
    }
  }
}
```

## Alternative: Using .env File

If you prefer to use a `.env` file (recommended for security):

1. Create a `.env` file in this directory with your credentials
2. Use this configuration:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross",
        "mcp-atlassian",
        "--env-file",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross/.env"
      ]
    }
  }
}
```

## Testing the Server

To test if the server works correctly, you can use the MCP Inspector:

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross
npx @modelcontextprotocol/inspector uv run --directory . mcp-atlassian
```

## Notes

- Replace the placeholder URLs and credentials with your actual Atlassian instance details
- For Server/Data Center, use `JIRA_PERSONAL_TOKEN` and `CONFLUENCE_PERSONAL_TOKEN` instead of username/token
- The server will automatically start when Cursor needs it - you don't need to run it manually




