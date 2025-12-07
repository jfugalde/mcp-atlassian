# Repository Split Cutover Runbook

## Pre-Cutover Checklist

Before starting the migration:

- [ ] Both repos are backed up (create backup branches)
- [ ] All uncommitted changes are committed or stashed
- [ ] Team is notified of migration (if applicable)
- [ ] CI/CD pipelines are paused (if applicable)
- [ ] Move map is reviewed and approved
- [ ] Target directory structure is confirmed

## Step-by-Step Execution

### Phase 1: Backup and Preparation

#### 1.1 Create Backup Branch in Farmacia_Macross

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross
git checkout -b backup/pre-split-state
git push origin backup/pre-split-state
git checkout main  # or your default branch
```

#### 1.2 Create Migration Branch in Farmacia_Macross

```bash
git checkout -b feature/remove-platform-code
```

#### 1.3 Setup RYU Platform Repo

**If creating new repo:**

```bash
cd /Users/jose.ugaldevivo/Dev/RYU
mkdir ryu-platform
cd ryu-platform
git init
git remote add origin <github-url>  # Update with actual URL
git checkout -b feature/repo-split-migration
```

**If using existing RYU repo:**

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/RYU
git checkout -b feature/add-platform-code
mkdir -p platform  # or mcp-atlassian
```

### Phase 2: Move Platform Files

#### 2.1 Move Core Platform Code

```bash
# From Farmacia_Macross repo
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross

# Copy src/mcp_atlassian to platform repo
cp -r src/mcp_atlassian /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/src/

# Copy tests
cp -r tests /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/

# Copy config files
cp pyproject.toml /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp uv.lock /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp Dockerfile /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp smithery.yaml /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp LICENSE /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
```

#### 2.2 Move Documentation Files

```bash
# Copy platform docs
cp -r docs/growth /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/docs/
cp -r docs/governance /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/docs/
cp docs/backlog-analysis.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/docs/  # if platform-level
cp docs/jira-sprint-assignments.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/docs/  # if platform-level

# Copy README and other docs
cp README.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp AGENTS.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp CONTRIBUTING.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp SECURITY.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp CURSOR_MCP_CONFIG.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp MULTIPLE_ACCOUNTS_SETUP.md /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
```

#### 2.3 Move Configuration Files

```bash
# Copy MCP config files
cp cursor-mcp-config.json /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp cursor-mcp-single-server.json /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/
cp cursor-mcp-multiple-accounts.json /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/

# Copy scripts
mkdir -p /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/scripts
cp scripts/oauth_authorize.py /Users/jose.ugaldevivo/Dev/RYU/ryu-platform/scripts/
```

#### 2.4 Setup .gitignore in Platform Repo

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/ryu-platform
# Create .gitignore (see REPO_SPLIT_SETUP_PLAN.md for content)
```

### Phase 3: Verify Platform Repo

#### 3.1 Test Platform Code

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/ryu-platform

# Install dependencies
uv sync --frozen --all-extras --dev

# Run tests
uv run pytest

# Run linter
pre-commit run --all-files
```

#### 3.2 Commit Platform Changes

```bash
git add .
git commit -m "feat: migrate MCP Atlassian platform code from Farmacia_Macross repo

- Move src/mcp_atlassian/ and tests/
- Move platform documentation and config files
- Setup platform repository structure

Github-Issue:#<issue-number>"
git push origin feature/repo-split-migration
```

### Phase 4: Cleanup Client Repo

#### 4.1 Remove Platform Files from Macross Repo

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross
git checkout feature/remove-platform-code

# Remove platform directories
git rm -r src/mcp_atlassian/
git rm -r tests/

# Remove platform config files
git rm pyproject.toml
git rm uv.lock
git rm Dockerfile
git rm smithery.yaml
git rm LICENSE  # Keep if Macross needs its own license
git rm README.md  # Will create new one
git rm AGENTS.md
git rm CONTRIBUTING.md
git rm SECURITY.md
git rm CURSOR_MCP_CONFIG.md
git rm MULTIPLE_ACCOUNTS_SETUP.md
git rm cursor-mcp-*.json

# Remove platform docs
git rm -r docs/growth/
git rm -r docs/governance/
git rm docs/backlog-analysis.md  # if platform-level
git rm docs/jira-sprint-assignments.md  # if platform-level

# Remove platform scripts
git rm scripts/oauth_authorize.py

# Remove other client files (if moving to separate repo)
git rm -r docs/suppathletik/
git rm scripts/fetch_suppathletik_jira.py
```

#### 4.2 Create New Client README

```bash
# Create new Macross-specific README
cat > README.md << 'EOF'
# Farmacias Macross - Client Project

