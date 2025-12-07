# Developer Technical Guide - farmaciasmacross.com.mx
## Guía Técnica de Implementación y Corrección

**Fecha de Auditoría:** Diciembre 2024  
**Sitio:** https://farmaciasmacross.com.mx  
**Plataforma:** Shopify  
**Tema:** Minimog (detectado)

---

## 📋 Resumen Técnico

### Métricas Actuales de Performance

**Mobile:**
- Performance Score: **42/100** ❌
- LCP (Largest Contentful Paint): **15.3s** (target: <2.5s) ❌
- FCP (First Contentful Paint): **8.8s** (target: <1.8s) ❌
- TTI (Time to Interactive): **19.9s** (target: <3.8s) ❌
- CLS (Cumulative Layout Shift): **0.176** (target: <0.1) ⚠️

**Desktop:**
- Performance Score: **74/100** ⚠️
- LCP: **1.02s** ✅
- FCP: **0.57s** ✅
- TTI: **3.87s** ⚠️
- CLS: **0.003** ✅

### Problemas Técnicos Identificados

1. **Hero Images demasiado grandes** (5000×2617px)
2. **Múltiples scripts de tracking** cargando síncronamente
3. **Scripts bloqueando renderizado** (vendor.min.js, app.min.js, foxkit-app.min.js)
4. **Fuentes sin preload** (Jost, Roboto Condensed)
5. **Falta de headers de seguridad** (HSTS, CSP, X-Frame-Options)
6. **Falta de banner de cookies**
7. **Schema markup incompleto** para productos
8. **Alt text faltante** en imágenes

---

## 🔧 Guía de Corrección por Issue

### Issue #1: Hero Images Demasiado Grandes (LCP Crítico)

**Problema:**
- Imagen hero: 5000×2617px
- Peso estimado: ~500KB-1MB
- Causa LCP de 15.3s en móvil

**Solución:**

#### Paso 1: Optimizar Imagen Original

```bash
# Usar ImageMagick o similar para optimizar
convert macrossshopy.jpg -resize 1920x1080 -quality 85 -strip macrossshopy-optimized.jpg

# Convertir a WebP
cwebp -q 85 macrossshopy-optimized.jpg -o macrossshopy.webp
```

#### Paso 2: Crear Variantes Responsive

```bash
# Móvil (375px ancho)
convert macrossshopy.jpg -resize 375x -quality 85 mobile-hero.webp

# Tablet (768px ancho)
convert macrossshopy.jpg -resize 768x -quality 85 tablet-hero.webp

# Desktop (1920px ancho)
convert macrossshopy.jpg -resize 1920x -quality 85 desktop-hero.webp
```

#### Paso 3: Implementar en Shopify Theme

**Archivo:** `sections/hero-banner.liquid` o similar

```liquid
{% comment %} Hero Image con srcset y lazy loading {% endcomment %}
<picture>
  <source 
    media="(max-width: 375px)" 
    srcset="{{ 'mobile-hero.webp' | asset_url }}"
    type="image/webp">
  <source 
    media="(max-width: 768px)" 
    srcset="{{ 'tablet-hero.webp' | asset_url }}"
    type="image/webp">
  <source 
    media="(min-width: 769px)" 
    srcset="{{ 'desktop-hero.webp' | asset_url }}"
    type="image/webp">
  <img 
    src="{{ 'desktop-hero.webp' | asset_url }}"
    alt="{{ section.settings.hero_alt_text }}"
    loading="lazy"
    width="1920"
    height="1080"
    fetchpriority="high">
</picture>
```

#### Paso 4: Preload Critical Image

**Archivo:** `theme.liquid` (en `<head>`)

```liquid
<link 
  rel="preload" 
  as="image" 
  href="{{ 'mobile-hero.webp' | asset_url }}"
  media="(max-width: 375px)">
<link 
  rel="preload" 
  as="image" 
  href="{{ 'desktop-hero.webp' | asset_url }}"
  media="(min-width: 769px)">
```

**Resultado Esperado:**
- LCP móvil: 15.3s → 2-3s (mejora de 80-85%)
- Tamaño de archivo: ~1MB → ~150-200KB (reducción de 80%)

---

### Issue #2: Múltiples Scripts de Tracking Bloqueando

**Problema:**
- Google Tag Manager, Facebook Pixel, Trekkie cargando síncronamente
- Bloquean renderizado y aumentan TTI

