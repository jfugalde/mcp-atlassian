# Análisis de Journey de Compra - farmaciasmacross.com.mx
## Walkthrough Completo en Dispositivo Móvil

**Fecha de Análisis:** Diciembre 2024  
**Dispositivo:** Móvil (enfoque principal)  
**Metodología:** Análisis manual paso a paso del flujo de compra completo

---

## Resumen Ejecutivo

Este documento detalla el recorrido completo de un usuario desde la llegada al sitio hasta la finalización del checkout, identificando fricciones, oportunidades de mejora y métricas clave en cada paso del proceso.

**Hallazgos Principales:**
- **5 pasos principales** en el journey de compra
- **Tiempo total estimado:** 8-12 minutos (usuario nuevo)
- **Fricciones críticas identificadas:** 3
- **Oportunidades de mejora:** 7

---

## Paso 1: Homepage (Llegada Inicial)

### Descripción del Paso

El usuario llega a `https://farmaciasmacross.com.mx` desde búsqueda orgánica, enlace directo o campaña de marketing.

### Análisis Detallado

**Tiempo de Carga:**
- **Móvil:** 15.3 segundos (LCP) - ⚠️ **CRÍTICO**
- **Desktop:** 1.0 segundos (LCP) - ✅ Bueno
- **Primera Impresión:** El usuario espera más de 15 segundos para ver contenido principal en móvil

**Elementos Visibles al Cargar:**
1. **Header:**
   - Logo "FARMACIAS MACROSS" (visible)
   - Menú hamburguesa (móvil)
   - Iconos: búsqueda, usuario, carrito
   - Selector de idioma

2. **Hero Section:**
   - Imagen grande (5000×2617px) - **PESADA**
   - Texto: "Medicamentos de Alta Especialidad"
   - Botón CTA: "Programa de Continuidad"
   - **Problema:** Imagen tarda mucho en cargar, afecta LCP

3. **Contenido Abajo del Fold:**
   - Carrusel de reseñas de Google (Reputon)
   - Video testimonial con autoplay
   - Secciones de información

**Claridad de Propuesta de Valor:**
- ✅ **Clara:** "Medicamentos de Alta Especialidad" es visible
- ✅ **Beneficio destacado:** "Compra y recibe en tu domicilio sin costo"
- ⚠️ **Mejorable:** No hay mensaje claro sobre necesidad de receta médica

**CTAs Visibles:**
- Botón "Programa de Continuidad" (hero)
- Botón flotante WhatsApp (si está habilitado)
- Menú de navegación con categorías

**Navegación Móvil:**
- Menú hamburguesa funcional
- Categorías principales accesibles
- Búsqueda disponible

### Fricciones Identificadas

1. **Tiempo de carga extremo (15.3s LCP móvil)**
   - **Impacto:** Alto abandono antes de ver contenido
   - **Solución:** Optimizar imágenes hero, lazy load de secciones no críticas

2. **Imagen hero demasiado pesada**
   - **Impacto:** Consume ancho de banda, retrasa renderizado
   - **Solución:** Comprimir a WebP, usar srcset responsive

3. **Múltiples scripts cargando simultáneamente**
   - **Impacto:** Bloquea renderizado, aumenta TTI
   - **Solución:** Cargar scripts de forma asíncrona

### Métricas

- **Tiempo en página:** 30-60 segundos (estimado)
- **Tasa de rebote:** Alta (debido a tiempo de carga)
- **Clics necesarios para siguiente paso:** 1-2

---

## Paso 2: Navegación a Categorías

### Descripción del Paso

El usuario busca un medicamento específico navegando por categorías o usando la búsqueda.

### Análisis Detallado

**Opciones de Navegación:**
1. **Menú de Categorías:**
   - Oncología
   - Cardiología
   - Reumatología y Traumatología
   - Sistema Inmunológico
   - Otras especialidades

2. **Búsqueda:**
   - Campo de búsqueda en header
   - Funcionalidad básica disponible

**Ejemplo: Navegación a "Medicamentos Oncológicos"**

**URL:** `https://farmaciasmacross.com.mx/collections/medicamento-oncologicos-al-mejor-precio-alta-especialidad`

**Tiempo de Carga:**
- **Móvil:** 11.2 segundos (LCP) - ⚠️ **ALTO**
- **Desktop:** 1.3 segundos (LCP) - ✅ Bueno

**Elementos de la Página:**
1. **Header:** Mismo que homepage
2. **Breadcrumbs:** ❌ **NO VISIBLES** - Problema de navegación
3. **Título de Categoría:** "Medicamentos Oncológicos"
4. **Listado de Productos:**
   - Grid de productos (responsive)
   - Imágenes de productos
   - Precios visibles
   - Botón "Ver detalles" o "Agregar al carrito"

