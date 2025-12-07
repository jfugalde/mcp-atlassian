# Farmacias Macross - Sinergia Digital: Risk Log

**Project Key**: FM  
**Last Updated**: [Fecha]  
**Risk Owner**: Project Manager

---

## Risk Assessment Matrix

| Probability | Impact | Risk Level |
|------------|--------|------------|
| High | High | 🔴 Critical |
| High | Medium | 🟠 High |
| Medium | High | 🟠 High |
| Medium | Medium | 🟡 Medium |
| Low | High | 🟡 Medium |
| Low | Medium | 🟢 Low |

---

## EPIC 1: FASE 1 - WordPress Fachada para Compliance

### Risk FM-1-R1: Retrasos en Aprobaciones del Cliente

**Risk ID**: FM-1-R1  
**Category**: Schedule / Client Dependency  
**Probability**: High  
**Impact**: Medium  
**Risk Level**: 🟠 High  
**Owner**: Project Manager

**Description**:  
El cliente no proporciona feedback o aprobaciones dentro del SLA de 72 horas, retrasando el inicio de desarrollo de páginas específicas.

**Impact**:  
- Retraso de 1-2 semanas en la entrega de Fase 1
- Afecta timeline de Fases 2 y 3
- Posible impacto en fecha de lanzamiento de Ads

**Mitigation**:  
- SLA de 72h documentado en contrato
- Recordatorios automáticos 48h antes de deadline
- Buffer de 1 semana incluido en timeline
- Escalación a stakeholders si retraso >5 días
- Plan B: Avanzar con supuestos documentados y ajustar después

**Contingency**:  
- Si retraso >1 semana: Revisar priorización de páginas, entregar MVP primero
- Si retraso >2 semanas: Activar cláusula de extensión de timeline en contrato

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-1-R2: Lista de 20 SKUs Incompleta o Tardía

**Risk ID**: FM-1-R2  
**Category**: Scope / Client Dependency  
**Probability**: Medium  
**Impact**: High  
**Risk Level**: 🟠 High  
**Owner**: Project Manager

**Description**:  
El cliente no proporciona la lista completa de 20 SKUs principales con toda la información requerida (nombre comercial, genérico, links, descripciones) en Semana 2-3.

**Impact**:  
- Bloquea desarrollo de catálogo OTC (FM-1-3)
- Retrasa SEO técnico relacionado
- Afecta contenido de Fase 2 que referencia productos

**Mitigation**:  
- Solicitar lista en Semana 0 (kickoff)
- Template de información requerida proporcionado
- Seguimiento semanal desde Semana 1
- Plan B: Usar productos genéricos de ejemplo y reemplazar después

**Contingency**:  
- Si lista incompleta: Desarrollar con información disponible, completar después
- Si lista tardía (>Semana 4): Priorizar otras tareas, catálogo en paralelo

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-1-R3: Problemas de Performance en Hosting

**Risk ID**: FM-1-R3  
**Category**: Technical / Infrastructure  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Technical Lead

**Description**:  
El hosting de Hostinger no cumple con los requisitos de performance necesarios para PageSpeed Score >80, especialmente en móvil.

**Impact**:  
- No se cumple AC de optimización de velocidad
- Posible impacto en SEO
- Experiencia de usuario degradada

**Mitigation**:  
- Auditoría de hosting en Semana 1
- Plan de optimización temprano
- CDN como backup si necesario
- Optimización agresiva de imágenes y assets
- Caching avanzado configurado

**Contingency**:  
- Si hosting insuficiente: Proponer upgrade de plan o migración parcial a CDN
- Si no se resuelve: Documentar limitación y ajustar expectativas

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-1-R4: Compliance Legal Más Complejo de lo Esperado

**Risk ID**: FM-1-R4  
**Category**: Legal / Compliance  
**Probability**: Low  
**Impact**: High  
**Risk Level**: 🟡 Medium  
**Owner**: Legal Advisor / PM

**Description**:  
Los requisitos de compliance COFEPRIS o sector salud son más estrictos de lo inicialmente evaluado, requiriendo cambios significativos en contenido o estructura.

**Impact**:  
- Retraso en entrega de páginas legales
- Posibles cambios en disclaimers en todas las páginas
- Riesgo de no poder activar Ads si no se resuelve

