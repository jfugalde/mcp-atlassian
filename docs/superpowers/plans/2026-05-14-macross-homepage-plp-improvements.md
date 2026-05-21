# Macross homepage and PLP hardening — implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align Shopify catalog handles with theme JSON, fix hero and category UX on the homepage, remove counterintuitive PLP filter configuration, and make `/collections` consistent with the live store—without introducing new theme abstractions.

**Architecture:** Treat **Shopify Admin** (collections, redirects, Search & Discovery filters) as the source of truth for URLs and product membership; treat **`Farmacia_Macross/theme/templates/*.json`** as declarative wiring that must reference valid handles. Prefer **minimal JSON edits** and **removing dead CSS blocks** over new Liquid. PLPs stay on `main-collection-product-grid.liquid`; behavior changes are **settings + optional filter type switch**, not rewrites of the Minimog section.

**Tech Stack:** Shopify Online Store 2.0 JSON templates, Liquid (Minimog 3.x), Shopify CLI `theme check` (optional), Python 3 `json` module for local JSON validation.

**Important:** Files under `theme/templates/*.json` are marked auto-generated in their headers; the theme editor can overwrite them. After merging, either **pin changes in Git as canonical** and avoid conflicting edits in the live theme editor, or **re-apply the same edits in the editor** and pull JSON back into the repo.

---

## File map (create / modify)

| File | Responsibility |
|------|----------------|
| `Farmacia_Macross/theme/templates/index.json` | Homepage section order, hero slideshow, product tabs, collection list tiles, inline `custom_css` hacks |
| `Farmacia_Macross/theme/templates/collection.json` | Default PLP: header + grid + recent viewed; filter visibility and tag groups |
| `Farmacia_Macross/theme/templates/collection.flash-sale.json` | Alternate PLP: flash banner + grid; recent viewed copy |
| `Farmacia_Macross/theme/templates/list-collections.json` | `/collections` index blocks (currently demo handles) |
| Shopify Admin → Collections | Merge duplicates, canonical handles, optional URL redirects |
| Shopify Admin → Navigation / Search & Discovery | Optional storefront filters instead of tag strings |

---

### Task 1: Catalog consolidation (Shopify Admin — no Git diff)

**Files:** None in repo. **Reference handles:** `lo-mas-vendido`, `lo-mas-vendido-1`, `medicamentos-para-el-sistema-inmunologico-1`, `enfermedades-infecciosas-y-parasitarias` (verify existence).

- [ ] **Step 1: Decide canonical “Lo más vendido” collection**

Pick **one** collection handle to keep (recommend **`lo-mas-vendido`**). In **Shopify Admin → Products → Collections**, open `lo-mas-vendido-1` and either (a) merge products into `lo-mas-vendido` and delete `lo-mas-vendido-1`, or (b) keep `lo-mas-vendido-1` as canonical and **update every theme reference** in Task 4–5 to that handle instead. Do not leave two live bestseller collections.

- [ ] **Step 2: Add URL redirect for deprecated handle**

In **Shopify Admin → Online Store → Navigation → View URL redirects** (or **Settings → Apps** if using a redirect app), add:

- **Redirect from:** `/collections/lo-mas-vendido-1`  
- **Redirect to:** `/collections/lo-mas-vendido`  
(if you chose the opposite canonical in Step 1, invert paths.)

- [ ] **Step 3: Verify immune-system collection handle**

Confirm the live collection handle is exactly **`medicamentos-para-el-sistema-inmunologico-1`** (with `-1`). If the handle without `-1` still exists as empty, delete or redirect it to the `-1` URL.

- [ ] **Step 4: Verify “infecciosas” collection**

Confirm whether **`enfermedades-infecciosas-y-parasitarias`** exists in Admin. If it was removed, note **delete or replace** that block in Task 5.

**Verification (manual):**

- Open storefront URLs (production or preview):  
  `https://farmaciasmacross.com.mx/collections/lo-mas-vendido`  
  `https://farmaciasmacross.com.mx/collections/medicamentos-para-el-sistema-inmunologico-1`  
- Deprecated URL should **301/302** to canonical bestseller collection.

- [ ] **Step 5: Commit**

No repo change for Task 1 only. If you maintain an internal runbook, add a one-line note there; otherwise skip commit.

---

### Task 2: JSON syntax gate (automated sanity check)

**Files:** None created. **Test:** Shell only.

- [ ] **Step 1: Validate all theme JSON templates parse**

Shopify theme JSON files start with a `/* ... */` banner; strip it before `json.loads` (stdlib JSON does not allow comments).

Run from repo root:

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

