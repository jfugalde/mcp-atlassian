# Repository Split Setup Plan

## Overview
This document outlines the setup steps for creating/maintaining the separated repositories after the split.

## Repository Structure Decision

### Option A: Use Existing RYU Repo (Recommended if frontend is separate)
- **Current State**: RYU repo contains frontend website code
- **Approach**: Create `platform/` or `mcp-atlassian/` subdirectory in RYU repo
- **Pros**: Single RYU repo, easier to manage
- **Cons**: Mixed concerns (frontend + platform)

### Option B: Create New `ryu-platform` Repo (Recommended for clean separation)
- **Approach**: Create new dedicated repo for MCP Atlassian platform code
- **Pros**: Clean separation, independent versioning, clearer ownership
- **Cons**: Additional repo to manage

**Recommendation**: **Option B** - Create new `ryu-platform` repo for cleaner separation.

## Setup Steps

### 1. Create RYU Platform Repo (if new)

```bash
# Create new repo directory
cd /Users/jose.ugaldevivo/Dev/RYU
mkdir ryu-platform
cd ryu-platform

# Initialize git repo
git init
git remote add origin <github-url-for-ryu-platform>

# Create initial structure
mkdir -p src/mcp_atlassian
mkdir -p tests
mkdir -p scripts
mkdir -p docs/growth
mkdir -p docs/governance
```

### 2. Setup .gitignore for RYU Platform

Create `.gitignore` in RYU platform repo:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.hypothesis/

# MCP
.mcp-atlassian/
*.log

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
.env.*.local

# Type checking
.mypy_cache/
.dmypy.json
dmypy.json

# Ruff
.ruff_cache/
```

### 3. Setup .gitignore for Macross Client Repo

Update `.gitignore` in Farmacia_Macross repo (remove platform-specific ignores, keep client-specific):

```gitignore
# Python (for client scripts)
__pycache__/
*.py[cod]
*$py.class
venv/
.venv/

# Node.js (for admin-app)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Client-specific
docs/shopify-analysis/perf_runs/*.json
# Keep analysis results but ignore large perf data if needed
```

### 4. Branching Strategy

#### For RYU Platform Repo:
```bash
# Create feature branch for migration
git checkout -b feature/repo-split-migration

# After migration complete, merge to main
git checkout main
git merge feature/repo-split-migration
```

#### For Macross Client Repo:
```bash
# Create backup branch before cleanup
git checkout -b backup/pre-split-state

# Create cleanup branch
git checkout -b feature/remove-platform-code

# After cleanup, merge to main
git checkout main
git merge feature/remove-platform-code
```

### 5. Update README Files

#### RYU Platform README
- Keep existing MCP Atlassian README content
- Add note about repo split
- Update any path references

#### Macross Client README
Create new `README.md` in Macross repo:

```markdown
# Farmacias Macross - Client Project

This repository contains client-specific deliverables for Farmacias Macross.

## Structure

- `docs/pm/` - Project management documentation
- `docs/shopify-analysis/` - Shopify audit and analysis
- `scripts/` - Client-specific automation scripts
- `admin-app/` - Shopify admin application

## Related Repositories

- [RYU Platform](https://github.com/...) - Core MCP Atlassian platform
```

### 6. CI/CD Setup (if applicable)

#### RYU Platform CI
- Run tests: `uv run pytest`
- Lint: `pre-commit run --all-files`
- Build Docker image
- Publish to registry (if applicable)

#### Macross Client CI
- Run client scripts validation
- Build admin-app (if applicable)
- No platform tests needed

### 7. Dependency Management

#### RYU Platform
- Use `uv` for Python dependencies (as per AGENTS.md)
- Maintain `pyproject.toml` and `uv.lock`
- No changes needed

#### Macross Client
- Client scripts may depend on platform code
- **Decision needed**: 
  - Option A: Install `mcp-atlassian` as PyPI package
  - Option B: Use git submodule
  - Option C: Copy shared utilities (not recommended)

**Recommendation**: Option A - Publish platform as package, client installs it.

### 8. Path Updates After Move

#### Files that may need path updates:

1. **`scripts/oauth_authorize.py`** (if moved to platform)
   - Check for relative imports
   - Update if needed

2. **Test files** (if moved to platform)
   - Verify import paths still work
   - Update if needed

3. **Documentation** (if moved to platform)
   - Update any relative links
   - Update path references

### 9. Version Control Considerations

#### Git History Preservation

**Option A: Preserve History (Recommended)**
```bash
# Use git filter-branch or git filter-repo to move files with history
git filter-repo --path src/mcp_atlassian --path tests/ --to-subdirectory-filter platform/
```

**Option B: Fresh Start**
- Start new repo without history
- Simpler but loses commit history

**Recommendation**: Option A if history is important, Option B for simplicity.

### 10. Verification Checklist

After setup, verify:

- [ ] Platform code builds successfully
- [ ] Platform tests pass
- [ ] Client scripts still work (if they depend on platform)
- [ ] Documentation links are correct
- [ ] .gitignore files are appropriate
- [ ] CI/CD pipelines work (if applicable)
- [ ] No hardcoded paths remain
- [ ] README files are updated
- [ ] License files are correct

## Migration Timeline

1. **Phase 1: Preparation** (Day 1)
   - Create backup branches
   - Review move map
   - Setup new repo structure (if needed)

2. **Phase 2: Migration** (Day 1-2)
   - Move platform files
   - Update paths
   - Test platform code

3. **Phase 3: Cleanup** (Day 2)
   - Remove platform files from client repo
   - Update documentation
   - Verify both repos

4. **Phase 4: Verification** (Day 2-3)
   - Run tests
   - Check CI/CD
   - Final review

## Rollback Plan

If issues arise:

1. **Restore from backup branch**:
   ```bash
   git checkout backup/pre-split-state
   git branch -D feature/remove-platform-code
   ```

2. **Revert moves in platform repo**:
   ```bash
   git revert <migration-commit>
   ```

3. **Manual file restoration** (if needed):
   - Copy files back from backup
   - Restore git history if preserved

