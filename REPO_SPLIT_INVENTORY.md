# Repository Split Inventory: RYU Platform vs Macross Client

## Classification Legend
- **PLATFORM (RYU)**: Core RYU platform code, reusable across clients
- **CLIENT (MACROSS)**: Macross client-specific deliverables
- **SHARED**: Could be used by multiple clients (needs review)
- **OTHER_CLIENT**: Belongs to another client (e.g., Suppathletik)
- **PLATFORM_DOCS**: RYU platform documentation/strategy

## Top-Level Inventory

### Platform (RYU) - Move to `RYU` repo or new `ryu-platform` repo

| Path | Type | Notes |
|------|------|-------|
| `src/mcp_atlassian/` | PLATFORM | Core MCP Atlassian server implementation |
| `tests/` | PLATFORM | Test suite for MCP Atlassian |
| `pyproject.toml` | PLATFORM | Python project config for MCP Atlassian |
| `uv.lock` | PLATFORM | Dependency lock file |
| `README.md` | PLATFORM | MCP Atlassian documentation |
| `AGENTS.md` | PLATFORM | Agent guidelines for MCP Atlassian |
| `CONTRIBUTING.md` | PLATFORM | Contribution guidelines |
| `SECURITY.md` | PLATFORM | Security documentation |
| `Dockerfile` | PLATFORM | Docker image for MCP server |
| `smithery.yaml` | PLATFORM | Smithery registry config |
| `LICENSE` | PLATFORM | MIT license |
| `CURSOR_MCP_CONFIG.md` | PLATFORM | MCP configuration docs |
| `cursor-mcp-config.json` | PLATFORM | MCP config example |
| `cursor-mcp-single-server.json` | PLATFORM | MCP config example |
| `cursor-mcp-multiple-accounts.json` | PLATFORM | MCP config example |
| `MULTIPLE_ACCOUNTS_SETUP.md` | PLATFORM | Multi-account setup docs |
| `scripts/oauth_authorize.py` | PLATFORM | OAuth setup script (if generic) |
| `docs/growth/ryu-growth-strategy-2025.md` | PLATFORM_DOCS | RYU platform strategy |
| `docs/growth/ryu-website-improvements.md` | PLATFORM_DOCS | RYU platform docs |
| `docs/governance/workflow-improvement-tickets.md` | PLATFORM_DOCS | Platform governance |
| `docs/backlog-analysis.md` | PLATFORM_DOCS | Platform backlog (if not client-specific) |
| `docs/jira-sprint-assignments.md` | PLATFORM_DOCS | Platform sprint planning (if not client-specific) |

### Client (Macross) - Keep in `Farmacia_Macross` repo

| Path | Type | Notes |
|------|------|-------|
| `docs/pm/farmacias-macross-*` | CLIENT | All Macross PM documentation |
| `docs/shopify-analysis/` | CLIENT | Macross Shopify audit and analysis |
| `scripts/shopify-analysis/` | CLIENT | Macross-specific Shopify analysis scripts |
| `admin-app/` | CLIENT | Macross Shopify admin app |
| `scripts/import_to_jira.py` | CLIENT | Imports Macross-specific Jira data |
| `scripts/parse_jira_xml.py` | CLIENT | Parses Macross Jira XML export |
| `scripts/create_remaining_tasks.py` | CLIENT | Creates Macross tasks (references Macross docs) |
| `scripts/import_tasks_to_jira.py` | CLIENT | Imports Macross tasks |
| `scripts/fetch_suppathletik_jira.py` | OTHER_CLIENT | Suppathletik client script (wrong location) |
| `Jira (1).xml` | CLIENT | Macross Jira export |
| `scripts/test_with_real_data.sh` | CLIENT | Macross testing script |

### Other Client - Move to appropriate client repo

| Path | Type | Notes |
|------|------|-------|
| `docs/suppathletik/` | OTHER_CLIENT | Suppathletik client docs (should be in separate repo) |

### Ambiguous - Needs Review

| Path | Type | Notes |
|------|------|-------|
| `typescript` | UNKNOWN | Empty or unclear purpose |
| `Farmacia_Macross.code-workspace` | UNKNOWN | VS Code workspace file (may reference both) |

## Detailed File Classification

### Platform Code (`src/mcp_atlassian/`)
- **Status**: 100% PLATFORM
- **Action**: Move entire directory to RYU platform repo
- **Structure**: 
  - `jira/` - Jira client implementation
  - `confluence/` - Confluence client implementation
  - `models/` - Pydantic models
  - `servers/` - FastMCP server implementations
  - `utils/` - Shared utilities
  - `preprocessing/` - Content preprocessing
  - `exceptions.py` - Exception classes

### Tests (`tests/`)
- **Status**: 100% PLATFORM
- **Action**: Move entire directory to RYU platform repo
- **Structure**:
  - `unit/` - Unit tests
  - `integration/` - Integration tests
  - `fixtures/` - Test fixtures
  - `utils/` - Test utilities

### Client Documentation (`docs/pm/farmacias-macross-*`)
- **Status**: 100% CLIENT
- **Action**: Keep in Macross repo
- **Files**:
  - `farmacias-macross-acceptance-criteria.md`
  - `farmacias-macross-client-comms.md`
  - `farmacias-macross-epics.md`
  - `farmacias-macross-handoff.md`
  - `farmacias-macross-index.md`
  - `farmacias-macross-jira-import.json`
  - `farmacias-macross-risks.md`
  - `farmacias-macross-technical-specs.md`
  - `farmacias-macross-timeline.md`
  - `task-improvement-status.md` (if Macross-specific)

### Client Analysis (`docs/shopify-analysis/`)
- **Status**: 100% CLIENT
- **Action**: Keep in Macross repo
- **Contents**: Shopify audit PDFs, JSON analysis results, performance data

### Client Scripts (`scripts/shopify-analysis/`)
- **Status**: 100% CLIENT
- **Action**: Keep in Macross repo
- **Note**: These scripts are Macross-specific (references `macross-pharma.myshopify.com`)

### Admin App (`admin-app/`)
- **Status**: CLIENT (likely)
- **Action**: Keep in Macross repo
- **Note**: Shopify admin app, likely Macross-specific

## Summary Statistics

- **Platform Files**: ~200+ files (src/, tests/, config files)
- **Client Files**: ~50+ files (docs/pm/, docs/shopify-analysis/, scripts/)
- **Other Client Files**: ~5 files (Suppathletik docs)
- **Ambiguous**: ~2 files (needs review)

## Next Steps

1. ✅ Complete inventory (this document)
2. ⏳ Create move map with exact paths
3. ⏳ Define target directory structures
4. ⏳ Create cutover runbook
5. ⏳ Execute migration

