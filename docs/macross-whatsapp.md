# Native Macross WhatsApp

Replaces the Seedgrow theme assets and **WhatsApp Chat Widget** Shopify app embed with a native theme module: geo routing, human Spanish pre-filled messages, and a 3-sucursal picker.

## Theme files

| File | Role |
|------|------|
| `snippets/macross-whatsapp-config.liquid` | Injects branch numbers + message templates as JSON |
| `snippets/macross-whatsapp-widget.liquid` | Desktop FAB + branch picker modal |
| `assets/macross-whatsapp.js` | Routing, launchers, `wa.me` links |
| `assets/macross-whatsapp.css` | FAB, modal, mobile menu launcher styles |

Layouts load config + widget before `</body>` and `macross-whatsapp.js` (defer).

## Theme settings (Macross section)

| Setting | Purpose |
|---------|---------|
| `macross_wa_cdmx_number` | CDMX WhatsApp (default `+525540729473`) |
| `macross_wa_puebla_number` | Puebla WhatsApp |
| `macross_wa_guadalajara_number` | Guadalajara distribution center WhatsApp (default CDMX number until local line is set) |
| `macross_wa_show_desktop_fab` | Show/hide desktop floating button |
| `macross_wa_fab_label` | FAB label (locale default: "WhatsApp") |
| `macross_whatsapp_pdp_addons_integration` | On PDP, hide desktop FAB; sticky ATC still works |

Message copy lives in locales under `macross.whatsapp.*` (`es.json`, `en.default.json`).

## Launchers

All use `data-macross-whatsapp-launcher`:

- Desktop FAB (`macross-whatsapp-widget.liquid`)
- Mobile menu (`macross-mobile-whatsapp.liquid`)
- Mobile sticky bar (`mobile-sticky-bar.liquid`)
- PDP sticky ATC (`sticky-atc.liquid`) — also `data-macross-whatsapp-context="product"` for product prefill

## Routing behavior

1. **Subdomain / `?macross_branch=`** → direct `wa.me` to that branch (high confidence).
2. **Apex, cookies declined** → native picker (3 sucursales).
3. **Apex, cookies accepted** → IP + optional GPS; high → direct; medium → picker + "Sucursal recomendada"; low → picker, reorder only.

Dev console: `MacrossWhatsApp.getActiveBranchKey()` (alias: `MacrossWhatsAppGeo`).

## Shopify Admin — remove app embed

After deploying the theme:

1. **Settings → Apps and sales channels** → uninstall or disable **WhatsApp Chat Widget** (Seedgrow) so it cannot re-inject an embed.
2. Confirm **Online Store → Themes → Customize → App embeds** has no WhatsApp Chat Widget block enabled.

The theme `settings_data.json` no longer includes the app embed block; Admin uninstall prevents duplicate desktop bubbles.

## Deploy checklist

1. Push theme (`shopify theme push --live` or dev theme).
2. Uninstall/disable WhatsApp Chat Widget app in Admin.
3. Verify branch numbers in **Theme settings → Macross → WhatsApp — sucursales**.
4. Test matrix:

| Scenario | Expected |
|----------|----------|
| Desktop FAB on apex, cookies declined | Picker, 3 sucursales, human copy |
| `puebla.farmaciasmacross.com.mx` | Direct Puebla `wa.me` + general message |
| PDP mobile sticky WhatsApp | Product prefill message |
| DOM | No `.wa__widget_container` (Seedgrow gone) |
| Theme dev | `127.0.0.1:9292?macross_branch=cdmx` routes to CDMX |

## Related

- Location subdomains DNS: `docs/location-subdomains-runbook.md`
