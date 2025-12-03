# Farmacias Macross - Sinergia Digital: Acceptance Criteria

**Project Key**: FM  
**Definition of Done (DoD)**: Cada entregable debe cumplir TODOS los criterios de aceptación listados para considerarse completo.

**Nota**: Este documento refleja los criterios de aceptación detallados para cada tarea en Jira. Todas las tareas (FM-22 a FM-120) incluyen:
- OBJETIVO claro
- ENTREGABLES medibles
- ALCANCE detallado
- CRITERIOS DE ACEPTACIÓN en formato checklist
- INPUTS REQUERIDOS
- DEPENDENCIAS
- ESTIMACIÓN (story points)
- PRIORIDAD

Para ver los detalles completos de cada tarea, consultar Jira o el archivo `farmacias-macross-epics.md`.

---

## EPIC 1: FASE 1 - WordPress Fachada para Compliance

### Story FM-5: Auditoría y Arquitectura de Información

**Story Key**: FM-5  
**Linked Tasks**: FM-22, FM-23, FM-24

#### Acceptance Criteria (consolidado de tareas FM-22, FM-23, FM-24):

**FM-22 - Auditoría técnica:**
- [ ] Documento entregado en formato PDF con índice navegable
- [ ] Mínimo 20 hallazgos documentados con evidencia
- [ ] Cada hallazgo incluye: descripción, impacto, prioridad, recomendación
- [ ] Matriz de priorización con al menos 5 items de alta prioridad
- [ ] Screenshots o capturas de pantalla para cada problema crítico
- [ ] Revisión técnica aprobada por PM antes de presentar a cliente

**FM-23 - Documento de análisis técnico:**
- [ ] Documento en formato PDF profesional con branding
- [ ] Resumen ejecutivo de máximo 1 página
- [ ] Mínimo 20 hallazgos documentados
- [ ] Cada hallazgo incluye: problema, impacto, esfuerzo estimado, recomendación
- [ ] Matriz de priorización con criterios claros (impacto vs esfuerzo)
- [ ] Roadmap sugerido con fases de implementación
- [ ] Aprobación de PM antes de entregar a cliente

**FM-24 - Arquitectura de información propuesta:**
- [ ] Sitemap visual entregado (Figma o PDF)
- [ ] Estructura de navegación documentada con justificación
- [ ] Taxonomía definida (mínimo 3 categorías blog, 2 tipos de productos)
- [ ] Mínimo 3 user journeys documentados (texto + diagrama)
- [ ] Wireframes de 8 páginas principales (baja fidelidad, pero completos)
- [ ] Cada wireframe incluye: estructura, CTAs principales, elementos clave
- [ ] Revisión y aprobación de PM antes de presentar a cliente
- [ ] Feedback del cliente en máximo 72 horas (SLA)

---

### Story FM-6: Sitio WordPress Rediseñado

**Story Key**: FM-6  
**Linked Tasks**: FM-25, FM-26, FM-27, FM-28, FM-29, FM-30, FM-31, FM-32, FM-33, FM-34, FM-35

#### Acceptance Criteria (consolidado de tareas FM-25 a FM-35):

**FM-25 - Setup WordPress:**
- [ ] WordPress versión estable instalada (mínimo 6.0+)
- [ ] Mínimo 5 plugins esenciales instalados y activos
- [ ] Tema base configurado y funcional
- [ ] Accesos de desarrollo creados (admin, editor)
- [ ] Backup inicial realizado y verificado
- [ ] Documento técnico de configuración entregado (formato checklist)
- [ ] Sitio accesible y sin errores críticos en consola
- [ ] Revisión técnica aprobada por desarrollador senior

**FM-26 - Diseño responsivo base:**
- [ ] Sistema de colores definido (mínimo 5 colores: primario, secundario, texto, fondo, acento)
- [ ] Tipografía definida (mínimo 2 fuentes: heading, body)
- [ ] Espaciado consistente (sistema de 8px o similar)
- [ ] Mínimo 8 componentes reutilizables creados (botón, card, input, CTA, etc.)
- [ ] Breakpoints documentados y testeados
- [ ] Testing de responsividad completado en: Chrome DevTools (3 tamaños), dispositivo móvil real
- [ ] Documento de guía de estilos entregado (Figma library o PDF)
- [ ] Aprobación de diseño por PM antes de desarrollo

**FM-27 - Homepage:**
- [ ] Homepage desarrollada y publicada en WordPress
- [ ] Hero section con imagen optimizada (máximo 200KB, formato WebP)
- [ ] Mínimo 3 secciones de valor con contenido relevante
- [ ] Mínimo 2 CTAs principales funcionales
- [ ] Botón flotante WhatsApp instalado y funcional
- [ ] Mensaje pre-escrito configurado: "Hola, quisiera consultar disponibilidad de medicamentos especializados"
- [ ] Testing de responsividad completado (desktop, tablet, móvil)
- [ ] PageSpeed score mínimo 80 (móvil) y 90 (desktop)
- [ ] Sin errores en consola del navegador
- [ ] Aprobación de cliente (SLA: 72 horas para feedback)