**Solución:**

#### Paso 1: Implementar Cookie Consent Banner

**Archivo:** `snippets/cookie-consent.liquid`

```liquid
<div id="cookie-consent-banner" class="cookie-banner" style="display: none;">
  <div class="cookie-banner-content">
    <p>Utilizamos cookies para mejorar su experiencia. ¿Acepta el uso de cookies?</p>
    <div class="cookie-banner-actions">
      <button id="accept-cookies" class="btn-primary">Aceptar</button>
      <button id="reject-cookies" class="btn-secondary">Rechazar</button>
      <a href="/policies/privacy-policy">Más información</a>
    </div>
  </div>
</div>

<script>
(function() {
  const banner = document.getElementById('cookie-consent-banner');
  const acceptBtn = document.getElementById('accept-cookies');
  const rejectBtn = document.getElementById('reject-cookies');
  
  // Verificar si ya hay consentimiento
  const consent = localStorage.getItem('cookie-consent');
  if (!consent) {
    banner.style.display = 'block';
  } else if (consent === 'accepted') {
    loadTrackingScripts();
  }
  
  acceptBtn.addEventListener('click', function() {
    localStorage.setItem('cookie-consent', 'accepted');
    banner.style.display = 'none';
    loadTrackingScripts();
  });
  
  rejectBtn.addEventListener('click', function() {
    localStorage.setItem('cookie-consent', 'rejected');
    banner.style.display = 'none';
  });
  
  function loadTrackingScripts() {
    // Cargar GTM de forma asíncrona
    (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-XXXXXXX');
    
    // Cargar Facebook Pixel de forma asíncrona
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', 'YOUR_PIXEL_ID');
    fbq('track', 'PageView');
  }
})();
</script>

<style>
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #fff;
  padding: 1rem;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
  z-index: 10000;
}
.cookie-banner-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.cookie-banner-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}
</style>
```

#### Paso 2: Modificar theme.liquid para Carga Condicional

**Archivo:** `theme.liquid` (remover scripts del `<head>`, mover a snippet)

```liquid
{% comment %} Remover estos scripts del head {% endcomment %}
{% comment %}
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
{% endcomment %}

{% comment %} Agregar snippet de cookie consent antes de </body> {% endcomment %}
{% render 'cookie-consent' %}
```

**Resultado Esperado:**
- TTI móvil: 19.9s → 8-10s (mejora de 50%)
- Cumplimiento legal: ✅
- Scripts solo cargan con consentimiento

---

### Issue #3: Scripts Bloqueando Renderizado

**Problema:**
- vendor.min.js, app.min.js, foxkit-app.min.js cargando síncronamente en `<head>`

**Solución:**

#### Paso 1: Identificar Scripts en theme.liquid

Buscar en `theme.liquid`:

```liquid
<script src="{{ 'vendor.min.js' | asset_url }}"></script>
<script src="{{ 'app.min.js' | asset_url }}"></script>
<script src="{{ 'foxkit-app.min.js' | asset_url }}"></script>
```

#### Paso 2: Mover Scripts No Críticos al Final del Body

**Archivo:** `theme.liquid`

```liquid
{% comment %} En <head>, solo scripts críticos {% endcomment %}
<head>
  {% comment %} Scripts críticos para renderizado inicial {% endcomment %}
  <script src="{{ 'critical.js' | asset_url }}" defer></script>
  
  {% comment %} Remover vendor.min.js, app.min.js, foxkit-app.min.js del head {% endcomment %}
</head>

<body>
  {% comment %} Contenido de la página {% endcomment %}
  {{ content_for_layout }}
  
  {% comment %} Scripts no críticos al final del body {% endcomment %}
  <script src="{{ 'vendor.min.js' | asset_url }}" defer></script>
  <script src="{{ 'app.min.js' | asset_url }}" defer></script>
  <script src="{{ 'foxkit-app.min.js' | asset_url }}" defer></script>
</body>
```

#### Paso 3: Usar Defer o Async

```liquid
{% comment %} Para scripts que no dependen del DOM {% endcomment %}
<script src="{{ 'analytics.js' | asset_url }}" async></script>

{% comment %} Para scripts que dependen del DOM {% endcomment %}
<script src="{{ 'app.js' | asset_url }}" defer></script>
```

