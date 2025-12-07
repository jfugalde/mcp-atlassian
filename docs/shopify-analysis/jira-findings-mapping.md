# Mapeo de Hallazgos de Auditoría vs Tickets Jira FM

**Fecha de Análisis:** Diciembre 2024  
**Sitio Auditado:** farmaciasmacross.com.mx (Shopify)  
**Proyecto Jira:** FM (Farmacias Macross)

---

## 📊 Resumen Ejecutivo

**Total de Hallazgos de Auditoría:** 25  
**Hallazgos con Tickets Existentes:** 8 (32%)  
**Hallazgos Sin Tickets (Oportunidades Nuevas):** 17 (68%)

**Análisis Clave:**
- Los tickets existentes en Jira están enfocados en **medicamentosespeciales.mx (WordPress)**
- La auditoría realizada es para **farmaciasmacross.com.mx (Shopify)**
- **17 hallazgos críticos** no tienen tickets correspondientes y representan trabajo billable nuevo
- Muchos hallazgos de performance y seguridad son específicos de Shopify y no están cubiertos

---

## 🔍 Mapeo Detallado: Hallazgos vs Tickets Jira

### ✅ Hallazgos CON Tickets Existentes (8)

| #   | Hallazgo de Auditoría                   | Ticket Jira                                               | Estado | ¿Puede Agregar Cargos?                                                    |
| --- | --------------------------------------- | --------------------------------------------------------- | ------ | ------------------------------------------------------------------------- |
| 1   | **SEO on-page completo**                | FM-1-4-1: SEO on-page completo                            | High   | ⚠️ Parcial - Ticket es para WordPress, necesita adaptación Shopify         |
| 2   | **Schema markup especializado**         | FM-1-4-2: Schema markup especializado                     | High   | ⚠️ Parcial - Ticket menciona LocalBusiness pero no Product schema completo |
| 3   | **Documentos legales health-compliant** | FM-1-4-5: Documentos legales health-compliant             | High   | ⚠️ Parcial - Ticket existe pero puede expandirse con hallazgos específicos |
| 4   | **Sitemap XML**                         | FM-1-4-3: Sitemap XML multinivel                          | Medium | ✅ Sí - Mismo trabajo, puede agregar horas                                 |
| 5   | **Robots.txt optimizado**               | FM-1-4-4: Robots.txt optimizado                           | Low    | ✅ Sí - Mismo trabajo, puede agregar horas                                 |
| 6   | **Optimización de velocidad**           | FM-1-2-11: Optimización de velocidad                      | High   | ⚠️ Parcial - Ticket es para WordPress, Shopify requiere enfoque diferente  |
| 7   | **Alt text para imágenes**              | FM-1-3-4: SEO optimizado por producto (menciona alt text) | High   | ⚠️ Parcial - Solo mencionado, puede expandirse                             |
| 8   | **Schema markup de producto**           | FM-1-3-3: Schema markup de producto                       | High   | ⚠️ Parcial - Ticket existe pero puede expandirse con hallazgos específicos |

**Nota:** Aunque estos tickets existen, están diseñados para WordPress. La implementación en Shopify requiere trabajo adicional que puede ser billable.

---

### ❌ Hallazgos SIN Tickets (17) - Oportunidades Nuevas

#### 🔴 Prioridad Alta - Críticos para Shopify (10 hallazgos)

