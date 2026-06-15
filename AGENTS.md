# Agent memory — Farmacia Macross (Shopify theme)

## Learned User Preferences

- Customer-facing copy, labels, and locale defaults must be Spanish-first (Mexico-only market).
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
- Footer sanitary licenses include COFEPRIS `085M2019 SSA IV` plus Ciudad de México and Puebla permits.
- Native Macross WhatsApp (`macross-whatsapp.js` + `macross-whatsapp.css`): desktop FAB, native 3-sucursal picker, human Spanish pre-filled `wa.me` messages. Branch numbers editable in theme settings (Macross section). No Seedgrow / app embed.
- WhatsApp branch routing: **hostname subdomains first** (`cdmx|puebla|interlomas.farmaciasmacross.com.mx` → high confidence, no cookie required); apex uses IP/GPS only after cookie accept; low-confidence geo shows picker without badge; theme dev override via `?macross_branch=cdmx|puebla|interlomas`.
- WhatsApp runbook: `docs/macross-whatsapp.md`; location subdomains: `docs/location-subdomains-runbook.md`.
