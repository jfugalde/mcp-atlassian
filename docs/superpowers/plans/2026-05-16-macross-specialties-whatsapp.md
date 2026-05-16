# Macross specialties, 404 collections, and mobile WhatsApp — implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore homepage specialty tiles (including Hematología and Infecciosas), fix 404s by publishing the missing Shopify collections at the handles the theme already references, and move WhatsApp access into the mobile hamburger menu instead of a floating overlay.

**Architecture:** **Shopify Admin** owns collection existence, smart rules, and menu URLs; **theme JSON** (`index.json`, `list-collections.json`) only wires handles that must already resolve on the storefront. Homepage gets a restored `collection-list` section aligned 1:1 with `/collections`. WhatsApp uses the existing **Seedgrow** widget (`.wa__widget_container` / `.wa__btn_popup`) already loaded in `theme/layout/theme.liquid`; mobile hides the floating launcher via CSS + app settings and adds a menu row that programmatically opens the same widget (same pattern as `pdp-whatsapp-addons.js`).

**Tech Stack:** Shopify Admin GraphQL Admin API (`collectionCreate`), Online Store 2.0 JSON templates, Liquid (Minimog 3.x), CSS, vanilla JS, Shopify CLI theme push (optional).

**Prerequisites:** Store API token with `read_products`, `write_products` (collections). Shop: `macross-pharma.myshopify.com` / storefront `https://farmaciasmacross.com.mx`. Branch: `PLPs-redo` (or current feature branch).

---

## File map (create / modify)

| File | Responsibility |
|------|----------------|
| Shopify Admin → Collections | Create/publish `hematologia`, `infecciosas-y-parasitarias` smart collections |
| Shopify Admin → Navigation | Ensure menu links use the same handles (if menu points at old URLs) |
| `Farmacia_Macross/theme/templates/index.json` | Restore `collection-list` with 8 specialty tiles; adjust section order |
| `Farmacia_Macross/theme/templates/list-collections.json` | Already references 8 handles — verify after Task 1 only |
| `Farmacia_Macross/theme/config/settings_data.json` | App embed: `show_on_mobile: false` for WhatsApp app block |
| `Farmacia_Macross/theme/assets/seedgrow-whatsapp-init.js` | Set `showOnMobile: "OFF"` in vendored init (matches theme behavior) |
| `Farmacia_Macross/theme/assets/whatsapp-widget-mobile.css` | Hide floating widget on mobile; style menu trigger area |
| `Farmacia_Macross/theme/snippets/macross-mobile-whatsapp.liquid` | **Create** — WhatsApp row in mobile drawer |
| `Farmacia_Macross/theme/assets/macross-mobile-whatsapp.js` | **Create** — open Seedgrow popup from menu |
| `Farmacia_Macross/theme/sections/header.liquid` | Render mobile WhatsApp snippet above customer block |
| `Farmacia_Macross/theme/layout/theme.liquid` | Load new JS asset |
| `Farmacia_Macross/theme/locales/es.json` | Mobile menu label string |
| `Farmacia_Macross/theme/locales/en.default.json` | English parity for label |

---

### Task 1: Create missing smart collections (Shopify Admin — fixes 404s)

**Files:** None in Git. **Reference:** `ryu-platform/tools/shopify-analysis/catalog_export.json` product types.

**Root cause:** Theme links to `/collections/hematologia` and `/collections/infecciosas-y-parasitarias`, but those collections were never created (or never published) in Admin. `productos-hormonales-especializados` already exists on production per crawl; only the two new handles need creation.

- [ ] **Step 1: Verify collections are missing**

Run (replace `SHOPIFY_ADMIN_TOKEN` and shop host):

```bash
curl -s -X POST "https://macross-pharma.myshopify.com/admin/api/2024-10/graphql.json" \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: $SHOPIFY_ADMIN_TOKEN" \
  -d '{"query":"{ hematologia: collectionByHandle(handle: \"hematologia\") { id handle } infecciosas: collectionByHandle(handle: \"infecciosas-y-parasitarias\") { id handle } }"}' | python3 -m json.tool
```

**Expected:** Both `hematologia` and `infecciosas` are `null`. If either exists, skip creation for that handle in Step 2.