| #   | Hallazgo                                              | Prioridad | Esfuerzo | ¿Puede Agregar Cargos?   | Justificación                                                |
| --- | ----------------------------------------------------- | --------- | -------- | ------------------------ | ------------------------------------------------------------ |
| 1   | **Carga Simultánea de Múltiples Scripts de Tracking** | High      | 6-12h    | ✅ **SÍ - $1,200-$2,400** | Específico de Shopify, no cubierto en tickets WordPress      |
| 2   | **Core Web Vitals Deficientes (LCP 15.3s)**           | High      | 12-20h   | ✅ **SÍ - $2,400-$4,000** | Problema crítico de performance, no mencionado en tickets    |
| 3   | **Hero Images Demasiado Grandes (5000×2617px)**       | High      | 4-8h     | ✅ **SÍ - $800-$1,600**   | Optimización específica de imágenes hero, no en scope actual |
| 4   | **Bloqueo de Renderizado por JavaScript**             | Medium    | 4-8h     | ✅ **SÍ - $800-$1,600**   | Optimización de scripts Shopify, diferente a WordPress       |
| 5   | **Fuentes Personalizadas Bloquean Renderizado**       | Medium    | 2-4h     | ✅ **SÍ - $400-$800**     | Preload de fuentes, no cubierto                              |
| 6   | **Cookie Consent Banner Missing**                     | High      | 4-6h     | ✅ **SÍ - $800-$1,200**   | Compliance legal crítico, no en tickets                      |
| 7   | **Content Security Policy (CSP) Missing**             | High      | 4-8h     | ✅ **SÍ - $800-$1,600**   | Seguridad crítica, no mencionado                             |
| 8   | **SSL Certificate and HTTPS Configuration**           | High      | 2-4h     | ✅ **SÍ - $400-$800**     | Revisión de configuración SSL, no en scope                   |
| 9   | **Mobile Responsiveness Testing**                     | High      | 8-16h    | ✅ **SÍ - $1,600-$3,200** | Testing específico, puede ser trabajo adicional              |
| 10  | **Page Load Speed Optimization**                      | High      | 12-20h   | ✅ **SÍ - $2,400-$4,000** | Optimización avanzada, expande FM-1-2-11                     |

#### 🟡 Prioridad Media - Optimizaciones (6 hallazgos)

| #   | Hallazgo                                         | Prioridad | Esfuerzo | ¿Puede Agregar Cargos?   | Justificación                                                               |
| --- | ------------------------------------------------ | --------- | -------- | ------------------------ | --------------------------------------------------------------------------- |
| 11  | **Puntuaciones de Rendimiento Bajas**            | Medium    | 8-16h    | ✅ **SÍ - $1,600-$3,200** | Trabajo adicional de optimización                                           |
| 12  | **Image Optimization Needed**                    | Medium    | 8-12h    | ✅ **SÍ - $1,600-$2,400** | Optimización WebP, lazy loading - expande optimización                      |
| 13  | **Caching Strategy Review**                      | Medium    | 4-8h     | ✅ **SÍ - $800-$1,600**   | Configuración de caché Shopify, no cubierto                                 |
| 14  | **Breadcrumb Navigation Missing**                | Medium    | 4-6h     | ✅ **SÍ - $800-$1,200**   | Implementación de breadcrumbs, no en tickets                                |
| 15  | **Internal Linking Strategy**                    | Medium    | 6-10h    | ✅ **SÍ - $1,200-$2,000** | Estrategia de enlaces internos, trabajo adicional                           |
| 16  | **URL Structure Optimization**                   | Medium    | 4-8h     | ✅ **SÍ - $800-$1,600**   | Optimización de URLs Shopify, no cubierto                                   |
| 17  | **Analytics and Tracking Implementation Review** | Medium    | 4-6h     | ⚠️ **PARCIAL**            | FM-4-1-11 (GA4) existe, pero revisión de implementación actual es adicional |
| 18  | **Form Validation and Error Handling**           | Medium    | 6-10h    | ✅ **SÍ - $1,200-$2,000** | Mejoras de formularios, no específicamente cubierto                         |
| 19  | **Search Functionality Optimization**            | Medium    | 8-12h    | ✅ **SÍ - $1,600-$2,400** | Optimización de búsqueda, trabajo adicional                                 |
| 20  | **Product Schema Markup for E-commerce**         | High      | 12-16h   | ⚠️ **PARCIAL**            | FM-1-3-3 existe pero puede expandirse con hallazgos específicos             |
| 21  | **Local Business Schema for Multiple Locations** | Medium    | 4-6h     | ⚠️ **PARCIAL**            | FM-1-4-2 menciona LocalBusiness pero puede expandirse                       |

#### 🟢 Prioridad Baja - Mejoras Menores (1 hallazgo)