**Resultado Esperado:**
- FCP: 8.8s → 2-3s (mejora de 65-70%)
- TTI: 19.9s → 10-12s (mejora de 40-50%)

---

### Issue #4: Fuentes Sin Preload

**Problema:**
- Fuentes Jost y Roboto Condensed bloquean renderizado

**Solución:**

#### Paso 1: Preload Fuentes Críticas

**Archivo:** `theme.liquid` (en `<head>`, antes de cargar fuentes)

```liquid
{% comment %} Preload fuentes críticas {% endcomment %}
<link 
  rel="preload" 
  href="https://fonts.shopifycdn.com/jost/jost_n4.woff2" 
  as="font" 
  type="font/woff2" 
  crossorigin="anonymous">
  
<link 
  rel="preload" 
  href="https://fonts.gstatic.com/s/robotocondensed/v25/ieVl2ZhZI2eCN5jzbjEETS9weq8-19K7DQk6YvM.woff2" 
  as="font" 
  type="font/woff2" 
  crossorigin="anonymous">

{% comment %} Luego cargar el CSS de fuentes {% endcomment %}
<link 
  href="https://fonts.shopifycdn.com/jost/jost.css" 
  rel="stylesheet" 
  media="print" 
  onload="this.media='all'">
<noscript>
  <link href="https://fonts.shopifycdn.com/jost/jost.css" rel="stylesheet">
</noscript>
```

#### Paso 2: Usar font-display: swap

**Archivo:** CSS personalizado o en `theme.liquid`

```css
@font-face {
  font-family: 'Jost';
  src: url('jost.woff2') format('woff2');
  font-display: swap; /* Muestra texto inmediatamente, luego carga fuente */
}
```

**Resultado Esperado:**
- FCP mejorado: texto visible inmediatamente
- CLS reducido: no hay shift cuando cargan las fuentes

---

### Issue #5: Headers de Seguridad Faltantes

**Problema:**
- Falta HSTS, CSP, X-Frame-Options, X-Content-Type-Options

**Solución:**

#### Opción 1: Usar Shopify App (Recomendado)

Instalar app como "Security Headers" o similar desde Shopify App Store.

#### Opción 2: Configurar en theme.liquid (Limitado)

Shopify no permite modificar headers HTTP directamente desde el tema, pero puedes:

**Archivo:** `theme.liquid` (meta tags en `<head>`)

```liquid
{% comment %} Meta tags de seguridad (limitado en Shopify) {% endcomment %}
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
<meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
```

#### Opción 3: Usar Cloudflare (Recomendado para Headers HTTP)

Si el dominio usa Cloudflare:

1. Ir a Cloudflare Dashboard
2. Security → Page Rules o Transform Rules
3. Agregar headers:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://connect.facebook.net; style-src 'self' 'unsafe-inline' https://fonts.shopifycdn.com; img-src 'self' data: https:; font-src 'self' https://fonts.shopifycdn.com https://fonts.gstatic.com;
```

**Resultado Esperado:**
- Protección contra XSS, clickjacking, MIME sniffing
- Mejor score en security audits

---

### Issue #6: Schema Markup para Productos

**Problema:**
- Falta Product schema markup completo

**Solución:**

#### Paso 1: Agregar Product Schema en product.liquid

**Archivo:** `sections/main-product.liquid` o `templates/product.liquid`

```liquid
{% comment %} Product Schema Markup {% endcomment %}
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": {{ product.title | json }},
  "image": [
    {% for image in product.images %}
    {{ image | image_url: width: 1200 | json }}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ],
  "description": {{ product.description | strip_html | truncate: 160 | json }},
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "brand": {
    "@type": "Brand",
    "name": "Farmacias Macross"
  },
  "offers": {
    "@type": "Offer",
    "url": {{ shop.url | append: product.url | json }},
    "priceCurrency": "MXN",
    "price": {{ product.selected_or_first_available_variant.price | money_without_currency | json }},
    "priceValidUntil": "2025-12-31",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/{% if product.available %}InStock{% else %}OutOfStock{% endif %}",
    "seller": {
      "@type": "Organization",
      "name": "Farmacias Macross"
    }
  },
  {% if product.metafields.reviews.rating.value %}
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": {{ product.metafields.reviews.rating.value | json }},
    "reviewCount": {{ product.metafields.reviews.count.value | json }}
  },
  {% endif %}
  "category": {{ product.type | json }}
}
</script>
```

#### Paso 2: Agregar LocalBusiness Schema

**Archivo:** `sections/footer.liquid` o `theme.liquid`

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Farmacias Macross",
  "image": "{{ 'logo.png' | asset_url }}",
  "@id": "{{ shop.url }}",
  "url": "{{ shop.url }}",
  "telephone": "+52-55-5440-9049",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Plaza Patio Pedregal, Periferico Sur 5270",
    "addressLocality": "Santa Ursula, Pedregal de Carrasco",
    "addressRegion": "Coyoacán",
    "postalCode": "04700",
    "addressCountry": "MX"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 19.3144,
    "longitude": -99.1964
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ],
    "opens": "09:00",
    "closes": "18:00"
  },
  "sameAs": [
    "https://www.facebook.com/farmaciasmacross",
    "https://www.instagram.com/farmaciasmacross"
  ]
}
</script>
```

