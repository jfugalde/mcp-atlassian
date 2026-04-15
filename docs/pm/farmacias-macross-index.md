# Farmacias Macross - Sinergia Digital: Project Documentation Index

**Project Key**: FM  
**Project Name**: Sinergia Digital - Ecosistema Digital para Medicamentos Especializados  
**Client**: Farmacias Macross  
**Total Investment**: $364,000 MXN (sin IVA)  
**Total Duration**: 20 semanas  
**Status**: Planning Complete

---

## Quick Reference

| Document | Purpose | Last Updated |
|----------|---------|--------------|
| [Epic Structure](./farmacias-macross-epics.md) | Complete breakdown of all epics, stories, and tasks | [Fecha] |
| [Timeline](./farmacias-macross-timeline.md) | 20-week schedule with milestones and dependencies | [Fecha] |
| [Acceptance Criteria](./farmacias-macross-acceptance-criteria.md) | DoD for all deliverables | [Fecha] |
| [Risk Log](./farmacias-macross-risks.md) | Identified risks and mitigation strategies | [Fecha] |
| [Client Communications](./farmacias-macross-client-comms.md) | Email templates and communication guides | [Fecha] |
| [Jira Import](./farmacias-macross-jira-import.json) | JSON format for bulk import to Jira | [Fecha] |
| [Technical Specs](./farmacias-macross-technical-specs.md) | Technical requirements and specifications | [Fecha] |
| [Handoff Procedures](./farmacias-macross-handoff.md) | Complete handoff process and documentation | [Fecha] |

---

## Project Overview

### Objective
Construir un ecosistema digital integrado que conecte:
- Tráfico (Ads + SEO) → Contenido → Sitios (Macross + Medicamentos Especiales)
- WhatsApp → Bot + CRM → Shopify → Venta → Métricas

### Key Deliverables
1. Sitio WordPress compliant (medicamentosespeciales.mx)
2. 15 artículos especializados con CTAs estratégicos
3. 2 lead magnets con landing pages
4. Bot WhatsApp con filtrado automático 24/7
5. CRM automatizado con pipeline personalizado
6. Google Ads configurado (3 campañas base)
7. Dashboard Looker Studio unificado

---

## Project Structure

### 4 Main Phases

#### FASE 1: WordPress Fachada para Compliance (5 semanas)
- **Epic**: FM-1
- **Investment**: $80,000 MXN
- **Stories**: 4 (FM-1-1 a FM-1-4)
- **Key Deliverable**: Sitio listo para Google Ads

#### FASE 2: Contenido Educativo Estratégico (6 semanas)
- **Epic**: FM-2
- **Investment**: $102,000 MXN
- **Stories**: 4 (FM-2-1 a FM-2-4)
- **Key Deliverable**: Sistema de captación operativo

#### FASE 3: Sistema de Filtrado Automatizado (5 semanas)
- **Epic**: FM-3
- **Investment**: $120,000 MXN
- **Stories**: 5 (FM-3-1 a FM-3-5)
- **Key Deliverable**: Filtrado automático operativo

#### FASE 4: Setup Google Ads + Dashboards (4 semanas)
- **Epic**: FM-4
- **Investment**: $62,000 MXN
- **Stories**: 4 (FM-4-1 a FM-4-4)
- **Key Deliverable**: Ecosistema completo medible

---

## Milestones

| Milestone | Week | Deliverables |
|-----------|------|--------------|
| Hito 1 - Arranque | 0 | Setup operativo completo |
| Hito 2 - Sitio Anunciable | 5 | WordPress funcional, catálogo OTC, SEO técnico |
| Hito 3 - Contenido + Ads Estructura | 10 | 15 artículos, lead magnets, GA4/GTM, Ads estructura |
| Hito 4 - Automatización | 15 | Bot funcional, CRM configurado, integraciones |
| Hito 5 - Optimización Final | 20 | Campañas optimizadas, Shopping, Dashboard final |

---

## Key Metrics & KPIs