**Mitigation**:  
- Revisión legal temprana (Semana 2)
- Consulta con abogado especializado en salud
- Template de disclaimers aprobado antes de desarrollo masivo
- Revisión de competencia para benchmark

**Contingency**:  
- Si cambios mayores requeridos: Activar change request, ajustar timeline
- Si bloquea Ads: Prioridad máxima, recursos adicionales si necesario

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

## EPIC 2: FASE 2 - Contenido Educativo Estratégico

### Risk FM-2-R1: Calidad/Precisión Médica del Contenido

**Risk ID**: FM-2-R1  
**Category**: Quality / Content  
**Probability**: Medium  
**Impact**: High  
**Risk Level**: 🟠 High  
**Owner**: Content Lead / Medical Reviewer

**Description**:  
El contenido médico requiere múltiples revisiones o correcciones significativas por imprecisiones, afectando timeline y calidad.

**Impact**:  
- Retraso en publicación de artículos
- Riesgo legal si información incorrecta
- Impacto en SEO si contenido no es de calidad

**Mitigation**:  
- Proceso de revisión médica definido desde inicio
- Medical reviewer asignado (interno o externo)
- Checklist de verificación médica por artículo
- Revisión en etapas (outline → draft → final)
- Fuentes médicas confiables requeridas

**Contingency**:  
- Si revisiones múltiples: Buffer de 1 semana incluido en timeline
- Si calidad insuficiente: Contratar medical writer especializado
- Si bloquea publicación: Priorizar artículos menos sensibles primero

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-2-R2: Aprobación de Artículos Piloto Tardía

**Risk ID**: FM-2-R2  
**Category**: Schedule / Client Dependency  
**Probability**: High  
**Impact**: Medium  
**Risk Level**: 🟠 High  
**Owner**: Project Manager

**Description**:  
El cliente no aprueba los 3 artículos piloto en Semana 6 dentro del SLA de 72h, bloqueando producción masiva de los 12 restantes.

**Impact**:  
- Retraso de 1-2 semanas en producción de contenido
- Afecta timeline de Fase 4 (Ads necesita contenido publicado)
- Posible impacto en lanzamiento de campañas

**Mitigation**:  
- Envío de artículos piloto en Semana 5 (antes de lo planeado)
- Recordatorios proactivos
- Reunión de revisión programada
- Plan B: Avanzar con supuestos de estilo/tono documentados

**Contingency**:  
- Si retraso >1 semana: Producción paralela de artículos con estilo documentado
- Si cambios mayores: Ajustar timeline, comunicar impacto a cliente

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-2-R3: Información Insuficiente para Lead Magnets

**Risk ID**: FM-2-R3  
**Category**: Scope / Client Dependency  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Content Lead

**Description**:  
El cliente no proporciona suficiente información, casos de uso, o datos para crear lead magnets de calidad (10-15 páginas cada uno).

**Impact**:  
- Lead magnets genéricos o de menor valor
- Menor tasa de conversión
- No cumple expectativas de calidad

**Mitigation**:  
- Solicitar información en Semana 0
- Template de información requerida
- Reunión de discovery en Semana 7
- Plan B: Usar información pública + investigación propia

**Contingency**:  
- Si información limitada: Reducir extensión a 8-10 páginas, enfocar en calidad
- Si no hay información: Crear guías más generales, ajustar expectativas

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

## EPIC 3: FASE 3 - Sistema de Filtrado Automatizado

### Risk FM-3-R1: Retrasos en Verificación WhatsApp Business API

**Risk ID**: FM-3-R1  
**Category**: Schedule / Third-Party  
**Probability**: High  
**Impact**: High  
**Risk Level**: 🔴 Critical  
**Owner**: Technical Lead

**Description**:  
WhatsApp tarda más de lo esperado (2-4 semanas típico) en verificar el negocio y aprobar la cuenta Business API, bloqueando desarrollo del bot.

**Impact**:  
- Bloquea desarrollo completo de FM-3-2 (Chatbot)
- Retrasa toda Fase 3
- Impacto crítico en timeline general
- No se puede activar filtrado automático

**Mitigation**:  
- Iniciar proceso de verificación en Semana 8 (antes de lo necesario)
- Documentación completa preparada de antemano
- Seguimiento diario del proceso
- Proveedor alternativo identificado (360 diálogo vs Twilio)
- Desarrollo del bot en sandbox/testing mientras se espera