**FM-28 - Página Sobre Nosotros:**
- [ ] Página desarrollada y publicada en WordPress
- [ ] Contenido sobre empresa (mínimo 300 palabras, máximo 500)
- [ ] Información completa de 2 centros (CDMX y Puebla): dirección, horarios, teléfono
- [ ] Mapa interactivo funcional con 2 marcadores
- [ ] Formulario de contacto funcional (mínimo 5 campos)
- [ ] Formulario envía email de notificación al enviar
- [ ] Testing de responsividad completado
- [ ] Imágenes optimizadas (máximo 300KB cada una, formato WebP)
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-29 - Template de Blog:**
- [ ] Template de blog posts desarrollado y funcional
- [ ] Sistema de categorías configurado (mínimo 3 categorías)
- [ ] Sistema de tags configurado y funcional
- [ ] Sidebar con mínimo 3 widgets (búsqueda, categorías, posts recientes)
- [ ] Paginación funcional (anterior/siguiente + números)
- [ ] Schema markup Article implementado y validado
- [ ] Breadcrumbs implementados
- [ ] Testing con 3 posts de prueba completado
- [ ] Aprobación de PM antes de usar para artículos reales

**FM-30 - Página Catálogo OTC:**
- [ ] Página catálogo desarrollada y publicada
- [ ] Grid de productos funcional (mínimo 20 productos mostrados)
- [ ] Sistema de filtros funcional (mínimo 2 filtros: categoría, disponibilidad)
- [ ] Búsqueda funcional (búsqueda en tiempo real o con botón)
- [ ] Enlaces externos configurados (mínimo 20 productos con links)
- [ ] UTM parameters configurados en todos los enlaces externos
- [ ] Enlaces abren en nueva pestaña (target="_blank")
- [ ] Tracking de clics configurado en GA4/GTM
- [ ] Testing de responsividad completado
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-31 - Landing Consulta Especializada:**
- [ ] Landing page desarrollada y publicada
- [ ] Hero section con headline claro y CTA principal
- [ ] Formulario funcional con mínimo 5 campos
- [ ] Formulario envía email de notificación al enviar
- [ ] Mínimo 2 CTAs a WhatsApp funcionales
- [ ] Mensaje pre-escrito configurado correctamente
- [ ] Información sobre proceso (mínimo 3 pasos explicados)
- [ ] Tracking de conversiones configurado (form submit, WhatsApp click en GA4)
- [ ] Testing de responsividad completado
- [ ] PageSpeed score mínimo 80 (móvil)
- [ ] A/B testing configurado (opcional, pero recomendado)
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-32 - Página FAQ:**
- [ ] Página FAQ desarrollada y publicada
- [ ] Mínimo 10 preguntas frecuentes con respuestas completas
- [ ] Mínimo 3 categorías de preguntas
- [ ] Accordion interactivo funcional (expandir/colapsar)
- [ ] Schema markup FAQPage implementado
- [ ] Validación de schema con Google Rich Results Test (sin errores)
- [ ] SEO optimizado (meta title, meta description, headings)
- [ ] Testing de responsividad completado
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-33 - Páginas legales:**
- [ ] Aviso de Privacidad desarrollado y publicado (mínimo 8 secciones)
- [ ] Términos y Condiciones desarrollados y publicados (mínimo 6 secciones)
- [ ] Política de Cookies desarrollada y publicada
- [ ] Disclaimers médicos en footer de todas las páginas
- [ ] Links a páginas legales en footer funcionales
- [ ] Revisión legal completada (o documentación de cumplimiento)
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-34 - Página Contacto:**
- [ ] Página contacto desarrollada y publicada
- [ ] Formulario funcional con mínimo 5 campos
- [ ] Formulario envía email de notificación al enviar
- [ ] Información de contacto completa (teléfono, email, direcciones)
- [ ] Mapa interactivo funcional con marcadores
- [ ] Horarios de atención documentados por centro
- [ ] Testing de responsividad completado
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-35 - Optimización de velocidad:**
- [ ] PageSpeed score mínimo 80 (móvil) y 90 (desktop)
- [ ] Todas las imágenes optimizadas (formato WebP, máximo 200KB por imagen)
- [ ] Lazy loading implementado en imágenes
- [ ] Caching configurado y funcional
- [ ] CSS/JS minificados
- [ ] CDN configurado (si aplica)
- [ ] Reporte de performance antes/después entregado
- [ ] Testing completado en PageSpeed Insights y GTmetrix
- [ ] Aprobación de PM antes de considerar completo

---

### Story FM-7: Catálogo Fachada OTC - 20 Productos

**Story Key**: FM-7  
**Linked Tasks**: FM-36, FM-37, FM-38, FM-39, FM-40

#### Acceptance Criteria (consolidado de tareas FM-36 a FM-40):

**FM-36 - Template de producto OTC:**
- [ ] Template desarrollado y funcional en WordPress
- [ ] Custom Post Type o ACF configurado para productos OTC
- [ ] Mínimo 8 campos personalizados (nombre, descripción, beneficios, advertencias, precio, enlace externo, imagen, categoría)
- [ ] Template responsivo (desktop, tablet, móvil)
- [ ] Testing con 1 producto de prueba completado
- [ ] Documentación del template entregada (cómo usar, qué campos llenar)
- [ ] Aprobación de PM antes de crear las 20 páginas

**FM-37 - Creación de 20 páginas de productos:**
- [ ] 20 páginas de productos OTC creadas y publicadas
- [ ] Cada página tiene descripción de 250-300 palabras
- [ ] Cada página tiene mínimo 3 beneficios documentados
- [ ] Cada página tiene advertencias/disclaimers médicos
- [ ] CTA primario configurado en todas las páginas (enlace externo)
- [ ] CTA secundario configurado en todas las páginas (WhatsApp)
- [ ] Imágenes optimizadas (WebP, máximo 200KB cada una)
- [ ] Schema markup Product implementado y validado en todas las páginas
- [ ] Testing de responsividad completado (3 dispositivos)
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-38 - Schema markup de producto:**
- [ ] Schema markup Product implementado en las 20 páginas
- [ ] Validación de schema con Google Rich Results Test (sin errores)
- [ ] Mínimo 5 campos requeridos por producto (name, description, image, price, availability)
- [ ] Testing completado en 3 páginas de muestra
- [ ] Documentación de implementación entregada
- [ ] Aprobación de PM antes de considerar completo

