# Categories Icon Strip + Scroll Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace collection image tiles with icon-based pill strips that auto-scroll on the homepage and reveal progressively on the /collections page, using Font Awesome Free icons driven by a collection metafield with SVG fallback.

**Architecture:** A new `snippets/collection-icon.liquid` renders the icon layer (FA icon if metafield set, else existing SVG from `category-icon.liquid`). The homepage `collection-list` section gets a CSS marquee loop mode. The `/collections` page gets a compact icon-card grid with IntersectionObserver fade-in reveal. Font Awesome Free 6 is loaded via CDN in `theme.liquid` behind a theme setting toggle.

**Tech Stack:** Shopify Liquid, CSS `@keyframes` marquee, vanilla JS IntersectionObserver, Font Awesome Free 6 CDN, Shopify Collection Metafields (`custom.fa_icon`)

---

## Approach Comparison

| Approach | Deps | Admin work | Flexibility | Recommended for |
|---|---|---|---|---|
| **A. FA + Metafield** | FA CDN (~40KB) | Set icon per collection in admin | Any FA icon per collection | This plan |
| **B. Inline SVG map** | None | Edit Liquid snippet | Fixed map in code | Already done (`category-icon.liquid`) |
| **C. Phosphor Icons** | None | Edit Liquid snippet | 1000+ icons inline | If CDN unacceptable |

**Chosen: Approach A** — FA metafield gives admin full control. SVG fallback from existing `category-icon.liquid` covers any collection without a metafield set.

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `layout/theme.liquid` | Modify | Add FA CDN link behind `settings.enable_fa_icons` toggle |
| `config/settings_schema.json` | Modify | Add FA toggle + metafield namespace/key settings |
| `snippets/collection-icon.liquid` | **Create** | Renders FA `<i>` OR SVG fallback per collection |
| `snippets/collection-card.liquid` | Modify | Accept `icon_mode` param; render icon strip pill or image card |
| `sections/collection-list.liquid` | Modify | Add `icon_mode` + `marquee` settings; CSS marquee output |
| `sections/collection-list-template.liquid` | Modify | Compact icon-card grid + IntersectionObserver reveal |
| `assets/sf-collection-icons.css` | **Create** | Marquee animation, pill styles, reveal animation |

---

## Metafield Setup (manual, admin)

Before any code runs, merchant must create the metafield definition in Shopify:

1. Shopify Admin → Settings → Custom data → Collections
2. Add definition: namespace `custom`, key `fa_icon`, type `Single line text`
3. Per collection, set value to FA class string: e.g. `fa-solid fa-ribbon`

Available FA Free icons per specialty:
- Oncología → `fa-solid fa-ribbon`
- Hematología → `fa-solid fa-droplet`
- Reumatología y traumatología → `fa-solid fa-bone`
- Infecciosas y parasitarias → `fa-solid fa-virus`
- Sistema inmunológico → `fa-solid fa-shield-halved`
- Hormonales → `fa-solid fa-flask`
- Cardiología → `fa-solid fa-heart-pulse`
- Nefrología → *(no free FA kidney icon)* → leave blank → SVG fallback renders

---

## Task 1: Theme Setting + FA CDN

**Files:**
- Modify: `config/settings_schema.json`
- Modify: `layout/theme.liquid` (after `<head>` charset meta, before `</head>`)

- [ ] **Step 1: Add FA toggle to settings_schema.json**

Find the last object in `settings_schema.json` array (before the closing `]`). Add a new settings group:

```json
{
  "name": "Icons",
  "settings": [
    {
      "type": "checkbox",
      "id": "enable_fa_icons",
      "label": "Enable Font Awesome icons",
      "default": true,
      "info": "Loads Font Awesome Free 6 from CDN (~40 KB). Used for collection icon strips."
    }
  ]
}
```

- [ ] **Step 2: Add FA CDN link to theme.liquid**

