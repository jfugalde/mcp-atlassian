# Farmacias Macross - Sinergia Digital: Technical Specifications

**Project Key**: FM  
**Last Updated**: [Fecha]  
**Technical Lead**: [Nombre]

---

## Infrastructure & Hosting

### WordPress Site (medicamentosespeciales.mx)

**Hosting Provider**: Hostinger  
**Platform**: WordPress (versión más reciente estable)  
**PHP Version**: 8.0+  
**MySQL Version**: 5.7+ o MariaDB 10.3+

**Requirements**:
- SSL Certificate (HTTPS obligatorio)
- PHP Memory Limit: 256MB mínimo
- Max Upload Size: 64MB mínimo
- PHP Execution Time: 300 segundos
- Database: MySQL/MariaDB con soporte UTF-8

**Performance Targets**:
- PageSpeed Score: >80 (desktop y móvil)
- First Contentful Paint: <1.8s
- Time to Interactive: <3.5s
- Largest Contentful Paint: <2.5s
- Cumulative Layout Shift: <0.1

**CDN**: Opcional pero recomendado (Cloudflare, KeyCDN, o similar)

---

## Technology Stack

### Frontend
- **Framework**: WordPress Theme (custom o basado en tema existente)
- **CSS**: Responsive design, mobile-first approach
- **JavaScript**: Vanilla JS o jQuery (según tema)
- **Image Format**: WebP con fallback a JPEG/PNG
- **Font Loading**: Web fonts optimizadas (preload, font-display: swap)

### Backend
- **CMS**: WordPress
- **Plugins Esenciales**:
  - SEO: Yoast SEO o Rank Math
  - Performance: WP Rocket, W3 Total Cache, o similar
  - Security: Wordfence o similar
  - Forms: Contact Form 7 o Gravity Forms
  - Schema: Schema Pro o similar

### WhatsApp Integration
- **Provider**: 360 diálogo o Twilio
- **API**: WhatsApp Business API v2.x
- **Backend**: Node.js 18+ o Python 3.10+
- **Automation Platform**: n8n, Zapier, o custom solution
- **Database**: Para almacenar conversaciones y estados

### CRM Integration
- **Platform**: HubSpot CRM (gratuito) o Pipedrive
- **API**: REST API v3 (HubSpot) o API v1 (Pipedrive)
- **Authentication**: OAuth 2.0 o API Key
- **Webhooks**: Para sincronización bidireccional

### Analytics & Tracking
- **Google Analytics**: GA4 (versión más reciente)
- **Google Tag Manager**: Container ID configurado
- **Google Search Console**: Propiedad verificada
- **Google Ads**: Cuenta estructurada con conversiones

---

## Integration Specifications

### WordPress ↔ WhatsApp

**Connection Method**: WhatsApp API links con parámetros UTM

**URL Format**:
```
https://wa.me/52[PHONE]?text=[ENCODED_MESSAGE]&utm_source=[SOURCE]&utm_medium=whatsapp&utm_campaign=[CAMPAIGN]&utm_content=[CONTENT]
```