**FM-39 - SEO optimizado por producto:**
- [ ] Meta titles configurados en las 20 páginas (máximo 60 caracteres)
- [ ] Meta descriptions configuradas en las 20 páginas (máximo 160 caracteres)
- [ ] Headings H1-H6 correctos (1 H1, estructura lógica)
- [ ] Alt text en todas las imágenes (descriptivo, sin "imagen de")
- [ ] URLs amigables configuradas (slug optimizado)
- [ ] Mínimo 3 enlaces internos por página
- [ ] Keywords primarias y secundarias identificadas y usadas
- [ ] Testing de SEO completado (Yoast o Rank Math sin errores críticos)
- [ ] Aprobación de PM antes de considerar completo

**FM-40 - Integración con enlaces externos:**
- [ ] Enlaces externos configurados en las 20 páginas
- [ ] UTM parameters configurados en todos los enlaces (source, medium, campaign, content)
- [ ] Enlaces abren en nueva pestaña (target="_blank")
- [ ] Tracking de clics configurado en GA4/GTM
- [ ] Evento "external_link_click" configurado en GTM
- [ ] Testing de clics completado (verificar que UTM se pasa correctamente)
- [ ] Aprobación de PM antes de considerar completo

---

### Story FM-8: SEO Técnico + Compliance Legal

**Story Key**: FM-8  
**Linked Tasks**: FM-41, FM-42, FM-43, FM-44, FM-45, FM-46

#### Acceptance Criteria (consolidado de tareas FM-41 a FM-46):

**FM-41 - SEO on-page completo:**
- [ ] Meta tags optimizados en todas las páginas (mínimo 15 páginas)
- [ ] Headings structure corregida (1 H1 por página, jerarquía lógica)
- [ ] Internal linking implementado (mínimo 3 enlaces internos por página)
- [ ] Todas las imágenes tienen alt text descriptivo
- [ ] URLs amigables configuradas (sin caracteres especiales)
- [ ] Sitemap XML generado y actualizado
- [ ] Testing de SEO completado (Yoast o Rank Math sin errores críticos)
- [ ] Aprobación de PM antes de considerar completo

**FM-42 - Schema markup especializado:**
- [ ] Schema Organization implementado y validado
- [ ] Schema LocalBusiness implementado para 2 centros (CDMX, Puebla)
- [ ] Schema MedicalBusiness implementado y validado
- [ ] Schema Product implementado en 20 productos (ya completado en FM-38)
- [ ] Schema BreadcrumbList implementado en todas las páginas
- [ ] Validación de todos los schemas con Google Rich Results Test (sin errores)
- [ ] Testing completado en 5 páginas de muestra
- [ ] Documentación de implementación entregada
- [ ] Aprobación de PM antes de considerar completo

**FM-43 - Sitemap XML multinivel:**
- [ ] Sitemap XML generado (mínimo 25 URLs)
- [ ] Prioridades configuradas (homepage: 1.0, páginas principales: 0.8)
- [ ] Frecuencias configuradas (homepage: daily, páginas principales: weekly)
- [ ] Sitemap submit a Google Search Console
- [ ] Verificación de que Google indexa el sitemap (sin errores)
- [ ] Documentación de configuración entregada
- [ ] Aprobación de PM antes de considerar completo

**FM-44 - Robots.txt optimizado:**
- [ ] robots.txt creado y publicado en raíz del sitio
- [ ] Configuración de crawlers (User-agent: *, Allow, Disallow)
- [ ] Exclusiones configuradas (wp-admin, archivos privados)
- [ ] Referencia al sitemap configurada (Sitemap: URL)
- [ ] Testing de robots.txt completado (verificar con Google Search Console)
- [ ] Documentación de configuración entregada
- [ ] Aprobación de PM antes de considerar completo

**FM-45 - Documentos legales health-compliant:**
- [ ] Aviso de Privacidad desarrollado (mínimo 8 secciones requeridas)
- [ ] Términos y Condiciones desarrollados (mínimo 6 secciones)
- [ ] Disclaimers médicos en las 20 páginas de productos
- [ ] Política de cookies desarrollada y publicada
- [ ] Revisión legal completada (o documentación de cumplimiento)
- [ ] Links a documentos legales en footer funcionales
- [ ] Aprobación de cliente (SLA: 72 horas)

**FM-46 - Configuración Google Search Console:**
- [ ] Google Search Console configurado y verificado
- [ ] Sitemap submit completado (sitemap.xml)
- [ ] Configuración de parámetros URL (mínimo 3 parámetros configurados)
- [ ] Monitoreo inicial configurado (alertas, errores)
- [ ] Testing de indexación completado (verificar que Google indexa páginas)
- [ ] Documentación de configuración entregada
- [ ] Aprobación de PM antes de considerar completo

---

## EPIC 2: FASE 2 - Contenido Educativo Estratégico

### Story FM-9: Research y Estrategia de Contenido

**Story Key**: FM-9  
**Linked Tasks**: FM-47, FM-48, FM-49, FM-50, FM-51

#### Acceptance Criteria (consolidado de tareas FM-47 a FM-51):

**FM-47 - Keyword research especializado:**
- [ ] Mínimo 100 keywords identificadas y documentadas
- [ ] Cada keyword incluye: término, volumen mensual, dificultad SEO, intención, competencia
- [ ] Keywords agrupadas por categorías (mínimo 5 categorías)
- [ ] Análisis de competencia completado (top 10 resultados analizados)
- [ ] Documento entregado en formato Excel/Sheets con columnas: Keyword, Volumen, Dificultad, Intención, Competencia, Categoría
- [ ] Keywords priorizadas (top 30 identificadas)
- [ ] Aprobación de PM antes de usar para content calendar

