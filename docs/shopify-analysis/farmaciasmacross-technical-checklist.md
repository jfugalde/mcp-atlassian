# Checklist Técnico - farmaciasmacross.com.mx
## Items Accionables para Equipo Técnico

**Fecha:** Diciembre 2024  
**Prioridad:** 🔴 Crítica | 🟡 Alta | 🟢 Media

---

## Performance

| #   | Item                                                                         | Prioridad | Esfuerzo | Estado |
| --- | ---------------------------------------------------------------------------- | --------- | -------- | ------ |
| 1   | Optimizar imágenes hero homepage (WebP, max 1920px ancho, srcset responsive) | 🔴         | 4-6h     | ⬜      |
| 2   | Implementar lazy loading en imágenes below-the-fold                          | 🔴         | 2-4h     | ⬜      |
| 3   | Convertir scripts bloqueantes a async/defer (32 scripts identificados)       | 🔴         | 4-6h     | ⬜      |
| 4   | Mover scripts no críticos al final de `<body>`                               | 🔴         | 2-3h     | ⬜      |
| 5   | Precargar fuentes críticas con `<link rel="preload">`                        | 🟡         | 1-2h     | ⬜      |
| 6   | Optimizar imágenes de productos (WebP, lazy load)                            | 🟡         | 6-10h    | ⬜      |
| 7   | Implementar caché de navegador (Cache-Control headers)                       | 🟡         | 2-4h     | ⬜      |
| 8   | Minificar CSS/JS no minificados                                              | 🟢         | 2-4h     | ⬜      |

**Objetivo:** LCP móvil < 3s, Performance score > 75

---

## Compliance Legal

| #   | Item                                                                  | Prioridad | Esfuerzo | Estado |
| --- | --------------------------------------------------------------------- | --------- | -------- | ------ |
| 9   | Implementar banner de consentimiento de cookies                       | 🔴         | 2-3h     | ⬜      |
| 10  | Integrar scripts de tracking con consentimiento (GTM, Facebook Pixel) | 🔴         | 1-2h     | ⬜      |
| 11  | Actualizar política de privacidad para reflejar uso real de cookies   | 🔴         | 1h       | ⬜      |
| 12  | Agregar disclaimers sobre necesidad de receta en páginas de producto  | 🟡         | 2-3h     | ⬜      |
| 13  | Revisar y actualizar términos de servicio y políticas de envío        | 🟢         | 2-4h     | ⬜      |

**Objetivo:** Cumplimiento legal completo, sin riesgo de multas

---

## UX/UI - Navegación

| #   | Item                                               | Prioridad | Esfuerzo | Estado |
| --- | -------------------------------------------------- | --------- | -------- | ------ |
| 14  | Implementar breadcrumbs en categorías y productos  | 🟡         | 2-3h     | ⬜      |
| 15  | Agregar schema.org BreadcrumbList JSON-LD          | 🟡         | 1h       | ⬜      |
| 16  | Agregar filtros avanzados en páginas de categorías | 🟢         | 4-6h     | ⬜      |
| 17  | Implementar autocompletado en búsqueda             | 🟢         | 2-4h     | ⬜      |
| 18  | Mejorar resultados de búsqueda con sugerencias     | 🟢         | 2-4h     | ⬜      |

**Objetivo:** Navegación más intuitiva, mejor SEO

---

## UX/UI - Journey de Compra

| #   | Item                                                                          | Prioridad | Esfuerzo | Estado |
| --- | ----------------------------------------------------------------------------- | --------- | -------- | ------ |
| 19  | Agregar banner/mensaje sobre necesidad de receta médica (homepage, productos) | 🟡         | 1-2h     | ⬜      |
| 20  | Mostrar indicador de disponibilidad claro en productos                        | 🟡         | 2-3h     | ⬜      |
| 21  | Agregar estimación de envío visible en carrito                                | 🟡         | 2-3h     | ⬜      |
| 22  | Implementar indicador de progreso en checkout ("Paso 1 de 3")                 | 🟡         | 1-2h     | ⬜      |
| 23  | Mostrar tiempos de entrega claros por región en checkout                      | 🟡         | 2-3h     | ⬜      |
| 24  | Implementar validación de formulario en tiempo real                           | 🟡         | 4-6h     | ⬜      |
| 25  | Agregar mensajes de error claros y visibles                                   | 🟡         | 2-3h     | ⬜      |