| #   | Hallazgo                           | Prioridad | Esfuerzo | ¿Puede Agregar Cargos? | Justificación                   |
| --- | ---------------------------------- | --------- | -------- | ---------------------- | ------------------------------- |
| 22  | **404 Error Pages Not Customized** | Low       | 2-4h     | ✅ **SÍ - $400-$800**   | Mejora de UX, trabajo adicional |

---

## 💰 Análisis de Oportunidades Billables

### Trabajo Nuevo Identificado

**Total de Horas Estimadas (Hallazgos Sin Tickets):** 120-200 horas  
**Rango de Inversión Estimada:** $24,000 - $40,000 USD

**Desglose por Categoría:**

#### Performance & Optimización (Crítico)
- **Horas:** 50-80 horas
- **Inversión:** $10,000 - $16,000 USD
- **Hallazgos:** LCP crítico, hero images, scripts bloqueando, fuentes, optimización avanzada

#### Seguridad & Compliance (Crítico)
- **Horas:** 10-18 horas
- **Inversión:** $2,000 - $3,600 USD
- **Hallazgos:** Cookie banner, CSP, SSL review

#### SEO & Estructura (Alto Valor)
- **Horas:** 30-50 horas
- **Inversión:** $6,000 - $10,000 USD
- **Hallazgos:** Breadcrumbs, internal linking, URL optimization, search optimization

#### UX & Accesibilidad (Medio)
- **Horas:** 20-32 horas
- **Inversión:** $4,000 - $6,400 USD
- **Hallazgos:** Mobile testing, form validation, 404 pages

#### Analytics & Tracking (Medio)
- **Horas:** 10-16 horas
- **Inversión:** $2,000 - $3,200 USD
- **Hallazgos:** Analytics review, tracking optimization

---

## 🎯 Recomendaciones para Agregar Cargos

### Estrategia 1: Crear Tickets Nuevos para Shopify

**Recomendación:** Crear nuevos tickets en el proyecto FM específicos para farmaciasmacross.com.mx (Shopify)

**Tickets Sugeridos:**

1. **FM-SHOP-1: Optimización Crítica de Performance Shopify**
   - Scope: LCP, hero images, scripts, fuentes
   - Horas: 30-50h
   - Inversión: $6,000 - $10,000 USD
   - Prioridad: Highest

2. **FM-SHOP-2: Compliance Legal y Seguridad Shopify**
   - Scope: Cookie banner, CSP, SSL, headers de seguridad
   - Horas: 10-18h
   - Inversión: $2,000 - $3,600 USD
   - Prioridad: Highest

3. **FM-SHOP-3: Optimización SEO Avanzada Shopify**
   - Scope: Breadcrumbs, internal linking, URL optimization, search
   - Horas: 30-50h
   - Inversión: $6,000 - $10,000 USD
   - Prioridad: High

4. **FM-SHOP-4: Testing y Optimización UX Shopify**
   - Scope: Mobile testing, form validation, 404 pages
   - Horas: 20-32h
   - Inversión: $4,000 - $6,400 USD
   - Prioridad: Medium

### Estrategia 2: Expandir Tickets Existentes

**Tickets que pueden expandirse con trabajo adicional:**

- **FM-1-2-11 (Optimización de velocidad):** Agregar 20-30h de trabajo específico Shopify
- **FM-1-4-2 (Schema markup):** Expandir con Product schema completo y LocalBusiness detallado
- **FM-1-4-5 (Documentos legales):** Agregar implementación de cookie banner
- **FM-1-3-3 (Schema producto):** Expandir con hallazgos específicos de auditoría

**Inversión Adicional Estimada:** $8,000 - $12,000 USD

---

## 📋 Matriz de Decisión: ¿Agregar Cargos?