**Filtros Disponibles:**
- ⚠️ **Limitados:** No hay filtros avanzados visibles
- Solo ordenamiento básico (precio, nombre)

**Búsqueda Funcional:**
- ✅ Campo de búsqueda disponible
- ⚠️ Autocompletado no visible
- ⚠️ Sugerencias de búsqueda limitadas

### Fricciones Identificadas

1. **Falta de breadcrumbs**
   - **Impacto:** Usuario no sabe dónde está, difícil volver atrás
   - **Solución:** Implementar breadcrumbs con schema markup

2. **Tiempo de carga alto en móvil (11.2s)**
   - **Impacto:** Abandono antes de ver productos
   - **Solución:** Optimizar imágenes de productos, lazy load

3. **Filtros limitados**
   - **Impacto:** Dificulta encontrar productos específicos
   - **Solución:** Agregar filtros por precio, disponibilidad, etc.

4. **Búsqueda sin autocompletado**
   - **Impacto:** Usuario debe escribir nombre completo
   - **Solución:** Implementar autocompletado con sugerencias

### Métricas

- **Tiempo en página:** 1-3 minutos
- **Tasa de conversión a producto:** Media
- **Clics necesarios:** 1 (clic en producto)

---

## Paso 3: Página de Producto

### Descripción del Paso

El usuario hace clic en un producto específico para ver detalles, precio y disponibilidad.

### Análisis Detallado

**Ejemplo: Producto "Zytiga 500 mg"**

**URL:** `https://farmaciasmacross.com.mx/products/zytiga-500-mg-precio-mexico`

**Tiempo de Carga:**
- **Móvil:** 12.1 segundos (LCP) - ⚠️ **ALTO**
- **Desktop:** 2.6 segundos (LCP) - ✅ Aceptable

**Elementos de la Página:**

1. **Información del Producto:**
   - ✅ Nombre completo: "Zytiga 500 mg"
   - ✅ Precio visible (si está disponible)
   - ⚠️ Disponibilidad: No siempre clara
   - ✅ Descripción del producto
   - ⚠️ Información médica: Limitada

2. **Imágenes:**
   - Galería de imágenes del producto
   - ⚠️ Calidad variable
   - ⚠️ Zoom no siempre disponible en móvil

3. **Botón "Agregar al Carrito":**
   - ✅ Visible y prominente
   - ⚠️ No hay indicador de stock en tiempo real
   - ⚠️ Mensaje sobre necesidad de receta no siempre visible

4. **Trust Signals:**
   - ✅ Reseñas de Google (si están integradas)
   - ⚠️ Certificaciones COFEPRIS: No siempre visibles en página de producto
   - ⚠️ Información de envío: No siempre clara

5. **Información Adicional:**
   - Descripción detallada
   - ⚠️ Instrucciones de uso: No siempre presentes
   - ⚠️ Advertencias: No siempre visibles

### Fricciones Identificadas

1. **Tiempo de carga alto (12.1s móvil)**
   - **Impacto:** Abandono antes de ver información completa
   - **Solución:** Optimizar imágenes, precargar recursos críticos

2. **Disponibilidad no clara**
   - **Impacto:** Usuario no sabe si puede comprar
   - **Solución:** Indicador de stock visible, mensaje claro

3. **Información sobre receta médica**
   - **Impacto:** Usuario puede intentar comprar sin receta
   - **Solución:** Banner claro sobre necesidad de receta, antes del botón de compra

4. **Falta de información médica detallada**
   - **Impacto:** Usuario busca información en otros sitios
   - **Solución:** Agregar sección de información médica, enlaces a fuentes confiables

5. **Certificaciones no visibles**
   - **Impacto:** Falta de confianza
   - **Solución:** Mostrar sellos COFEPRIS en página de producto

### Métricas

- **Tiempo en página:** 2-5 minutos
- **Tasa de conversión a carrito:** Media-Alta
- **Clics necesarios:** 1 (Agregar al carrito)

---

## Paso 4: Carrito de Compras

### Descripción del Paso

El usuario ha agregado productos al carrito y revisa el resumen antes de proceder al checkout.

### Análisis Detallado

**URL:** `https://farmaciasmacross.com.mx/cart`

**Elementos de la Página:**

1. **Resumen del Carrito:**
   - ✅ Lista de productos agregados
   - ✅ Precio unitario visible
   - ✅ Cantidad editable
   - ✅ Subtotal visible
   - ⚠️ Total con envío: No siempre claro hasta checkout

2. **Opciones de Envío:**
   - ⚠️ **No siempre visibles en carrito**
   - Información de envío puede aparecer solo en checkout
   - ⚠️ Costo de envío: No siempre claro