### Marketing Metrics
- Leads totales generados
- CPL (Costo Por Lead)
- Leads calificados por bot
- Tasa de conversión bot
- Clicks a farmaciasmacross.com.mx

### Traffic Metrics
- Visitas totales
- Tráfico por fuente (Orgánico, Google Ads, Directo, Referral)
- Páginas más visitadas
- Tasa de rebote por fuente

### Google Ads Metrics
- Inversión por campaña
- Impresiones, clicks, CTR
- CPC promedio
- Conversiones por tipo
- Costo por conversión

### WhatsApp & Bot Metrics
- Conversaciones WhatsApp iniciadas
- Leads calificados por el bot (por medicamento)
- Leads descartados (por razón)
- Tiempo promedio de respuesta del equipo
- Conversión bot → humano (%)

### SEO Metrics
- Posiciones en Google Search Console
- Clicks orgánicos
- Impresiones orgánicas
- CTR orgánico
- Top queries

---

## Critical Dependencies

### Client Dependencies
- **Week 0**: Accesos (WordPress, Shopify, Google)
- **Week 2-3**: Lista de 20 SKUs principales
- **Week 6**: Aprobación de 3 artículos piloto
- **Week 10**: Número WhatsApp + documentos legales
- **Week 15**: Accesos Google Ads/Analytics + presupuesto

### Internal Dependencies
- FM-1-1 → FM-1-2 (Arquitectura antes de desarrollo)
- FM-1-2 → FM-1-3, FM-1-4 (Sitio base antes de productos y SEO)
- FM-1-2 → FM-2-2 (Sitio funcional antes de contenido)
- FM-2-2 → FM-4-1 (Contenido antes de Ads)
- FM-3-1 → FM-3-2 (WhatsApp API antes de bot)
- FM-3-2, FM-3-3 → FM-3-5 (Bot y CRM antes de capacitación)

---

## Risk Summary

### Critical Risks (🔴)
- **FM-TR1**: Cambios de Alcance (Scope Creep)

### High Risks (🟠)
- **FM-1-R1**: Retrasos en Aprobaciones del Cliente
- **FM-1-R2**: Lista de 20 SKUs Incompleta o Tardía
- **FM-2-R1**: Calidad/Precisión Médica del Contenido
- **FM-2-R2**: Aprobación de Artículos Piloto Tardía
- **FM-3-R1**: Retrasos en Verificación WhatsApp Business API
- **FM-3-R2**: Complejidad de Lógica de Filtrado Subestimada

### Medium Risks (🟡)
- **FM-1-R3**: Problemas de Performance en Hosting
- **FM-1-R4**: Compliance Legal Más Complejo de lo Esperado
- **FM-2-R3**: Información Insuficiente para Lead Magnets
- **FM-3-R3**: Integración CRM Más Compleja de lo Esperado
- **FM-3-R4**: Disponibilidad del Equipo para Capacitación
- **FM-4-R1**: Google Ads No Aprueba Campañas por Compliance
- **FM-4-R2**: Accesos Google Ads/Analytics No Proporcionados a Tiempo
- **FM-TR2**: Disponibilidad de Recursos del Equipo
- **FM-TR3**: Problemas con Servicios de Terceros
- **FM-TR4**: Expectativas de Resultados No Realistas

---

## Payment Schedule

| Payment | Amount | Trigger | Week |
|---------|--------|---------|------|
| Pago 1 | $22,000 MXN | Fase 0 + Anticipo Fase 1 | 0 |
| Pago 2 | $60,000 MXN | Cierre Fase 1 | 5 |
| Pago 3 | $20,000 MXN | Anticipo Fase 2 | 4-5 |
| Pago 4 | $82,000 MXN | Cierre Fase 2 | 10 |
| Pago 5 | $20,000 MXN | Subfase 4.A (Ads adelantado) | 4-10 |
| Pago 6 | $24,000 MXN | Anticipo Fase 3 | 10 |
| Pago 7 | $96,000 MXN | Cierre Fase 3 | 15 |
| Pago 8 | $42,000 MXN | Subfase 4.B (restante Fase 4) | 20 |

