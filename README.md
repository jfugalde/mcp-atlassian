# Farmacias Macross - Client Project

This repository contains client-specific deliverables for Farmacias Macross.

## Structure
- `theme/` – **Live Shopify theme** (Liquid, `config/`, `sections/`). Point Shopify CLI, deployments, and theme-check here. Config: `theme/.theme-check.yml`.
- `vendor/skeleton-reference/Macross-V1.0.1/` – Archived **Shopify skeleton** copy for reference only; not deployed.
- `docs/pm/` – Project management documentation for Macross
- `docs/shopify-analysis/` – Audit outputs (see `scripts/README.md`; canonical tooling lives in `ryu-platform`)
- `scripts/` – GraphQL snapshots and pointers to shared tooling (`scripts/shopify-analysis/`)
- `admin-app/` – Shopify admin app (Macross)

## Analysis tooling

Canonical code: **`ryu-platform/tools/shopify-analysis/`** (sibling git checkout). This repo keeps **`scripts/shopify-analysis/run_tool.sh`** plus a short README so commands can delegate there without duplicating Python.

1. Clone `ryu-platform` next to this repo (same parent folder; see `scripts/shopify-analysis/README.md`).
2. Configure `.env` in `ryu-platform/tools/shopify-analysis` (e.g. `SHOPIFY_SHOP_DOMAIN=macross-pharma.myshopify.com`).
3. Save generated JSON / reports under `docs/shopify-analysis/` when you want them versioned here.

Upstream docs: [ryu-platform `tools/shopify-analysis`](https://github.com/jfugalde/ryu-platform/tree/main/tools/shopify-analysis).

## Related Repositories
- `ryu-platform`: Shared Shopify analysis and enrichment tooling (`tools/shopify-analysis`)
- `RYU`: Marketing/website frontend

## Notes
- Platform code and tooling have been moved to `ryu-platform`
- This repo contains only Macross-specific deliverables and outputs
