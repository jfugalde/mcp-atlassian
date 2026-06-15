# Agent memory — Farmacia Macross (Shopify theme)

## Learned User Preferences

- Customer-facing copy, labels, and locale defaults must be Spanish-first (Mexico-only market); PDP tab headers too (e.g. Descripción, not Description).
- Pharmaceutical copy must be Google Ads, PROFECO, and COFEPRIS compliant—no promising or prohibited wording.
- Navigation, homepage collection tiles, and main menu must pull from live Shopify collections—not hardcoded theme JSON blocks.
- Use Macross brand colors in UI work; WhatsApp and promo CTAs should match brand styling, not generic off-brand palettes.
- Mobile WhatsApp belongs under the mobile menu, sticky bar, or PDP sticky ATC—not as a persistent floating overlay.
- Mobile menu WhatsApp label should be standalone **WhatsApp** (not branch-picker wording like “elige sucursal”).
- Validate mobile layout and spacing with Playwright screenshots before claiming UX fixes are done.
- Category icons must be merchant-editable (collection `fa_icon` metafield), not hardcoded Font Awesome classes in templates.
- PDP metafield tabs: hide empty tabs; if all are empty, fall back to product description.
- Discount/promo PDP wording should feel natural and ecommerce-native—not generic or bot-like.

## Learned Workspace Facts

- Production storefront: `farmaciasmacross.com.mx`; Shopify admin store: `macross-pharma`.
- Theme source lives in `theme/`; local preview via Shopify CLI (`shopify theme dev`, typically `http://127.0.0.1:9292`).
- Catalog enrichment, COFEPRIS tooling, and collection fixes run from sibling repo `ryu-platform/tools/shopify-analysis`—not from this repo.
- PDP content tabs use `custom.*` product metafields; product description is used for Merchant Center compliance.
- Collection category icons read the collection `fa_icon` metafield (single-line string, e.g. `fa-solid fa-heart-pulse`).
- `pharmacy-promo` (discount PDP) template supports promo imagery via `custom.macross_promo_image` / `custom.macross_promo` metafields or gallery alt-text `promo`.
- Footer sanitary licenses (vigentes): CDMX `09 004 09 0206`, Puebla `1061160245`. Do not use `085M2019 SSA IV` (that is a drug registration, not an establishment license).
- Native Macross WhatsApp (`macross-whatsapp.js` + `macross-whatsapp.css`): desktop FAB, native 3-location picker, human Spanish pre-filled `wa.me` messages (no bot-like wording). Branch numbers editable in theme settings (Macross section). No Seedgrow / app embed. Routing: **hostname subdomains first** (`cdmx|puebla|guadalajara.farmaciasmacross.com.mx` → high confidence, no cookie); apex uses IP/GPS only after cookie accept; low-confidence geo shows picker; dev override `?macross_branch=cdmx|puebla|guadalajara`.
- WhatsApp runbook: `docs/macross-whatsapp.md`; location subdomains: `docs/location-subdomains-runbook.md`.
- Acerca de nosotros (`/pages/acerca-de-nosotros`) uses `page.acerca.json` and `macross-about` section (`theme/sections/macross-about.liquid`); legacy `page.about-us.json` defers to the same section.
- Licencias (`/pages/nuestras-licencias`) uses `page.nuestras-licencias.json` and `macross-licenses` section — only CDMX and Puebla (vigentes).
- LLM/agent discovery: Shopify `agents.md.liquid` at `/agents.md` plus extended `llms-full.txt.liquid` at `/llms-full.txt` (Spanish, Mexico market; uses `agents` object).
- Core Web Vitals baselines and Lighthouse comparisons live in `docs/shopify-analysis/` (e.g. `core_web_vitals_summary.json`, `performance_comparison_*.json`).