**Total**: $364,000 MXN (sin IVA)

---

## Team Roles & Responsibilities

### Project Manager
- **Responsibilities**: Overall project coordination, client communication, risk management, timeline tracking
- **Time Allocation**: 20% del proyecto

### Technical Lead
- **Responsibilities**: Architecture decisions, technical implementation, code reviews, integration oversight
- **Time Allocation**: 30% del proyecto

### Development Team
- **WordPress Developer**: Sitio WordPress, páginas, templates
- **Frontend Developer**: Diseño responsivo, UI/UX implementation
- **Backend Developer**: Bot development, API integrations, CRM setup
- **Time Allocation**: 40% del proyecto

### Content Team
- **Content Strategist**: Keyword research, content calendar, briefs
- **Content Writers**: 15 artículos especializados
- **Medical Reviewer**: Revisión médica de contenido
- **Time Allocation**: 20% del proyecto

### Marketing Team
- **SEO Specialist**: SEO técnico, schema markup, Search Console
- **Google Ads Specialist**: Configuración de campañas, optimización
- **Analytics Specialist**: GA4, GTM, Dashboard Looker Studio
- **Time Allocation**: 15% del proyecto

---

## Tools & Platforms

### Project Management
- **Jira**: Epic, story, task tracking
- **Slack**: Team communication
- **Google Drive**: File sharing and documentation

### Development
- **WordPress**: CMS para medicamentosespeciales.mx
- **Hostinger**: Hosting provider
- **Git**: Version control
- **Node.js / Python**: Bot development

### Marketing & Analytics
- **Google Analytics 4**: Web analytics
- **Google Tag Manager**: Tag management
- **Google Search Console**: SEO monitoring
- **Google Ads**: Paid advertising
- **Looker Studio**: Dashboard visualization

### Communication & Automation
- **WhatsApp Business API**: 360 diálogo o Twilio
- **CRM**: HubSpot CRM (gratuito) o Pipedrive
- **n8n / Zapier**: Automation platform

### Design & Collaboration
- **Figma**: Design review and collaboration
- **Adobe Creative Suite**: PDF design for lead magnets

---

## Success Criteria

### Technical Success
- ✅ Sitio WordPress funcional y optimizado (PageSpeed >80)
- ✅ Bot WhatsApp funcionando 24/7 con >90% accuracy
- ✅ CRM automatizado con sincronización bidireccional
- ✅ Google Ads configurado y listo para activar
- ✅ Dashboard Looker Studio completo y actualizado

### Business Success
- ✅ Sistema de captación operativo
- ✅ Filtrado automático funcionando (solo leads calificados)
- ✅ Tracking completo del funnel
- ✅ Equipo capacitado y operando independientemente

### Client Success
- ✅ Documentación completa entregada
- ✅ Capacitación completada (4 sesiones)
- ✅ Sistema operable sin dependencia diaria del equipo
- ✅ Métricas visibles y accionables

---

## Change Request Process

### When to Submit Change Request
- Solicitud de nueva funcionalidad no incluida en scope
- Cambio en diseño o estructura
- Modificación de entregables
- Cambio en timeline o prioridades

### Change Request Evaluation
1. **Impact Analysis**: Tiempo, costo, dependencias afectadas
2. **Options Provided**: Implementar completo, parcial, o postponer
3. **Recommendation**: Recomendación del equipo con justificación
4. **Client Decision**: Cliente decide opción preferida
5. **Approval**: Sign-off formal antes de implementar

