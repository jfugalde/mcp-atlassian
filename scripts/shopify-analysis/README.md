# Shopify analysis (canonical tooling)

Python tooling lives in the **`ryu-platform`** repository:

`ryu-platform/tools/shopify-analysis/`

## Layout

Clone this repo next to `ryu-platform` under the same parent directory (see [RYU workspace README](../../README.md) when both live under `Dev/RYU/`):

```text
.../RYU/
  Farmacia_Macross/    ← this repo
  ryu-platform/        ← sibling
```

## Run from here

```bash
chmod +x ./run_tool.sh   # once
./run_tool.sh python run_analysis.py
./run_tool.sh python performance_analysis.py
# any command with cwd = ryu-platform/tools/shopify-analysis
```

Or `cd` manually:

```bash
cd ../../ryu-platform/tools/shopify-analysis
# follow that folder’s README / SETUP.md
```

## Outputs for Macross

Save generated JSON and reports under **`docs/shopify-analysis/`** in this repository when you need them versioned with the client project.