**FM-48 - Content calendar 6 meses:**
- [ ] Content calendar creado (formato calendario, 6 meses)
- [ ] Frecuencia de publicación definida (mínimo 2 artículos/mes)
- [ ] Temas asignados por mes (mínimo 2 temas/mes)
- [ ] Alineación con campañas Google Ads documentada
- [ ] Fechas sugeridas de publicación definidas
- [ ] Documento entregado en formato Excel/Sheets o calendario visual
- [ ] Aprobación de PM antes de usar para producción de contenido

**FM-49 - Matriz de intención de búsqueda:**
- [ ] Matriz creada con mínimo 50 keywords clasificadas
- [ ] Cada keyword tiene intención asignada (Awareness/Consideration/Decision)
- [ ] Mapeo de keywords a artículos completado (mínimo 15 artículos mapeados)
- [ ] Priorización documentada (top 30 keywords identificadas)
- [ ] Justificación de clasificación incluida
- [ ] Documento entregado en formato Excel/Sheets
- [ ] Aprobación de PM antes de usar para briefs de artículos

**FM-50 - Estrategia de CTAs por categoría:**
- [ ] Estrategia de CTAs documentada (formato documento)
- [ ] CTAs definidos para 3 categorías (Awareness, Consideration, Decision)
- [ ] Mensajes de CTAs escritos (mínimo 2 variantes por categoría)
- [ ] Ubicación de CTAs definida (dónde colocar en artículo)
- [ ] Documento entregado con ejemplos visuales
- [ ] Aprobación de PM antes de usar en artículos

**FM-51 - Brief detallado para cada artículo:**
- [ ] 15 briefs creados (uno por artículo)
- [ ] Cada brief incluye: título, keywords, estructura, CTAs, enlaces internos, word count
- [ ] Keywords primarias y secundarias identificadas
- [ ] Estructura sugerida documentada (mínimo 5 secciones por artículo)
- [ ] CTAs específicos definidos según categoría
- [ ] Enlaces internos sugeridos (mínimo 3 por artículo)
- [ ] Documento entregado en formato Word/Google Docs
- [ ] Aprobación de PM antes de iniciar producción

---

### Story FM-10: 15 Artículos de Blog Especializados

**Story Key**: FM-10  
**Linked Tasks**: FM-52, FM-53, FM-54, FM-55

#### Acceptance Criteria:
- [ ] **AC-2-2-1**: 4 artículos Awareness publicados
  - Cada artículo tiene mínimo 1,200 palabras
  - Temas: Condiciones médicas, tratamientos disponibles, sistema de salud
  - CTA: "Más información" → WhatsApp funcional
  - SEO optimizado (meta, headings, alt text)
  - Imágenes optimizadas (WebP, <150KB cada una)
  - Estructura H1-H6 correcta
  - Mínimo 5 enlaces internos estratégicos
  - Schema markup de artículo médico implementado
  - Tabla de contenido con jump links funcional
  - Sección FAQ con schema (mínimo 3 preguntas)
  - Disclaimers médicos en footer
  
- [ ] **AC-2-2-2**: 8 artículos Consideration publicados
  - Cada artículo tiene mínimo 1,600 palabras
  - Temas: Medicamentos especializados, comparativas, acceso, casos de uso
  - CTA: "Consulta disponibilidad" → WhatsApp + botón a farmaciasmacross.com.mx funcional
  - SEO optimizado (meta, headings, alt text)
  - Imágenes optimizadas (WebP, <150KB cada una)
  - Estructura H1-H6 correcta
  - Mínimo 7 enlaces internos estratégicos
  - Schema markup de artículo médico implementado
  - Tabla de contenido con jump links funcional
  - Sección FAQ con schema (mínimo 5 preguntas)
  - Disclaimers médicos en footer
  
- [ ] **AC-2-2-3**: 3 artículos Decision publicados
  - Cada artículo tiene mínimo 2,000 palabras
  - Temas: Guías completas de top 3 SKUs, costos, proceso de compra
  - CTA: "Ver precio en farmacia" → DIRECTO a farmaciasmacross.com.mx funcional
  - SEO optimizado (meta, headings, alt text)
  - Imágenes optimizadas (WebP, <150KB cada una)
  - Estructura H1-H6 correcta
  - Mínimo 10 enlaces internos estratégicos
  - Schema markup de artículo médico implementado
  - Tabla de contenido con jump links funcional
  - Sección FAQ con schema (mínimo 7 preguntas)
  - Disclaimers médicos en footer
  
- [ ] **AC-2-2-4**: Publicación y optimización final
  - Todos los artículos publicados en WordPress
  - Formato consistente en todos los artículos
  - CTAs funcionando correctamente
  - Schema validado sin errores
  - Aprobación del cliente recibida (3 artículos piloto primero)

---

### Story FM-11: 2 Lead Magnets Enfocados

**Story Key**: FM-11  
**Linked Tasks**: FM-56, FM-57, FM-58, FM-59, FM-60, FM-61

#### Acceptance Criteria:
- [ ] **AC-2-3-1**: Guía 1 - "Guía del Paciente: Acceso a Medicamentos Especializados en México"
  - Contenido completo (10-15 páginas)
  - Diseño branded profesional
  - PDF optimizado (<5MB)
  - Revisión médica completada
  - Sin errores ortográficos o gramaticales
  