In `layout/theme.liquid`, find `</head>` and insert before it:

```liquid
{% if settings.enable_fa_icons %}
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" media="print" onload="this.media='all'" crossorigin="anonymous">
  <noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous"></noscript>
{% endif %}
```

`media="print" onload="this.media='all'"` = non-render-blocking load (performance).

- [ ] **Step 3: Verify in browser**

Open any page → DevTools → Network → filter `font-awesome` → should appear as one CSS request.

- [ ] **Step 4: Commit**

```bash
git add layout/theme.liquid config/settings_schema.json
git commit -m "feat(theme): add Font Awesome Free 6 CDN behind settings toggle"
```

---

## Task 2: Create `snippets/collection-icon.liquid`

**Files:**
- Create: `snippets/collection-icon.liquid`

**Interface:** accepts `collection` (Liquid collection object), `size` (CSS class string, default `text-4xl`).

- [ ] **Step 1: Create the snippet**

```liquid
{%- liquid
  assign fa_icon = collection.metafields.custom.fa_icon | strip
  assign icon_size = size | default: 'text-4xl'
-%}
<span class="collection-icon" aria-hidden="true">
  {%- if fa_icon != blank -%}
    <i class="{{ fa_icon }} {{ icon_size }}"></i>
  {%- else -%}
    {%- render 'category-icon', collection: collection -%}
  {%- endif -%}
</span>
```

- [ ] **Step 2: Test render manually**

In a test Liquid template or via theme editor preview, call:
```liquid
{% render 'collection-icon', collection: collections['cardiologia'], size: 'text-3xl' %}
```
Expected: FA heart icon if metafield set, else SVG from category-icon.liquid.

- [ ] **Step 3: Commit**

```bash
git add snippets/collection-icon.liquid
git commit -m "feat(theme): add collection-icon snippet with FA + SVG fallback"
```

---

## Task 3: Create `assets/sf-collection-icons.css`

**Files:**
- Create: `assets/sf-collection-icons.css`

- [ ] **Step 1: Create CSS file**

```css
/* ── Collection icon pill strip ───────────────────────────────── */
.sf-icon-strip {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  scroll-snap-type: x mandatory;
  padding-bottom: 8px;
}
.sf-icon-strip::-webkit-scrollbar { display: none; }

.sf-icon-pill {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  flex: 0 0 auto;
  scroll-snap-align: start;
  padding: 16px 20px;
  border-radius: 16px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.07);
  text-decoration: none;
  color: inherit;
  transition: box-shadow 0.2s, transform 0.2s;
  min-width: 90px;
}
.sf-icon-pill:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.sf-icon-pill .collection-icon { font-size: 28px; color: var(--color-primary, #1f4e8c); }
.sf-icon-pill .collection-icon svg { width: 36px; height: 36px; }
.sf-icon-pill__label { font-size: 12px; font-weight: 600; text-align: center; line-height: 1.2; color: #111; }

/* ── Marquee mode (homepage auto-scroll) ─────────────────────── */
.sf-marquee-track {
  display: flex;
  gap: 16px;
  width: max-content;
  animation: sf-marquee 30s linear infinite;
}
.sf-marquee-track:hover { animation-play-state: paused; }
.sf-marquee-wrapper {
  overflow: hidden;
  width: 100%;
}
@keyframes sf-marquee {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ── /collections page compact grid ─────────────────────────── */
.sf-icon-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
@media (min-width: 640px)  { .sf-icon-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1024px) { .sf-icon-grid { grid-template-columns: repeat(4, 1fr); } }

.sf-icon-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 20px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.07);
  text-decoration: none;
  color: inherit;
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.4s, transform 0.4s, box-shadow 0.2s;
}
.sf-icon-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}
.sf-icon-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
.sf-icon-card .collection-icon { font-size: 24px; flex: 0 0 auto; color: var(--color-primary, #1f4e8c); }
.sf-icon-card .collection-icon svg { width: 28px; height: 28px; }
.sf-icon-card__text { display: flex; flex-direction: column; }
.sf-icon-card__title { font-size: 14px; font-weight: 600; color: #111; }
.sf-icon-card__count { font-size: 12px; color: #777; }
```