- [ ] **Step 2: Create `hematologia` smart collection**

```bash
curl -s -X POST "https://macross-pharma.myshopify.com/admin/api/2024-10/graphql.json" \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: $SHOPIFY_ADMIN_TOKEN" \
  -d '{
    "query": "mutation($input: CollectionInput!) { collectionCreate(input: $input) { collection { id handle title } userErrors { field message } } }",
    "variables": {
      "input": {
        "title": "Hematología",
        "handle": "hematologia",
        "descriptionHtml": "<p>Medicamentos hematológicos y oncohematológicos de alta especialidad.</p>",
        "ruleSet": {
          "appliedDisjunctively": true,
          "rules": [
            { "column": "TYPE", "relation": "EQUALS", "condition": "Hematología" },
            { "column": "TYPE", "relation": "EQUALS", "condition": "Hematológico" },
            { "column": "TYPE", "relation": "EQUALS", "condition": "Oncológico y Hematológico" },
            { "column": "TYPE", "relation": "EQUALS", "condition": "Hematológico y Reumatología" }
          ]
        }
      }
    }
  }' | python3 -m json.tool
```

**Expected:** `"handle": "hematologia"`, `userErrors: []`. Catalog has ~18 products across those types (5+3+8+2).

- [ ] **Step 3: Create `infecciosas-y-parasitarias` smart collection**

```bash
curl -s -X POST "https://macross-pharma.myshopify.com/admin/api/2024-10/graphql.json" \
  -H "Content-Type: application/json" \
  -H "X-Shopify-Access-Token: $SHOPIFY_ADMIN_TOKEN" \
  -d '{
    "query": "mutation($input: CollectionInput!) { collectionCreate(input: $input) { collection { id handle title } userErrors { field message } } }",
    "variables": {
      "input": {
        "title": "Infecciosas y Parasitarias",
        "handle": "infecciosas-y-parasitarias",
        "descriptionHtml": "<p>Antirretrovirales, antifúngicos y tratamientos para enfermedades infecciosas y parasitarias.</p>",
        "ruleSet": {
          "appliedDisjunctively": false,
          "rules": [
            { "column": "TYPE", "relation": "EQUALS", "condition": "Infecciosas y Parasitarias" }
          ]
        }
      }
    }
  }' | python3 -m json.tool
```

**Expected:** `"handle": "infecciosas-y-parasitarias"`, ~11 products from catalog.

- [ ] **Step 4: Publish collections to Online Store**

In **Shopify Admin → Products → Collections**, open each new collection → **Sales channels** → ensure **Online Store** is enabled. Or via GraphQL `publishablePublish` if your integration uses publications.

- [ ] **Step 5: Add redirect if an old handle was used in menus**

If navigation still links to `/collections/enfermedades-infecciosas-y-parasitarias`, add redirect:

- **From:** `/collections/enfermedades-infecciosas-y-parasitarias`
- **To:** `/collections/infecciosas-y-parasitarias`

(Admin → **Content → Menus** or URL redirects; scope `write_online_store_navigation`.)

- [ ] **Step 6: Manual verification**

Open in browser (production or preview):

- `https://farmaciasmacross.com.mx/collections/hematologia` → **200**, products listed
- `https://farmaciasmacross.com.mx/collections/infecciosas-y-parasitarias` → **200**, products listed

- [ ] **Step 7: Commit**

No repo change for Task 1 unless you document handles in a runbook. Skip Git commit.

---

### Task 2: JSON syntax gate

**Files:** `Farmacia_Macross/theme/templates/index.json` (will change in Task 3).

- [ ] **Step 1: Validate theme JSON parses**

From repo root:

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