**Objetivo:** Reducir fricciones, mejorar tasa de conversión

---

## Trust & Security

| #   | Item                                                                     | Prioridad | Esfuerzo | Estado |
| --- | ------------------------------------------------------------------------ | --------- | -------- | ------ |
| 26  | Agregar sellos de seguridad SSL/PCI en checkout                          | 🟡         | 1-2h     | ⬜      |
| 27  | Mostrar certificaciones COFEPRIS en homepage y productos                 | 🟡         | 2-3h     | ⬜      |
| 28  | Hacer información de contacto más prominente (teléfono, WhatsApp, email) | 🟡         | 1-2h     | ⬜      |
| 29  | Agregar sección de garantías y políticas en checkout                     | 🟡         | 2-3h     | ⬜      |
| 30  | Implementar headers de seguridad (CSP, HSTS, X-Frame-Options)            | 🟢         | 4-8h     | ⬜      |
| 31  | Agregar `rel="noopener noreferrer"` a enlaces externos                   | 🟢         | 1-2h     | ⬜      |

**Objetivo:** Mayor confianza, reducción de abandono en checkout

---

## SEO Técnico

| #   | Item                                                                        | Prioridad | Esfuerzo | Estado |
| --- | --------------------------------------------------------------------------- | --------- | -------- | ------ |
| 32  | Agregar meta descripciones únicas a todas las páginas                       | 🟡         | 4-6h     | ⬜      |
| 33  | Implementar Product schema completo en páginas de producto                  | 🟡         | 6-10h    | ⬜      |
| 34  | Agregar LocalBusiness schema para ubicaciones (CDMX, Puebla)                | 🟡         | 2-4h     | ⬜      |
| 35  | Optimizar alt text en todas las imágenes                                    | 🟡         | 8-12h    | ⬜      |
| 36  | Revisar y optimizar estructura de headings (H1-H6)                          | 🟢         | 4-6h     | ⬜      |
| 37  | Implementar estrategia de internal linking (3+ enlaces internos por página) | 🟢         | 6-10h    | ⬜      |
| 38  | Optimizar URLs para SEO (cortas, descriptivas, keywords)                    | 🟢         | 4-8h     | ⬜      |
| 39  | Verificar y corregir sitemap.xml                                            | 🟢         | 1-2h     | ⬜      |
| 40  | Revisar y optimizar robots.txt                                              | 🟢         | 1h       | ⬜      |

**Objetivo:** Mejor visibilidad en buscadores, más tráfico orgánico

---

## Testing y Validación

| #   | Item                                               | Prioridad | Esfuerzo | Estado |
| --- | -------------------------------------------------- | --------- | -------- | ------ |
| 41  | Ejecutar PageSpeed Insights después de cada mejora | 🔴         | 0.5h     | ⬜      |
| 42  | Validar Core Web Vitals (LCP, FCP, TTI, CLS)       | 🔴         | 0.5h     | ⬜      |
| 43  | Testing de funcionalidad en móvil (iOS, Android)   | 🟡         | 2-4h     | ⬜      |
| 44  | Validar schema markup con Google Rich Results Test | 🟡         | 1h       | ⬜      |
| 45  | Testing de accesibilidad (WCAG 2.1)                | 🟢         | 4-6h     | ⬜      |
| 46  | Validar formularios en diferentes navegadores      | 🟢         | 2-3h     | ⬜      |

**Objetivo:** Asegurar calidad y funcionalidad

---

## Notas

- **Prioridad 🔴:** Implementar inmediatamente (Fase 1)
- **Prioridad 🟡:** Implementar en Fase 2 (alto impacto)
- **Prioridad 🟢:** Implementar en Fase 3 (optimización)

- Marcar con ✅ cuando se complete cada item
- Documentar cualquier problema o bloqueador encontrado
- Validar cada mejora antes de marcar como completa

---

**Total Items:** 46  
**Esfuerzo Total Estimado:** 100-180 horas  
**Inversión Estimada:** $11,200 - $19,200 USD