- [ ] **Step 2: Commit**

```bash
git add assets/sf-collection-icons.css
git commit -m "feat(theme): add collection icon strip, marquee, and grid CSS"
```

---

## Task 4: Update `sections/collection-list.liquid` — Marquee Mode

**Files:**
- Modify: `sections/collection-list.liquid` (top `{% liquid %}` block, `{% style %}` block, render block, schema)

- [ ] **Step 1: Load CSS at top of section**

Add as first line of `collection-list.liquid`:

```liquid
{{ 'sf-collection-icons.css' | asset_url | stylesheet_tag }}
```

- [ ] **Step 2: Add icon_mode + marquee settings to schema**

In the section schema `"settings"` array, add after the existing heading/subheading settings:

```json
{
  "type": "header",
  "content": "Icon strip mode"
},
{
  "type": "checkbox",
  "id": "icon_mode",
  "label": "Icon strip mode (replaces image tiles)",
  "default": false
},
{
  "type": "checkbox",
  "id": "marquee_mode",
  "label": "Auto-scroll marquee (homepage use)",
  "default": false,
  "info": "Loops collection pills continuously. Works best with icon mode enabled."
}
```

- [ ] **Step 3: Add icon strip render block**

Find where blocks are looped (around line 148–160 in `collection-list.liquid`). Wrap the existing render with a condition; add icon strip branch:

```liquid
{% if section.settings.icon_mode %}
  {%- if section.settings.marquee_mode -%}
    <div class="sf-marquee-wrapper">
      <div class="sf-marquee-track">
        {%- for block in section.blocks -%}
          {%- assign collection = collections[block.settings.collection] -%}
          {%- assign pill_title = block.settings.title | default: collection.title -%}
          <a href="{{ collection.url }}" class="sf-icon-pill" {{ block.shopify_attributes }}>
            {%- render 'collection-icon', collection: collection, size: 'text-3xl' -%}
            <span class="sf-icon-pill__label">{{ pill_title }}</span>
          </a>
        {%- endfor -%}
        {%- comment -%}Duplicate set for seamless loop{%- endcomment -%}
        {%- for block in section.blocks -%}
          {%- assign collection = collections[block.settings.collection] -%}
          {%- assign pill_title = block.settings.title | default: collection.title -%}
          <a href="{{ collection.url }}" class="sf-icon-pill" aria-hidden="true">
            {%- render 'collection-icon', collection: collection, size: 'text-3xl' -%}
            <span class="sf-icon-pill__label">{{ pill_title }}</span>
          </a>
        {%- endfor -%}
      </div>
    </div>
  {%- else -%}
    <div class="sf-icon-strip">
      {%- for block in section.blocks -%}
        {%- assign collection = collections[block.settings.collection] -%}
        {%- assign pill_title = block.settings.title | default: collection.title -%}
        <a href="{{ collection.url }}" class="sf-icon-pill" {{ block.shopify_attributes }}>
          {%- render 'collection-icon', collection: collection, size: 'text-3xl' -%}
          <span class="sf-icon-pill__label">{{ pill_title }}</span>
        </a>
      {%- endfor -%}
    </div>
  {%- endif -%}
{% else %}
  {{- existing_grid_html -}}  {# keep existing grid render unchanged #}
{% endif %}
```

> **Note to implementer:** The `{{- existing_grid_html -}}` placeholder above means: keep ALL the existing grid/slider Liquid from the original section unchanged inside the `{% else %}` branch. Do not delete it.

- [ ] **Step 4: Verify homepage**

In theme editor → homepage → "Explora por especialidad" → enable "Icon strip mode" + "Auto-scroll marquee". Confirm pills render and scroll.