def parse_shopify_theme_json(path: Path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", "", text, count=1, flags=re.S)
    return json.loads(text)

root = Path("Farmacia_Macross/theme/templates")
for p in sorted(root.glob("*.json")):
    parse_shopify_theme_json(p)
    print("OK", p.name)
PY
```

**Expected:** `OK index.json` (and siblings) with no traceback.

---

### Task 3: Restore homepage specialty tiles (`index.json`)

**Files:**
- Modify: `Farmacia_Macross/theme/templates/index.json`

**Context:** Commit `7af9986` replaced `collection-list` with `explora-cta` (text + button to `/collections`). Users still need **visual tiles** on the homepage. Restore `collection-list` with the **same 8 handles** as `list-collections.json`, using the section definition from commit `9e7181b` plus three additional blocks.

- [ ] **Step 1: Add `collection-list` section to `sections`**

Inside `"sections": { ... }`, add a new key `"collection-list"` (place after `"explora-cta"` block in the file for readability). Use this full section object:

```json
    "collection-list": {
      "type": "collection-list",
      "blocks": {
        "cl-onc": {
          "type": "collection_block",
          "settings": {
            "collection": "medicamento-oncologicos-al-mejor-precio-alta-especialidad",
            "title": "",
            "item_image": "shopify://shop_images/imagen_2023-04-03_142546553.png"
          }
        },
        "cl-hema": {
          "type": "collection_block",
          "settings": {
            "collection": "hematologia",
            "title": "Hematología",
            "item_image": "shopify://shop_images/imagen_2023-04-03_142546553.png"
          }
        },
        "cl-reuma": {
          "type": "collection_block",
          "settings": {
            "collection": "reumatologia-y-traumatologia",
            "title": "Reumatología y traumatología",
            "item_image": "shopify://shop_images/imagen_2023-04-03_145556394.png"
          }
        },
        "cl-infec": {
          "type": "collection_block",
          "settings": {
            "collection": "infecciosas-y-parasitarias",
            "title": "Infecciosas y Parasitarias",
            "item_image": "shopify://shop_images/imagen_2023-04-03_142914263.png"
          }
        },
        "cl-immune": {
          "type": "collection_block",
          "settings": {
            "collection": "medicamentos-para-el-sistema-inmunologico-1",
            "title": "",
            "item_image": "shopify://shop_images/imagen_2023-04-03_142021791.png"
          }
        },
        "cl-hormonal": {
          "type": "collection_block",
          "settings": {
            "collection": "productos-hormonales-especializados",
            "title": "",
            "item_image": "shopify://shop_images/imagen_2023-04-03_142914263.png"
          }
        },
        "cl-cardio": {
          "type": "collection_block",
          "settings": {
            "collection": "cardiologia",
            "title": "Cardiológicos",
            "item_image": "shopify://shop_images/imagen_2023-04-03_143736464.png"
          }
        },
        "cl-mas-vendido": {
          "type": "collection_block",
          "settings": {
            "collection": "lo-mas-vendido",
            "title": "Lo más vendido",
            "item_image": "shopify://shop_images/imagen_2023-04-03_143736464.png"
          }
        }
      },
      "block_order": [
        "cl-onc",
        "cl-hema",
        "cl-reuma",
        "cl-infec",
        "cl-immune",
        "cl-hormonal",
        "cl-cardio",
        "cl-mas-vendido"
      ],
      "custom_css": [],
      "settings": {
        "heading": "Explora por especialidad",
        "subheading": "",
        "description": "<p>Medicamentos de alta especialidad organizados por área terapéutica.</p>",
        "header_alignment": "center",
        "container": "container",
        "background_color": "",
        "layout": "grid",
        "expanded": true,
        "card_style": "inside",
        "text_alignment": "left",
        "hover_effect": "scaling-up",
        "show_product_count": false,
        "count_inline_title": true,
        "image_rounded": false,
        "items_per_row": 4,
        "item_gap": 30,
        "enable_slider": true,
        "show_pagination": true,
        "show_navigation": true,
        "autorotate": false,
        "autorotate_speed": 4,
        "use_scroll_mobile": true,
        "mobile_gap": 16,
        "hidden_slide_control_mobile": false,
        "padding_top": 40,
        "padding_bottom": 40,
        "custom_class": "sf-home__collection-list"
      }
    }
```

- [ ] **Step 2: Slim down `explora-cta` (optional but recommended)**

Keep `explora-cta` as a short intro **above** the tiles, or remove it to avoid duplicate headings. **Recommended:** set `explora-cta` block title to empty and shorten text; remove duplicate H2 from `explora-text` settings:

```json
            "title": "",
            "text": "<p>Oncología, hematología, reumatología, cardiología, inmunología, hormonales y más.</p>",
            "button_label": "Ver todas las categorías",
```

Section heading now lives on `collection-list` (`"heading": "Explora por especialidad"`).

- [ ] **Step 3: Update homepage `order` array**

Set `"order"` to:

```json
  "order": [
    "slideshow",
    "explora-cta",
    "collection-list",
    "product-tabs",
    "1680553798df70faa0",
    "f53b0faf-c303-4932-b6b1-6704cc2be1b4",
    "d1931db9-7c55-4c61-906b-2eb379b3e320"
  ]
```

- [ ] **Step 4: Run JSON validation**

```bash
python3 - <<'PY'
import json, re
from pathlib import Path
p = Path("Farmacia_Macross/theme/templates/index.json")
t = re.sub(r"/\*.*?\*/", "", p.read_text(), count=1, flags=re.S)
d = json.loads(t)
assert "collection-list" in d["sections"]
assert "collection-list" in d["order"]
blocks = d["sections"]["collection-list"]["blocks"]
assert blocks["cl-hema"]["settings"]["collection"] == "hematologia"
assert blocks["cl-infec"]["settings"]["collection"] == "infecciosas-y-parasitarias"
print("OK", len(blocks), "tiles")
PY
```

**Expected:** `OK 8 tiles`

- [ ] **Step 5: Commit**

```bash
git add Farmacia_Macross/theme/templates/index.json
git commit -m "fix(theme): restore homepage specialty collection tiles"
```

---

### Task 4: Align navigation menu links (Admin — quick check)

**Files:** Shopify Admin → **Content → Menus** (main / mobile menu).

- [ ] **Step 1: Audit Especialidades submenu**

Confirm each child URL matches a live handle:

| Label (expected) | Handle |
|------------------|--------|
| Oncológicos | `medicamento-oncologicos-al-mejor-precio-alta-especialidad` |
| Hematología | `hematologia` |
| Reumatología | `reumatologia-y-traumatologia` |
| Infecciosas y Parasitarias | `infecciosas-y-parasitarias` |
| Inmunológicos | `medicamentos-para-el-sistema-inmunologico-1` |
| Hormonales | `productos-hormonales-especializados` |
| Cardiología | `cardiologia` |
| Lo más vendido | `lo-mas-vendido` |

- [ ] **Step 2: Fix any stale URLs**

Update or add redirects for legacy paths (e.g. `enfermedades-infecciosas-y-parasitarias` → `infecciosas-y-parasitarias`).

No Git commit unless menu is exported to theme (unusual).

---

### Task 5: WhatsApp in mobile menu (hide floating overlay)

**Files:**
- Modify: `Farmacia_Macross/theme/config/settings_data.json`
- Modify: `Farmacia_Macross/theme/assets/seedgrow-whatsapp-init.js`
- Modify: `Farmacia_Macross/theme/assets/whatsapp-widget-mobile.css`
- Create: `Farmacia_Macross/theme/snippets/macross-mobile-whatsapp.liquid`
- Create: `Farmacia_Macross/theme/assets/macross-mobile-whatsapp.js`
- Modify: `Farmacia_Macross/theme/sections/header.liquid`
- Modify: `Farmacia_Macross/theme/layout/theme.liquid`
- Modify: `Farmacia_Macross/theme/locales/es.json`
- Modify: `Farmacia_Macross/theme/locales/en.default.json`

**Approach:** Desktop keeps floating WhatsApp. Mobile (`max-width: 767px`) hides `.wa__widget_container` until opened from menu. Menu button uses `[data-mobile-whatsapp-launcher]` and shared JS to click `.wa__btn_popup` (proven on PDP in `pdp-whatsapp-addons.js`).

- [ ] **Step 1: Disable mobile float in app embed settings**

In `Farmacia_Macross/theme/config/settings_data.json`, locate block `11813581335429059158` (whatsapp-chat-widget app embed) and set:

```json
          "show_on_mobile": false,
          "show_label_on_mobile": false,
```

Leave `show_on_desktop: true`.

- [ ] **Step 2: Disable mobile in Seedgrow init**

In `Farmacia_Macross/theme/assets/seedgrow-whatsapp-init.js`, find the `options` object and change:

```javascript
"showOnMobile":"OFF"
```

(was `"ON"`). This matches the vendored widget’s display flags.

- [ ] **Step 3: Hide floating launcher on mobile in CSS**

Append to `Farmacia_Macross/theme/assets/whatsapp-widget-mobile.css`:

```css
@media screen and (max-width: 767px) {
  /* No floating bubble — opened from mobile menu only */
  .wa__widget_container {
    display: none !important;
  }

  .wa__widget_container.wa__mobile-menu-open,
  .wa__widget_container:has(.wa__popup_chat_box.wa__active) {
    display: block !important;
    transform: scale(1);
    bottom: max(12px, env(safe-area-inset-bottom, 0px)) !important;
    right: max(6px, env(safe-area-inset-right, 0px)) !important;
  }
}

.sf-menu-mobile-whatsapp {
  border-top: 1px solid #eee;
  margin-top: 1rem;
  padding: 0 1rem 1rem;
}

.sf-menu-mobile-whatsapp__btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.875rem 1rem;
  border-radius: 8px;
  background: #2db742;
  color: #fff;
  font-weight: 500;
  border: none;
  cursor: pointer;
}

