# Farmacias Macross - Sinergia Digital: Jira Epic Structure

**Project Key**: FM  
**Total Duration**: 20 semanas  
**Total Investment**: $364,000 MXN (sin IVA)

**Nota Importante**: 
- Todas las tareas (FM-22 a FM-120) están vinculadas a sus respectivos epics en Jira
- Las tareas mejoradas (FM-22 a FM-51) incluyen formato detallado con OBJETIVO, ENTREGABLES, ALCANCE, CRITERIOS DE ACEPTACIÓN, INPUTS REQUERIDOS, DEPENDENCIAS, ESTIMACIÓN y PRIORIDAD
- Las tareas restantes mantienen descripciones básicas que serán mejoradas progresivamente
- Todas las tareas están también vinculadas a sus stories padre mediante relaciones "Relates"

**Estructura en Jira:**
- **4 Epics**: FM-1 (Fase 1), FM-2 (Fase 2), FM-3 (Fase 3), FM-4 (Fase 4)
- **17 Stories**: FM-5 a FM-21 (vinculadas a epics)
- **99 Tasks**: FM-22 a FM-120 (vinculadas a epics y stories)

---

## EPIC 1: FASE 1 - WordPress Fachada para Compliance

**Epic Key**: FM-1  
**Summary**: Sitio WordPress rediseñado, catálogo OTC fachada, SEO técnico y compliance legal  
**Timeline**: Semanas 1-5 (Dic 2025 - Primera mitad Ene 2026)  
**Investment**: $80,000 MXN  
**Status**: To Do

### Story FM-5: Auditoría y Arquitectura de Información

**Story Key**: FM-5  
**Summary**: Análisis técnico del sitio actual y propuesta de arquitectura de información  
**Investment**: $7,000 MXN  
**Estimate**: 1 semana  
**Priority**: Highest

#### Tasks:
- **FM-22**: Auditoría técnica del sitio medicamentosespeciales.mx actual (Story Points: 3, Priority: Highest)
  - **OBJETIVO**: Realizar auditoría técnica completa del sitio medicamentosespeciales.mx para identificar estado actual, problemas técnicos y oportunidades de mejora.
  - **ENTREGABLES**: Documento PDF de análisis técnico (mínimo 15 páginas), Matriz de problemas priorizados (Alto/Medio/Bajo), Recomendaciones técnicas con estimaciones de esfuerzo, Screenshots y evidencias de problemas identificados
  - **ALCANCE**: Análisis de estructura actual, identificación de problemas técnicos, evaluación de performance, revisión de SEO on-page existente, análisis de compliance legal actual, inventario de plugins y dependencias, análisis de hosting y configuración actual
  - **CRITERIOS DE ACEPTACIÓN**: Documento entregado en formato PDF con índice navegable, Mínimo 20 hallazgos documentados con evidencia, Cada hallazgo incluye: descripción, impacto, prioridad, recomendación, Matriz de priorización con al menos 5 items de alta prioridad, Screenshots o capturas de pantalla para cada problema crítico, Revisión técnica aprobada por PM antes de presentar a cliente
  - **INPUTS REQUERIDOS**: Acceso admin WordPress (medicamentosespeciales.mx), Acceso hosting Hostinger, Lista de URLs principales del sitio actual
  - **DEPENDENCIAS**: Ninguna (es el primer entregable de Fase 1)
  
- **FM-23**: Documento de análisis técnico (Story Points: 1, Priority: High)
  - **OBJETIVO**: Documentar hallazgos de la auditoría en formato estructurado y priorizado para toma de decisiones.
  - **ENTREGABLES**: Documento de análisis técnico completo (PDF, mínimo 15 páginas), Resumen ejecutivo (1 página) para stakeholders, Matriz de priorización de mejoras
  - **ALCANCE**: Redacción de documento completo con hallazgos y recomendaciones, Priorización de mejoras (Alto/Medio/Bajo impacto), Estimaciones de esfuerzo por mejora, Roadmap sugerido de implementación
  - **CRITERIOS DE ACEPTACIÓN**: Documento en formato PDF profesional con branding, Resumen ejecutivo de máximo 1 página, Mínimo 20 hallazgos documentados, Cada hallazgo incluye: problema, impacto, esfuerzo estimado, recomendación, Matriz de priorización con criterios claros (impacto vs esfuerzo), Roadmap sugerido con fases de implementación, Aprobación de PM antes de entregar a cliente
  - **INPUTS REQUERIDOS**: Resultados de auditoría técnica (FM-22), Plantilla de documento aprobada
  - **DEPENDENCIAS**: FM-22 (bloquea)
  
- **FM-24**: Arquitectura de información propuesta (Story Points: 1, Priority: High)
  - **OBJETIVO**: Diseñar arquitectura de información propuesta para medicamentosespeciales.mx que soporte compliance, SEO y conversión.
  - **ENTREGABLES**: Mapa de sitio (sitemap conceptual) en formato visual, Estructura de navegación propuesta, Taxonomía de contenido (categorías, tags, tipos de página), Flujos de usuario principales (user journeys), Wireframes de alto nivel (máximo 8 páginas principales)
  - **ALCANCE**: Mapa de sitio (sitemap conceptual) con jerarquía clara, Estructura de navegación (menús principales, secundarios, footer), Taxonomía de contenido (categorías blog, tipos de productos, páginas estáticas), Flujos de usuario principales (homepage → producto, blog → WhatsApp, lead magnet → CRM), Wireframes de alto nivel para: Homepage, Blog, Catálogo, Producto, Consulta Especializada, FAQ, Legal, Contacto
  - **CRITERIOS DE ACEPTACIÓN**: Sitemap visual entregado (Figma o PDF), Estructura de navegación documentada con justificación, Taxonomía definida (mínimo 3 categorías blog, 2 tipos de productos), Mínimo 3 user journeys documentados (texto + diagrama), Wireframes de 8 páginas principales (baja fidelidad, pero completos), Cada wireframe incluye: estructura, CTAs principales, elementos clave, Revisión y aprobación de PM antes de presentar a cliente, Feedback del cliente en máximo 72 horas (SLA)
  - **INPUTS REQUERIDOS**: Resultados de auditoría (FM-22, FM-23), Logo y guía de marca (si existe), Lista de 20 SKUs principales
  - **DEPENDENCIAS**: FM-22, FM-23 (bloquea)

**Dependencies**: Acceso a Hostinger/WordPress admin (cliente)

---

### Story FM-6: Sitio WordPress Rediseñado

**Story Key**: FM-6  
**Summary**: Rediseño completo del sitio WordPress con 8 tipos de páginas principales  
**Investment**: $20,000 - $42,000 MXN (variable según reuso de componentes)  
**Estimate**: 3 semanas  
**Priority**: Highest

#### Tasks:
- **FM-25**: Setup y configuración inicial WordPress (Story Points: 2, Priority: Highest)
  - **OBJETIVO**: Configurar entorno WordPress en Hostinger listo para desarrollo, con plugins esenciales y configuración base.
  - **ENTREGABLES**: WordPress instalado/actualizado a versión estable más reciente, Plugins esenciales instalados y configurados, Tema base configurado, Accesos de desarrollo configurados, Documento de configuración técnica
  - **ALCANCE**: Configuración de hosting Hostinger (si requiere ajustes), Instalación/actualización de WordPress (versión estable), Configuración de plugins esenciales (SEO, Caching, Seguridad, Formularios, Schema markup), Setup de tema base (tema hijo si aplica), Configuración de permisos y usuarios, Backup inicial configurado
  - **CRITERIOS DE ACEPTACIÓN**: WordPress versión estable instalada (mínimo 6.0+), Mínimo 5 plugins esenciales instalados y activos, Tema base configurado y funcional, Accesos de desarrollo creados (admin, editor), Backup inicial realizado y verificado, Documento técnico de configuración entregado (formato checklist), Sitio accesible y sin errores críticos en consola, Revisión técnica aprobada por desarrollador senior
  - **INPUTS REQUERIDOS**: Acceso admin Hostinger, Acceso admin WordPress (medicamentosespeciales.mx), Credenciales de hosting
  - **DEPENDENCIAS**: FM-24 (arquitectura aprobada)
  
- **FM-26**: Diseño responsivo base (Story Points: 3, Priority: Highest)
  - **OBJETIVO**: Crear sistema de diseño responsivo base que funcione en desktop, tablet y móvil, siguiendo guía de marca.
  - **ENTREGABLES**: Sistema de diseño documentado (colores, tipografía, espaciado), Componentes reutilizables creados, Breakpoints definidos y testeados, Documento de guía de estilos
  - **ALCANCE**: Sistema de diseño (colores primarios/secundarios, tipografía, espaciado consistente), Componentes reutilizables (botones, cards, formularios, CTAs), Breakpoints definidos (desktop: 1200px+, tablet: 768px-1199px, móvil: <768px), Testing de responsividad en dispositivos reales o emuladores, Documento de guía de estilos (Figma o PDF)
  - **CRITERIOS DE ACEPTACIÓN**: Sistema de colores definido (mínimo 5 colores: primario, secundario, texto, fondo, acento), Tipografía definida (mínimo 2 fuentes: heading, body), Espaciado consistente (sistema de 8px o similar), Mínimo 8 componentes reutilizables creados (botón, card, input, CTA, etc.), Breakpoints documentados y testeados, Testing de responsividad completado en: Chrome DevTools (3 tamaños), dispositivo móvil real, Documento de guía de estilos entregado (Figma library o PDF), Aprobación de diseño por PM antes de desarrollo
  - **INPUTS REQUERIDOS**: Logo y guía de marca (si existe), Wireframes aprobados (FM-24)
  - **DEPENDENCIAS**: FM-24 (wireframes aprobados), FM-25 (WordPress configurado)
  