**Contingency**:  
- Si retraso >2 semanas: Desarrollo completo en sandbox, migración rápida cuando se apruebe
- Si retraso >4 semanas: Evaluar proveedor alternativo o número alternativo
- Si bloquea crítico: Activar plan de contingencia con solución temporal

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-3-R2: Complejidad de Lógica de Filtrado Subestimada

**Risk ID**: FM-3-R2  
**Category**: Technical / Scope  
**Probability**: Medium  
**Impact**: High  
**Risk Level**: 🟠 High  
**Owner**: Technical Lead

**Description**:  
La lógica de reconocimiento de intención y filtrado (especialmente reconocimiento de nombres comerciales de 20 SKUs) es más compleja de lo estimado, requiriendo más tiempo de desarrollo.

**Impact**:  
- Retraso en entrega de bot funcional
- Accuracy menor a la esperada (>90%)
- Necesidad de más testing y ajustes
- Posible sobrecosto

**Mitigation**:  
- Proof of concept en Semana 11 (antes de desarrollo completo)
- Testing temprano con casos reales
- Machine learning/NLP si necesario para reconocimiento
- Buffer de 1 semana incluido en estimación
- Revisión de alcance con cliente si necesario

**Contingency**:  
- Si complejidad mayor: Priorizar funcionalidad core, features avanzadas en fase 2
- Si accuracy insuficiente: Más testing, ajuste de algoritmos, fallback a humano más frecuente
- Si sobrecosto: Activar change request, ajustar scope

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-3-R3: Integración CRM Más Compleja de lo Esperado

**Risk ID**: FM-3-R3  
**Category**: Technical / Integration  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Technical Lead

**Description**:  
La integración bidireccional WhatsApp ↔ CRM requiere más configuración o desarrollo custom de lo estimado, especialmente automatizaciones complejas.

**Impact**:  
- Retraso en entrega de CRM automatizado
- Automatizaciones no funcionan como esperado
- Necesidad de trabajo manual adicional

**Mitigation**:  
- Evaluación técnica temprana de CRM elegido (HubSpot vs Pipedrive)
- APIs documentadas revisadas antes de desarrollo
- Proof of concept de integraciones críticas
- Plan B: Automatizaciones básicas primero, avanzadas después

**Contingency**:  
- Si integración compleja: Simplificar automatizaciones, proceso manual temporal
- Si no funciona: Evaluar CRM alternativo o solución custom
- Si retraso: Priorizar funcionalidad core, features avanzadas después

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-3-R4: Disponibilidad del Equipo para Capacitación

**Risk ID**: FM-3-R4  
**Category**: Schedule / Client Dependency  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Project Manager

**Description**:  
El equipo del cliente no tiene disponibilidad para las 4 sesiones de capacitación (7 horas total) en las semanas 14-15, retrasando handoff y operación.

**Impact**:  
- Retraso en operación del sistema
- Equipo no preparado para usar bot/CRM
- Posible impacto en soporte post-lanzamiento

**Mitigation**:  
- Confirmar disponibilidad en Semana 10 (con anticipación)
- Flexibilidad en horarios (mañana/tarde)
- Opción de sesiones grabadas si necesario
- Material de auto-estudio disponible
- Plan B: Sesiones más cortas distribuidas

**Contingency**:  
- Si no hay disponibilidad: Sesiones grabadas + Q&A asíncrono
- Si retraso crítico: Capacitación intensiva 1 día, seguimiento extendido
- Si no se completa: Documentación exhaustiva, soporte extendido

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

## EPIC 4: FASE 4 - Setup Google Ads + Dashboards

### Risk FM-4-R1: Google Ads No Aprueba Campañas por Compliance

**Risk ID**: FM-4-R1  
**Category**: Compliance / Third-Party  
**Probability**: Low  
**Impact**: High  
**Risk Level**: 🟡 Medium  
**Owner**: Ads Specialist / PM

**Description**:  
Google Ads rechaza las campañas o anuncios por políticas de salud/farmacéuticas, a pesar de que el sitio es compliant.