- [ ] **AC-2-3-2**: Guía 2 - "Tratamientos de Alta Especialidad: Opciones y Procesos"
  - Contenido completo (10-15 páginas)
  - Diseño branded profesional
  - PDF optimizado (<5MB)
  - Revisión médica completada
  - Sin errores ortográficos o gramaticales
  
- [ ] **AC-2-3-3**: Landing page para Guía 1
  - Diseño optimizado para conversión
  - Formulario de captura funcional
  - Preview de contenido visible
  - SEO optimizado
  - Tasa de conversión objetivo >15%
  
- [ ] **AC-2-3-4**: Landing page para Guía 2
  - Diseño optimizado para conversión
  - Formulario de captura funcional
  - Preview de contenido visible
  - SEO optimizado
  - Tasa de conversión objetivo >15%
  
- [ ] **AC-2-3-5**: Integración con CRM
  - Formularios conectados a CRM
  - Campos personalizados configurados
  - Automatización de entrega funcionando
  - Datos sincronizados correctamente
  
- [ ] **AC-2-3-6**: Emails de entrega automatizados
  - Email de bienvenida configurado
  - Email con descarga funcionando
  - PDF adjunto o link de descarga funcional
  - Testing de envío completado

---

### Story FM-12: Optimización de Conversión

**Story Key**: FM-12  
**Linked Tasks**: FM-62, FM-63, FM-64, FM-65, FM-66

#### Acceptance Criteria:
- [ ] **AC-2-4-1**: Pop-ups estratégicos implementados
  - Pop-up de salida configurado
  - Pop-up de tiempo en página configurado
  - Pop-up de scroll configurado
  - Diseño y copy optimizados
  - CTAs funcionando
  - Testing de funcionamiento completado
  
- [ ] **AC-2-4-2**: Banners de anuncio interno
  - Banners contextuales implementados
  - Rotación de mensajes configurada
  - CTAs claros y funcionales
  - Diseño consistente con marca
  
- [ ] **AC-2-4-3**: Sticky bar con CTA
  - Barra fija superior o inferior implementada
  - Mensaje contextual configurado
  - CTA destacado y funcional
  - No interfiere con contenido
  
- [ ] **AC-2-4-4**: Botón flotante WhatsApp personalizado
  - Diseño branded implementado
  - Animación sutil configurada
  - Mensaje pre-escrito funcional
  - Tracking de clics implementado
  - Visible en todas las páginas relevantes
  
- [ ] **AC-2-4-5**: A/B testing configurado
  - Herramienta de testing instalada
  - Variantes definidas (mínimo 2 por elemento)
  - Métricas de conversión configuradas
  - Documentación de setup completada
  - Plan de análisis definido

---

## EPIC 3: FASE 3 - Sistema de Filtrado Automatizado

### Story FM-13: WhatsApp Business API - Implementación

**Story Key**: FM-13  
**Linked Tasks**: FM-67, FM-68, FM-69, FM-70

#### Acceptance Criteria:
- [ ] **AC-3-1-1**: Proveedor seleccionado y configurado
  - Proveedor elegido (360 diálogo/Twilio)
  - Cuenta creada y verificada
  - Accesos configurados
  
- [ ] **AC-3-1-2**: Número telefónico dedicado registrado
  - Número obtenido y verificado
  - Verificación de número completada
  - Configuración inicial funcional
  
- [ ] **AC-3-1-3**: Verificación de negocio completada
  - Documentos legales de empresa enviados
  - Proceso de verificación WhatsApp iniciado
  - Aprobación de negocio recibida
  - Estado verificado en dashboard
  
- [ ] **AC-3-1-4**: Templates de mensajes aprobados
  - 6 templates esenciales creados
  - Revisión de políticas WhatsApp completada
  - Envío para aprobación realizado
  - Aprobación recibida para todos los templates
  - Templates listos para usar

---

### Story FM-14: Chatbot Inteligente con Lógica de Filtrado

**Story Key**: FM-14  
**Linked Tasks**: FM-71, FM-72, FM-73, FM-74, FM-75, FM-76

#### Acceptance Criteria:
- [ ] **AC-3-2-1**: Flujo principal del bot funcional
  - Saludo inicial personalizado implementado
  - Menú de opciones claro y funcional
  - Identificación de intención funcionando
  - Ruteo inteligente operativo
  
- [ ] **AC-3-2-2**: Lógica Rama A - OTC/Genérico funcionando
  - Detección de intención OTC/Genérico precisa (>90% accuracy)
  - Respuesta: "Este medicamento lo encuentras en farmacias tradicionales"
  - Envío de link a Farmalisto/Similares funcionando
  - Ofrece ayuda adicional
  - Cierre de conversación sin escalar a humano
  - Testing de 10+ escenarios completado
  
- [ ] **AC-3-2-3**: Lógica Rama B - SKUs especializados funcionando
  - Detección de uno de los 20 SKUs especializados precisa (>95% accuracy)
  - Respuesta: "Este medicamento lo manejamos"
  - Captura de datos esenciales:
    - Nombre completo (validado)
    - Medicamento específico (confirmado)
    - Ciudad/Estado (validado)
    - ¿Tiene receta? (Sí/No) (capturado)
    - Email (opcional) (validado si se proporciona)
  - Creación de registro en CRM automático funcionando
  - Asignación a centro más cercano funcionando
  - Notificación a agente humano funcionando (Slack/Email/WhatsApp)
  - Mensaje: "Un especialista te atenderá en 15 minutos" enviado
  - Testing de 15+ escenarios completado
  
