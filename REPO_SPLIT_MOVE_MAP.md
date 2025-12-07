# Repository Split Move Map

## Overview
This document specifies the exact source and destination paths for each file/folder during the repo split.

## Assumptions
- **RYU Platform Repo**: `/Users/jose.ugaldevivo/Dev/RYU/RYU` (existing) OR new `ryu-platform` repo
- **Macross Client Repo**: `/Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross` (current, will be cleaned)
- **Suppathletik Client Repo**: To be created separately (not in scope)

## Move Operations

### 1. Platform Code → RYU Platform Repo

#### Source: `Farmacia_Macross/src/mcp_atlassian/`
#### Destination: `RYU/src/mcp_atlassian/` (or `ryu-platform/src/mcp_atlassian/`)

**Action**: Move entire directory tree
```bash
# All files under src/mcp_atlassian/ move as-is
src/mcp_atlassian/ → RYU/src/mcp_atlassian/
```

#### Source: `Farmacia_Macross/tests/`
#### Destination: `RYU/tests/` (or `ryu-platform/tests/`)

**Action**: Move entire directory tree
```bash
tests/ → RYU/tests/
```

#### Source: `Farmacia_Macross/pyproject.toml`
#### Destination: `RYU/pyproject.toml` (or `ryu-platform/pyproject.toml`)

**Action**: Move file (may need merge if RYU repo has existing pyproject.toml)

#### Source: `Farmacia_Macross/uv.lock`
#### Destination: `RYU/uv.lock` (or `ryu-platform/uv.lock`)

**Action**: Move file (may need merge)

#### Source: `Farmacia_Macross/README.md`
#### Destination: `RYU/README.md` (or `ryu-platform/README.md`)

**Action**: Move file (may need merge/rename if RYU has existing README)

#### Source: `Farmacia_Macross/AGENTS.md`
#### Destination: `RYU/AGENTS.md` (or `ryu-platform/AGENTS.md`)

**Action**: Move file

#### Source: `Farmacia_Macross/CONTRIBUTING.md`
#### Destination: `RYU/CONTRIBUTING.md` (or `ryu-platform/CONTRIBUTING.md`)

**Action**: Move file

#### Source: `Farmacia_Macross/SECURITY.md`
#### Destination: `RYU/SECURITY.md` (or `ryu-platform/SECURITY.md`)

**Action**: Move file

#### Source: `Farmacia_Macross/Dockerfile`
#### Destination: `RYU/Dockerfile` (or `ryu-platform/Dockerfile`)

**Action**: Move file

#### Source: `Farmacia_Macross/smithery.yaml`
#### Destination: `RYU/smithery.yaml` (or `ryu-platform/smithery.yaml`)

**Action**: Move file

#### Source: `Farmacia_Macross/LICENSE`
#### Destination: `RYU/LICENSE` (or `ryu-platform/LICENSE`)

**Action**: Move file (may need merge if license differs)

#### Source: `Farmacia_Macross/CURSOR_MCP_CONFIG.md`
#### Destination: `RYU/CURSOR_MCP_CONFIG.md` (or `ryu-platform/CURSOR_MCP_CONFIG.md`)

**Action**: Move file

#### Source: `Farmacia_Macross/cursor-mcp-*.json`
#### Destination: `RYU/cursor-mcp-*.json` (or `ryu-platform/cursor-mcp-*.json`)

**Action**: Move all cursor-mcp config files
- `cursor-mcp-config.json`
- `cursor-mcp-single-server.json`
- `cursor-mcp-multiple-accounts.json`

#### Source: `Farmacia_Macross/MULTIPLE_ACCOUNTS_SETUP.md`
#### Destination: `RYU/MULTIPLE_ACCOUNTS_SETUP.md` (or `ryu-platform/MULTIPLE_ACCOUNTS_SETUP.md`)

**Action**: Move file

#### Source: `Farmacia_Macross/scripts/oauth_authorize.py`
#### Destination: `RYU/scripts/oauth_authorize.py` (or `ryu-platform/scripts/oauth_authorize.py`)

**Action**: Move file (create `scripts/` directory if needed)

#### Source: `Farmacia_Macross/docs/growth/`
#### Destination: `RYU/docs/growth/` (or `ryu-platform/docs/growth/`)

**Action**: Move entire directory
- `ryu-growth-strategy-2025.md`
- `ryu-website-improvements.md`

#### Source: `Farmacia_Macross/docs/governance/`
#### Destination: `RYU/docs/governance/` (or `ryu-platform/docs/governance/`)

**Action**: Move entire directory
- `workflow-improvement-tickets.md`

#### Source: `Farmacia_Macross/docs/backlog-analysis.md`
#### Destination: `RYU/docs/backlog-analysis.md` (or `ryu-platform/docs/backlog-analysis.md`)

**Action**: Move file (if platform-level, not client-specific)

#### Source: `Farmacia_Macross/docs/jira-sprint-assignments.md`
#### Destination: `RYU/docs/jira-sprint-assignments.md` (or `ryu-platform/docs/jira-sprint-assignments.md`)

**Action**: Move file (if platform-level, not client-specific)

### 2. Client Code → Keep in Macross Repo (No Move)

**Action**: Keep these in `Farmacia_Macross/` repo:

- `docs/pm/farmacias-macross-*` (all files)
- `docs/shopify-analysis/` (entire directory)
- `scripts/shopify-analysis/` (entire directory)
- `admin-app/` (entire directory)
- `scripts/import_to_jira.py`
- `scripts/parse_jira_xml.py`
- `scripts/create_remaining_tasks.py`
- `scripts/import_tasks_to_jira.py`
- `Jira (1).xml`
- `scripts/test_with_real_data.sh`

### 3. Other Client → Remove or Move to Separate Repo

#### Source: `Farmacia_Macross/docs/suppathletik/`
#### Destination: `[Suppathletik Repo]/docs/` (to be created separately)

**Action**: Move to separate Suppathletik client repo (out of scope for this split)

#### Source: `Farmacia_Macross/scripts/fetch_suppathletik_jira.py`
#### Destination: `[Suppathletik Repo]/scripts/` (to be created separately)

**Action**: Move to separate Suppathletik client repo

### 4. Ambiguous Files - Needs Decision

#### `Farmacia_Macross/typescript`
**Status**: UNKNOWN
**Action**: Review contents, decide if platform or client

#### `Farmacia_Macross/Farmacia_Macross.code-workspace`
**Status**: CLIENT (workspace file)
**Action**: Keep in Macross repo (or delete if not needed)

## Target Directory Structures

### RYU Platform Repo Structure (After Move)

```
RYU/
├── src/
│   └── mcp_atlassian/          # Moved from Farmacia_Macross
│       ├── jira/
│       ├── confluence/
│       ├── models/
│       ├── servers/
│       ├── utils/
│       ├── preprocessing/
│       └── exceptions.py
├── tests/                       # Moved from Farmacia_Macross
│   ├── unit/
│   ├── integration/
│   ├── fixtures/
│   └── utils/
├── scripts/                     # Created if needed
│   └── oauth_authorize.py      # Moved from Farmacia_Macross
├── docs/
│   ├── growth/                 # Moved from Farmacia_Macross
│   └── governance/              # Moved from Farmacia_Macross
├── pyproject.toml              # Moved from Farmacia_Macross
├── uv.lock                     # Moved from Farmacia_Macross
├── README.md                   # Moved from Farmacia_Macross
├── AGENTS.md                   # Moved from Farmacia_Macross
├── CONTRIBUTING.md             # Moved from Farmacia_Macross
├── SECURITY.md                 # Moved from Farmacia_Macross
├── Dockerfile                  # Moved from Farmacia_Macross
├── smithery.yaml               # Moved from Farmacia_Macross
├── LICENSE                     # Moved from Farmacia_Macross
├── CURSOR_MCP_CONFIG.md       # Moved from Farmacia_Macross
├── cursor-mcp-config.json      # Moved from Farmacia_Macross
├── cursor-mcp-single-server.json # Moved from Farmacia_Macross
├── cursor-mcp-multiple-accounts.json # Moved from Farmacia_Macross
└── MULTIPLE_ACCOUNTS_SETUP.md  # Moved from Farmacia_Macross
```

**Note**: RYU repo currently has frontend code (`src/`, `dist/`, etc.). Platform code should be organized separately, possibly in a subdirectory like `platform/` or `mcp-atlassian/`.

### Macross Client Repo Structure (After Cleanup)

```
Farmacia_Macross/
├── docs/
│   ├── pm/
│   │   └── farmacias-macross-*  # All Macross PM docs
│   └── shopify-analysis/        # All Shopify analysis
├── scripts/
│   ├── shopify-analysis/        # Macross Shopify scripts
│   ├── import_to_jira.py
│   ├── parse_jira_xml.py
│   ├── create_remaining_tasks.py
│   ├── import_tasks_to_jira.py
│   └── test_with_real_data.sh
├── admin-app/                   # Macross Shopify admin app
├── Jira (1).xml                 # Macross Jira export
├── README.md                    # New Macross-specific README
└── .gitignore
```

## Merge Conflicts & Special Cases

### Potential Conflicts

1. **README.md**: RYU repo may have existing README for frontend
   - **Solution**: Rename platform README to `README-MCP.md` or merge content

2. **pyproject.toml**: RYU repo may have existing Python config
   - **Solution**: Merge dependencies or keep separate (platform in subdirectory)

3. **LICENSE**: Both repos should have same license
   - **Solution**: Verify license compatibility

4. **.gitignore**: May need to merge ignore patterns
   - **Solution**: Merge both .gitignore files

### Files Requiring Path Updates

After moving files, these scripts may need path updates:

1. **`scripts/import_to_jira.py`**: References `docs/pm/farmacias-macross-jira-import.json`
   - **Status**: Path remains valid (file stays in Macross repo)

2. **`scripts/shopify-analysis/run_analysis.py`**: May reference paths
   - **Status**: Review for hardcoded paths

## Execution Order

1. Create backup branch in Farmacia_Macross repo
2. Move platform files to RYU repo (or new platform repo)
3. Update any hardcoded paths in moved files
4. Remove moved files from Farmacia_Macross repo
5. Update .gitignore in both repos
6. Test that platform code still works in new location
7. Update documentation references
8. Commit changes to both repos

