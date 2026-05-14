# Discount banner promo image — alt-text marker design

**Status:** Approved direction (brainstorming closure)  
**Scope:** `discount-product` PDP masthead promo slot + product media pipeline  
**Non-goals:** Hidden catalog products, metafield-linked gift SKUs, variant-picker JS sync for promo (phase 2 if needed)

---

## Problem

Merchants want a **vial / pack shot** (or similar) shown **only in the discount masthead banner**, while keeping normal PDP gallery behavior for standard merchandising images. The asset may **live in Shopify product media** for convenience, but must **not** appear as a normal carousel/gallery slide.

---

## Approach

### 1. Reserved alt-text token

- Store a dedicated image in **product media**.
- Set its **alt text** to include a reserved, documented substring (case-insensitive), e.g. **`[macross-promo]`**.
- The substring should appear in addition to any human-readable description the team wants (e.g. `Frasco 30 ml [macross-promo]`) so accessibility is not reduced to an empty or meaningless alt.

**Rationale:** No new metafields, no duplicate products. Single admin surface (Media). Easy to grep in Liquid.

### 2. Resolution order (banner image)

1. **Section** `masthead_promo_image` (existing theme setting) — if present, use it (campaign / one-off override). Alt: `masthead_promo_image_alt` when non-blank.
2. Else **first product media** whose `alt` contains `[macross-promo]` (case-insensitive match on `media.alt` or preview image alt as available in Liquid).
3. Else **no extra promo image** in the masthead (current behavior when section image blank).

### 3. Exclude marked media from the main product gallery

- Where the theme builds the **product media list** for the PDP (same template using `discount-product`), **omit** any media whose alt contains `[macross-promo]`.
- **Invariant:** A given media item is either shown in the **banner** (when selected by the rule above) or must not appear in the **default** gallery loop. If multiple media match the marker, **only the first match** is used for the banner; **all** matches are excluded from the main gallery to avoid duplicates and accidental “hidden” slides.

**Implementation note:** Identify the single Liquid/JavaScript choke point that supplies `product.media` to `product-media` (or equivalent) for this template only, so other templates are unchanged unless we explicitly want global behavior (default: **discount template / discount-product section only**).

### 4. Edge cases

| Case | Behavior |
|------|----------|
| Marker present, section image also set | Section image wins; marked media still excluded from main gallery |
| Multiple marked images | First match → banner; all marked → excluded from gallery |
| No marker, no section image | No promo well image (unchanged) |
| Marker on only variant-specific association | Defer to phase 2 if Minimog variant media logic requires JS; v1 documents product-level `product.media` only |

### 5. Documentation (merchant-facing)

- Short paragraph in internal runbook or theme editor **info** on the section setting: exact token, example alt string, reminder that marked images **do not** show in the main gallery on discount PDP.

---

## Alternatives considered (not chosen)

- **Featured image fallback:** Rejected — user requires explicit marker and separation from “normal” display images.
- **Metafield file:** Rejected for v1 — extra admin surface; user preferred gallery + marker.
- **Hidden products + metafield link:** Rejected — operational complexity.

---

## Self-review

- **Placeholders:** None.
- **Consistency:** Section override precedes marker; exclusion applies to all marked items.
- **Scope:** Single template/section behavior unless explicitly broadened.
- **Ambiguity:** Token fixed as `[macross-promo]`; document in theme strings / README if locale-specific copy is needed later.

---

## Next step

Use **writing-plans** to produce an implementation plan: Liquid assignments in `discount-product.liquid`, media filtering hook (likely `product-media` or snippet used only on discount PDP), optional section `info` text, and manual QA checklist (marker only, section override, no marker).