.sf-menu-mobile-whatsapp__btn svg {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
}
```

- [ ] **Step 4: Create snippet `macross-mobile-whatsapp.liquid`**

```liquid
<div class="sf-menu-mobile-whatsapp xl:hidden">
  <button
    type="button"
    class="sf-menu-mobile-whatsapp__btn"
    data-mobile-whatsapp-launcher
    aria-label="{{ 'layout.mobile_menu.whatsapp' | t }}"
  >
    {% render 'icon', name: 'whatsapp', size: 'medium' %}
    <span>{{ 'layout.mobile_menu.whatsapp' | t }}</span>
  </button>
</div>
```

- [ ] **Step 5: Create `macross-mobile-whatsapp.js`**

```javascript
(function () {
  function showWidgetRoot(root) {
    root.classList.add('wa__mobile-menu-open');
    root.style.display = 'block';
    root.style.visibility = 'visible';
    root.style.opacity = '1';
    root.style.pointerEvents = 'auto';
  }

  function hideWidgetRoot(root) {
    var box = root.querySelector('.wa__popup_chat_box');
    if (box && box.classList.contains('wa__active')) return;
    root.classList.remove('wa__mobile-menu-open');
    root.style.display = '';
    root.style.opacity = '';
    root.style.visibility = '';
    root.style.pointerEvents = '';
  }

  document.addEventListener(
    'click',
    function (e) {
      var trigger =
        e.target && e.target.closest && e.target.closest('[data-mobile-whatsapp-launcher]');
      if (!trigger) return;
      e.preventDefault();
      var root = document.querySelector('.wa__widget_container');
      var btn = document.querySelector('.wa__btn_popup');
      if (!root || !btn) return;
      showWidgetRoot(root);
      window.setTimeout(function () {
        btn.click();
      }, 0);
    },
    true
  );

  function attachCloseObserver() {
    var root = document.querySelector('.wa__widget_container');
    var box = root && root.querySelector('.wa__popup_chat_box');
    if (!root || !box || typeof MutationObserver === 'undefined') return;
    var obs = new MutationObserver(function () {
      hideWidgetRoot(root);
    });
    obs.observe(box, { attributes: true, attributeFilter: ['class'] });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachCloseObserver);
  } else {
    attachCloseObserver();
  }
})();
```

- [ ] **Step 6: Render snippet in mobile menu**

In `Farmacia_Macross/theme/sections/header.liquid`, inside the mobile drawer, **after** the `{% endfor %}` that closes `linklists[menu].links` (around line 511) and **before** `{% render 'mega-menu-customer', section: section %}`, add:

```liquid
                    {% render 'macross-mobile-whatsapp' %}