This repository contains client-specific deliverables for Farmacias Macross.

## Structure

- `docs/pm/` - Project management documentation
- `docs/shopify-analysis/` - Shopify audit and analysis
- `scripts/` - Client-specific automation scripts
- `admin-app/` - Shopify admin application

## Related Repositories

- [RYU Platform](https://github.com/...) - Core MCP Atlassian platform
EOF

git add README.md
```

#### 4.3 Update .gitignore

```bash
# Update .gitignore (remove platform-specific, keep client-specific)
# See REPO_SPLIT_SETUP_PLAN.md for content
```

#### 4.4 Verify Client Repo

```bash
# Check that client scripts still work
cd scripts/shopify-analysis
python run_analysis.py --help  # or similar test

# Verify no broken imports
grep -r "from mcp_atlassian" scripts/  # Should find none (or update if needed)
```

#### 4.5 Commit Client Cleanup

```bash
git add .
git commit -m "refactor: remove platform code, keep only Macross client deliverables

- Remove MCP Atlassian platform code (moved to ryu-platform repo)
- Remove platform documentation and configs
- Create Macross-specific README
- Update .gitignore for client-only content

Github-Issue:#<issue-number>"
git push origin feature/remove-platform-code
```

### Phase 5: Final Verification

#### 5.1 Platform Repo Verification

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/ryu-platform

# Run full test suite
uv run pytest

# Check linting
pre-commit run --all-files

# Verify imports work
python -c "from mcp_atlassian import ..."  # Test key imports
```

#### 5.2 Client Repo Verification

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross

# Verify no platform code remains
find . -name "*.py" -exec grep -l "mcp_atlassian" {} \;  # Should be empty or only in comments

# Verify client scripts work
cd scripts/shopify-analysis
python -m pytest  # if tests exist
```

#### 5.3 Merge to Main Branches

**Platform Repo:**

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/ryu-platform
git checkout main
git merge feature/repo-split-migration
git push origin main
```

**Client Repo:**

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross
git checkout main
git merge feature/remove-platform-code
git push origin main
```

### Phase 6: Post-Migration Tasks

#### 6.1 Update Documentation

- [ ] Update any external references to old repo structure
- [ ] Update team documentation
- [ ] Update CI/CD configurations (if applicable)

#### 6.2 Update Dependencies

If client scripts depend on platform code:

```bash
# In Macross repo, update requirements
# Option A: Install from PyPI (if published)
echo "mcp-atlassian>=X.X.X" >> scripts/shopify-analysis/requirements.txt

# Option B: Use git submodule
git submodule add <platform-repo-url> platform
```

#### 6.3 Cleanup

```bash
# Delete feature branches after merge (optional)
git branch -d feature/remove-platform-code
git branch -d feature/repo-split-migration

# Keep backup branch for safety
# git branch -d backup/pre-split-state  # Don't delete yet
```

## Rollback Procedure

If issues are discovered:

### Rollback Platform Repo

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/ryu-platform
git checkout main
git reset --hard HEAD~1  # Revert last commit
# Or restore from backup
```

### Rollback Client Repo

```bash
cd /Users/jose.ugaldevivo/Dev/RYU/Farmacia_Macross
git checkout backup/pre-split-state
git checkout -b restore/pre-split
git push origin restore/pre-split
# Review and merge if needed
```

## Verification Checklist

After migration:

- [ ] Platform repo builds successfully
- [ ] Platform tests pass
- [ ] Platform linting passes
- [ ] Client repo has no platform code
- [ ] Client scripts work (if applicable)
- [ ] Documentation is updated
- [ ] .gitignore files are correct
- [ ] No broken imports
- [ ] CI/CD works (if applicable)
- [ ] Both repos can be cloned fresh and work

## Troubleshooting

### Issue: Import errors in platform repo

**Solution**: Check Python path and ensure `src/` is in PYTHONPATH or use editable install:
```bash
uv pip install -e .
```

### Issue: Tests fail after move

**Solution**: Check import paths in test files, update if needed.

### Issue: Client scripts can't find platform code

**Solution**: Install platform as package or use git submodule.

### Issue: Git history lost

**Solution**: Use `git filter-repo` to preserve history (see setup plan).

## Success Criteria

Migration is successful when:

1. ✅ Platform code is in dedicated repo and works
2. ✅ Client code is clean (no platform code)
3. ✅ Both repos build/test successfully
4. ✅ Documentation is updated
5. ✅ Team can work with new structure
6. ✅ No broken dependencies