- [ ] **Step 5: Commit**

```bash
git add sections/collection-list.liquid
git commit -m "feat(theme): add icon strip + marquee mode to collection-list section"
```

---

## Task 5: Update `sections/collection-list-template.liquid` — Icon Grid + Reveal

**Files:**
- Modify: `sections/collection-list-template.liquid`

- [ ] **Step 1: Load CSS**

Add as first line:

```liquid
{{ 'sf-collection-icons.css' | asset_url | stylesheet_tag }}
```

- [ ] **Step 2: Replace static grid with icon-card grid**

Replace the inner `<div class="grid sf-grid ...">` block and everything inside it with:

```liquid
<div class="sf-icon-grid" id="sf-collection-grid">
  {% if section.settings.display_type == 'all' %}
    {% for collection in collections %}
      <a href="{{ collection.url }}" class="sf-icon-card">
        {%- render 'collection-icon', collection: collection -%}
        <div class="sf-icon-card__text">
          <span class="sf-icon-card__title">{{ collection.title }}</span>
          <span class="sf-icon-card__count">{{ collection.all_products_count }} productos</span>
        </div>
      </a>
    {% endfor %}
  {% else %}
    {% for block in section.blocks %}
      {%- assign collection = collections[block.settings.collection] -%}
      <a href="{{ collection.url }}" class="sf-icon-card" {{ block.shopify_attributes }}>
        {%- render 'collection-icon', collection: collection -%}
        <div class="sf-icon-card__text">
          <span class="sf-icon-card__title">{{ collection.title }}</span>
          <span class="sf-icon-card__count">{{ collection.all_products_count }} productos</span>
        </div>
      </a>
    {% endfor %}
  {% endif %}
</div>
<script>
  (function () {
    var cards = document.querySelectorAll('#sf-collection-grid .sf-icon-card');
    if (!cards.length) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    cards.forEach(function (c, i) {
      c.style.transitionDelay = (i * 40) + 'ms';
      io.observe(c);
    });
  })();
</script>
```

- [ ] **Step 3: Verify /collections page**

Navigate to `/collections`. Cards should fade in staggered as they enter viewport. Each shows icon + name + product count.

- [ ] **Step 4: Commit**

```bash
git add sections/collection-list-template.liquid
git commit -m "feat(theme): icon-card grid with IntersectionObserver reveal on /collections"
```

---

## Task 6: Wire up index.json for Homepage Marquee

**Files:**
- Modify: `templates/index.json`

- [ ] **Step 1: Enable icon + marquee mode in homepage collection-list block**

In `templates/index.json`, find `"collection-list"` section settings and add:

```json
"icon_mode": true,
"marquee_mode": true
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "
import json, re
s = open('templates/index.json').read()
json.loads(re.sub(r'/\*.*?\*/', '', s, flags=re.S))
print('OK')
"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add templates/index.json
git commit -m "feat(theme): enable icon marquee mode on homepage collection strip"
```

---

## Self-Review

**Spec coverage:**
- ✅ Infinite scroll → marquee auto-scroll on homepage + horizontal swipe on /collections
- ✅ Font Awesome icons per collection
- ✅ Metafield (`custom.fa_icon`) for admin icon configuration
- ✅ SVG fallback when metafield blank (uses existing `category-icon.liquid`)
- ✅ `/collections` page icon-card grid with reveal animation
- ✅ Alternatives documented (Phosphor, inline SVG map)

**Gaps / notes:**
- Marquee animation speed (30s) is hardcoded — could add a schema `range` setting if needed
- `display_type: all` on /collections paginates at 20 collections max per Liquid loop — if store ever exceeds 20, add `paginate` tag + AJAX load-more
- FA CDN is loaded on every page once toggle is on — acceptable given pharmacy site scale
- Nefrología has no free FA kidney icon → SVG fallback renders correctly
