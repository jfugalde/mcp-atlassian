# Multiple Accounts Setup Guide

You can configure multiple Atlassian accounts by creating separate `.env` files. There are two approaches:

## Approach 1: Single MCP Server (Recommended)

Use **one MCP server** and switch between accounts by changing the `.env` file path in the configuration. This avoids duplicate tools.

### Setup:

1. **Create separate .env files:**
   - `.env` - Account 1 (default)
   - `.env.account2` - Account 2
   - `.env.account3` - Account 3 (if needed)

2. **Configure ONE MCP server in Cursor:**

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

3. **To switch accounts:**
   - Change the `--env-file` path in Cursor settings
   - Or rename your `.env` files (e.g., rename `.env.account2` to `.env`)
   - Restart/reload the MCP server in Cursor

### Pros:
- ✅ No duplicate tools
- ✅ Cleaner interface
- ✅ One set of tools

### Cons:
- ⚠️ Can only use one account at a time
- ⚠️ Need to manually switch when changing accounts

---

## Approach 2: Multiple MCP Servers (Advanced)

Use **multiple MCP servers** if you need to access both accounts simultaneously. This will create duplicate tools (one set per server).

### Setup:

1. **Create separate .env files** (same as Approach 1)

2. **Configure MULTIPLE MCP servers in Cursor:**

```json
{
  "mcpServers": {
    "mcp-atlassian-account1": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross",
        "mcp-atlassian",
        "--env-file",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross/.env"
      ]
    },
    "mcp-atlassian-account2": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross",
        "mcp-atlassian",
        "--env-file",
        "/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross/.env.account2"
      ]
    }
  }
}
```

### Pros:
- ✅ Can use both accounts simultaneously
- ✅ Tools are prefixed with server name (e.g., `mcp-atlassian-account1_jira_get_issue`)

### Cons:
- ⚠️ Duplicate tools (one set per account)
- ⚠️ More cluttered interface
- ⚠️ Need to specify which server to use

---

## Approach 3: Environment Variables (No .env files)

Pass credentials directly in the MCP configuration (not recommended for security, but useful for quick switching):

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
        "JIRA_URL": "https://account1.atlassian.net",
        "JIRA_USERNAME": "user1@example.com",
        "JIRA_API_TOKEN": "token1"
      }
    }
  }
}
```

To switch, just change the `env` values in Cursor settings.

---

## Recommendation

**Use Approach 1** (Single MCP Server) if you typically work with one account at a time. It's cleaner and avoids tool duplication.

**Use Approach 2** (Multiple MCP Servers) only if you need to access both accounts simultaneously in the same session.

## Security Note

- Never commit `.env` files to version control (already in `.gitignore`)
- Keep each account's credentials in separate files
- Use descriptive names for your `.env` files