- **FM-27**: Homepage con hero y secciones estratégicas (Story Points: 2, Priority: High)
  - **OBJETIVO**: Desarrollar homepage de medicamentosespeciales.mx con hero section, secciones de valor y CTAs estratégicos conectados a WhatsApp.
  - **ENTREGABLES**: Homepage funcional y responsiva, Hero section con CTA principal, Mínimo 3 secciones de valor, Integración con WhatsApp (botón flotante + CTAs), Testing de funcionalidad completado
  - **ALCANCE**: Diseño de hero section (imagen/video, headline, subheadline, CTA principal), Secciones de valor (mínimo 3: qué ofrecemos, cómo funciona, beneficios), CTAs principales (mínimo 2: "Consultar vía WhatsApp", "Ver catálogo"), Integración con WhatsApp (botón flotante + CTAs con mensaje pre-escrito), Optimización de imágenes (WebP, lazy loading), Testing en 3 dispositivos (desktop, tablet, móvil)
  - **CRITERIOS DE ACEPTACIÓN**: Homepage desarrollada y publicada en WordPress, Hero section con imagen optimizada (máximo 200KB, formato WebP), Mínimo 3 secciones de valor con contenido relevante, Mínimo 2 CTAs principales funcionales, Botón flotante WhatsApp instalado y funcional, Mensaje pre-escrito configurado: "Hola, quisiera consultar disponibilidad de medicamentos especializados", Testing de responsividad completado (desktop, tablet, móvil), PageSpeed score mínimo 80 (móvil) y 90 (desktop), Sin errores en consola del navegador, Aprobación de cliente (SLA: 72 horas para feedback)
  - **INPUTS REQUERIDOS**: Wireframes aprobados (FM-24), Sistema de diseño (FM-26), Contenido de homepage (textos, imágenes)
  - **DEPENDENCIAS**: FM-24 (wireframes), FM-26 (sistema de diseño), FM-25 (WordPress configurado)
  