- [ ] **AC-3-2-4**: Inteligencia adicional implementada
  - Reconocimiento de nombres comerciales de 20 SKUs principales (>90% accuracy)
  - Detección de urgencia (palabras clave) funcionando
  - Horarios de atención configurados (fuera de horario = aviso automático)
  - Follow-up automático si no hay respuesta en 24h funcionando
  
- [ ] **AC-3-2-5**: Testing del bot completado
  - 30+ escenarios de prueba realistas ejecutados
  - Manejo de errores probado
  - Fallback a humano si bot no entiende funcionando
  - Testing de integraciones completado
  - Documentación de resultados
  
- [ ] **AC-3-2-6**: Desarrollo técnico completado
  - Node.js + WhatsApp API funcionando
  - Setup n8n o custom operativo
  - Integración con CRM funcionando
  - Logging y monitoreo implementados
  - Documentación técnica completada

---

### Story FM-15: CRM y Pipeline Automatizado

**Story Key**: FM-15  
**Linked Tasks**: FM-77, FM-78, FM-79, FM-80, FM-81

#### Acceptance Criteria:
- [ ] **AC-3-3-1**: CRM configurado
  - Cuenta creada (HubSpot CRM gratuito o Pipedrive)
  - Configuración inicial completada
  - Permisos y usuarios configurados
  
- [ ] **AC-3-3-2**: Pipeline de ventas personalizado
  - Stage 1: Lead Bot (automático) configurado
  - Stage 2: Calificado configurado
  - Stage 3: Link Shopify compartido configurado
  - Stage 4: Esperando pago configurado
  - Stage 5: Won/Lost + motivo configurado
  - Transiciones entre etapas funcionando
  
- [ ] **AC-3-3-3**: Custom fields creados
  - Medicamento solicitado (campo personalizado)
  - Ciudad (campo personalizado)
  - Tiene receta (Sí/No) (campo personalizado)
  - Urgencia (Alta/Media/Baja) (campo personalizado)
  - Centro asignado (campo personalizado)
  - Precio cotizado (campo personalizado)
  - Link Shopify enviado (campo personalizado)
  
- [ ] **AC-3-3-4**: Automatizaciones configuradas
  - Lead del bot → Crea deal automático funcionando
  - Asignación geográfica inteligente:
    - CDMX → Agente CDMX funcionando
    - Puebla → Agente Puebla funcionando
    - Otros → Round-robin funcionando
  - Notificaciones multicanal (email, Slack, WhatsApp) funcionando
  - Escalación si no hay respuesta en 15 min funcionando
  - Follow-ups programados (1 día, 3 días, 7 días) funcionando
  - Recordatorios de tareas funcionando
  
- [ ] **AC-3-3-5**: Integración bidireccional funcionando
  - Sincronización de conversaciones WhatsApp ↔ CRM
  - Actualización de registros automática
  - Historial completo visible en CRM
  - Testing de sincronización completado

---

### Story FM-16: Integración WordPress ↔ WhatsApp

**Story Key**: FM-16  
**Linked Tasks**: FM-82, FM-83, FM-84, FM-85

#### Acceptance Criteria:
- [ ] **AC-3-4-1**: CTAs conectados a WhatsApp
  - Todos los botones "Consultar vía WhatsApp" funcionando
  - Botón flotante funcionando
  - CTAs en artículos funcionando
  - CTAs en páginas de productos funcionando
  
- [ ] **AC-3-4-2**: Parámetros UTM implementados
  - UTM source (página específica) funcionando
  - UTM medium (WhatsApp) funcionando
  - UTM campaign (tipo de contenido) funcionando
  - UTM content (botón específico) funcionando
  - Tracking en Analytics funcionando
  
- [ ] **AC-3-4-3**: Pre-fill de información funcionando
  - Mensaje pre-escrito contextual implementado
  - Ejemplo: "Hola, [Medicamento]. Quisiera consultar disponibilidad." funcionando
  - Adaptación según página de origen funcionando
  - Testing en diferentes páginas completado
  
- [ ] **AC-3-4-4**: Tracking de clics en Analytics
  - Eventos en GA4 configurados y funcionando
  - Eventos en GTM configurados y funcionando
  - Métricas de conversión visibles
  - Reportes generados

---

### Story FM-17: Capacitación Operativa Completa

**Story Key**: FM-17  
**Linked Tasks**: FM-86, FM-87, FM-88, FM-89, FM-90

#### Acceptance Criteria:
- [ ] **AC-3-5-1**: Documentación entregada
  - Manual de operación (20+ páginas) entregado
  - Scripts de conversación para agentes entregados
  - Guía de troubleshooting entregada
  - FAQs operativas entregadas
  - Formato PDF y Word disponible
  
- [ ] **AC-3-5-2**: Sesión 1 - Overview del sistema completada
  - Duración: 2 horas
  - Arquitectura completa explicada
  - Flujos principales demostrados
  - Roles y responsabilidades definidos
  - Q&A completado
  - Asistencia mínima: 80% del equipo
  
- [ ] **AC-3-5-3**: Sesión 2 - Operación del CRM completada
  - Duración: 2 horas
  - Navegación del CRM demostrada
  - Gestión de leads practicada
  - Pipeline y etapas explicadas
  - Automatizaciones demostradas
  - Q&A completado
  - Asistencia mínima: 80% del equipo
  
- [ ] **AC-3-5-4**: Sesión 3 - WhatsApp y bot completada
  - Duración: 1.5 horas
  - Funcionamiento del bot explicado
  - Cuándo intervenir definido
  - Escalación a humano practicada
  - Mejores prácticas compartidas
  - Q&A completado
  - Asistencia mínima: 80% del equipo
  