**Impact**:  
- No se pueden activar campañas
- Retraso en lanzamiento de Ads
- Posible necesidad de cambios en copy/landing pages
- Impacto en ROI del proyecto

**Mitigation**:  
- Revisión de políticas Google Ads en Semana 1
- Copy de anuncios revisado por especialista en salud
- Landing pages compliant desde Fase 1
- Aplicación temprana (Semana 10) para identificar problemas
- Consulta con Google Ads support si necesario

**Contingency**:  
- Si rechazo: Ajustar copy según feedback, re-aplicar
- Si bloqueo permanente: Evaluar alternativas (Bing Ads, Meta con restricciones)
- Si cambios mayores: Activar change request, ajustar timeline

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-4-R2: Accesos Google Ads/Analytics No Proporcionados a Tiempo

**Risk ID**: FM-4-R2  
**Category**: Schedule / Client Dependency  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Project Manager

**Description**:  
El cliente no proporciona accesos a Google Ads o Google Analytics en Semana 15, bloqueando configuración de campañas y dashboard.

**Impact**:  
- Retraso en configuración de Ads
- No se puede completar dashboard
- Posible retraso en lanzamiento

**Mitigation**:  
- Solicitar accesos en Semana 10 (con anticipación)
- Opción de crear cuentas nuevas si no tienen
- Recordatorios semanales
- Plan B: Configuración en cuenta de prueba, migración después

**Contingency**:  
- Si no hay accesos: Crear cuentas nuevas, transferir ownership después
- Si retraso: Configuración en staging, activación cuando accesos disponibles
- Si bloquea crítico: Escalación a stakeholders

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-4-R3: Presupuesto Google Ads No Definido

**Risk ID**: FM-4-R3  
**Category**: Scope / Client Dependency  
**Probability**: Medium  
**Impact**: Low  
**Risk Level**: 🟢 Low  
**Owner**: Project Manager

**Description**:  
El cliente no define el presupuesto mensual de Google Ads en Semana 15, afectando configuración de campañas (presupuestos sugeridos vs reales).

**Impact**:  
- Campañas configuradas con presupuestos estimados
- Necesidad de ajuste después
- Posible confusión en expectativas

**Mitigation**:  
- Discusión de presupuesto en Semana 0 (kickoff)
- Rango de presupuesto sugerido documentado
- Configuración flexible (fácil de ajustar)
- Comunicación clara de que presupuesto es responsabilidad cliente

**Contingency**:  
- Si no definido: Configurar con presupuestos sugeridos, ajustar cuando se defina
- Si cambio mayor: Reconfiguración rápida, sin impacto en timeline

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-4-R4: Complejidad de Dashboard Looker Studio

**Risk ID**: FM-4-R4  
**Category**: Technical / Scope  
**Probability**: Low  
**Impact**: Medium  
**Risk Level**: 🟢 Low  
**Owner**: Analytics Specialist

**Description**:  
La integración de múltiples fuentes de datos (GA4, Google Ads, CRM) en Looker Studio es más compleja de lo esperado, requiriendo más tiempo.

**Impact**:  
- Retraso en entrega de dashboard
- Métricas no disponibles a tiempo
- Posible necesidad de simplificación

**Mitigation**:  
- Evaluación técnica de integraciones en Semana 15
- APIs documentadas revisadas
- Dashboard MVP primero, features avanzadas después
- Testing temprano de conexiones

**Contingency**:  
- Si complejidad mayor: Dashboard simplificado primero, features avanzadas después
- Si no funciona: Alternativas (Google Sheets, exportaciones manuales temporalmente)
- Si retraso: Priorizar métricas críticas, resto después

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

## Riesgos Transversales (Aplican a Todo el Proyecto)

### Risk FM-TR1: Cambios de Alcance (Scope Creep)

**Risk ID**: FM-TR1  
**Category**: Scope / Change Management  
**Probability**: High  
**Impact**: High  
**Risk Level**: 🔴 Critical  
**Owner**: Project Manager

**Description**:  
El cliente solicita cambios o features adicionales fuera del scope definido, sin pasar por proceso de change request formal.

**Impact**:  
- Retrasos en timeline
- Sobrecostos
- Desviación de objetivos originales
- Equipo sobrecargado