**Resultado Esperado:**
- Rich snippets en Google Search
- Mejor visibilidad en Google Shopping
- Mejor SEO local

---

### Issue #7: Alt Text Faltante en Imágenes

**Problema:**
- Algunas imágenes sin alt text descriptivo

**Solución:**

#### Paso 1: Auditar Imágenes

Usar herramienta o script para encontrar imágenes sin alt:

```javascript
// Ejecutar en consola del navegador
document.querySelectorAll('img:not([alt]), img[alt=""]').forEach(img => {
  console.log('Imagen sin alt:', img.src);
});
```

#### Paso 2: Agregar Alt Text en Shopify Admin

1. Ir a **Products** → Seleccionar producto
2. En cada imagen, agregar **Alt text** descriptivo
3. Ejemplo: "Eligard 22.5 mg Leuprorelina - Tratamiento oncológico"

#### Paso 3: Template Code para Alt Text Automático

**Archivo:** `snippets/product-card.liquid`

```liquid
<img 
  src="{{ product.featured_image | image_url: width: 500 }}"
  alt="{{ product.featured_image.alt | default: product.title }}"
  loading="lazy"
  width="500"
  height="500">
```

**Resultado Esperado:**
- Mejor accesibilidad (WCAG compliance)
- Mejor SEO (imágenes indexables)
- Mejor experiencia para usuarios con lectores de pantalla

---

## 🚀 Optimización de Performance - Guía Completa

### Estrategia de Optimización

1. **Critical Rendering Path Optimization**
2. **Resource Hints** (preload, prefetch, preconnect)
3. **Lazy Loading** de imágenes y contenido
4. **Code Splitting** y defer/async
5. **Caching Strategy**

### Implementación de Resource Hints

**Archivo:** `theme.liquid` (en `<head>`)

```liquid
{% comment %} Preconnect a dominios externos críticos {% endcomment %}
<link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>
<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<link rel="dns-prefetch" href="https://connect.facebook.net">

{% comment %} Preload recursos críticos {% endcomment %}
<link rel="preload" href="{{ 'critical.css' | asset_url }}" as="style">
<link rel="preload" href="{{ 'critical.js' | asset_url }}" as="script">
```

### Lazy Loading de Imágenes

**Archivo:** `snippets/product-card.liquid`

```liquid
<img 
  src="{{ product.featured_image | image_url: width: 300 }}"
  srcset="{{ product.featured_image | image_url: width: 300 }} 300w,
          {{ product.featured_image | image_url: width: 600 }} 600w,
          {{ product.featured_image | image_url: width: 900 }} 900w"
  sizes="(max-width: 375px) 300px, (max-width: 768px) 600px, 900px"
  alt="{{ product.title }}"
  loading="lazy"
  decoding="async"
  width="300"
  height="300">
```

### Code Splitting con Shopify Sections

**Archivo:** `theme.liquid`

```liquid
{% comment %} Cargar secciones de forma diferida {% endcomment %}
{% for section in sections %}
  {% if section.settings.load_async %}
    <script>
      // Cargar sección de forma asíncrona
      fetch('{{ section.url }}')
        .then(response => response.text())
        .then(html => {
          document.getElementById('section-{{ section.id }}').innerHTML = html;
        });
    </script>
  {% endif %}
{% endfor %}
```

---

## 🔒 Implementación de Seguridad

### Content Security Policy (CSP)