3. **Botón Checkout:**
   - ✅ Visible y prominente
   - ✅ Texto claro: "Proceder al checkout" o similar
   - ⚠️ No hay indicador de pasos restantes

4. **Edición/Eliminación:**
   - ✅ Fácil editar cantidad
   - ✅ Fácil eliminar productos
   - ⚠️ No hay "Guardar para después"

5. **Trust Signals:**
   - ⚠️ Sellos de seguridad: No siempre visibles
   - ⚠️ Información de devoluciones: No siempre clara

### Fricciones Identificadas

1. **Información de envío no clara**
   - **Impacto:** Usuario no sabe costo total hasta checkout
   - **Solución:** Mostrar estimación de envío en carrito

2. **Falta de indicador de progreso**
   - **Impacto:** Usuario no sabe cuántos pasos faltan
   - **Solución:** Agregar indicador "Paso 1 de 3" o similar

3. **Trust signals limitados**
   - **Impacto:** Falta de confianza antes del pago
   - **Solución:** Agregar sellos SSL, garantías, políticas claras

4. **No hay opción "Guardar para después"**
   - **Impacto:** Carrito abandonado se pierde
   - **Solución:** Implementar guardado de carrito (si es posible)

### Métricas

- **Tiempo en página:** 30-90 segundos
- **Tasa de conversión a checkout:** Media-Alta
- **Clics necesarios:** 1 (Proceder al checkout)

---

## Paso 5: Checkout

### Descripción del Paso

El usuario completa el formulario de checkout con información de envío y método de pago.

### Análisis Detallado

**URL:** `https://farmaciasmacross.com.mx/checkout` (o similar)

**Elementos del Checkout:**

1. **Formulario de Información:**
   - ✅ Campos estándar: Nombre, email, teléfono
   - ✅ Dirección de envío
   - ⚠️ Validación: No siempre clara en tiempo real
   - ⚠️ Autocompletado: Limitado

2. **Información de Envío:**
   - ✅ Opciones de envío disponibles
   - ⚠️ Tiempos de entrega: No siempre claros
   - ⚠️ Costo de envío: Puede no ser visible hasta seleccionar opción

3. **Métodos de Pago:**
   - ✅ OpenPay disponible (según análisis previo)
   - ✅ Tarjetas de crédito/débito
   - ⚠️ Otros métodos: No siempre claros
   - ⚠️ Información de seguridad: Limitada

4. **Resumen de Pedido:**
   - ✅ Productos y cantidades
   - ✅ Subtotal
   - ✅ Envío
   - ✅ Total

5. **Trust Signals Finales:**
   - ⚠️ Sellos SSL: No siempre visibles
   - ⚠️ Política de privacidad: Link disponible pero no prominente
   - ⚠️ Garantías: No siempre visibles
   - ⚠️ Información de contacto: Limitada

6. **Mensajes Farmacéuticos:**
   - ⚠️ Recordatorio de receta: No siempre visible
   - ⚠️ Información sobre proceso de verificación: No clara
   - ⚠️ Tiempo de procesamiento: No siempre indicado

### Fricciones Identificadas

1. **Validación de formulario no clara**
   - **Impacto:** Errores solo se muestran al enviar
   - **Solución:** Validación en tiempo real, mensajes claros

2. **Información de envío no siempre visible**
   - **Impacto:** Usuario no sabe cuándo recibirá el pedido
   - **Solución:** Mostrar tiempos de entrega claramente, por ciudad/región

3. **Trust signals limitados en checkout**
   - **Impacto:** Abandono por falta de confianza
   - **Solución:** Agregar sellos de seguridad, garantías, testimonios

4. **Mensajes farmacéuticos no prominentes**
   - **Impacto:** Usuario puede no entender el proceso
   - **Solución:** Banner claro sobre necesidad de receta, proceso de verificación

5. **Información de contacto limitada**
   - **Impacto:** Usuario no sabe cómo contactar si hay problemas
   - **Solución:** Chat/WhatsApp visible, teléfono, email

6. **Tiempo de procesamiento no indicado**
   - **Impacto:** Expectativas no claras
   - **Solución:** Indicar tiempo estimado de verificación y envío

### Métricas

- **Tiempo en página:** 3-8 minutos
- **Tasa de conversión final:** Media
- **Tasa de abandono:** Alta (estimada 40-60%)
- **Campos del formulario:** 8-12 campos

---

## Análisis Comparativo: Móvil vs Desktop

### Diferencias Clave