- **FM-28**: Página Sobre Nosotros / Centros de Distribución (Story Points: 2, Priority: Medium)
  - **OBJETIVO**: Crear página "Sobre Nosotros / Centros de Distribución" con información de empresa, ubicaciones (CDMX, Puebla) y formulario de contacto.
  - **ENTREGABLES**: Página "Sobre Nosotros" funcional y responsiva, Información de centros de distribución (CDMX, Puebla), Mapa interactivo con ubicaciones, Formulario de contacto integrado
  - **ALCANCE**: Contenido sobre la empresa (historia, misión, valores - máximo 500 palabras), Información de centros (CDMX: dirección, horarios, contacto; Puebla: dirección, horarios, contacto), Mapa interactivo (Google Maps embebido o similar) con marcadores de ubicaciones, Formulario de contacto (nombre, email, teléfono, mensaje, centro de interés), Integración de formulario con email y/o CRM (configuración básica), Optimización de imágenes (fotos de centros si disponibles)
  - **CRITERIOS DE ACEPTACIÓN**: Página desarrollada y publicada en WordPress, Contenido sobre empresa (mínimo 300 palabras, máximo 500), Información completa de 2 centros (CDMX y Puebla): dirección, horarios, teléfono, Mapa interactivo funcional con 2 marcadores, Formulario de contacto funcional (mínimo 5 campos), Formulario envía email de notificación al enviar, Testing de responsividad completado, Imágenes optimizadas (máximo 300KB cada una, formato WebP), Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Información de centros (direcciones exactas, horarios, contactos), Fotos de centros (si disponibles), Contenido sobre empresa (o borrador para editar)
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-29**: Template de Blog dinámico (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear template dinámico de blog que soporte categorías, tags, sidebar con widgets y paginación para los 15 artículos especializados.
  - **ENTREGABLES**: Template de blog posts funcional, Sistema de categorías y tags configurado, Sidebar con widgets personalizados, Paginación implementada, Testing de funcionalidad completado
  - **ALCANCE**: Estructura de blog posts (header con fecha/autor, contenido, footer con CTA), Categorías y tags (mínimo 3 categorías: Awareness, Consideration, Decision), Sidebar con widgets (búsqueda, categorías, posts recientes, CTA WhatsApp), Paginación (anterior/siguiente, números de página), Integración con schema markup de artículo, Optimización para SEO (meta tags dinámicos, breadcrumbs)
  - **CRITERIOS DE ACEPTACIÓN**: Template de blog posts desarrollado y funcional, Sistema de categorías configurado (mínimo 3 categorías), Sistema de tags configurado y funcional, Sidebar con mínimo 3 widgets (búsqueda, categorías, posts recientes), Paginación funcional (anterior/siguiente + números), Schema markup Article implementado y validado, Breadcrumbs implementados, Testing con 3 posts de prueba completado, Aprobación de PM antes de usar para artículos reales
  - **INPUTS REQUERIDOS**: Wireframes de blog (FM-24), Sistema de diseño (FM-26)
  - **DEPENDENCIAS**: FM-24 (wireframes), FM-26 (sistema de diseño), FM-25 (WordPress configurado)
  
- **FM-30**: Página Catálogo Productos OTC (fachada) (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear página de catálogo de productos OTC (fachada) con listado, filtros, búsqueda y enlaces externos a Farmalisto/Similares.
  - **ENTREGABLES**: Página catálogo funcional con grid de productos, Sistema de filtros y búsqueda, Enlaces externos a Farmalisto/Similares con tracking, Testing de funcionalidad completado
  - **ALCANCE**: Listado de productos (grid responsivo, mínimo 3 columnas desktop, 2 tablet, 1 móvil), Filtros (por categoría, precio, disponibilidad), Búsqueda funcional (búsqueda en tiempo real), Grid de productos (imagen, nombre, precio, CTA "Comprar en [Enlace externo]"), Enlaces externos a Farmalisto/SimilaresOnline (apertura en nueva pestaña), Tracking de clics (UTM parameters: source=medicamentosespeciales, medium=catalog, campaign=otc), Paginación si hay más de 20 productos
  - **CRITERIOS DE ACEPTACIÓN**: Página catálogo desarrollada y publicada, Grid de productos funcional (mínimo 20 productos mostrados), Sistema de filtros funcional (mínimo 2 filtros: categoría, disponibilidad), Búsqueda funcional (búsqueda en tiempo real o con botón), Enlaces externos configurados (mínimo 20 productos con links), UTM parameters configurados en todos los enlaces externos, Enlaces abren en nueva pestaña (target="_blank"), Tracking de clics configurado en GA4/GTM, Testing de responsividad completado, Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Lista de 20 productos OTC con información básica, Enlaces externos a Farmalisto/Similares para cada producto, Imágenes de productos (si disponibles)
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-31**: Landing Consulta Especializada (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear landing page "Consulta Especializada" optimizada para conversión con formulario de contacto, CTAs a WhatsApp e información del proceso.
  - **ENTREGABLES**: Landing page "Consulta Especializada" funcional y responsiva, Formulario de contacto optimizado para conversión, CTAs a WhatsApp con mensaje pre-escrito, Información sobre proceso de consulta, Testing de conversión completado
  - **ALCANCE**: Diseño optimizado para conversión (hero section, beneficios, proceso paso a paso, testimonios si disponibles), Formulario de contacto (mínimo 5 campos: nombre, teléfono, email, medicamento de interés, ciudad), CTAs a WhatsApp (mínimo 2: botón principal, botón secundario), Mensaje pre-escrito: "Hola, necesito consultar disponibilidad de [medicamento]. Estoy en [ciudad].", Información sobre proceso (cómo funciona, tiempo de respuesta, qué necesitan), Integración de formulario con email y CRM (configuración básica), Tracking de conversiones (form submit, WhatsApp click)
  - **CRITERIOS DE ACEPTACIÓN**: Landing page desarrollada y publicada, Hero section con headline claro y CTA principal, Formulario funcional con mínimo 5 campos, Formulario envía email de notificación al enviar, Mínimo 2 CTAs a WhatsApp funcionales, Mensaje pre-escrito configurado correctamente, Información sobre proceso (mínimo 3 pasos explicados), Tracking de conversiones configurado (form submit, WhatsApp click en GA4), Testing de responsividad completado, PageSpeed score mínimo 80 (móvil), A/B testing configurado (opcional, pero recomendado), Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Contenido de landing (textos, beneficios, proceso), Información sobre proceso de consulta
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-32**: Página Preguntas Frecuentes (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Crear página de Preguntas Frecuentes (FAQ) con estructura interactiva, schema markup y optimización SEO.
  - **ENTREGABLES**: Página FAQ funcional con accordion interactivo, Schema markup FAQ implementado y validado, Optimización SEO completada, Testing de funcionalidad completado
  - **ALCANCE**: Estructura de FAQ (mínimo 10 preguntas frecuentes organizadas por categorías), Accordion interactivo (expandir/colapsar preguntas), Schema markup FAQ (FAQPage schema de Google), Optimización SEO (meta title, meta description, headings H1-H6), Categorías de preguntas (mínimo 3: productos, proceso, contacto), Búsqueda dentro de FAQ (opcional pero recomendado)
  - **CRITERIOS DE ACEPTACIÓN**: Página FAQ desarrollada y publicada, Mínimo 10 preguntas frecuentes con respuestas completas, Mínimo 3 categorías de preguntas, Accordion interactivo funcional (expandir/colapsar), Schema markup FAQPage implementado, Validación de schema con Google Rich Results Test (sin errores), SEO optimizado (meta title, meta description, headings), Testing de responsividad completado, Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Lista de preguntas frecuentes (o borrador para desarrollar), Respuestas a preguntas frecuentes
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-33**: Páginas legales (Aviso de Privacidad / Términos) (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear páginas legales (Aviso de Privacidad, Términos y Condiciones) compliant con COFEPRIS y sector salud.
  - **ENTREGABLES**: Página "Aviso de Privacidad" COFEPRIS compliant, Página "Términos y Condiciones" sector salud, Página "Política de Cookies", Disclaimers médicos en footer, Revisión legal completada
  - **ALCANCE**: Aviso de Privacidad COFEPRIS compliant (mínimo 8 secciones requeridas por ley), Términos y Condiciones sector salud (mínimo 6 secciones), Política de cookies (GDPR compliant si aplica), Disclaimers médicos en footer de todas las páginas, Revisión legal por abogado especializado en salud (opcional pero recomendado), Links a páginas legales en footer
  - **CRITERIOS DE ACEPTACIÓN**: Aviso de Privacidad desarrollado y publicado (mínimo 8 secciones), Términos y Condiciones desarrollados y publicados (mínimo 6 secciones), Política de Cookies desarrollada y publicada, Disclaimers médicos en footer de todas las páginas, Links a páginas legales en footer funcionales, Revisión legal completada (o documentación de cumplimiento), Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Datos fiscales de la empresa, Información de contacto para aviso de privacidad, Revisión legal (si se contrata servicio externo)
  - **DEPENDENCIAS**: FM-25 (WordPress configurado)
  
- **FM-34**: Página Contacto (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Crear página de contacto con formulario, información de contacto, mapa interactivo y horarios de atención.
  - **ENTREGABLES**: Página contacto funcional y responsiva, Formulario de contacto integrado, Información de contacto completa, Mapa interactivo con ubicaciones, Horarios de atención documentados
  - **ALCANCE**: Formulario de contacto (nombre, email, teléfono, asunto, mensaje), Información de contacto (teléfono, email, direcciones de centros), Mapa interactivo (Google Maps embebido con marcadores), Horarios de atención (días y horarios por centro), Integración de formulario con email, Links a redes sociales (si aplica)
  - **CRITERIOS DE ACEPTACIÓN**: Página contacto desarrollada y publicada, Formulario funcional con mínimo 5 campos, Formulario envía email de notificación al enviar, Información de contacto completa (teléfono, email, direcciones), Mapa interactivo funcional con marcadores, Horarios de atención documentados por centro, Testing de responsividad completado, Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Información de contacto (teléfono, email, direcciones), Horarios de atención por centro
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-35**: Optimización de velocidad (Story Points: 2, Priority: High)
  - **OBJETIVO**: Optimizar velocidad del sitio WordPress para cumplir con estándares de performance (PageSpeed mínimo 80 móvil, 90 desktop).
  - **ENTREGABLES**: Sitio optimizado para velocidad, Reporte de performance antes/después, Configuración de caching documentada, Testing de performance completado
  - **ALCANCE**: Optimización de imágenes (WebP, lazy loading, compresión), Caching configurado (WP Rocket o similar), Minificación CSS/JS, CDN configurado (si aplica), Testing de performance (PageSpeed Insights, GTmetrix), Optimización de base de datos (limpieza, índices)
  - **CRITERIOS DE ACEPTACIÓN**: PageSpeed score mínimo 80 (móvil) y 90 (desktop), Todas las imágenes optimizadas (formato WebP, máximo 200KB por imagen), Lazy loading implementado en imágenes, Caching configurado y funcional, CSS/JS minificados, CDN configurado (si aplica), Reporte de performance antes/después entregado, Testing completado en PageSpeed Insights y GTmetrix, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Acceso a hosting Hostinger, Acceso admin WordPress
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), Todas las páginas principales desarrolladas

**Dependencies**: 
- FM-5 (Arquitectura de información)
- Logo y guía de marca (cliente)
- Feedback en wireframes (cliente, SLA 72h)

---

### Story FM-7: Catálogo Fachada OTC - 20 Productos

**Story Key**: FM-7  
**Summary**: 20 páginas de productos OTC con SEO optimizado y CTAs estratégicos  
**Investment**: $16,000 MXN  
**Estimate**: 2 semanas  
**Priority**: High

#### Tasks:
- **FM-36**: Template de página de producto OTC (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear template reutilizable de página de producto OTC que pueda usarse para los 20 productos con campos personalizados.
  - **ENTREGABLES**: Template de página de producto OTC funcional, Campos personalizados configurados en WordPress, Documentación del template
  - **ALCANCE**: Diseño de template reutilizable (estructura, layout, componentes), Estructura de contenido (imagen, nombre, descripción, beneficios, advertencias, CTAs), Campos personalizados (Custom Post Type o ACF para productos OTC), Integración con schema markup Product, Testing del template con 1 producto de prueba
  - **CRITERIOS DE ACEPTACIÓN**: Template desarrollado y funcional en WordPress, Custom Post Type o ACF configurado para productos OTC, Mínimo 8 campos personalizados (nombre, descripción, beneficios, advertencias, precio, enlace externo, imagen, categoría), Template responsivo (desktop, tablet, móvil), Testing con 1 producto de prueba completado, Documentación del template entregada (cómo usar, qué campos llenar), Aprobación de PM antes de crear las 20 páginas
  - **INPUTS REQUERIDOS**: Sistema de diseño (FM-26), Wireframes de producto (FM-24)
  - **DEPENDENCIAS**: FM-25 (WordPress configurado), FM-26 (sistema de diseño)
  
- **FM-37**: Creación de 20 páginas de productos (Story Points: 5, Priority: High)
  - **OBJETIVO**: Crear 20 páginas de productos OTC completas con contenido optimizado, CTAs estratégicos y enlaces externos.
  - **ENTREGABLES**: 20 páginas de productos OTC publicadas, Contenido optimizado por producto (250-300 palabras), CTAs estratégicos configurados, Enlaces externos con tracking
  - **ALCANCE**: Descripción del producto (250-300 palabras, optimizada SEO), Usos y beneficios principales (mínimo 3 beneficios), Advertencias básicas (disclaimers médicos), CTAs estratégicos: CTA Primario: "Comprar en [Enlace Farmalisto/Similares]", CTA Secundario: "¿Necesitas medicamento especializado?" → WhatsApp, Imágenes optimizadas (WebP, máximo 200KB), Schema markup Product implementado
  - **CRITERIOS DE ACEPTACIÓN**: 20 páginas de productos OTC creadas y publicadas, Cada página tiene descripción de 250-300 palabras, Cada página tiene mínimo 3 beneficios documentados, Cada página tiene advertencias/disclaimers médicos, CTA primario configurado en todas las páginas (enlace externo), CTA secundario configurado en todas las páginas (WhatsApp), Imágenes optimizadas (WebP, máximo 200KB cada una), Schema markup Product implementado y validado en todas las páginas, Testing de responsividad completado (3 dispositivos), Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Lista de 20 productos OTC con información básica, Enlaces externos a Farmalisto/Similares para cada producto, Imágenes de productos (si disponibles)
  - **DEPENDENCIAS**: FM-36 (template de producto)
  
- **FM-38**: Schema markup de producto (Story Points: 1, Priority: High)
  - **OBJETIVO**: Implementar schema markup Product en todas las páginas de productos OTC para mejorar visibilidad en Google.
  - **ENTREGABLES**: Schema markup Product implementado en 20 páginas, Validación de schema completada, Testing con Google Rich Results
  - **ALCANCE**: Implementación de Product schema (nombre, descripción, precio, imagen, disponibilidad), Datos estructurados validados (sin errores), Testing con Google Rich Results Test, Verificación de que schema aparece en búsquedas (opcional, puede tardar)
  - **CRITERIOS DE ACEPTACIÓN**: Schema markup Product implementado en las 20 páginas, Validación de schema con Google Rich Results Test (sin errores), Mínimo 5 campos requeridos por producto (name, description, image, price, availability), Testing completado en 3 páginas de muestra, Documentación de implementación entregada, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Páginas de productos creadas (FM-37)
  - **DEPENDENCIAS**: FM-37 (páginas de productos creadas)
  
- **FM-39**: SEO optimizado por producto (Story Points: 2, Priority: High)
  - **OBJETIVO**: Optimizar SEO on-page de todas las páginas de productos OTC para mejorar rankings y visibilidad orgánica.
  - **ENTREGABLES**: SEO optimizado en 20 páginas de productos, Meta tags configurados, Headings estructurados correctamente, URLs amigables, Internal linking implementado
  - **ALCANCE**: Meta titles y descriptions (máximo 60 caracteres title, 160 caracteres description), Headings H1-H6 correctos (1 H1 por página, estructura lógica), Alt text en imágenes (descriptivo, máximo 125 caracteres), URLs amigables (slug optimizado, sin caracteres especiales), Internal linking (mínimo 3 enlaces internos por página), Optimización de keywords (keywords primarias y secundarias)
  - **CRITERIOS DE ACEPTACIÓN**: Meta titles configurados en las 20 páginas (máximo 60 caracteres), Meta descriptions configuradas en las 20 páginas (máximo 160 caracteres), Headings H1-H6 correctos (1 H1, estructura lógica), Alt text en todas las imágenes (descriptivo, sin "imagen de"), URLs amigables configuradas (slug optimizado), Mínimo 3 enlaces internos por página, Keywords primarias y secundarias identificadas y usadas, Testing de SEO completado (Yoast o Rank Math sin errores críticos), Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Páginas de productos creadas (FM-37), Keywords research (FM-47)
  - **DEPENDENCIAS**: FM-37 (páginas de productos)
  
- **FM-40**: Integración con enlaces externos (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Configurar enlaces externos a Farmalisto/SimilaresOnline con tracking UTM y apertura en nueva pestaña.
  - **ENTREGABLES**: Enlaces externos configurados en 20 páginas, UTM parameters implementados, Tracking de clics configurado, Testing de funcionalidad completado
  - **ALCANCE**: Links a Farmalisto/SimilaresOnline (mínimo 20 productos con enlaces), Tracking de clics (UTM parameters: source=medicamentosespeciales, medium=product, campaign=otc, content=[nombre-producto]), Apertura en nueva pestaña (target="_blank"), Tracking en GA4/GTM (evento de clic externo)
  - **CRITERIOS DE ACEPTACIÓN**: Enlaces externos configurados en las 20 páginas, UTM parameters configurados en todos los enlaces (source, medium, campaign, content), Enlaces abren en nueva pestaña (target="_blank"), Tracking de clics configurado en GA4/GTM, Evento "external_link_click" configurado en GTM, Testing de clics completado (verificar que UTM se pasa correctamente), Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Páginas de productos con CTAs (FM-37), Enlaces externos a Farmalisto/Similares
  - **DEPENDENCIAS**: FM-37 (páginas de productos), GA4/GTM configurado (FM-101, FM-102)

**Dependencies**: 
- FM-6 (Sitio WordPress base)
- Lista de 20 SKUs principales (cliente, Semana 2-3)

---

### Story FM-8: SEO Técnico + Compliance Legal

**Story Key**: FM-8  
**Summary**: SEO on-page completo, schema markup especializado, documentos legales health-compliant  
**Investment**: $18,000 MXN  
**Estimate**: 2 semanas  
**Priority**: High

#### Tasks:
- **FM-41**: SEO on-page completo (todas las páginas) (Story Points: 3, Priority: High)
  - **OBJETIVO**: Optimizar SEO on-page de todas las páginas del sitio (homepage, blog, catálogo, productos, estáticas) para mejorar rankings orgánicos.
  - **ENTREGABLES**: SEO on-page optimizado en todas las páginas, Meta tags configurados, Headings structure corregida, Internal linking strategy implementada, Image optimization completada, URL structure optimizada
  - **ALCANCE**: Optimización de meta tags (titles, descriptions en todas las páginas), Headings structure (H1-H6 correctos, jerarquía lógica), Internal linking strategy (mínimo 3 enlaces internos por página, anchor text relevante), Image optimization (alt text, nombres de archivo, compresión), URL structure (URLs amigables, sin parámetros innecesarios), Sitemap XML generado y actualizado
  - **CRITERIOS DE ACEPTACIÓN**: Meta tags optimizados en todas las páginas (mínimo 15 páginas), Headings structure corregida (1 H1 por página, jerarquía lógica), Internal linking implementado (mínimo 3 enlaces internos por página), Todas las imágenes tienen alt text descriptivo, URLs amigables configuradas (sin caracteres especiales), Sitemap XML generado y actualizado, Testing de SEO completado (Yoast o Rank Math sin errores críticos), Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Todas las páginas desarrolladas, Keywords research (FM-47)
  - **DEPENDENCIAS**: Todas las páginas principales desarrolladas
  
- **FM-42**: Schema markup especializado (Story Points: 2, Priority: High)
  - **OBJETIVO**: Implementar schema markup especializado (Organization, LocalBusiness, MedicalBusiness, Product, BreadcrumbList) para mejorar visibilidad en Google.
  - **ENTREGABLES**: Schema markup Organization implementado, Schema markup LocalBusiness implementado (CDMX, Puebla), Schema markup MedicalBusiness implementado, Schema markup Product implementado (20 productos OTC), Schema markup BreadcrumbList implementado, Validación de todos los schemas completada
  - **ALCANCE**: Organization schema (nombre, logo, URL, contacto), LocalBusiness schema (cada centro: CDMX, Puebla - dirección, horarios, teléfono), MedicalBusiness schema (tipo de negocio, servicios), Product schema (20 productos OTC - ya implementado en FM-38), BreadcrumbList schema (navegación jerárquica), Validación con Google Rich Results Test
  - **CRITERIOS DE ACEPTACIÓN**: Schema Organization implementado y validado, Schema LocalBusiness implementado para 2 centros (CDMX, Puebla), Schema MedicalBusiness implementado y validado, Schema Product implementado en 20 productos (ya completado en FM-38), Schema BreadcrumbList implementado en todas las páginas, Validación de todos los schemas con Google Rich Results Test (sin errores), Testing completado en 5 páginas de muestra, Documentación de implementación entregada, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Información de empresa (nombre, logo, contacto), Información de centros (direcciones, horarios)
  - **DEPENDENCIAS**: FM-38 (Product schema), Todas las páginas desarrolladas
  
- **FM-43**: Sitemap XML multinivel (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Generar sitemap XML multinivel con prioridades y frecuencias optimizadas, y submit a Google Search Console.
  - **ENTREGABLES**: Sitemap XML generado y actualizado, Prioridades y frecuencias configuradas, Submit a Google Search Console completado, Documentación de configuración
  - **ALCANCE**: Generación de sitemap (todas las páginas, posts, productos), Prioridades configuradas (homepage: 1.0, páginas principales: 0.8, productos: 0.6, blog: 0.7), Frecuencias configuradas (homepage: daily, páginas principales: weekly, productos: monthly, blog: weekly), Submit a Google Search Console, Verificación de que sitemap se indexa correctamente
  - **CRITERIOS DE ACEPTACIÓN**: Sitemap XML generado (mínimo 25 URLs), Prioridades configuradas (homepage: 1.0, páginas principales: 0.8), Frecuencias configuradas (homepage: daily, páginas principales: weekly), Sitemap submit a Google Search Console, Verificación de que Google indexa el sitemap (sin errores), Documentación de configuración entregada, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Todas las páginas desarrolladas, Acceso a Google Search Console
  - **DEPENDENCIAS**: Todas las páginas principales desarrolladas, Google Search Console configurado (FM-46)
  
- **FM-44**: Robots.txt optimizado (Story Points: 1, Priority: Low)
  - **OBJETIVO**: Configurar robots.txt optimizado para controlar crawlers, exclusiones necesarias y referencia al sitemap.
  - **ENTREGABLES**: robots.txt optimizado y publicado, Configuración de crawlers documentada, Referencia al sitemap configurada
  - **ALCANCE**: Configuración de crawlers (User-agent, Allow, Disallow), Exclusiones necesarias (admin, wp-admin, archivos privados), Sitemap reference (Sitemap: URL del sitemap XML), Testing de robots.txt (verificar que funciona correctamente)
  - **CRITERIOS DE ACEPTACIÓN**: robots.txt creado y publicado en raíz del sitio, Configuración de crawlers (User-agent: *, Allow, Disallow), Exclusiones configuradas (wp-admin, archivos privados), Referencia al sitemap configurada (Sitemap: URL), Testing de robots.txt completado (verificar con Google Search Console), Documentación de configuración entregada, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Sitemap XML generado (FM-43)
  - **DEPENDENCIAS**: FM-43 (sitemap XML)
  
- **FM-45**: Documentos legales health-compliant (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear documentos legales health-compliant (Aviso de Privacidad COFEPRIS, Términos sector salud, Disclaimers, Política de cookies) y completar revisión legal.
  - **ENTREGABLES**: Aviso de Privacidad COFEPRIS compliant, Términos y Condiciones sector salud, Disclaimers médicos en cada página producto, Política de cookies, Revisión legal completada
  - **ALCANCE**: Aviso de Privacidad COFEPRIS (mínimo 8 secciones requeridas por ley mexicana), Términos y Condiciones sector salud (mínimo 6 secciones: uso, responsabilidades, limitaciones), Disclaimers en cada página producto (advertencias médicas, consultar médico), Política de cookies (GDPR compliant si aplica), Revisión legal por abogado especializado (opcional pero recomendado)
  - **CRITERIOS DE ACEPTACIÓN**: Aviso de Privacidad desarrollado (mínimo 8 secciones requeridas), Términos y Condiciones desarrollados (mínimo 6 secciones), Disclaimers médicos en las 20 páginas de productos, Política de cookies desarrollada y publicada, Revisión legal completada (o documentación de cumplimiento), Links a documentos legales en footer funcionales, Aprobación de cliente (SLA: 72 horas)
  - **INPUTS REQUERIDOS**: Datos fiscales de la empresa, Información de contacto para aviso de privacidad, Revisión legal (si se contrata servicio externo)
  - **DEPENDENCIAS**: FM-33 (páginas legales base), FM-37 (páginas de productos)
  
- **FM-46**: Configuración Google Search Console (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Configurar Google Search Console con verificación de propiedad, submit de sitemap, configuración de parámetros URL y monitoreo inicial.
  - **ENTREGABLES**: Google Search Console configurado y verificado, Sitemap submit completado, Configuración de parámetros URL, Monitoreo inicial configurado
  - **ALCANCE**: Verificación de propiedad (método: HTML tag, DNS, o archivo), Submit sitemap (sitemap.xml), Configuración de parámetros URL (qué parámetros ignorar), Monitoreo inicial (configurar alertas, revisar errores), Testing de indexación (verificar que Google indexa páginas)
  - **CRITERIOS DE ACEPTACIÓN**: Google Search Console configurado y verificado, Sitemap submit completado (sitemap.xml), Configuración de parámetros URL (mínimo 3 parámetros configurados), Monitoreo inicial configurado (alertas, errores), Testing de indexación completado (verificar que Google indexa páginas), Documentación de configuración entregada, Aprobación de PM antes de considerar completo
  - **INPUTS REQUERIDOS**: Acceso a Google Search Console (o crear cuenta nueva), Sitemap XML generado (FM-43)
  - **DEPENDENCIAS**: FM-43 (sitemap XML)

**Dependencies**: 
- FM-6 (Sitio WordPress)
- FM-7 (Páginas de productos)
- Acceso a Google Search Console (cliente)

---

## EPIC 2: FASE 2 - Contenido Educativo Estratégico

**Epic Key**: FM-2  
**Summary**: 15 artículos especializados, 2 lead magnets, optimización de conversión  
**Timeline**: Semanas 4-10 (Finales Dic 2025 - Principios Feb 2026)  
**Investment**: $102,000 MXN  
**Status**: To Do

### Story FM-9: Research y Estrategia de Contenido

**Story Key**: FM-9  
**Summary**: Keyword research, content calendar, matriz de intención, briefs detallados  
**Investment**: $13,000 MXN  
**Estimate**: 1.5 semanas  
**Priority**: Highest

#### Tasks:
- **FM-47**: Keyword research especializado (Story Points: 3, Priority: High)
  - **OBJETIVO**: Realizar keyword research especializado para identificar 100+ términos realistas relacionados con medicamentos especializados, con análisis de competencia, volumen y dificultad SEO.
  - **ENTREGABLES**: Lista de 100+ keywords identificadas, Análisis de competencia por keyword, Volumen de búsqueda documentado, Dificultad SEO calculada, Intención de búsqueda clasificada (Awareness/Consideration/Decision), Documento de keyword research (Excel o Google Sheets)
  - **ALCANCE**: 100+ términos realistas identificados (herramientas: Google Keyword Planner, SEMrush, Ahrefs), Análisis de competencia (top 10 resultados por keyword), Volumen de búsqueda (mensual, estacionalidad), Dificultad SEO (score 0-100), Intención de búsqueda (Awareness: informacional, Consideration: comparación, Decision: compra), Agrupación por categorías (medicamentos específicos, condiciones médicas, procesos)
  - **CRITERIOS DE ACEPTACIÓN**: Mínimo 100 keywords identificadas y documentadas, Cada keyword incluye: término, volumen mensual, dificultad SEO, intención, competencia, Keywords agrupadas por categorías (mínimo 5 categorías), Análisis de competencia completado (top 10 resultados analizados), Documento entregado en formato Excel/Sheets con columnas: Keyword, Volumen, Dificultad, Intención, Competencia, Categoría, Keywords priorizadas (top 30 identificadas), Aprobación de PM antes de usar para content calendar
  - **INPUTS REQUERIDOS**: Lista de 20 SKUs principales, Acceso a herramientas de keyword research (Google Keyword Planner, SEMrush, Ahrefs)
  - **DEPENDENCIAS**: Ninguna (puede iniciar en paralelo con Fase 1)
  
- **FM-48**: Content calendar 6 meses sugeridos (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Crear content calendar sugerido para 6 meses con frecuencia de publicación, temas por mes y alineación con campañas de Google Ads.
  - **ENTREGABLES**: Content calendar 6 meses (formato calendario), Frecuencia de publicación definida, Temas por mes asignados, Alineación con campañas Google Ads documentada
  - **ALCANCE**: Calendario editorial (6 meses, formato mensual), Frecuencia de publicación (sugerido: 2-3 artículos/mes), Temas por mes (alineados con keywords y campañas), Alineación con campañas (qué artículos apoyan qué campañas), Fechas sugeridas de publicación, Responsables sugeridos (si aplica)
  - **CRITERIOS DE ACEPTACIÓN**: Content calendar creado (formato calendario, 6 meses), Frecuencia de publicación definida (mínimo 2 artículos/mes), Temas asignados por mes (mínimo 2 temas/mes), Alineación con campañas Google Ads documentada, Fechas sugeridas de publicación definidas, Documento entregado en formato Excel/Sheets o calendario visual, Aprobación de PM antes de usar para producción de contenido
  - **INPUTS REQUERIDOS**: Keyword research (FM-47), Estrategia de campañas Google Ads (FM-91)
  - **DEPENDENCIAS**: FM-47 (keyword research)
  
- **FM-49**: Matriz de intención de búsqueda por keyword (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Crear matriz de intención de búsqueda por keyword que clasifique términos en Awareness, Consideration, Decision y mapee keywords a artículos.
  - **ENTREGABLES**: Matriz de intención de búsqueda (Excel/Sheets), Clasificación de keywords (Awareness/Consideration/Decision), Mapeo de keywords a artículos, Priorización de keywords documentada
  - **ALCANCE**: Clasificación: Awareness (informacional), Consideration (comparación), Decision (compra), Mapeo de keywords a artículos (qué keyword va en qué artículo), Priorización (keywords más importantes primero), Justificación de clasificación (por qué cada keyword es Awareness/Consideration/Decision)
  - **CRITERIOS DE ACEPTACIÓN**: Matriz creada con mínimo 50 keywords clasificadas, Cada keyword tiene intención asignada (Awareness/Consideration/Decision), Mapeo de keywords a artículos completado (mínimo 15 artículos mapeados), Priorización documentada (top 30 keywords identificadas), Justificación de clasificación incluida, Documento entregado en formato Excel/Sheets, Aprobación de PM antes de usar para briefs de artículos
  - **INPUTS REQUERIDOS**: Keyword research (FM-47)
  - **DEPENDENCIAS**: FM-47 (keyword research)
  
- **FM-50**: Estrategia de CTAs por categoría de contenido (Story Points: 1, Priority: Medium)
  - **OBJETIVO**: Definir estrategia de CTAs por categoría de contenido (Awareness → WhatsApp, Consideration → WhatsApp + farmaciasmacross.com.mx, Decision → farmaciasmacross.com.mx directo).
  - **ENTREGABLES**: Estrategia de CTAs documentada, CTAs definidos por categoría (Awareness/Consideration/Decision), Mensajes de CTAs escritos, Documento de estrategia
  - **ALCANCE**: CTAs para Awareness (→ WhatsApp: "Más información"), CTAs para Consideration (→ WhatsApp + botón a farmaciasmacross.com.mx: "Consulta disponibilidad"), CTAs para Decision (→ farmaciasmacross.com.mx directo: "Ver precio en farmacia"), Mensajes de CTAs escritos (copy para cada tipo), Ubicación de CTAs (dónde colocar en cada tipo de artículo)
  - **CRITERIOS DE ACEPTACIÓN**: Estrategia de CTAs documentada (formato documento), CTAs definidos para 3 categorías (Awareness, Consideration, Decision), Mensajes de CTAs escritos (mínimo 2 variantes por categoría), Ubicación de CTAs definida (dónde colocar en artículo), Documento entregado con ejemplos visuales, Aprobación de PM antes de usar en artículos
  - **INPUTS REQUERIDOS**: Matriz de intención (FM-49)
  - **DEPENDENCIAS**: FM-49 (matriz de intención)
  
- **FM-51**: Brief detallado para cada artículo (Story Points: 2, Priority: High)
  - **OBJETIVO**: Crear brief detallado para cada uno de los 15 artículos con título propuesto, keywords, estructura, CTAs y enlaces internos sugeridos.
  - **ENTREGABLES**: 15 briefs de artículos (uno por artículo), Título propuesto por artículo, Keywords primarias y secundarias, Estructura sugerida, CTAs específicos, Enlaces internos sugeridos
  - **ALCANCE**: Título propuesto (máximo 60 caracteres, optimizado SEO), Keywords primarias y secundarias (mínimo 1 primaria, 3 secundarias), Estructura sugerida (headings H2-H3, secciones), CTAs específicos (según categoría: Awareness/Consideration/Decision), Enlaces internos sugeridos (mínimo 3 por artículo), Word count objetivo (Awareness: 1,200, Consideration: 1,600, Decision: 2,000)
  - **CRITERIOS DE ACEPTACIÓN**: 15 briefs creados (uno por artículo), Cada brief incluye: título, keywords, estructura, CTAs, enlaces internos, word count, Keywords primarias y secundarias identificadas, Estructura sugerida documentada (mínimo 5 secciones por artículo), CTAs específicos definidos según categoría, Enlaces internos sugeridos (mínimo 3 por artículo), Documento entregado en formato Word/Google Docs, Aprobación de PM antes de iniciar producción
  - **INPUTS REQUERIDOS**: Keyword research (FM-47), Matriz de intención (FM-49), Estrategia de CTAs (FM-50)
  - **DEPENDENCIAS**: FM-47, FM-49, FM-50 (bloquea)

**Dependencies**: 
- FM-5 (Arquitectura de información)
- Lista de 20 SKUs principales (cliente)

---

### Story FM-10: 15 Artículos de Blog Especializados

**Story Key**: FM-10  
**Summary**: 15 artículos publicados y optimizados con CTAs directos a farmaciasmacross.com.mx  
**Investment**: $68,000 MXN  
**Estimate**: 4 semanas  
**Priority**: High

#### Tasks:
- **FM-2-2-1**: 4 artículos Awareness (1,200 palabras c/u) (Story Points: 8)
  - Condiciones médicas relacionadas a sus SKUs
  - Tratamientos disponibles en México
  - Navegación del sistema de salud
  - CTA: "Más información" → WhatsApp
  - SEO optimizado
  - Imágenes optimizadas (WebP)
  - Estructura H1-H6 correcta
  - Enlaces internos estratégicos
  - Schema markup de artículo médico
  - Tabla de contenido con jump links
  - Sección FAQ con schema
  - Disclaimers médicos en footer
  
- **FM-2-2-2**: 8 artículos Consideration (1,600 palabras c/u) (Story Points: 10)
  - Medicamentos especializados específicos
  - Comparativas de tratamientos
  - Acceso y disponibilidad en México
  - Casos de uso reales
  - CTA: "Consulta disponibilidad" → WhatsApp + botón a farmaciasmacross.com.mx
  - SEO optimizado
  - Imágenes optimizadas (WebP)
  - Estructura H1-H6 correcta
  - Enlaces internos estratégicos
  - Schema markup de artículo médico
  - Tabla de contenido con jump links
  - Sección FAQ con schema
  - Disclaimers médicos en footer
  
- **FM-2-2-3**: 3 artículos Decision (2,000 palabras c/u) (Story Points: 5)
  - Guías completas de medicamentos específicos (top 3 SKUs)
  - Costos y opciones realistas
  - Proceso de compra paso a paso
  - CTA: "Ver precio en farmacia" → DIRECTO a farmaciasmacross.com.mx
  - SEO optimizado
  - Imágenes optimizadas (WebP)
  - Estructura H1-H6 correcta
  - Enlaces internos estratégicos
  - Schema markup de artículo médico
  - Tabla de contenido con jump links
  - Sección FAQ con schema
  - Disclaimers médicos en footer
  
- **FM-2-2-4**: Publicación y optimización final (Story Points: 2)
  - Publicación en WordPress
  - Revisión de formato
  - Testing de CTAs
  - Validación de schema
  - Aprobación de cliente (3 artículos piloto primero)

**Dependencies**: 
- FM-9 (Research y estrategia)
- FM-6 (Sitio WordPress funcional)
- Aprobación de 3 artículos piloto (cliente, SLA 72h)

---

### Story FM-11: 2 Lead Magnets Enfocados

**Story Key**: FM-11  
**Summary**: 2 guías descargables en PDF con landing pages dedicadas e integración CRM  
**Investment**: $14,000 MXN  
**Estimate**: 2 semanas  
**Priority**: Medium

#### Tasks:
- **FM-2-3-1**: Guía 1 - "Guía del Paciente: Acceso a Medicamentos Especializados en México" (Story Points: 3)
  - Contenido (10-15 páginas)
  - Diseño branded profesional
  - PDF optimizado
  - Revisión médica
  
- **FM-2-3-2**: Guía 2 - "Tratamientos de Alta Especialidad: Opciones y Procesos" (Story Points: 3)
  - Contenido (10-15 páginas)
  - Diseño branded profesional
  - PDF optimizado
  - Revisión médica
  
- **FM-2-3-3**: Landing page para Guía 1 (Story Points: 1)
  - Diseño optimizado para conversión
  - Formulario de captura
  - Preview de contenido
  - SEO optimizado
  
- **FM-2-3-4**: Landing page para Guía 2 (Story Points: 1)
  - Diseño optimizado para conversión
  - Formulario de captura
  - Preview de contenido
  - SEO optimizado
  
- **FM-2-3-5**: Integración con CRM (Story Points: 1)
  - Formularios conectados a CRM
  - Campos personalizados
  - Automatización de entrega
  
- **FM-2-3-6**: Emails de entrega automatizados (Story Points: 1)
  - Email de bienvenida
  - Email con descarga
  - Seguimiento (opcional)

**Dependencies**: 
- FM-9 (Estrategia de contenido)
- FM-15 (CRM configurado) - puede hacerse en paralelo con integración posterior
- Información para lead magnets (cliente)

---

### Story FM-12: Optimización de Conversión

**Story Key**: FM-12  
**Summary**: Pop-ups estratégicos, banners, sticky bar, botón WhatsApp, A/B testing  
**Investment**: $6,000 MXN  
**Estimate**: 1 semana  
**Priority**: Medium

#### Tasks:
- **FM-2-4-1**: Pop-ups estratégicos (Story Points: 2)
  - Pop-up de salida
  - Pop-up de tiempo en página
  - Pop-up de scroll
  - Diseño y copy optimizados
  
- **FM-2-4-2**: Banners de anuncio interno (Story Points: 1)
  - Banners contextuales
  - Rotación de mensajes
  - CTAs claros
  
- **FM-2-4-3**: Sticky bar con CTA (Story Points: 1)
  - Barra fija superior/inferior
  - Mensaje contextual
  - CTA destacado
  
- **FM-2-4-4**: Botón flotante WhatsApp personalizado (Story Points: 1)
  - Diseño branded
  - Animación sutil
  - Mensaje pre-escrito
  - Tracking de clics
  
- **FM-2-4-5**: A/B testing configurado (Story Points: 1)
  - Setup de herramienta de testing
  - Variantes definidas
  - Métricas de conversión
  - Documentación de resultados

**Dependencies**: 
- FM-6 (Sitio WordPress)
- FM-10 (Artículos publicados)

---

## EPIC 3: FASE 3 - Sistema de Filtrado Automatizado

**Epic Key**: FM-3  
**Summary**: WhatsApp Business API, chatbot inteligente, CRM automatizado, integraciones  
**Timeline**: Semanas 10-15 (Feb-Mar 2026)  
**Investment**: $120,000 MXN  
**Status**: To Do

### Story FM-13: WhatsApp Business API - Implementación

**Story Key**: FM-13  
**Summary**: Configuración completa de WhatsApp Business API con proveedor  
**Investment**: $22,000 MXN  
**Estimate**: 1.5 semanas  
**Priority**: Highest

#### Tasks:
- **FM-3-1-1**: Selección y setup de proveedor (360 diálogo/Twilio) (Story Points: 1)
  - Evaluación de proveedores
  - Selección final
  - Creación de cuenta
  
- **FM-3-1-2**: Número telefónico dedicado registrado (Story Points: 1)
  - Obtención de número
  - Verificación de número
  - Configuración inicial
  
- **FM-3-1-3**: Verificación de negocio completada (Story Points: 2)
  - Documentos legales de empresa
  - Proceso de verificación WhatsApp
  - Aprobación de negocio
  
- **FM-3-1-4**: Templates de mensajes aprobados por WhatsApp (Story Points: 2)
  - Creación de 6 templates esenciales
  - Revisión de políticas WhatsApp
  - Envío para aprobación
  - Ajustes según feedback

**Dependencies**: 
- Número telefónico para WhatsApp Business (cliente, Semana 10)
- Documentos legales de empresa (cliente)

---

### Story FM-14: Chatbot Inteligente con Lógica de Filtrado

**Story Key**: FM-14  
**Summary**: Bot conversacional programado con lógica de filtrado automatizada  
**Investment**: $55,000 MXN  
**Estimate**: 3 semanas  
**Priority**: Highest

#### Tasks:
- **FM-3-2-1**: Flujo principal del bot (Story Points: 2)
  - Saludo inicial personalizado
  - Menú de opciones claro
  - Identificación de intención
  - Ruteo inteligente
  
- **FM-3-2-2**: Lógica de filtrado automatizada - Rama A (OTC/Genérico) (Story Points: 3)
  - Detección de intención OTC/Genérico
  - Respuesta: "Este medicamento lo encuentras en farmacias tradicionales"
  - Envío de link a Farmalisto/Similares
  - Ofrece ayuda adicional
  - Cierre de conversación (NO pasa a humano)
  
- **FM-3-2-3**: Lógica de filtrado automatizada - Rama B (SKUs especializados) (Story Points: 5)
  - Detección de uno de los 20 SKUs especializados
  - Respuesta: "Este medicamento lo manejamos"
  - Captura de datos esenciales:
    - Nombre completo
    - Medicamento específico
    - Ciudad/Estado
    - ¿Tiene receta? (Sí/No)
    - Email (opcional)
  - Creación de registro en CRM automático
  - Asignación a centro más cercano
  - Notificación a agente humano (Slack/Email/WhatsApp)
  - Mensaje: "Un especialista te atenderá en 15 minutos"
  
- **FM-3-2-4**: Inteligencia adicional (Story Points: 2)
  - Reconocimiento de nombres comerciales de 20 SKUs principales
  - Detección de urgencia (palabras clave)
  - Horarios de atención (fuera de horario = aviso automático)
  - Follow-up automático si no hay respuesta en 24h
  
- **FM-3-2-5**: Testing del bot (Story Points: 2)
  - 30+ escenarios de prueba realistas
  - Manejo de errores
  - Fallback a humano si bot no entiende
  - Testing de integraciones
  
- **FM-3-2-6**: Desarrollo técnico (Story Points: 3)
  - Node.js + WhatsApp API
  - Setup n8n o custom
  - Integración con CRM
  - Logging y monitoreo

**Dependencies**: 
- FM-13 (WhatsApp Business API configurado)
- FM-15 (CRM configurado) - puede desarrollarse en paralelo
- Lista de 20 SKUs con nombres comerciales (cliente)

---

### Story FM-15: CRM y Pipeline Automatizado

**Story Key**: FM-15  
**Summary**: CRM configurado con pipeline personalizado y automatizaciones  
**Investment**: $30,000 MXN  
**Estimate**: 2 semanas  
**Priority**: High

#### Tasks:
- **FM-3-3-1**: Setup de CRM (HubSpot CRM gratuito o Pipedrive) (Story Points: 1)
  - Creación de cuenta
  - Configuración inicial
  - Permisos y usuarios
  
- **FM-3-3-2**: Pipeline de ventas personalizado (Story Points: 1)
  - Stage 1: Lead Bot (automático)
  - Stage 2: Calificado
  - Stage 3: Link Shopify compartido
  - Stage 4: Esperando pago
  - Stage 5: Won/Lost + motivo
  
- **FM-3-3-3**: Custom fields (Story Points: 1)
  - Medicamento solicitado
  - Ciudad
  - Tiene receta (Sí/No)
  - Urgencia (Alta/Media/Baja)
  - Centro asignado
  - Precio cotizado
  - Link Shopify enviado
  
- **FM-3-3-4**: Automatizaciones configuradas (Story Points: 3)
  - Lead del bot → Crea deal automático
  - Asignación geográfica inteligente:
    - CDMX → Agente CDMX
    - Puebla → Agente Puebla
    - Otros → Round-robin
  - Notificaciones multicanal (email, Slack, WhatsApp)
  - Escalación si no hay respuesta en 15 min
  - Follow-ups programados (1 día, 3 días, 7 días)
  - Recordatorios de tareas
  
- **FM-3-3-5**: Integración bidireccional: WhatsApp ↔ CRM (Story Points: 2)
  - Sincronización de conversaciones
  - Actualización de registros
  - Historial completo

**Dependencies**: 
- Acceso a CRM (cliente decide HubSpot o Pipedrive)
- Información de centros y agentes (cliente)

---

### Story FM-16: Integración WordPress ↔ WhatsApp

**Story Key**: FM-16  
**Summary**: Todos los CTAs del sitio conectados a WhatsApp con tracking  
**Investment**: $12,000 MXN  
**Estimate**: 1 semana  
**Priority**: Medium

#### Tasks:
- **FM-3-4-1**: Conexión de CTAs a WhatsApp (Story Points: 2)
  - Todos los botones "Consultar vía WhatsApp"
  - Botón flotante
  - CTAs en artículos
  - CTAs en páginas de productos
  
- **FM-3-4-2**: Parámetros UTM para trackear origen (Story Points: 1)
  - UTM source (página específica)
  - UTM medium (WhatsApp)
  - UTM campaign (tipo de contenido)
  - UTM content (botón específico)
  
- **FM-3-4-3**: Pre-fill de información cuando sea posible (Story Points: 1)
  - Mensaje pre-escrito contextual
  - Ejemplo: "Hola, [Medicamento]. Quisiera consultar disponibilidad."
  - Adaptación según página de origen
  
- **FM-3-4-4**: Tracking de clics en Analytics (Story Points: 1)
  - Eventos en GA4
  - Eventos en GTM
  - Métricas de conversión
  - Reportes

**Dependencies**: 
- FM-6 (Sitio WordPress)
- FM-13 (WhatsApp Business API)
- FM-18 (GA4/GTM configurado) - puede hacerse en paralelo

---

### Story FM-17: Capacitación Operativa Completa

**Story Key**: FM-17  
**Summary**: Documentación y sesiones de capacitación para el equipo  
**Investment**: $13,000 MXN  
**Estimate**: 1 semana  
**Priority**: Medium

#### Tasks:
- **FM-3-5-1**: Documentación (Story Points: 2)
  - Manual de operación (20+ páginas)
  - Scripts de conversación para agentes
  - Guía de troubleshooting
  - FAQs operativas
  
- **FM-3-5-2**: Sesión 1 - Overview del sistema (2 horas) (Story Points: 1)
  - Arquitectura completa
  - Flujos principales
  - Roles y responsabilidades
  
- **FM-3-5-3**: Sesión 2 - Operación del CRM (2 horas) (Story Points: 1)
  - Navegación del CRM
  - Gestión de leads
  - Pipeline y etapas
  - Automatizaciones
  
- **FM-3-5-4**: Sesión 3 - WhatsApp y bot (1.5 horas) (Story Points: 1)
  - Funcionamiento del bot
  - Cuándo intervenir
  - Escalación a humano
  - Mejores prácticas
  
- **FM-3-5-5**: Sesión 4 - Role-playing y casos (1.5 horas) (Story Points: 1)
  - Simulación de conversaciones
  - Casos reales
  - Resolución de problemas
  - Q&A

**Dependencies**: 
- FM-14 (Bot funcional)
- FM-15 (CRM configurado)
- Equipo para capacitación (cliente, Semana 14-15)
- Disponibilidad para 4 sesiones (7 horas total)

---

## EPIC 4: FASE 4 - Setup Google Ads + Dashboards

**Epic Key**: FM-4  
**Summary**: Configuración Google Ads, Analytics, Tag Manager, Dashboard Looker Studio  
**Timeline**: Semanas 15-20 (Mar-May 2026) + Subfase 4.A adelantada (Semanas 4-10)  
**Investment**: $62,000 MXN  
**Status**: To Do

### Story FM-18: Google Ads y Analytics - Configuración Completa

**Story Key**: FM-18  
**Summary**: Cuenta Google Ads estructurada, GA4, GTM, 3 campañas base  
**Investment**: $45,000 MXN  
**Estimate**: 3 semanas  
**Priority**: High

#### Tasks:
- **FM-4-1-1**: Estructura de cuenta Google Ads (Story Points: 1)
  - Organización de campañas
  - Convenciones de nombres
  - Configuración de cuenta
  
- **FM-4-1-2**: Conversiones configuradas (5 tipos) (Story Points: 2)
  - Form submit
  - WhatsApp click
  - Lead magnet download
  - Shopify redirect
  - Custom conversions
  
- **FM-4-1-3**: Audiencias personalizadas (Story Points: 1)
  - Listas de remarketing (múltiples segmentos)
  - Audiencias similares
  - Exclusiones (negativas estratégicas)
  
- **FM-4-1-4**: Campaña 1 - Search Brand Protection (Story Points: 2)
  - Targeting: Keywords de marca
  - 2 ad groups, 8 keywords, 4 anuncios
  - Presupuesto sugerido: $80-120/día
  - Extensiones de anuncios
  - Negative keywords
  
- **FM-4-1-5**: Campaña 2 - Search Medicamentos Especializados (Story Points: 3)
  - Targeting: 5-10 SKUs principales + variaciones
  - 3 ad groups por categoría
  - 30 keywords enfocadas, 8 anuncios variados
  - Presupuesto sugerido: $300-500/día
  - Extensiones de anuncios
  - Negative keywords
  
- **FM-4-1-6**: Campaña 3 - Search Informacional + Display Remarketing (Story Points: 2)
  - Search: Términos educativos relacionados
  - Display: Audiencias de visitantes del sitio
  - 3 ad groups Search + 2 ad sets Display
  - 15 keywords + 10 banners (5 tamaños)
  - Presupuesto sugerido: $150-250/día combinado
  
- **FM-4-1-7**: Extensiones de anuncios configuradas (Story Points: 1)
  - Sitelinks (mínimo 8)
  - Callouts (mínimo 6)
  - Call extensions
  - Location extensions (CDMX, Puebla)
  
- **FM-4-1-8**: Negative keywords - Lista inicial de 100+ términos (Story Points: 1)
  - Genéricos de bajo valor
  - Términos de OTC
  - Búsquedas irrelevantes
  - Competencia
  
- **FM-4-1-9**: Configuración avanzada (Story Points: 2)
  - Bid strategies recomendadas por campaña
  - Ad scheduling (horarios óptimos)
  - Geo-targeting preciso (CDMX, Puebla, zonas de interés)
  - Device bid adjustments
  - Audience targeting por campaña
  
- **FM-4-1-10**: Scripts de automatización básicos (Story Points: 1)
  - Pausa de keywords con mal performance
  - Alertas de presupuesto
  - Reportes automáticos por email
  
- **FM-4-1-11**: Google Analytics 4 (Story Points: 3)
  - Instalación completa
  - Eventos custom configurados (10+ eventos)
  - Embudos de conversión mapeados
  - Integración con CRM
  - Reportes personalizados
  
- **FM-4-1-12**: Google Tag Manager (Story Points: 2)
  - Instalado y configurado
  - Tags de eventos importantes
  - Triggers optimizados
  - Variables personalizadas
  - Testing y debugging completado
  
- **FM-4-1-13**: Documento de mejores prácticas (20 páginas) (Story Points: 2)
  - Cómo interpretar métricas
  - Cuándo optimizar
  - Estrategias de puja
  - Testing de anuncios
  - Calendario de optimización sugerido

**Dependencies**: 
- FM-6 (Sitio WordPress funcional)
- FM-10 (Contenido publicado)
- Acceso a Google Ads (cliente, Semana 15)
- Acceso a Google Analytics (cliente)
- Decisión sobre presupuesto mensual (cliente)

---

### Story FM-19: Dashboard Unificado de Marketing

**Story Key**: FM-19  
**Summary**: Dashboard Looker Studio completo con todas las métricas del ecosistema  
**Investment**: $17,000 MXN  
**Estimate**: 2 semanas  
**Priority**: Medium

#### Tasks:
- **FM-4-2-1**: Sección 1 - Resumen Ejecutivo (Story Points: 1)
  - Inversión total del mes
  - Leads totales generados
  - CPL (Costo Por Lead)
  - Leads calificados por bot
  - Tasa de conversión bot
  - Clicks a farmaciasmacross.com.mx
  
- **FM-4-2-2**: Sección 2 - Tráfico del Sitio (Story Points: 1)
  - Visitas totales
  - Usuarios nuevos vs recurrentes
  - Tráfico por fuente (Orgánico, Google Ads, Directo, Referral)
  - Páginas más visitadas
  - Tiempo promedio en sitio
  - Tasa de rebote por fuente
  - Dispositivos (desktop, móvil, tablet)
  
- **FM-4-2-3**: Sección 3 - Performance Google Ads (Story Points: 2)
  - Inversión por campaña
  - Impresiones, clicks, CTR
  - CPC promedio
  - Conversiones por tipo
  - Costo por conversión
  - Quality Score promedio
  - Posición promedio
  - Search impression share
  - Mejores keywords (por conversiones)
  - Peores keywords (por costo sin conversión)
  
- **FM-4-2-4**: Sección 4 - Leads y WhatsApp (Story Points: 2)
  - Leads capturados por fuente
  - Conversaciones WhatsApp iniciadas
  - Leads calificados por el bot (por medicamento)
  - Leads descartados (por razón)
  - Tiempo promedio de respuesta del equipo
  - Conversión bot → humano (%)
  - Leads por centro (CDMX vs Puebla)
  
- **FM-4-2-5**: Sección 5 - SEO Orgánico (Story Points: 1)
  - Posiciones en Google Search Console
  - Clicks orgánicos
  - Impresiones orgánicas
  - CTR orgánico
  - Top queries
  - Top landing pages
  
- **FM-4-2-6**: Sección 6 - Conversión y Revenue (si integran) (Story Points: 1)
  - Clicks a Shopify
  - Conversión final (si proporcionan datos)
  - Revenue (si proporcionan datos)
  - ROAS estimado
  
- **FM-4-2-7**: Filtros interactivos (Story Points: 1)
  - Por fecha (hoy, ayer, últimos 7/30/90 días, mes actual/anterior)
  - Por campaña
  - Por centro de distribución
  - Por medicamento/SKU
  - Por fuente de tráfico
  
- **FM-4-2-8**: Configuración técnica (Story Points: 1)
  - Actualizaciones automáticas cada hora
  - Conexiones de datos (GA4, Google Ads, CRM)
  - Formato y diseño profesional
  
- **FM-4-2-9**: PDF guía de métricas (Story Points: 1)
  - Explicación de cada KPI
  - Cómo interpretar los datos
  - Acciones recomendadas

**Dependencies**: 
- FM-18 (Google Ads y Analytics configurados)
- FM-15 (CRM con datos)
- Acceso a Looker Studio (cliente)

---

### Story FM-20: Subfase 4.A - Ads Adelantado + Conversión Básica

**Story Key**: FM-20  
**Summary**: Estructura de campañas, keywords, conversiones básicas adelantadas para Hito 3  
**Investment**: $20,000 MXN  
**Estimate**: 2 semanas (Semanas 4-10, en paralelo con Fase 2)  
**Priority**: High

#### Tasks:
- **FM-113**: Estructura de cuenta y campañas (borrador) (Story Points: 1, Priority: Medium)
  - Organización preliminar
  - Convenciones de nombres
  - Estructura de carpetas
  
- **FM-114**: Keyword research (Story Points: 2, Priority: Medium)
  - Lista inicial de keywords
  - Agrupación por intención
  - Priorización
  
- **FM-115**: Listas de negativas iniciales (Story Points: 1, Priority: Medium)
  - Términos a excluir
  - Genéricos de bajo valor
  - Competencia
  
- **FM-116**: Configuración de conversiones clave en GA4/GTM para Ads (Story Points: 2, Priority: Medium)
  - WhatsApp click
  - Form submit
  - Lead magnet download
  - Clicks a tienda/productos
  - Testing de eventos

**Dependencies**: 
- FM-6 (Sitio WordPress funcional)
- FM-18 parcial (GA4/GTM básico)

---

### Story FM-21: Subfase 4.B - Optimización Ads + Shopping + Dashboards

**Story Key**: FM-21  
**Summary**: Afinación de campañas con datos reales, Shopping, Dashboard final  
**Investment**: $42,000 MXN  
**Estimate**: 3 semanas (Semanas 15-20, Hito 5)  
**Priority**: High

#### Tasks:
- **FM-117**: Afinación de campañas con datos reales (Story Points: 3, Priority: High)
  - Análisis de performance inicial
  - Optimización de pujas
  - Ajuste de keywords
  - Pausa de keywords no rentables
  - Expansión de keywords ganadoras
  
- **FM-118**: Configuración Shopping con SKUs aprobados (Story Points: 3, Priority: High)
  - Setup de Merchant Center
  - Feed de productos
  - Configuración de campaña Shopping
  - Solo productos aprobados
  - Testing y validación
  
- **FM-119**: Dashboard Looker Studio final (Story Points: 2, Priority: High)
  - Integración completa de todas las fuentes
  - Métricas consolidadas
  - Visualizaciones optimizadas
  - Filtros avanzados
  
- **FM-120**: Guía para lectura de métricas (Story Points: 1, Priority: Medium)
  - Documentación completa
  - Interpretación de KPIs
  - Acciones recomendadas
  - Sesión de walkthrough con cliente

**Dependencies**: 
- FM-18 (Campañas base funcionando)
- Datos reales de al menos 2 semanas de operación
- FM-19 (Dashboard base)

---

## Resumen de Epics

| Epic | Key                          | Fase | Duración  | Inversión | Prioridad | Tasks Vinculados          |
| ---- | ---------------------------- | ---- | --------- | --------- | --------- | ------------------------- |
| FM-1 | FASE 1 - WordPress Fachada   | 1    | 5 semanas | $80,000   | Highest   | FM-22 a FM-46 (25 tasks)  |
| FM-2 | FASE 2 - Contenido Educativo | 2    | 6 semanas | $102,000  | High      | FM-47 a FM-66 (20 tasks)  |
| FM-3 | FASE 3 - Sistema Filtrado    | 3    | 5 semanas | $120,000  | Highest   | FM-67 a FM-90 (24 tasks)  |
| FM-4 | FASE 4 - Ads + Dashboards    | 4    | 4 semanas | $62,000   | High      | FM-91 a FM-120 (30 tasks) |

**Total**: 20 semanas, $364,000 MXN

---

## Mapeo Completo Epic → Story → Task

### Epic FM-1 (FASE 1) - 25 Tasks
- **Story FM-5**: FM-22, FM-23, FM-24
- **Story FM-6**: FM-25, FM-26, FM-27, FM-28, FM-29, FM-30, FM-31, FM-32, FM-33, FM-34, FM-35
- **Story FM-7**: FM-36, FM-37, FM-38, FM-39, FM-40
- **Story FM-8**: FM-41, FM-42, FM-43, FM-44, FM-45, FM-46

### Epic FM-2 (FASE 2) - 20 Tasks
- **Story FM-9**: FM-47, FM-48, FM-49, FM-50, FM-51
- **Story FM-10**: FM-52, FM-53, FM-54, FM-55
- **Story FM-11**: FM-56, FM-57, FM-58, FM-59, FM-60, FM-61
- **Story FM-12**: FM-62, FM-63, FM-64, FM-65, FM-66

### Epic FM-3 (FASE 3) - 24 Tasks
- **Story FM-13**: FM-67, FM-68, FM-69, FM-70
- **Story FM-14**: FM-71, FM-72, FM-73, FM-74, FM-75, FM-76
- **Story FM-15**: FM-77, FM-78, FM-79, FM-80, FM-81
- **Story FM-16**: FM-82, FM-83, FM-84, FM-85
- **Story FM-17**: FM-86, FM-87, FM-88, FM-89, FM-90

### Epic FM-4 (FASE 4) - 30 Tasks
- **Story FM-18**: FM-91, FM-92, FM-93, FM-94, FM-95, FM-96, FM-97, FM-98, FM-99, FM-100, FM-101, FM-102, FM-103
- **Story FM-19**: FM-104, FM-105, FM-106, FM-107, FM-108, FM-109, FM-110, FM-111, FM-112
- **Story FM-20**: FM-113, FM-114, FM-115, FM-116
- **Story FM-21**: FM-117, FM-118, FM-119, FM-120

---

## Notas Importantes

1. **Trabajo en Paralelo**: Fases 1 y 2 pueden tener trabajo paralelo, especialmente en semanas 4-5
2. **Subfase 4.A**: Se adelanta durante Hito 3 (semanas 4-10) para tener estructura lista
3. **Dependencias Cliente**: Múltiples entregables requieren aprobación/input del cliente con SLA de 72h
4. **Cambios de Alcance**: Cualquier cambio fuera de scope debe pasar por proceso de change request
5. **Garantía**: 60 días técnica + 45 días soporte post-lanzamiento incluidos