- [ ] **AC-3-5-5**: Sesión 4 - Role-playing y casos completada
  - Duración: 1.5 horas
  - Simulación de conversaciones practicada
  - Casos reales resueltos
  - Resolución de problemas practicada
  - Q&A final completado
  - Asistencia mínima: 80% del equipo
  - Evaluación de comprensión completada

---

## EPIC 4: FASE 4 - Setup Google Ads + Dashboards

### Story FM-18: Google Ads y Analytics - Configuración Completa

**Story Key**: FM-18  
**Linked Tasks**: FM-91, FM-92, FM-93, FM-94, FM-95, FM-96, FM-97, FM-98, FM-99, FM-100, FM-101, FM-102, FM-103

#### Acceptance Criteria:
- [ ] **AC-4-1-1**: Estructura de cuenta Google Ads
  - Organización de campañas clara
  - Convenciones de nombres definidas
  - Configuración de cuenta completada
  
- [ ] **AC-4-1-2**: Conversiones configuradas
  - Form submit (conversión configurada)
  - WhatsApp click (conversión configurada)
  - Lead magnet download (conversión configurada)
  - Shopify redirect (conversión configurada)
  - Custom conversions adicionales configuradas
  - Testing de conversiones completado
  
- [ ] **AC-4-1-3**: Audiencias personalizadas
  - Listas de remarketing (múltiples segmentos) creadas
  - Audiencias similares configuradas
  - Exclusiones (negativas estratégicas) configuradas
  
- [ ] **AC-4-1-4**: Campaña 1 - Search Brand Protection
  - Targeting: Keywords de marca configurado
  - 2 ad groups creados
  - 8 keywords configuradas
  - 4 anuncios creados y aprobados
  - Presupuesto sugerido: $80-120/día configurado
  - Extensiones de anuncios configuradas
  - Negative keywords configuradas
  - Lista para activar (o activada si cliente aprueba)
  
- [ ] **AC-4-1-5**: Campaña 2 - Search Medicamentos Especializados
  - Targeting: 5-10 SKUs principales + variaciones configurado
  - 3 ad groups por categoría creados
  - 30 keywords enfocadas configuradas
  - 8 anuncios variados creados y aprobados
  - Presupuesto sugerido: $300-500/día configurado
  - Extensiones de anuncios configuradas
  - Negative keywords configuradas
  - Lista para activar (o activada si cliente aprueba)
  
- [ ] **AC-4-1-6**: Campaña 3 - Search Informacional + Display Remarketing
  - Search: Términos educativos relacionados configurados
  - Display: Audiencias de visitantes del sitio configuradas
  - 3 ad groups Search creados
  - 2 ad sets Display creados
  - 15 keywords configuradas
  - 10 banners (5 tamaños) creados y aprobados
  - Presupuesto sugerido: $150-250/día combinado configurado
  - Lista para activar (o activada si cliente aprueba)
  
- [ ] **AC-4-1-7**: Extensiones de anuncios configuradas
  - Sitelinks (mínimo 8) creados
  - Callouts (mínimo 6) creados
  - Call extensions configuradas
  - Location extensions (CDMX, Puebla) configuradas
  
- [ ] **AC-4-1-8**: Negative keywords configuradas
  - Lista inicial de 100+ términos creada
  - Genéricos de bajo valor excluidos
  - Términos de OTC excluidos
  - Búsquedas irrelevantes excluidas
  - Competencia excluida
  
- [ ] **AC-4-1-9**: Configuración avanzada
  - Bid strategies recomendadas por campaña configuradas
  - Ad scheduling (horarios óptimos) configurado
  - Geo-targeting preciso (CDMX, Puebla, zonas de interés) configurado
  - Device bid adjustments configurados
  - Audience targeting por campaña configurado
  
- [ ] **AC-4-1-10**: Scripts de automatización básicos
  - Pausa de keywords con mal performance configurado
  - Alertas de presupuesto configuradas
  - Reportes automáticos por email configurados
  - Testing de scripts completado
  
- [ ] **AC-4-1-11**: Google Analytics 4 configurado
  - Instalación completa verificada
  - Eventos custom configurados (10+ eventos)
  - Embudos de conversión mapeados
  - Integración con CRM configurada
  - Reportes personalizados creados
  - Testing de eventos completado
  
- [ ] **AC-4-1-12**: Google Tag Manager configurado
  - Instalado y configurado
  - Tags de eventos importantes configurados
  - Triggers optimizados configurados
  - Variables personalizadas configuradas
  - Testing y debugging completado
  - Sin errores en GTM Preview
  
- [ ] **AC-4-1-13**: Documento de mejores prácticas entregado
  - Documento de 20 páginas entregado
  - Cómo interpretar métricas explicado
  - Cuándo optimizar definido
  - Estrategias de puja documentadas
  - Testing de anuncios explicado
  - Calendario de optimización sugerido incluido

---

### Story FM-19: Dashboard Unificado de Marketing

**Story Key**: FM-19  
**Linked Tasks**: FM-104, FM-105, FM-106, FM-107, FM-108, FM-109, FM-110, FM-111, FM-112

#### Acceptance Criteria:
- [ ] **AC-4-2-1**: Sección 1 - Resumen Ejecutivo
  - Inversión total del mes visible
  - Leads totales generados visible
  - CPL (Costo Por Lead) calculado y visible
  - Leads calificados por bot visible
  - Tasa de conversión bot visible
  - Clicks a farmaciasmacross.com.mx visible
  
- [ ] **AC-4-2-2**: Sección 2 - Tráfico del Sitio
  - Visitas totales visible
  - Usuarios nuevos vs recurrentes visible
  - Tráfico por fuente (Orgánico, Google Ads, Directo, Referral) visible
  - Páginas más visitadas visible
  - Tiempo promedio en sitio visible
  - Tasa de rebote por fuente visible
  - Dispositivos (desktop, móvil, tablet) visible
  