**Parameters**:
- `utm_source`: Página de origen (ej: "homepage", "blog-article-1", "product-otc-5")
- `utm_medium`: Siempre "whatsapp"
- `utm_campaign**: Tipo de contenido (ej: "awareness", "consideration", "decision", "lead-magnet")
- `utm_content`: Elemento específico (ej: "hero-cta", "article-cta", "floating-button")

**Pre-fill Message Examples**:
- Desde homepage: "Hola, me interesa conocer más sobre medicamentos especializados."
- Desde artículo: "Hola, leí sobre [MEDICAMENTO]. Quisiera consultar disponibilidad."
- Desde producto OTC: "Hola, necesito información sobre medicamentos especializados."

---

### WhatsApp Bot ↔ CRM

**Integration Type**: REST API + Webhooks

**Data Flow**:
1. Bot detecta lead calificado (Rama B)
2. Bot captura datos: nombre, medicamento, ciudad, receta, email
3. Bot hace POST a CRM API creando contacto/deal
4. CRM responde con ID de registro
5. Bot actualiza conversación con ID de CRM
6. CRM webhook notifica a agente (Slack/Email/WhatsApp)

**CRM Fields Mapping**:

| Bot Data | CRM Field | Type | Required |
|----------|-----------|------|----------|
| Nombre completo | First Name + Last Name | String | Yes |
| Medicamento | Custom: Medicamento Solicitado | String | Yes |
| Ciudad/Estado | Custom: Ciudad | String | Yes |
| Tiene receta | Custom: Tiene Receta | Boolean | Yes |
| Email | Email | String | No |
| Urgencia detectada | Custom: Urgencia | Enum (Alta/Media/Baja) | No |
| Centro asignado | Custom: Centro Asignado | String | Auto |
| Timestamp | Created Date | DateTime | Auto |

**Webhook Payload Example**:
```json
{
  "event": "lead_calificado",
  "contact_id": "12345",
  "deal_id": "67890",
  "medicamento": "Medicamento X",
  "ciudad": "CDMX",
  "centro_asignado": "CDMX",
  "timestamp": "2026-02-15T10:30:00Z"
}
```

---

### WordPress ↔ Google Analytics 4

**Tracking Implementation**: Google Tag Manager + GA4

**Events to Track**:

1. **whatsapp_click**
   - Trigger: Click en cualquier botón WhatsApp
   - Parameters: page_path, page_title, cta_location, utm_source, utm_campaign

2. **form_submit**
   - Trigger: Submit de formulario de contacto
   - Parameters: form_name, page_path

3. **lead_magnet_download**
   - Trigger: Descarga de PDF
   - Parameters: guide_name, page_path

4. **external_link_click**
   - Trigger: Click en link externo (Farmalisto/Similares)
   - Parameters: link_url, link_text, page_path

5. **shopify_redirect**
   - Trigger: Click a farmaciasmacross.com.mx
   - Parameters: source_page, product_referenced

6. **article_read**
   - Trigger: Scroll >75% de artículo
   - Parameters: article_title, article_category, reading_time

7. **faq_expand**
   - Trigger: Expand de pregunta FAQ
   - Parameters: question_text, page_path

8. **popup_display**
   - Trigger: Display de pop-up
   - Parameters: popup_type, page_path

9. **popup_close**
   - Trigger: Cierre de pop-up
   - Parameters: popup_type, page_path, time_visible

10. **search_performed**
    - Trigger: Búsqueda en catálogo
    - Parameters: search_term, results_count

**Conversion Events** (marcados como conversiones en GA4):
- whatsapp_click
- form_submit
- lead_magnet_download
- shopify_redirect

---

### CRM ↔ Google Analytics 4

**Integration Method**: Measurement Protocol API o Data Import

**Data to Sync**:
- Leads creados desde bot → GA4 como evento "lead_created"
- Deals movidos a "Won" → GA4 como conversión "deal_won"
- Revenue (si disponible) → GA4 como parámetro de evento

**Frequency**: Real-time via webhook o batch cada hora

---

## Database Schema (Bot)

### Conversations Table
```sql
CREATE TABLE conversations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  whatsapp_id VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  status ENUM('active', 'closed', 'escalated'),
  current_flow VARCHAR(50),
  detected_intent VARCHAR(50),
  detected_medication VARCHAR(255),
  crm_contact_id VARCHAR(100),
  crm_deal_id VARCHAR(100),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  last_message_at TIMESTAMP
);
```

### Messages Table
```sql
CREATE TABLE messages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  conversation_id INT,
  direction ENUM('inbound', 'outbound'),
  message_text TEXT,
  message_type VARCHAR(50),
  timestamp TIMESTAMP,
  FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);
```

### Lead Data Table
```sql
CREATE TABLE lead_data (
  id INT PRIMARY KEY AUTO_INCREMENT,
  conversation_id INT,
  full_name VARCHAR(255),
  medication VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  has_prescription BOOLEAN,
  email VARCHAR(255),
  urgency ENUM('Alta', 'Media', 'Baja'),
  center_assigned VARCHAR(50),
  crm_synced BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP,
  FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);
