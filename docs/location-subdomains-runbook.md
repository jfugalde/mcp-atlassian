# Location subdomains — runbook

Serve the Macross Shopify store on three location subdomains and route WhatsApp to the matching branch via theme hostname logic.

**Store:** `macross-pharma.myshopify.com`  
**Primary domain:** `farmaciasmacross.com.mx` (keep as primary; do not redirect subdomains to apex)

| Subdomain | Branch | WhatsApp |
|-----------|--------|----------|
| `cdmx.farmaciasmacross.com.mx` | Sucursal CDMX | +525540729473 |
| `puebla.farmaciasmacross.com.mx` | Sucursal Puebla | +522224454192 |
| `guadalajara.farmaciasmacross.com.mx` | Centro de distribución Guadalajara | CDMX (+525540729473) |

Theme routing lives in `theme/assets/macross-whatsapp.js` (hostname > cookie-gated IP/GPS on apex). See also `docs/macross-whatsapp.md`.

---

## 1. Cloudflare DNS

**Prerequisites:** Zone `farmaciasmacross.com.mx` active in Cloudflare. API token / account ID in 1Password (`Infrastructure/Cloudflare Admin Key`).

1. Open **Cloudflare Dashboard → farmaciasmacross.com.mx → DNS**.
2. **SSL/TLS → Overview:** set encryption to **Full (strict)**.
3. Complete **Shopify domain connection first** (step 2) so you have the CNAME target for each subdomain.
4. Add records (**DNS only / grey cloud** recommended initially):

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `cdmx` | *(from Shopify)* | DNS only |
| CNAME | `puebla` | *(from Shopify)* | DNS only |
| CNAME | `guadalajara` | *(from Shopify)* | DNS only |

5. Wait for DNS propagation (minutes to hours).

**Verify:**

```bash
curl -sI "https://cdmx.farmaciasmacross.com.mx" | head -5
curl -sI "https://puebla.farmaciasmacross.com.mx" | head -5
curl -sI "https://guadalajara.farmaciasmacross.com.mx" | head -5
```

Expect `HTTP/2 200` (or 301 to HTTPS then 200) and valid TLS.

---

## 2. Shopify Admin — connect subdomains

1. **Settings → Domains → Connect existing domain**.
2. Enter `cdmx.farmaciasmacross.com.mx` → follow DNS instructions → verify.
3. Repeat for `puebla.farmaciasmacross.com.mx` and `guadalajara.farmaciasmacross.com.mx`.
4. Confirm **primary domain** remains `farmaciasmacross.com.mx`.
5. For each location subdomain, set domain type to **Alias** (not Redirect):
   - **Alias** — serves the Online Store on that hostname; **address bar stays** `cdmx.farmaciasmacross.com.mx` (required for theme hostname WhatsApp routing).
   - **Redirect** — sends visitors to the primary domain and **breaks** branch detection (`301` → apex).
   - Shopify notes alias misuse can affect SEO; here it is intentional (location entry points). Use alias only for these three subdomains, not as a blanket pattern.
   - Docs: [Shopify routing domains / SEO](https://help.shopify.com/en/manual/domains/domain-type/routing-domain#seo-considerations)

**Verify:** Open each subdomain in a browser — URL bar must **keep** the subdomain (e.g. `puebla.farmaciasmacross.com.mx`), homepage loads with the live theme.

```bash
curl -sI "https://cdmx.farmaciasmacross.com.mx" | head -5
# Bad:  location: https://farmaciasmacross.com.mx/
# Good: HTTP 200, no redirect to apex
```

---

## 3. Deploy theme

From `Farmacia_Macross/theme/`:

```bash
shopify theme push --only assets/macross-whatsapp-geo.js,assets/macross-whatsapp-geo.css,layout/theme.liquid,config/settings_schema.json,locales/es.json,locales/en.default.json
```

Or merge your branch and publish the theme in Admin.

---

## 4. Local dev testing (before DNS)

With `shopify theme dev` at `http://127.0.0.1:9292`:

```text
http://127.0.0.1:9292/?macross_branch=puebla
http://127.0.0.1:9292/?macross_branch=cdmx
http://127.0.0.1:9292/?macross_branch=guadalajara
```

**Console checks:**

```javascript
JSON.parse(sessionStorage.getItem('macross_wa_branch'));
// expect branchKey + confidence: "high" + source: "hostname"

window.MacrossWhatsAppGeo.getActiveBranchKey();
// "puebla" etc.
```

**WhatsApp tap:** should open `wa.me` for that branch without cookie accept (hostname is not tracking).

**Automated sanity checks (no browser):** from repo root, the hostname/dev-query helpers in `macross-whatsapp-geo.js` can be spot-checked with Node (hostname map, `?macross_branch=` parsing, low-confidence badge skip). Re-run after edits to that file.

**Production go-live checklist:**

1. [ ] Cloudflare CNAMEs live (grey cloud) + Full (strict) SSL
2. [ ] All three subdomains connected in Shopify Domains (no redirect to apex)
3. [ ] Theme pushed/published with `macross-whatsapp-geo.js`
4. [ ] Run test matrix (section 5) on each subdomain + apex
5. [ ] Update marketing QR/links to location URLs (section 6)

---

## 5. Production test matrix

| # | URL / setup | Cookie | Action | Expected |
|---|-------------|--------|--------|----------|
| 1 | `puebla.farmaciasmacross.com.mx` | any | Tap WhatsApp (menu / sticky / PDP) | Direct `wa.me` Puebla |
| 2 | `cdmx.farmaciasmacross.com.mx` | any | Tap WhatsApp | Direct `wa.me` CDMX |
| 3 | `guadalajara.farmaciasmacross.com.mx` | any | Tap WhatsApp | Direct `wa.me` Guadalajara |
| 4 | `farmaciasmacross.com.mx` | Decline | Tap WhatsApp | Plain branch picker, no badge |
| 5 | `farmaciasmacross.com.mx` | Accept | Tap WhatsApp | IP/GPS routing (direct or picker per confidence) |
| 6 | Apex | Accept, unknown region | Tap WhatsApp | Picker, reorder only (no badge if low confidence) |

**Reset state in DevTools:**

```javascript
localStorage.removeItem('theme_cookie_banner_ack');
localStorage.removeItem('macross_tracking_consent');
sessionStorage.removeItem('macross_wa_branch');
location.reload();
```

---

## 6. Marketing links / QR

Use location URLs so WhatsApp skips geo guessing:

- CDMX: `https://cdmx.farmaciasmacross.com.mx`
- Puebla: `https://puebla.farmaciasmacross.com.mx`
- Guadalajara: `https://guadalajara.farmaciasmacross.com.mx`

---

## 7. Troubleshooting

| Symptom | Check |
|---------|--------|
| Subdomain SSL error | Shopify domain verified? Cloudflare Full (strict)? |
| Subdomain redirects to apex | Shopify Domains → change subdomain from **Redirect** to **Alias** |
| Wrong WhatsApp branch | `sessionStorage.macross_wa_branch`; clear and reload |
| Geo not running on apex | Cookie accept → `macross_tracking_consent === "1"` |

---

## Out of scope (v1)

- Cloudflare Worker
- Separate Shopify stores per location
- Automated DNS via Terraform