| Criterio                                                | Hallazgo Sin Ticket          | Hallazgo Con Ticket Parcial       |
| ------------------------------------------------------- | ---------------------------- | --------------------------------- |
| **Es trabajo nuevo?**                                   | ✅ Sí - 100% nuevo            | ⚠️ Parcial - Expansión de scope    |
| **Es específico de Shopify?**                           | ✅ Sí - No aplica a WordPress | ⚠️ Depende - Algunos son genéricos |
| **Está fuera del scope original?**                      | ✅ Sí - No estaba planificado | ⚠️ Parcial - Puede estar implícito |
| **Puede justificarse como "descubierto en auditoría"?** | ✅ Sí - Hallazgo nuevo        | ✅ Sí - Detalle descubierto        |
| **Recomendación**                                       | ✅ **CREAR TICKET NUEVO**     | ✅ **EXPANDIR TICKET EXISTENTE**   |

---

## 💡 Justificación para Cliente

### Argumentos Clave:

1. **"Trabajo Descubierto en Auditoría"**
   - Los 25 hallazgos fueron identificados mediante auditoría técnica profunda
   - Muchos problemas no eran visibles sin análisis especializado
   - El trabajo original (tickets FM-1-*) estaba enfocado en WordPress, no Shopify

2. **"Problemas Críticos de Performance"**
   - LCP de 15.3s es un problema crítico que afecta conversiones
   - Estos problemas no estaban identificados antes de la auditoría
   - Requieren trabajo especializado de optimización

3. **"Compliance Legal Crítico"**
   - Falta de cookie banner es riesgo de multas
   - Headers de seguridad faltantes exponen a ataques
   - Estos son requisitos legales, no opcionales

4. **"Scope Diferente: WordPress vs Shopify"**
   - Tickets existentes son para medicamentosespeciales.mx (WordPress)
   - Auditoría es para farmaciasmacross.com.mx (Shopify)
   - Implementación requiere conocimiento específico de Shopify

---

## 📊 Resumen de Oportunidades Billables

### Trabajo Nuevo Total

| Categoría                             | Hallazgos | Horas        | Inversión USD         |
| ------------------------------------- | --------- | ------------ | --------------------- |
| **Crítico (Performance + Seguridad)** | 10        | 60-98h       | $12,000 - $19,600     |
| **Alto Valor (SEO + UX)**             | 9         | 50-82h       | $10,000 - $16,400     |
| **Mejoras Menores**                   | 1         | 2-4h         | $400 - $800           |
| **TOTAL**                             | **20**    | **112-184h** | **$22,400 - $36,800** |

### Trabajo de Expansión (Tickets Existentes)

| Ticket              | Expansión Propuesta           | Horas Adicionales | Inversión Adicional USD |
| ------------------- | ----------------------------- | ----------------- | ----------------------- |
| FM-1-2-11           | Optimización avanzada Shopify | 20-30h            | $4,000 - $6,000         |
| FM-1-4-2            | Schema markup completo        | 8-12h             | $1,600 - $2,400         |
| FM-1-4-5            | Cookie banner implementation  | 4-6h              | $800 - $1,200           |
| FM-1-3-3            | Product schema detallado      | 6-10h             | $1,200 - $2,000         |
| **TOTAL EXPANSIÓN** |                               | **38-58h**        | **$7,600 - $11,600**    |

### **TOTAL OPORTUNIDAD BILLABLE**

**Horas Totales:** 150-242 horas  
**Inversión Total:** $30,000 - $48,400 USD

---

## ✅ Conclusión y Recomendaciones

### Hallazgos Principales:

1. **68% de los hallazgos (17 de 25) NO tienen tickets correspondientes**
2. **Problemas críticos de performance** (LCP 15.3s) no están cubiertos
3. **Riesgos de compliance legal** (cookie banner, seguridad) no están en scope
4. **Tickets existentes están para WordPress**, no Shopify

### Recomendación Final:

**✅ SÍ, se puede agregar trabajo billable significativo:**

1. **Crear nuevos tickets** para hallazgos críticos de Shopify (FM-SHOP-1 a FM-SHOP-4)
2. **Expandir tickets existentes** con trabajo adicional descubierto en auditoría
3. **Justificar como "scope descubierto"** - problemas no identificados antes de la auditoría técnica

**Inversión Total Justificable:** $30,000 - $48,400 USD

---

*Este análisis demuestra que la auditoría técnica ha identificado trabajo significativo que no estaba en el scope original del proyecto FM, justificando la creación de nuevos tickets y expansión de trabajo billable.*