```

---

## API Endpoints (Bot)

### Internal APIs

**POST /api/bot/webhook**
- Recibe mensajes de WhatsApp
- Valida firma
- Procesa mensaje
- Responde según lógica

**POST /api/bot/create-lead**
- Crea lead en CRM
- Asigna centro
- Notifica agente
- Retorna confirmación

**GET /api/bot/conversation/:id**
- Obtiene historial de conversación
- Para integración con CRM

**POST /api/bot/update-status**
- Actualiza estado de conversación
- Desde CRM o agente humano

---

## Security Requirements

### WordPress
- **SSL**: Obligatorio (HTTPS en todas las páginas)
- **WordPress Updates**: Automáticos para seguridad
- **Plugin Updates**: Revisión semanal
- **Backups**: Diarios automáticos (Hostinger o plugin)
- **File Permissions**: 644 para archivos, 755 para directorios
- **Database**: Usuario con permisos mínimos necesarios

### WhatsApp API
- **Webhook Verification**: Validar firma de WhatsApp en cada request
- **Rate Limiting**: Implementar límites para prevenir abuse
- **Error Handling**: Logging de errores sin exponer información sensible
- **API Keys**: Almacenar en variables de entorno, nunca en código

### CRM
- **OAuth 2.0**: Para autenticación (preferido sobre API keys)
- **Scope**: Permisos mínimos necesarios
- **Webhook Security**: Validar firma de webhooks
- **Data Encryption**: Datos sensibles encriptados en tránsito y reposo

### Analytics
- **IP Anonymization**: Activada en GA4
- **Cookie Consent**: Implementar según política de cookies
- **Data Retention**: Configurar según políticas de privacidad

---

## Performance Requirements

### WordPress Site
- **Page Load Time**: <3 segundos (conexión 3G)
- **Time to First Byte (TTFB)**: <600ms
- **Image Optimization**: 
  - WebP format
  - Lazy loading
  - Responsive images (srcset)
  - Max file size: 200KB por imagen
- **Caching**:
  - Browser caching: 1 año para assets estáticos
  - Page caching: 1 hora para páginas dinámicas
  - Object caching: Redis o Memcached (opcional)

### Bot Response Time
- **Initial Response**: <2 segundos
- **Message Processing**: <5 segundos
- **CRM Sync**: <10 segundos
- **Uptime**: 99.9% (excluyendo mantenimiento programado)

### API Response Times
- **WordPress API**: <500ms
- **CRM API Calls**: <2 segundos
- **WhatsApp API**: <3 segundos

---

## Browser & Device Support

### Desktop Browsers
- Chrome (últimas 2 versiones)
- Firefox (últimas 2 versiones)
- Safari (últimas 2 versiones)
- Edge (últimas 2 versiones)

### Mobile Browsers
- Chrome Mobile (Android)
- Safari Mobile (iOS)
- Samsung Internet

### Devices
- Desktop: 1920px, 1366px, 1280px
- Tablet: 1024px, 768px
- Mobile: 414px, 375px, 360px

### Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 1023px
- Desktop: ≥ 1024px

---

## Testing Requirements

### Functional Testing
- Todos los formularios funcionan correctamente
- Todos los CTAs redirigen correctamente
- WhatsApp links abren con mensaje pre-escrito
- Bot responde correctamente en todos los escenarios
- CRM sincroniza datos correctamente
- Analytics captura todos los eventos

### Performance Testing
- PageSpeed en todas las páginas principales
- Load testing del bot (100+ conversaciones simultáneas)
- API response time testing
- Database query optimization

### Security Testing
- SSL certificate válido
- SQL injection prevention
- XSS prevention
- CSRF protection
- API authentication/authorization

### Cross-Browser Testing
- Testing visual en todos los navegadores soportados
- Testing funcional en todos los navegadores
- Testing responsive en todos los dispositivos

### Integration Testing
- WordPress ↔ WhatsApp
- Bot ↔ CRM
- CRM ↔ Analytics
- Analytics ↔ Google Ads

---

## Monitoring & Logging

### Application Monitoring
- **Uptime Monitoring**: UptimeRobot, Pingdom, o similar
- **Error Tracking**: Sentry, Rollbar, o similar
- **Performance Monitoring**: New Relic, Datadog, o similar

### Logging Requirements
- **Application Logs**: Todas las acciones del bot
- **Error Logs**: Todos los errores con stack traces
- **API Logs**: Todas las llamadas a APIs externas
- **Analytics Logs**: Eventos importantes para debugging

### Alerting
- **Critical Errors**: Notificación inmediata (Slack/Email)
- **Performance Degradation**: Alerta si response time >5s
- **Uptime Issues**: Alerta si downtime >5 minutos
- **CRM Sync Failures**: Alerta si sincronización falla

---

## Backup & Recovery

### WordPress
- **Backup Frequency**: Diario automático
- **Retention**: 30 días
- **Backup Location**: Hostinger backup + external storage (opcional)
- **Recovery Time Objective (RTO)**: <4 horas
- **Recovery Point Objective (RPO)**: 24 horas máximo

### Database (Bot)
- **Backup Frequency**: Cada 6 horas
- **Retention**: 7 días
- **Backup Location**: Cloud storage (AWS S3, Google Cloud Storage, o similar)

### CRM
- **Backup**: Responsabilidad del proveedor (HubSpot/Pipedrive)
- **Export Manual**: Semanal de datos críticos

---

## Deployment Process

### WordPress
1. Desarrollo en staging environment
2. Testing en staging
3. Backup de producción
4. Deploy a producción
5. Smoke testing post-deploy
6. Rollback plan si necesario

### Bot
1. Desarrollo en desarrollo environment
2. Testing en staging con WhatsApp sandbox
3. Deploy a producción
4. Monitoring de primeros minutos
5. Rollback plan si necesario

### Configuration Management
- **Environment Variables**: Para todas las configuraciones sensibles
- **Version Control**: Git para todo el código
- **Documentation**: Actualizada con cada cambio

---

## Third-Party Services

### Required Services
- **Hostinger**: Hosting WordPress
- **WhatsApp Business API**: 360 diálogo o Twilio
- **CRM**: HubSpot CRM (gratuito) o Pipedrive
- **Google Analytics**: GA4 (gratuito)
- **Google Tag Manager**: (gratuito)
- **Google Search Console**: (gratuito)
- **Google Ads**: (pago según presupuesto cliente)

### Optional Services
- **CDN**: Cloudflare, KeyCDN, o similar
- **Email Service**: Para emails automatizados (SendGrid, Mailgun, o similar)
- **Monitoring**: UptimeRobot, Sentry, o similar
- **Backup Service**: External backup storage

---

## Compliance & Legal

### COFEPRIS Compliance
- Aviso de Privacidad actualizado y visible
- Disclaimers médicos en todas las páginas relevantes
- Política de cookies implementada
- Términos y Condiciones del sector salud

### Data Privacy
- **GDPR Compliance**: Si aplica (usuarios internacionales)
- **LGPD Compliance**: Si aplica (usuarios brasileños)
- **Data Retention**: Política clara de retención de datos
- **User Rights**: Proceso para ejercer derechos de acceso/eliminación

### WhatsApp Compliance
- Templates aprobados por WhatsApp
- Políticas de WhatsApp respetadas
- Opt-out mechanism implementado
- Rate limits respetados

---

## Scalability Considerations

### Current Capacity
- **WordPress**: Soporta 10,000+ visitas/mes sin problemas
- **Bot**: Soporta 100+ conversaciones simultáneas
- **CRM**: Límites según plan (HubSpot gratuito: 1M contactos, Pipedrive: según plan)

### Future Scaling
- **WordPress**: CDN y caching avanzado si tráfico >50K visitas/mes
- **Bot**: Load balancing si >500 conversaciones simultáneas
- **CRM**: Upgrade de plan si necesario
- **Database**: Optimización de queries, índices, particionamiento si >1M registros

---

## Documentation Requirements

### Technical Documentation
- **API Documentation**: Endpoints, parámetros, respuestas
- **Database Schema**: Diagramas y descripciones
- **Deployment Guide**: Proceso paso a paso
- **Troubleshooting Guide**: Problemas comunes y soluciones

### User Documentation
- **Manual de Operación**: Para equipo del cliente
- **Scripts de Conversación**: Para agentes
- **Guía de CRM**: Navegación y uso
- **Guía de Dashboard**: Interpretación de métricas

---

## Change Management

### Code Changes
- **Version Control**: Git con branches por feature
- **Code Review**: Obligatorio antes de merge
- **Testing**: Obligatorio antes de deploy
- **Documentation**: Actualizada con cada cambio

### Configuration Changes
- **Change Log**: Registro de todos los cambios
- **Approval Process**: Aprobación antes de cambios en producción
- **Rollback Plan**: Plan de reversión para cada cambio

---

## Support & Maintenance

### Post-Launch Support (45 días)
- **Response Time**: <4 horas hábiles
- **Critical Issues**: <2 horas
- **Support Channels**: WhatsApp, Email, Slack

### Maintenance Windows
- **Scheduled Maintenance**: Domingos 2-4 AM (tiempo México)
- **Emergency Maintenance**: Cuando sea necesario, con notificación previa

### Update Schedule
- **WordPress Core**: Actualización mensual
- **Plugins**: Actualización semanal
- **Security Patches**: Inmediato
- **Feature Updates**: Según roadmap del proyecto

---

## Notes

- Todas las configuraciones sensibles deben estar en variables de entorno
- No hardcodear credenciales, API keys, o información sensible
- Documentar todas las decisiones técnicas importantes
- Mantener changelog actualizado
- Revisar y actualizar esta documentación mensualmente