**Mitigation**:  
- Scope claramente documentado en contrato
- Exclusiones explícitas listadas
- Proceso de change request definido
- Comunicación proactiva de impactos
- Revisión semanal de scope

**Contingency**:  
- Si cambio solicitado: Evaluar impacto, cotizar, aprobar antes de implementar
- Si cambio crítico: Revisar priorización, ajustar timeline/costo
- Si scope creep continuo: Reunión de alineación con stakeholders

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-TR2: Disponibilidad de Recursos del Equipo

**Risk ID**: FM-TR2  
**Category**: Resource / Internal  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Project Manager

**Description**:  
Miembros clave del equipo no están disponibles por enfermedad, vacaciones, o otros proyectos, afectando capacidad de entrega.

**Impact**:  
- Retrasos en entregas
- Calidad comprometida
- Sobrecarga de otros miembros

**Mitigation**:  
- Plan de recursos con buffer
- Documentación continua (knowledge sharing)
- Cross-training de funciones críticas
- Backup resources identificados
- Comunicación proactiva de disponibilidad

**Contingency**:  
- Si ausencia corta: Redistribución de trabajo, ajuste de prioridades
- Si ausencia prolongada: Activar recursos de backup, ajustar timeline
- Si crítico: Escalación, recursos adicionales si necesario

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-TR3: Problemas con Servicios de Terceros

**Risk ID**: FM-TR3  
**Category**: Technical / Third-Party  
**Probability**: Low  
**Impact**: High  
**Risk Level**: 🟡 Medium  
**Owner**: Technical Lead

**Description**:  
Servicios de terceros (WhatsApp, Google, Hostinger, CRM) experimentan downtime, cambios de API, o problemas que afectan el proyecto.

**Impact**:  
- Bloqueo de desarrollo
- Retrasos en entregas
- Necesidad de workarounds

**Mitigation**:  
- Monitoreo de status de servicios
- APIs versionadas cuando posible
- Planes de fallback identificados
- Comunicación proactiva con proveedores
- Testing de integraciones temprano

**Contingency**:  
- Si downtime corto: Workarounds temporales, desarrollo en sandbox
- Si cambio de API: Actualización rápida, comunicación con proveedor
- Si servicio crítico caído: Activar plan de contingencia, alternativas

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

### Risk FM-TR4: Expectativas de Resultados No Realistas

**Risk ID**: FM-TR4  
**Category**: Communication / Expectations  
**Probability**: Medium  
**Impact**: Medium  
**Risk Level**: 🟡 Medium  
**Owner**: Project Manager

**Description**:  
El cliente tiene expectativas no realistas sobre resultados (leads, conversiones, rankings SEO) en tiempos cortos, causando frustración.

**Impact**:  
- Insatisfacción del cliente
- Presión para garantizar resultados
- Posible conflicto en entregas

**Mitigation**:  
- Expectativas claramente establecidas en contrato
- Exclusiones explícitas (no garantizamos métricas específicas)
- Comunicación proactiva de timelines realistas (SEO toma 3-6 meses)
- Educación sobre proceso de marketing digital
- Reportes transparentes de progreso

**Contingency**:  
- Si expectativas no realistas: Reunión de alineación, revisar contrato
- Si presión por resultados: Reforzar exclusiones, enfocar en entregables
- Si conflicto: Escalación, mediación si necesario

**Status**: 🟡 Active  
**Last Review**: [Fecha]

---

## Risk Review Schedule

- **Semanal**: Revisión de riesgos activos en standup
- **Quincenal**: Actualización de probabilidad/impacto
- **Mensual**: Revisión completa de risk log con stakeholders
- **Por Hito**: Revisión exhaustiva antes de cada hito

---

## Risk Escalation Matrix

| Risk Level | Escalation | Action Required |
|------------|------------|-----------------|
| 🔴 Critical | Immediate to PM + Client | Mitigation plan within 24h |
| 🟠 High | PM + Team Lead | Mitigation plan within 48h |
| 🟡 Medium | PM | Monitor, mitigate as needed |
| 🟢 Low | Team awareness | Monitor, mitigate if worsens |

---

## Notes

- Todos los riesgos deben tener owner asignado
- Mitigation plans deben ser específicos y accionables
- Contingency plans deben ser realistas y probados cuando posible
- Risk log debe actualizarse continuamente, no solo en reviews formales