- [ ] **AC-4-2-3**: Sección 3 - Performance Google Ads
  - Inversión por campaña visible
  - Impresiones, clicks, CTR visible
  - CPC promedio visible
  - Conversiones por tipo visible
  - Costo por conversión visible
  - Quality Score promedio visible
  - Posición promedio visible
  - Search impression share visible
  - Mejores keywords (por conversiones) visible
  - Peores keywords (por costo sin conversión) visible
  
- [ ] **AC-4-2-4**: Sección 4 - Leads y WhatsApp
  - Leads capturados por fuente visible
  - Conversaciones WhatsApp iniciadas visible
  - Leads calificados por el bot (por medicamento) visible
  - Leads descartados (por razón) visible
  - Tiempo promedio de respuesta del equipo visible
  - Conversión bot → humano (%) visible
  - Leads por centro (CDMX vs Puebla) visible
  
- [ ] **AC-4-2-5**: Sección 5 - SEO Orgánico
  - Posiciones en Google Search Console visible
  - Clicks orgánicos visible
  - Impresiones orgánicas visible
  - CTR orgánico visible
  - Top queries visible
  - Top landing pages visible
  
- [ ] **AC-4-2-6**: Sección 6 - Conversión y Revenue (si integran)
  - Clicks a Shopify visible
  - Conversión final (si proporcionan datos) visible
  - Revenue (si proporcionan datos) visible
  - ROAS estimado visible
  
- [ ] **AC-4-2-7**: Filtros interactivos funcionando
  - Por fecha (hoy, ayer, últimos 7/30/90 días, mes actual/anterior) funcionando
  - Por campaña funcionando
  - Por centro de distribución funcionando
  - Por medicamento/SKU funcionando
  - Por fuente de tráfico funcionando
  
- [ ] **AC-4-2-8**: Configuración técnica
  - Actualizaciones automáticas cada hora funcionando
  - Conexiones de datos (GA4, Google Ads, CRM) funcionando
  - Formato y diseño profesional
  - Acceso compartido con cliente configurado
  
- [ ] **AC-4-2-9**: PDF guía de métricas entregado
  - Explicación de cada KPI incluida
  - Cómo interpretar los datos explicado
  - Acciones recomendadas documentadas
  - Formato PDF entregado

---

### Story FM-20: Subfase 4.A - Ads Adelantado + Conversión Básica

**Story Key**: FM-20  
**Linked Tasks**: FM-113, FM-114, FM-115, FM-116

#### Acceptance Criteria:
- [ ] **AC-4-3-1**: Estructura de cuenta y campañas (borrador)
  - Organización preliminar creada
  - Convenciones de nombres definidas
  - Estructura de carpetas configurada
  
- [ ] **AC-4-3-2**: Keyword research completado
  - Lista inicial de keywords creada
  - Agrupación por intención completada
  - Priorización definida
  
- [ ] **AC-4-3-3**: Listas de negativas iniciales creadas
  - Términos a excluir identificados
  - Genéricos de bajo valor excluidos
  - Competencia excluida
  
- [ ] **AC-4-3-4**: Conversiones clave en GA4/GTM configuradas
  - WhatsApp click (evento configurado)
  - Form submit (evento configurado)
  - Lead magnet download (evento configurado)
  - Clicks a tienda/productos (evento configurado)
  - Testing de eventos completado

---

### Story FM-21: Subfase 4.B - Optimización Ads + Shopping + Dashboards

**Story Key**: FM-21  
**Linked Tasks**: FM-117, FM-118, FM-119, FM-120

#### Acceptance Criteria:
- [ ] **AC-4-4-1**: Afinación de campañas con datos reales
  - Análisis de performance inicial completado
  - Optimización de pujas realizada
  - Ajuste de keywords completado
  - Pausa de keywords no rentables realizada
  - Expansión de keywords ganadoras realizada
  - Mejora de CTR documentada
  
- [ ] **AC-4-4-2**: Configuración Shopping con SKUs aprobados
  - Setup de Merchant Center completado
  - Feed de productos configurado
  - Configuración de campaña Shopping completada
  - Solo productos aprobados incluidos
  - Testing y validación completados
  - Campaña activa y funcionando
  
- [ ] **AC-4-4-3**: Dashboard Looker Studio final
  - Integración completa de todas las fuentes funcionando
  - Métricas consolidadas visibles
  - Visualizaciones optimizadas
  - Filtros avanzados funcionando
  - Actualizaciones automáticas funcionando
  
- [ ] **AC-4-4-4**: Guía para lectura de métricas entregada
  - Documentación completa entregada
  - Interpretación de KPIs explicada
  - Acciones recomendadas documentadas
  - Sesión de walkthrough con cliente completada
  - Q&A final completado

---

## Criterios Generales de Aceptación (Aplican a Todos los Entregables)

### Calidad Técnica:
- [ ] Código/documentación sin errores críticos
- [ ] Testing básico completado
- [ ] Compatibilidad cross-browser verificada (Chrome, Firefox, Safari)
- [ ] Responsive design verificado en dispositivos reales

### Documentación:
- [ ] Documentación técnica actualizada
- [ ] Guías de usuario disponibles cuando aplique
- [ ] Changelog mantenido

### Aprobación Cliente:
- [ ] Revisión del cliente completada
- [ ] Feedback incorporado o justificado
- [ ] Sign-off formal recibido (cuando aplique)

### Entrega:
- [ ] Entregable disponible en producción/staging según corresponda
- [ ] Accesos compartidos con cliente
- [ ] Handoff documentado