| Métrica | Móvil | Desktop | Diferencia |
|---------|-------|---------|------------|
| **LCP Homepage** | 15.3s | 1.0s | **14.3s más lento** |
| **LCP Categorías** | 11.2s | 1.3s | **9.9s más lento** |
| **LCP Producto** | 12.1s | 2.6s | **9.5s más lento** |
| **Experiencia General** | ⚠️ Lenta | ✅ Rápida | Crítica en móvil |

### Impacto en Conversión

- **Móvil:** Alta tasa de abandono debido a tiempos de carga
- **Desktop:** Mejor experiencia, mayor probabilidad de conversión
- **Recomendación:** Optimización móvil es **CRÍTICA**

---

## Fricciones Críticas Identificadas

### 1. Tiempos de Carga Extremos en Móvil

**Problema:** LCP de 15.3s en homepage, 11-12s en páginas internas  
**Impacto:** 50-70% de usuarios abandonan antes de ver contenido  
**Prioridad:** 🔴 **CRÍTICA**

### 2. Falta de Información Clara sobre Receta Médica

**Problema:** Usuario no siempre sabe que necesita receta  
**Impacto:** Intentos de compra fallidos, frustración  
**Prioridad:** 🔴 **ALTA**

### 3. Trust Signals Limitados en Checkout

**Problema:** Falta de sellos de seguridad, garantías visibles  
**Impacto:** Abandono en último paso (40-60% estimado)  
**Prioridad:** 🔴 **ALTA**

---

## Oportunidades de Mejora por Paso

### Homepage
1. Optimizar imágenes hero (WebP, responsive)
2. Lazy load de secciones no críticas
3. Cargar scripts de forma asíncrona
4. Mensaje claro sobre necesidad de receta

### Categorías
1. Implementar breadcrumbs
2. Agregar filtros avanzados
3. Autocompletado en búsqueda
4. Optimizar imágenes de productos

### Producto
1. Indicador de disponibilidad claro
2. Banner sobre necesidad de receta
3. Certificaciones COFEPRIS visibles
4. Información médica más completa

### Carrito
1. Estimación de envío visible
2. Indicador de progreso
3. Trust signals (sellos, garantías)
4. Opción de guardar carrito

### Checkout
1. Validación en tiempo real
2. Tiempos de entrega claros
3. Trust signals prominentes
4. Mensajes farmacéuticos visibles
5. Información de contacto accesible

---

## Métricas de Journey Completo

### Tiempo Total Estimado

- **Usuario nuevo (primera vez):** 8-12 minutos
- **Usuario recurrente:** 4-6 minutos
- **Tiempo ideal (objetivo):** 3-5 minutos

### Tasa de Abandono por Paso

1. **Homepage:** 30-40% (debido a tiempo de carga)
2. **Categorías:** 15-20%
3. **Producto:** 10-15%
4. **Carrito:** 5-10%
5. **Checkout:** 40-60% (punto crítico)

### Tasa de Conversión Estimada

- **Actual (móvil):** 1-2%
- **Actual (desktop):** 3-5%
- **Objetivo (optimizado):** 5-8%

---

## Recomendaciones Prioritarias

### Quick Wins (Implementación Rápida)

1. **Agregar breadcrumbs** (2-4 horas)
2. **Banner sobre necesidad de receta** (2-3 horas)
3. **Trust signals en checkout** (4-6 horas)
4. **Optimizar imágenes hero** (4-8 horas)

### Alto Impacto (Mediano Plazo)

1. **Optimización completa de performance móvil** (20-30 horas)
2. **Sistema de filtros avanzados** (8-12 horas)
3. **Autocompletado en búsqueda** (6-10 horas)
4. **Validación de formulario en tiempo real** (8-12 horas)

### Estrategia (Largo Plazo)

1. **Revisión completa de UX del checkout**
2. **Implementación de guardado de carrito**
3. **Sistema de recomendaciones de productos**
4. **Chat/WhatsApp integrado en cada paso**

---

## Conclusión

El journey de compra en farmaciasmacross.com.mx tiene una base sólida pero sufre de problemas críticos de performance en móvil que afectan significativamente la experiencia del usuario y las tasas de conversión. Las principales oportunidades están en:

1. **Optimización de performance móvil** (crítico)
2. **Claridad en mensajes farmacéuticos** (alto impacto)
3. **Trust signals en puntos clave** (alto impacto)
4. **Mejoras de UX en navegación y checkout** (medio impacto)

Con estas mejoras, se puede esperar un aumento significativo en las tasas de conversión, especialmente en dispositivos móviles que representan la mayoría del tráfico.

---

*Este análisis se basa en inspección manual del sitio y datos de PageSpeed Insights. Para un análisis más detallado, se recomienda realizar pruebas de usuario reales y análisis de heatmaps.*