```

- [ ] **Step 7: Load script in layout**

In `Farmacia_Macross/theme/layout/theme.liquid`, after the existing Seedgrow scripts:

```liquid
  <script src="{{ 'macross-mobile-whatsapp.js' | asset_url }}" defer="defer"></script>
```

- [ ] **Step 8: Add locale strings**

In `Farmacia_Macross/theme/locales/es.json`, under `"layout"` (add key if missing):

```json
    "mobile_menu": {
      "whatsapp": "WhatsApp — elige sucursal"
    },
```

In `Farmacia_Macross/theme/locales/en.default.json`:

```json
    "mobile_menu": {
      "whatsapp": "WhatsApp — choose a branch"
    },
```

If `"layout"` already has nested keys, merge `mobile_menu` without breaking JSON commas.

- [ ] **Step 9: Manual verification**

1. Desktop (≥1024px): floating green WhatsApp button still visible.
2. Mobile (≤767px): **no** floating button on homepage, PLP, or PDP (except PDP sticky integration if `macross_whatsapp_pdp_addons_integration` is on — floating still hidden; sticky bar WhatsApp unchanged).
3. Open hamburger menu → green **WhatsApp — elige sucursal** row → tap → branch picker opens (same popup as before).
4. Close popup → floating button stays hidden on mobile.

- [ ] **Step 10: Commit**

```bash
git add Farmacia_Macross/theme/config/settings_data.json \
  Farmacia_Macross/theme/assets/seedgrow-whatsapp-init.js \
  Farmacia_Macross/theme/assets/whatsapp-widget-mobile.css \
  Farmacia_Macross/theme/snippets/macross-mobile-whatsapp.liquid \
  Farmacia_Macross/theme/assets/macross-mobile-whatsapp.js \
  Farmacia_Macross/theme/sections/header.liquid \
  Farmacia_Macross/theme/layout/theme.liquid \
  Farmacia_Macross/theme/locales/es.json \
  Farmacia_Macross/theme/locales/en.default.json