def parse_shopify_theme_json(path: Path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", "", text, count=1, flags=re.DOTALL)
    return json.loads(text)

root = Path("Farmacia_Macross/theme/templates")
for p in sorted(root.glob("*.json")):
    parse_shopify_theme_json(p)
    print("OK", p)
PY
```

**Expected:** Each line `OK Farmacia_Macross/theme/templates/<name>.json` with exit code **0**.

- [ ] **Step 2: Commit**

Skip if no file changes.

---

### Task 3: PLP — default collection template (`collection.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/collection.json`

**Decision (locked for this plan):** You currently have **`filters_type`: `tags_filter`**, one **filter** block with `filtergroup`: `Cardiologia,Oncologia,`, and **`show_filter`: false**—filters never render. Either **enable** the sidebar or **remove** the dead block. This plan implements **enable tag sidebar** so the configured block is not misleading. If product tags in the catalog do not include `Cardiologia` / `Oncologia` exactly, update `filtergroup` in Step 3 to comma-separated tags that **exist on products** (verify in Admin → product → tags).

- [ ] **Step 1: Enable filter UI**

Replace the `main` section `settings` value for `show_filter` from `false` to `true`.

Minimal diff (apply with editor; only this key changes):

```json
"show_filter": true,
```

Full context for locate/replace in `collection.json` (lines 46–64 region):

```json
      "settings": {
        "container": "container",
        "grid_layout": "grid",
        "grid_columns": "4",
        "show_columns_switcher": true,
        "pagination_limit": 12,
        "paginate_type": "paginate",
        "show_sorting": true,
        "show_filter": true,
        "filters_type": "tags_filter",
```

- [ ] **Step 2: Align tag filter strings with real catalog tags**

Edit block `00b3badd-1613-4230-85d8-f87f04306aaa` → `settings` → `filtergroup` to match **actual** product tags used for pharmacy navigation (example only—replace with verified tags):

```json
"filtergroup": "Cardiologia,Oncologia,Reumatologia,",
```

Trailing comma after last tag is acceptable if theme already had it; match existing theme behavior.

- [ ] **Step 3: Re-run JSON parse check**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/collection.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

**Expected:** no traceback.

- [ ] **Step 4: Manual PLP check**

On a collection with tagged products (e.g. oncology), confirm sidebar filter appears and narrowing still paginates. If tag filters are wrong for the business, switch **later** to `storefront_filters` in Admin (Search & Discovery) and then set `"filters_type": "storefront_filters"` and `"show_filter": true`—out of scope unless you complete Admin filter setup.

- [ ] **Step 5: Commit**

```bash
git add Farmacia_Macross/theme/templates/collection.json
git commit -m "fix(theme): enable collection PLP tag filters"
```

---

### Task 4: PLP — flash-sale template copy (`collection.flash-sale.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/collection.flash-sale.json`

- [ ] **Step 1: Spanish heading for recent viewed**

In section `recent-viewed` → `settings` → `heading`, replace:

```json
"heading": "Recently Viewed Products",
```

with:

```json
"heading": "Recientemente vistos",
```

- [ ] **Step 2: Optional parity with default PLP**

If flash-sale collections should also show filters, copy the same `"show_filter": true` (and same `blocks` / `block_order` as `collection.json` `main`) into the `main` section here. **If** you do not want filters on flash pages, set `"show_filter": false` and **remove** any filter blocks from `main` in this file for consistency (currently there are no blocks—leave as-is).

- [ ] **Step 3: Validate JSON**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/collection.flash-sale.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

- [ ] **Step 4: Commit**

```bash
git add Farmacia_Macross/theme/templates/collection.flash-sale.json
git commit -m "fix(theme): align flash-sale PLP recent viewed copy with Spanish"
```

---

### Task 5: Homepage — collection list handles and accessibility CSS (`index.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/index.json`

- [ ] **Step 1: Fix immune-system collection handle**

In section `collection-list` → block `collection-list-1` → `settings` → `collection`, set:

```json
"collection": "medicamentos-para-el-sistema-inmunologico-1",
```

- [ ] **Step 2: Fix or remove “infecciosas” tile**

If Task 1 Step 4 confirmed the collection **does not exist**, delete block `collection-list-2` from `blocks` and remove `"collection-list-2"` from `block_order`. If it **exists**, leave as-is.

Example `block_order` after removal (only if you removed that block):

```json
      "block_order": [
        "6d4abb37-5aa2-4499-a2b0-5d85f0d36eec",
        "collection-list-1",
        "12985deb-0775-45ce-80f6-6be7f3150a91",
        "65e38235-f03b-43c9-8590-38c9c656e51c"
      ],
```

- [ ] **Step 3: Remove `font-size: 0` title hack on collection list**

In the same file, section `collection-list` → `custom_css`, replace the array with an empty array **or** delete the rule that sets link font size to `0px`. Preferred: **empty `custom_css`** so titles render normally:

```json
      "custom_css": [],
```

- [ ] **Step 4: Validate JSON**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/index.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

- [ ] **Step 5: Commit**

```bash
git add Farmacia_Macross/theme/templates/index.json
git commit -m "fix(theme): correct homepage collection handles and collection list CSS"
```

---

### Task 6: Homepage — product tabs (`index.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/index.json`

- [ ] **Step 1: Remove or fix the `new-arrivals` tab**

If collection **`new-arrivals`** does not exist in Admin, **delete** block `product-tabs-1` from `product-tabs` → `blocks` and remove `"product-tabs-1"` from `block_order`, leaving only `product-tabs-0`.

If **`new-arrivals`** exists and should show, leave block and ensure collection has products.

- [ ] **Step 2: Restore visible tab UI (if two tabs remain)**

Remove the rule hiding the tab header from `product-tabs` → `custom_css`. Change:

```json
      "custom_css": [
        ".product-tabs__header {margin-bottom: 50px; display: none;}"
      ],
```

to:

```json
      "custom_css": [
        ".product-tabs__header { margin-bottom: 50px; }"
      ],
```

If only **one** tab remains after Step 1, consider replacing `product-tabs` section with a single **`featured-collection`** section in a **follow-up** (not required here—YAGNI).

- [ ] **Step 3: Validate JSON**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/index.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

- [ ] **Step 4: Commit**

```bash
git add Farmacia_Macross/theme/templates/index.json
git commit -m "fix(theme): homepage product tabs visibility and dead collection tab"
```

---

### Task 7: Homepage — hero slideshow (`index.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/index.json`

- [ ] **Step 1: Align first slide CTA with image link**

In `slideshow` → block `slideshow-0` → `settings`, set `button_link` to the same destination as `image_link` (oncology collection):

```json
            "image_link": "shopify://collections/medicamento-oncologicos-al-mejor-precio-alta-especialidad",
            "button_text": "",
            "button_link": "shopify://collections/medicamento-oncologicos-al-mejor-precio-alta-especialidad",
```

Remove or blank **`button_text`** if no button should show; if the theme still renders a footer button, set Spanish label explicitly, e.g. `"footer_button": "Comprar ahora"` and `footer_link` to the same collection URL.

- [ ] **Step 2: Fix slides with empty `image_link`**

For each of `slider_item_cyLUVL`, `slider_item_VbEmYL`, `slider_item_44ybkN` (and any slide where `image_link` is `""`), either:

- Set `image_link` to a real `shopify://collections/...` or `shopify://products/...`, **or**
- Set `"disabled": true` on that **block** if the slide should not go live yet.

- [ ] **Step 3: Remove English demo footer copy**

In `slider_item_hfjzzr` (and any block still showing `New Collection` / `Shop Now`), set `footer_text`, `footer_button`, `footer_link` to **Spanish** or clear strings consistent with `slideshow-0`.

- [ ] **Step 4: Validate JSON**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/index.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

- [ ] **Step 5: Commit**

```bash
git add Farmacia_Macross/theme/templates/index.json
git commit -m "fix(theme): homepage hero links, disabled slides, and Spanish CTAs"
```

---

### Task 8: `/collections` index — replace demo (`list-collections.json`)

**Files:**

- Modify: `Farmacia_Macross/theme/templates/list-collections.json`

Replace demo blocks (`sweaters`, `leather-boots`, etc.) with **five** `collection_item` blocks pointing at real handles (reuse homepage `shopify://shop_images/...` URLs; change in editor if an image is a better fit for hormonal vs infectious art).

**Full file contents** for `Farmacia_Macross/theme/templates/list-collections.json` (includes Shopify banner comment):

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "sections": {
    "main": {
      "type": "collection-list-template",
      "blocks": {
        "cl-onc": {
          "type": "collection_item",
          "settings": {
            "collection": "medicamento-oncologicos-al-mejor-precio-alta-especialidad",
            "image": "shopify://shop_images/imagen_2023-04-03_142546553.png"
          }
        },
        "cl-immune": {
          "type": "collection_item",
          "settings": {
            "collection": "medicamentos-para-el-sistema-inmunologico-1",
            "image": "shopify://shop_images/imagen_2023-04-03_142021791.png"
          }
        },
        "cl-cardio": {
          "type": "collection_item",
          "settings": {
            "collection": "cardiologia",
            "image": "shopify://shop_images/imagen_2023-04-03_143736464.png"
          }
        },
        "cl-reuma": {
          "type": "collection_item",
          "settings": {
            "collection": "reumatologia-y-traumatologia",
            "image": "shopify://shop_images/imagen_2023-04-03_145556394.png"
          }
        },
        "cl-hormonal": {
          "type": "collection_item",
          "settings": {
            "collection": "productos-hormonales-especializados",
            "image": "shopify://shop_images/imagen_2023-04-03_142914263.png"
          }
        }
      },
      "block_order": [
        "cl-onc",
        "cl-immune",
        "cl-cardio",
        "cl-reuma",
        "cl-hormonal"
      ],
      "settings": {
        "title": "Categorías",
        "description": "<p>Medicamentos de alta especialidad por área terapéutica.</p>"
      }
    }
  },
  "order": [
    "main"
  ]
}
```

- [ ] **Step 1: Replace entire file** with the block above (overwrite previous demo `collection_item` blocks).

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/list-collections.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
```

- [ ] **Step 3: Commit**

```bash
git add Farmacia_Macross/theme/templates/list-collections.json
git commit -m "fix(theme): replace demo list-collections with Macross categories"
```

---

### Task 9: Optional cleanup — homepage `order` and noise

**Files:**

- Modify: `Farmacia_Macross/theme/templates/index.json`

- [ ] **Step 1: Remove disabled sections from `order` array** (optional but recommended)

Remove `"video_CAiz8N"` from the root `"order"` list if that section is permanently disabled, **or** delete the entire `video_CAiz8N` section object. Same for `8b631405-afe0-44ff-82fd-eb2e7446734b` if disabled.

Current tail reference:

```json
  "order": [
    "custom-code",
    "slideshow",
    "1680553798df70faa0",
    "video_CAiz8N",
    "video_HpTgng",
    ...
  ]
```

- [ ] **Step 2: Validate JSON + commit**

```bash
python3 -c "import json,re; t=open('Farmacia_Macross/theme/templates/index.json').read(); t=re.sub(r'/\\*.*?\\*/','',t,count=1,flags=re.S); json.loads(t)"
git add Farmacia_Macross/theme/templates/index.json
git commit -m "chore(theme): drop disabled homepage sections from template order"
```

---

### Task 10: Theme Check (optional CI-style gate)

**Files:** None.

- [ ] **Step 1: Run Shopify Theme Check** (requires [Shopify CLI](https://shopify.dev/docs/themes/tools/cli/install))

```bash
cd Farmacia_Macross/theme && shopify theme check
```

**Expected:** Exit code **0**, or fix reported **error**-level issues only (warnings may pre-exist).

- [ ] **Step 2: Commit**

Only if `theme check` config or fixes were added; otherwise skip.

---

## Self-review (plan quality)

**1. Spec coverage (prior conversation notes):**

| Note | Task |
|------|------|
| Duplicate `lo-mas-vendido` / `-1` | Task 1 |
| Handle `medicamentos-…-1` vs theme `…` without `-1` | Task 5 |
| Missing / orphan `enfermedades-infecciosas-y-parasitarias` | Task 1 + 5 |
| `new-arrivals` tab likely invalid | Task 6 |
| `show_filter` false with filter block | Task 3 |
| Flash-sale English recent viewed | Task 4 |
| Hero `image_link` vs `button_link` to `/all` | Task 7 |
| Empty slide links, English “New Collection” | Task 7 |
| `list-collections` demo sweaters | Task 8 |
| Hidden tab header CSS | Task 6 |
| `font-size: 0` on collection titles | Task 5 |
| Disabled sections in `order` | Task 9 |
| Optional: migrate to storefront filters | Task 3 manual note (not automated) |

**2. Placeholder scan:** No `TBD` / `TODO` / vague “add validation” steps; all JSON fragments are concrete. Tag strings in Task 3 require merchant verification—called out explicitly.

**3. Type consistency:** All `collection` settings use string **handles** only, matching Minimog section schemas.

---

**Plan complete and saved to** `Farmacia_Macross/docs/superpowers/plans/2026-05-14-macross-homepage-plp-improvements.md`.

**Two execution options:**

1. **Subagent-driven (recommended)** — dispatch a fresh subagent per task, review between tasks, fast iteration (`superpowers:subagent-driven-development`).

2. **Inline execution** — run tasks in this session with checkpoints (`superpowers:executing-plans`).

**Which approach do you want?**
