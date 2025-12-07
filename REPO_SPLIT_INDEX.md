# Repository Split Planning - Master Index

## Overview

This directory contains the complete planning documentation for splitting the Farmacia_Macross repository to separate RYU platform code from Macross client-specific deliverables.

## Documents

### 1. [REPO_SPLIT_INVENTORY.md](./REPO_SPLIT_INVENTORY.md)
**Purpose**: Complete inventory and classification of all files/folders

**Contents**:
- Classification of all files as Platform, Client, Shared, or Other
- Detailed breakdown by directory
- Summary statistics

**Use this when**: You need to understand what files belong where

### 2. [REPO_SPLIT_MOVE_MAP.md](./REPO_SPLIT_MOVE_MAP.md)
**Purpose**: Exact source and destination paths for migration

**Contents**:
- Detailed move operations for each file/folder
- Target directory structures for both repos
- Merge conflict identification
- Files requiring path updates

**Use this when**: You're ready to execute the migration

### 3. [REPO_SPLIT_SETUP_PLAN.md](./REPO_SPLIT_SETUP_PLAN.md)
**Purpose**: Repository setup and configuration

**Contents**:
- Repository structure decisions
- .gitignore configurations
- Branching strategy
- CI/CD setup considerations
- Dependency management approach
- Verification checklist

**Use this when**: Setting up the new repository structure

### 4. [REPO_SPLIT_CUTOVER_RUNBOOK.md](./REPO_SPLIT_CUTOVER_RUNBOOK.md)
**Purpose**: Step-by-step execution guide

**Contents**:
- Pre-cutover checklist
- Phase-by-phase execution steps
- Git commands for each step
- Verification procedures
- Rollback procedures
- Troubleshooting guide

**Use this when**: Executing the actual migration

## Quick Start

1. **Review the inventory** to understand what's being split
2. **Check the move map** to see where files will go
3. **Review the setup plan** to understand the target structure
4. **Follow the runbook** to execute the migration

## Key Decisions

### Repository Structure
- **RYU Platform**: New `ryu-platform` repo (recommended) OR subdirectory in existing RYU repo
- **Macross Client**: Keep in `Farmacia_Macross` repo (cleaned up)

### Platform Code (→ RYU Platform)
- `src/mcp_atlassian/` - Core MCP server
- `tests/` - Test suite
- `pyproject.toml`, `uv.lock` - Python config
- Platform documentation (`docs/growth/`, `docs/governance/`)
- Platform config files (Dockerfile, README, etc.)

### Client Code (→ Stay in Macross)
- `docs/pm/farmacias-macross-*` - PM documentation
- `docs/shopify-analysis/` - Shopify audit
- `scripts/shopify-analysis/` - Client scripts
- `admin-app/` - Shopify admin app
- Client-specific Jira imports/exports

### Other Client (→ Separate Repo)
- `docs/suppathletik/` - Suppathletik client docs
- `scripts/fetch_suppathletik_jira.py` - Suppathletik script

## Migration Phases

1. **Preparation**: Backup, review, setup
2. **Migration**: Move platform files
3. **Cleanup**: Remove platform code from client repo
4. **Verification**: Test both repos
5. **Finalization**: Merge to main, update docs

## Estimated Timeline

- **Preparation**: 1-2 hours
- **Migration**: 2-4 hours
- **Verification**: 1-2 hours
- **Total**: 4-8 hours

## Success Criteria

✅ Platform code in dedicated repo and working  
✅ Client code clean (no platform code)  
✅ Both repos build/test successfully  
✅ Documentation updated  
✅ No broken dependencies  

## Getting Help

If you encounter issues:

1. Check the **Troubleshooting** section in the runbook
2. Review the **Rollback Procedure** if needed
3. Consult the **Verification Checklist** to identify issues

## Next Steps

1. Review all planning documents
2. Get approval for the split approach
3. Execute the runbook
4. Verify success criteria
5. Update team documentation

---

**Created**: 2025-01-27  
**Status**: Planning Complete - Ready for Execution  
**Owner**: PMO