**Nota:** Shopify limita la implementación de CSP desde el tema. Usar Cloudflare o app de Shopify.

**Configuración CSP Recomendada:**

```
default-src 'self';
script-src 'self' 'unsafe-inline' 'unsafe-eval' 
  https://www.googletagmanager.com 
  https://connect.facebook.net 
  https://cdn.shopify.com;
style-src 'self' 'unsafe-inline' 
  https://fonts.shopifycdn.com 
  https://fonts.googleapis.com;
img-src 'self' data: https:;
font-src 'self' 
  https://fonts.shopifycdn.com 
  https://fonts.gstatic.com;
connect-src 'self' 
  https://www.google-analytics.com 
  https://www.googletagmanager.com;
```

### HTTPS y HSTS

**Configuración en Cloudflare:**

1. SSL/TLS → Full (strict)
2. Always Use HTTPS: ON
3. HSTS: Enable
4. Max Age: 31536000 (1 año)
5. Include Subdomains: ON
6. Preload: ON (opcional, requiere registro)

---

## 📊 Testing y Verificación

### Herramientas de Testing

1. **Google PageSpeed Insights**
   ```bash
   # API call
   curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://farmaciasmacross.com.mx&strategy=mobile&key=YOUR_API_KEY"
   ```

2. **Lighthouse CLI**
   ```bash
   npm install -g lighthouse
   lighthouse https://farmaciasmacross.com.mx --view --only-categories=performance
   ```

3. **WebPageTest**
   - https://www.webpagetest.org/
   - Test desde múltiples ubicaciones

### Checklist de Verificación

**Performance:**
- [ ] LCP móvil < 2.5s
- [ ] FCP móvil < 1.8s
- [ ] TTI móvil < 3.8s
- [ ] CLS < 0.1
- [ ] Performance Score > 70

**Security:**
- [ ] HSTS header presente
- [ ] CSP configurado
- [ ] X-Frame-Options: SAMEORIGIN
- [ ] X-Content-Type-Options: nosniff

**SEO:**
- [ ] Schema markup validado (https://search.google.com/test/rich-results)
- [ ] Meta descriptions en todas las páginas
- [ ] Alt text en todas las imágenes
- [ ] Sitemap.xml generado y enviado

**Compliance:**
- [ ] Cookie banner implementado
- [ ] Políticas de privacidad actualizadas
- [ ] Consentimiento de cookies funcional

---

## 🐛 Troubleshooting

### Problema: Imágenes no cargan después de optimización

**Solución:**
```liquid
{% comment %} Verificar que las URLs de assets sean correctas {% endcomment %}
{{ 'image.webp' | asset_url }}

{% comment %} Verificar que el archivo existe en /assets/ {% endcomment %}
```

### Problema: Scripts no cargan con defer/async

**Solución:**
- Verificar dependencias entre scripts
- Scripts que dependen de otros deben usar `defer` (no `async`)
- Scripts independientes pueden usar `async`

### Problema: Schema markup no aparece en Google

**Solución:**
1. Validar en https://search.google.com/test/rich-results
2. Verificar que el JSON-LD esté bien formado
3. Esperar 1-2 semanas para indexación
4. Enviar sitemap a Google Search Console

---

## 📝 Notas de Implementación

### Orden Recomendado de Implementación

1. **Fase 1 (Crítico - 1 semana):**
   - Optimizar imágenes hero
   - Implementar cookie banner
   - Mover scripts no críticos al final

2. **Fase 2 (Alto Impacto - 2 semanas):**
   - Agregar headers de seguridad
   - Implementar schema markup
   - Optimizar fuentes con preload

3. **Fase 3 (Optimización - 1 semana):**
   - Lazy loading de imágenes
   - Resource hints
   - Code splitting

### Consideraciones de Shopify

- **Limitaciones:** No se pueden modificar headers HTTP directamente desde el tema
- **Soluciones:** Usar apps de Shopify o Cloudflare
- **Assets:** Todos los assets deben estar en `/assets/` o usar CDN
- **Liquid:** Usar filtros de Liquid para optimización de imágenes

### Recursos Adicionales

- [Shopify Performance Best Practices](https://shopify.dev/themes/performance)
- [Core Web Vitals](https://web.dev/vitals/)
- [Schema.org Documentation](https://schema.org/)
- [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

*Última actualización: Diciembre 2024*