### Change Request Template
Ver: [Client Communications - Template 7](./farmacias-macross-client-comms.md#template-7-change-request-evaluation)

---

## Quality Assurance

### Testing Requirements
- **Functional Testing**: Todas las funcionalidades probadas
- **Performance Testing**: PageSpeed, API response times
- **Security Testing**: SSL, SQL injection, XSS prevention
- **Cross-Browser Testing**: Chrome, Firefox, Safari, Edge
- **Integration Testing**: WordPress ↔ WhatsApp, Bot ↔ CRM, etc.
- **User Acceptance Testing**: Cliente prueba sistema completo

### Quality Gates
- **Code Review**: Obligatorio antes de merge
- **Testing**: Obligatorio antes de deploy
- **Client Approval**: Obligatorio para entregables clave
- **Documentation**: Actualizada con cada cambio

---

## Communication Protocols

### Regular Communication
- **Weekly Status Updates**: Cada Lunes por email
- **Weekly Meetings**: Google Meet (30-90 min) cuando necesario
- **Daily Standups**: Interno del equipo (no con cliente)

### Ad-hoc Communication
- **Slack**: Canal principal (respuestas <4 horas hábiles)
- **Email**: Reportes y documentación formal
- **WhatsApp**: Solo emergencias críticas
- **Phone**: Solo urgencias que requieren atención inmediata

### Approval Process
- **SLA**: 72 horas para feedback/aprobaciones del cliente
- **Escalation**: Si no hay respuesta en 48h, recordatorio
- **Buffer**: 1 semana de buffer incluida en timeline para aprobaciones

---

## Documentation Standards

### All Documentation Must Include
- **Version Number**: Para tracking de cambios
- **Last Updated Date**: Para saber cuándo fue actualizado
- **Owner**: Responsable del documento
- **Status**: Draft, Review, Approved, Archived

### Documentation Formats
- **Markdown**: Para documentación técnica
- **PDF**: Para entregas al cliente
- **Word**: Para documentos editables
- **JSON**: Para datos estructurados (Jira import)

---

## Glossary

### Terms & Acronyms

**COFEPRIS**: Comisión Federal para la Protección contra Riesgos Sanitarios (regulador mexicano)

**OTC**: Over-the-Counter (medicamentos de venta libre)

**SKU**: Stock Keeping Unit (unidad de producto)

**GA4**: Google Analytics 4

**GTM**: Google Tag Manager

**CRM**: Customer Relationship Management

**CPL**: Costo Por Lead

**CTR**: Click-Through Rate

**CPC**: Costo Por Clic

**ROAS**: Return on Ad Spend

**UTM**: Urchin Tracking Module (parámetros de tracking)

**API**: Application Programming Interface

**REST**: Representational State Transfer (tipo de API)

**Webhook**: Callback HTTP para notificaciones en tiempo real

**n8n**: Plataforma de automatización open-source

**CDMX**: Ciudad de México

**SLA**: Service Level Agreement (acuerdo de nivel de servicio)

**DoD**: Definition of Done (definición de completado)

**MVP**: Minimum Viable Product (producto mínimo viable)

---

## Related Projects

### Farmacias Macross - Optimización Shopify
**Status**: Proyecto separado pero coordinado  
**Document**: [Referencia al documento del proyecto Shopify]  
**Coordination**: Contenido, analytics, y Ads son compartidos entre proyectos

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Fecha] | Initial documentation creation | PM Team |

---

## Contact Information

### Project Team
- **Project Manager**: [Nombre] - [email]
- **Technical Lead**: [Nombre] - [email]
- **Account Manager**: [Nombre] - [email]

### Client Contacts
- **Primary Contact**: [Nombre] - [email] - [tel]
- **Technical Contact**: [Nombre] - [email] - [tel]
- **Billing Contact**: [Nombre] - [email] - [tel]

---

## Notes

- Esta documentación es un documento vivo y se actualizará según avance el proyecto
- Todas las fechas son aproximadas y sujetas a ajustes según realidad del proyecto
- Los costos están en MXN y no incluyen IVA (16% adicional con factura)
- Cualquier pregunta sobre esta documentación debe dirigirse al Project Manager

---

**Última actualización**: [Fecha]  
**Próxima revisión**: [Fecha + 1 mes]