git commit -m "fix(theme): move WhatsApp launcher into mobile menu"
```

---

### Task 6: Deploy and smoke test

**Files:** None.

- [ ] **Step 1: Push theme to preview or live**

From `Farmacia_Macross/theme`:

```bash
shopify theme push --path . --json
```

Use development theme first; publish after QA.

- [ ] **Step 2: Smoke test checklist**

| Check | Pass |
|-------|------|
| Homepage shows 8 specialty tiles after hero | |
| Tile “Hematología” → 200, products | |
| Tile “Infecciosas y Parasitarias” → 200, products | |
| `/collections` page still shows same 8 tiles | |
| Mobile: no floating WhatsApp on scroll | |
| Mobile menu: WhatsApp opens branch picker | |
| Desktop: floating WhatsApp still works | |

- [ ] **Step 3: Commit**

No commit unless deployment notes are tracked in repo.

---

## Self-review (spec coverage)

| User requirement | Task |
|------------------|------|
| Homepage missing new specialties | Task 3 — restore `collection-list` with 8 tiles including hematología / infecciosas |
| 404 on hematologia, infecciosas | Task 1 — `collectionCreate` smart collections at exact handles |
| WhatsApp under mobile menu, not overlay | Task 5 — hide mobile float + menu launcher + JS |
| Menu / `/collections` consistency | Task 4 + existing `list-collections.json` |

**Placeholder scan:** None — all GraphQL, JSON, Liquid, CSS, and JS are specified inline.

**Dependency order:** Task 1 before Task 3 homepage QA (tiles 404 until collections exist). Task 5 independent of Task 1.

---

## Risks and notes

1. **`seedgrow-whatsapp-init.js` may be overwritten** when the WhatsApp app re-exports settings. Prefer `settings_data.json` `show_on_mobile: false` as source of truth; keep CSS hide as backup.
2. **Duplicate WhatsApp apps:** Theme loads vendored Seedgrow **and** Shopify app embed block. If two widgets appear on desktop, disable one embed in Admin (out of scope unless reported).
3. **Theme editor overwrite:** `index.json` header warns of auto-generation — treat Git as canonical after merge.
4. **Hormonales collection** already on production; only hematología / infecciosas need Admin creation.
5. **Unique tile images** for hematología / infecciosas / lo-mas-vendido are still reused assets — optional follow-up in Admin or `shop_images`.
