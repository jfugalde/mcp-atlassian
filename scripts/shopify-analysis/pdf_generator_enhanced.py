"""Enhanced PDF generator with comprehensive audit report structure."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


class EnhancedPDFReportGenerator:
    """Generate comprehensive PDF audit report in Spanish."""

    def __init__(self, output_path: Path):
        """Initialize PDF generator."""
        self.output_path = output_path
        self.story = []
        self.styles = getSampleStyleSheet()
        
        # Custom styles
        self.title_style = ParagraphStyle(
            "CustomTitle",
            parent=self.styles["Heading1"],
            fontSize=24,
            textColor=colors.HexColor("#1a1a1a"),
            spaceAfter=12,
            alignment=1,  # Center
        )
        
        self.heading1_style = ParagraphStyle(
            "CustomHeading1",
            parent=self.styles["Heading1"],
            fontSize=18,
            textColor=colors.HexColor("#2c3e50"),
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )
        
        self.heading2_style = ParagraphStyle(
            "CustomHeading2",
            parent=self.styles["Heading2"],
            fontSize=14,
            textColor=colors.HexColor("#34495e"),
            spaceAfter=8,
            fontName="Helvetica-Bold",
        )
        
        self.heading3_style = ParagraphStyle(
            "CustomHeading3",
            parent=self.styles["Heading3"],
            fontSize=12,
            textColor=colors.HexColor("#34495e"),
            spaceAfter=6,
            fontName="Helvetica-Bold",
        )
        
        self.body_style = ParagraphStyle(
            "CustomBody",
            parent=self.styles["BodyText"],
            fontSize=10,
            leading=14,
            spaceAfter=6,
        )
        
        self.bullet_style = ParagraphStyle(
            "Bullet",
            parent=self.body_style,
            leftIndent=20,
            bulletIndent=10,
            spaceAfter=4,
        )

    def add_title_page(self):
        """Add title page."""
        self.story.append(Spacer(1, 2 * inch))
        self.story.append(Paragraph("AUDITORÍA TÉCNICA", self.title_style))
        self.story.append(Spacer(1, 0.3 * inch))
        self.story.append(
            Paragraph("del sitio farmaciasmacross.com.mx", self.heading1_style)
        )
        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(
            Paragraph(
                f"Fecha: {datetime.now().strftime('%d de %B de %Y')}",
                self.body_style,
            )
        )
        self.story.append(PageBreak())

    def add_table_of_contents(self):
        """Add table of contents."""
        self.story.append(Paragraph("Índice", self.heading1_style))
        self.story.append(Spacer(1, 0.3 * inch))
        
        sections = [
            "Resumen ejecutivo",
            "Metodología",
            "Estructura y navegación",
            "Hallazgos técnicos",
            "  – 4.1 Rendimiento y experiencia de usuario",
            "  – 4.2 Compatibilidad y accesibilidad",
            "  – 4.3 Seguridad y privacidad",
            "  – 4.4 SEO on-page",
            "  – 4.5 Cumplimiento legal",
            "  – 4.6 Plugins, scripts y dependencias",
            "  – 4.7 Hosting y configuración",
            "Matriz de hallazgos priorizados",
            "Recomendaciones técnicas",
            "Conclusiones",
            "Referencias",
        ]
        
        for section in sections:
            self.story.append(Paragraph(section, self.body_style))
        
        self.story.append(PageBreak())

    def add_executive_summary(self, findings_data: Dict):
        """Add executive summary section."""
        self.story.append(Paragraph("Resumen ejecutivo", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        findings_list = findings_data.get("findings", [])
        priority_matrix = findings_data.get("priority_matrix", {})
        
        high_count = len(priority_matrix.get("High", []))
        medium_count = len(priority_matrix.get("Medium", []))
        low_count = len(priority_matrix.get("Low", []))
        
        content = [
            "El sitio farmaciasmacross.com.mx es la tienda en línea de Macross Pharma para medicamentos de alta especialidad. Se trata de un comercio electrónico basado en Shopify con un diseño moderno, pero carga numerosos scripts de análisis y widgets que provocan un rendimiento lento.",
            "",
            f"Durante la auditoría se identificaron {len(findings_list)} hallazgos, entre ellos enlaces rotos, contradicciones en las políticas de privacidad, falta de cumplimiento de accesibilidad, tiempos de carga altos y carencia de optimización para SEO.",
            "",
            "Las principales conclusiones son:",
            "",
            "• Rendimiento lento y recursos pesados: el sitio carga imágenes muy grandes en el hero y multiplica los scripts de análisis (Google Tag Manager, Facebook Pixel, Trekkie de Shopify, Reputon). Esto afecta negativamente el Largest Contentful Paint (LCP), el tiempo de interactividad y el Core Web Vitals.",
            "",
            "• Enlaces rotos y navegación confusa: existe un enlace de navegación titulado \"Acerca del servicio\" que redirige a los Términos del servicio, mientras que la ruta /acerca-del-servicio devuelve error 404.",
            "",
            "• Contradicción en políticas de privacidad: la política declara que no se utilizan cookies ni web beacons, pero el código fuente evidencia el uso de Google Tag Manager, Facebook Pixel y otros scripts de seguimiento.",
            "",
            "• Cumplimiento legal incompleto: aunque existen políticas de envío, reembolsos y términos de servicio, faltan menús claros con enlaces visibles a estos documentos desde el pie de página y carecen de un aviso de aceptación de cookies, requerido por la legislación mexicana.",
            "",
            "• SEO deficiente: hay meta descripciones en la página de inicio, pero muchas páginas carecen de contenido significativo. El sitio no implementa marcado schema org para productos o negocio local, perdiendo visibilidad en buscadores.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def add_methodology(self):
        """Add methodology section."""
        self.story.append(Paragraph("Metodología", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        content = [
            f"La auditoría se realizó entre el 6 y 7 de diciembre de {datetime.now().year}. Se emplearon las siguientes herramientas y pasos:",
            "",
            "1. Navegación manual: se recorrieron las páginas principales del sitio: la página de inicio, productos, búsqueda, páginas informativas (nosotros, preguntas frecuentes, licencias, atención persona a persona), políticas y términos. Se tomaron capturas de pantalla para evidenciar problemas y se registró la estructura de URLs.",
            "",
            "2. Inspección de código fuente: se usó la función view-source: para analizar la estructura del HTML y las cabeceras. Se revisaron las metaetiquetas (título, descripción, canonical, robots), el marcado JSON-LD, las hojas de estilos y scripts cargados.",
            "",
            "3. Revisión de políticas y cumplimiento: se leyeron las políticas de privacidad, términos de servicio, reembolsos y envíos para evaluar su claridad y coherencia. Se verificó si el contenido cumple con la normatividad mexicana (Ley Federal de Protección de Datos Personales) y la normativa internacional aplicable.",
            "",
            "4. Análisis de performance: se utilizó Google PageSpeed Insights para medir métricas de rendimiento, Core Web Vitals (LCP, CLS, FID) y puntuaciones de accesibilidad, mejores prácticas y SEO.",
            "",
            "5. Priorización: los hallazgos se clasificaron según su impacto (alto, medio, bajo) y complejidad de implementación. Se asignó una prioridad con base en el efecto sobre los usuarios y el negocio.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def add_structure_navigation(self):
        """Add structure and navigation section."""
        self.story.append(Paragraph("Estructura y navegación", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        content = [
            "La página de inicio presenta un encabezado con menú principal, selector de idioma, buscador, iconos de usuario y carrito, y una barra de promoción. A continuación se muestra una hero image de gran tamaño con texto y un botón de \"Programa de Continuidad\", destinada a fidelizar clientes.",
            "",
            "El menú principal contiene los enlaces \"Nosotros\", \"Preguntas frecuentes\", \"Acerca del servicio\", \"Nuestras licencias\" y \"Atención persona a persona\". No obstante, se detectó que el enlace \"Acerca del servicio\" redirige en realidad a los Términos del servicio (policies/terms-of-service), mientras que la ruta intuitiva /acerca-del-servicio devuelve un error 404. Esto crea confusión para los usuarios y afecta el rastreo de buscadores.",
            "",
            "La navegación utiliza menús desplegables para categorías de medicamentos; sin embargo, hay páginas internas con muy poco contenido. Por ejemplo, \"Nuestras licencias\" muestra únicamente logotipos y carece de texto. La página \"Acerca de nosotros\" se limita a una imagen y un enlace a un video.",
            "",
            "El buscador interno permite encontrar productos por nombre; se probó la búsqueda de \"Zytiga\", que devuelve variantes de 500mg y 250mg. Sin embargo, la funcionalidad de filtros es limitada y no hay categorías visibles en los resultados.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def add_technical_findings(self, findings_data: Dict, psi_results: Dict, onpage_results: Dict):
        """Add technical findings section with subsections."""
        self.story.append(Paragraph("Hallazgos técnicos", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        findings_list = findings_data.get("findings", [])
        
        # Group findings by category
        performance_findings = []
        accessibility_findings = []
        security_findings = []
        seo_findings = []
        compliance_findings = []
        plugins_findings = []
        hosting_findings = []
        
        for finding in findings_list:
            title_lower = finding.get("title", "").lower()
            if any(term in title_lower for term in ["rendimiento", "performance", "lcp", "carga", "script", "imagen", "hero"]):
                performance_findings.append(finding)
            elif any(term in title_lower for term in ["accesibilidad", "accessibility", "aria", "alt", "contraste"]):
                accessibility_findings.append(finding)
            elif any(term in title_lower for term in ["seguridad", "security", "hsts", "cookie", "privacidad", "header"]):
                security_findings.append(finding)
            elif any(term in title_lower for term in ["seo", "meta", "schema", "canonical", "descripción"]):
                seo_findings.append(finding)
            elif any(term in title_lower for term in ["legal", "compliance", "política", "licencia", "términos"]):
                compliance_findings.append(finding)
            elif any(term in title_lower for term in ["plugin", "script", "dependencia", "widget"]):
                plugins_findings.append(finding)
            elif any(term in title_lower for term in ["hosting", "cdn", "backup", "servidor"]):
                hosting_findings.append(finding)
            else:
                # Default to performance if unclear
                performance_findings.append(finding)
        
        # 4.1 Performance
        self.story.append(Paragraph("4.1 Rendimiento y experiencia de usuario", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        for i, finding in enumerate(performance_findings[:6], 1):
            self._add_finding_detail(finding, i)
        
        self.story.append(PageBreak())
        
        # 4.2 Accessibility
        self.story.append(Paragraph("4.2 Compatibilidad y accesibilidad", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        for i, finding in enumerate(accessibility_findings[:3], 1):
            self._add_finding_detail(finding, i)
        
        self.story.append(PageBreak())
        
        # 4.3 Security
        self.story.append(Paragraph("4.3 Seguridad y privacidad", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        for i, finding in enumerate(security_findings[:4], 1):
            self._add_finding_detail(finding, i)
        
        self.story.append(PageBreak())
        
        # 4.4 SEO
        self.story.append(Paragraph("4.4 SEO on-page", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        for i, finding in enumerate(seo_findings[:4], 1):
            self._add_finding_detail(finding, i)
        
        self.story.append(PageBreak())
        
        # 4.5 Compliance
        self.story.append(Paragraph("4.5 Cumplimiento legal", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        for i, finding in enumerate(compliance_findings[:4], 1):
            self._add_finding_detail(finding, i)
        
        self.story.append(PageBreak())
        
        # 4.6 Plugins
        self.story.append(Paragraph("4.6 Plugins, scripts y dependencias", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        content = [
            "El sitio utiliza Shopify, por lo que no hay plugins como en WordPress, pero se identificaron numerosos scripts externos:",
            "",
            "• Google Tag Manager y Facebook Pixel para analítica y remarketing.",
            "",
            "• Trekkie (script nativo de Shopify para análisis de tráfico).",
            "",
            "• Reputon para mostrar reseñas de Google, cargando scripts adicionales.",
            "",
            "• foxkit-app y vendor.min.js pertenecientes al tema Minimog.",
            "",
            "• Widgets de chat y WhatsApp para atención al cliente.",
            "",
            "Todos estos componentes aumentan el peso de la página y requieren actualizaciones periódicas para evitar vulnerabilidades.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())
        
        # 4.7 Hosting
        self.story.append(Paragraph("4.7 Hosting y configuración", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        content = [
            "El sitio está alojado en la infraestructura de Shopify, por lo que la optimización de servidores y CDN es gestionada por la plataforma. No obstante, es posible configurar parámetros a nivel de tema y aplicaciones:",
            "",
            "• CDN de Shopify: las imágenes y archivos estáticos se sirven desde cdn.shopify.com, lo que mejora la distribución global, pero las imágenes siguen siendo pesadas si no se optimizan previamente.",
            "",
            "• HTTP/2 y TLS: Shopify utiliza HTTPS con TLS moderno. Sin embargo, no se encontró encabezado HTTP Strict-Transport-Security, que podría reforzar la seguridad.",
            "",
            "• Sin backups visibles: no se visualiza información sobre copias de seguridad regulares ni procedimientos de recuperación ante desastres. Al ser una plataforma SaaS, Shopify ofrece redundancia, pero se recomienda un plan de contingencia.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def _add_finding_detail(self, finding: Dict, number: int):
        """Add detailed finding information."""
        import re
        
        def escape_html_tags(text: str) -> str:
            """Escape HTML tags that ReportLab can't parse."""
            # Replace <link> tags with plain text
            text = re.sub(r'<link[^>]*>', '', text)
            # Replace other problematic tags but keep <b>, <i>, <u>
            text = re.sub(r'<(?![/]?[biu]>)[^>]+>', '', text)
            return text
        
        title = escape_html_tags(finding.get('title', ''))
        description = escape_html_tags(finding.get('description', ''))
        impact = escape_html_tags(finding.get('impact', ''))
        recommendation = escape_html_tags(finding.get('recommendation', ''))
        
        self.story.append(
            Paragraph(f"{number}. {title}", self.heading3_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(f"<b>Descripción:</b> {description}", self.body_style)
        )
        self.story.append(Spacer(1, 0.05 * inch))
        
        self.story.append(
            Paragraph(f"<b>Impacto:</b> {impact}", self.body_style)
        )
        self.story.append(Spacer(1, 0.05 * inch))
        
        self.story.append(
            Paragraph(f"<b>Recomendación:</b> {recommendation}", self.body_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))

    def add_priority_matrix(self, findings_data: Dict):
        """Add prioritized findings matrix."""
        self.story.append(Paragraph("Matriz de hallazgos priorizados", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        priority_matrix = findings_data.get("priority_matrix", {})
        findings_list = findings_data.get("findings", [])
        
        # Create table data
        data = [["Nº", "Hallazgo", "Impacto", "Prioridad", "Recomendación"]]
        
        for i, finding in enumerate(findings_list, 1):
            title = finding.get("title", "")[:50] + "..." if len(finding.get("title", "")) > 50 else finding.get("title", "")
            impact = finding.get("impact", "")[:40] + "..." if len(finding.get("impact", "")) > 40 else finding.get("impact", "")
            priority = finding.get("priority", "")
            recommendation = finding.get("recommendation", "")[:50] + "..." if len(finding.get("recommendation", "")) > 50 else finding.get("recommendation", "")
            
            data.append([str(i), title, impact, priority, recommendation])
        
        table = Table(data, colWidths=[0.4 * inch, 2.5 * inch, 1.5 * inch, 0.8 * inch, 2.3 * inch])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#34495e")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 8),
                    ("FONTSIZE", (0, 1), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        
        self.story.append(table)
        self.story.append(PageBreak())

    def add_recommendations(self):
        """Add technical recommendations section."""
        self.story.append(Paragraph("Recomendaciones técnicas", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        self.story.append(Paragraph("Acciones de alto impacto y baja complejidad (≤ 1 semana)", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        quick_wins = [
            "1. Optimizar imágenes: Reducir tamaño de los banners; generar variantes en formato WebP y usar srcset para dispositivos móviles.",
            "",
            "2. Corregir enlaces rotos: Actualizar el enlace \"Acerca del servicio\" en el menú para que apunte a una página adecuada y crear redirecciones 301.",
            "",
            "3. Actualizar políticas de privacidad: Revisar con asesor legal y detallar qué cookies y scripts se usan. Implementar un banner de consentimiento de cookies.",
            "",
            "4. Agregar meta descripciones y contenido: Redactar descripciones únicas para cada página. Incluir contenido relevante en Nuestras licencias y Acerca de nosotros.",
            "",
            "5. Añadir alt y atributos ARIA: Revisar todas las imágenes y agregar texto alternativo relevante; añadir atributos aria a menús y botones.",
        ]
        
        for item in quick_wins:
            if item:
                self.story.append(Paragraph(item, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())
        
        self.story.append(Paragraph("Acciones de impacto medio y esfuerzo medio (1–3 semanas)", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        medium_effort = [
            "1. Reconfigurar scripts de tracking: Consolidar las herramientas de analítica y marketing para evitar duplicidad de scripts.",
            "",
            "2. Implementar datos estructurados: Utilizar las etiquetas JSON-LD recomendadas por schema.org para productos, negocio local y reseñas.",
            "",
            "3. Mejorar la accesibilidad: Ajustar el contraste de botones y textos; habilitar navegación por teclado; añadir roles y etiquetas ARIA.",
            "",
            "4. Mejorar políticas de envío y reembolso: Revisar la redacción para aclarar plazos, condiciones, opciones de cancelación y devoluciones.",
            "",
            "5. Revisar licencias: Publicar en texto los números de licencia sanitarios y enlace a la autoridad (COFEPRIS).",
        ]
        
        for item in medium_effort:
            if item:
                self.story.append(Paragraph(item, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())
        
        self.story.append(Paragraph("Acciones de impacto alto y esfuerzo alto (> 3 semanas)", self.heading2_style))
        self.story.append(Spacer(1, 0.1 * inch))
        
        high_effort = [
            "1. Implementar optimización avanzada (Core Web Vitals): Considerar dividir el sitio en secciones cargadas bajo demanda, aplicar técnicas de lazy load para videos y carruseles.",
            "",
            "2. Configurar encabezados de seguridad: Utilizar aplicaciones o proxies (por ejemplo, Cloudflare) para establecer políticas de seguridad HTTP como Content-Security-Policy, Strict-Transport-Security.",
            "",
            "3. Auditoría legal integral: Solicitar asesoría legal para revisar el cumplimiento de la Ley Federal de Protección de Datos Personales y la NOM-024-SSA3-2012.",
            "",
            "4. Plan de contingencia y backups: Elaborar un plan de respaldo de datos y establecer procedimientos de recuperación ante desastres.",
        ]
        
        for item in high_effort:
            if item:
                self.story.append(Paragraph(item, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def add_conclusions(self):
        """Add conclusions section."""
        self.story.append(Paragraph("Conclusiones", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        content = [
            "La auditoría revela que farmaciasmacross.com.mx tiene potencial para ofrecer una experiencia de compra efectiva de medicamentos de alta especialidad; sin embargo, los problemas técnicos y de cumplimiento identificados pueden comprometer la reputación y desempeño del sitio.",
            "",
            "La combinación de imágenes pesadas, numerosos scripts de análisis y contenido insuficiente reduce la velocidad de carga, afecta el SEO y puede vulnerar la privacidad de los usuarios. Además, la navegación confusa y la poca claridad de las políticas restan confianza.",
            "",
            "Implementar las recomendaciones aquí expuestas permitirá mejorar la experiencia de usuario, cumplir con la normativa aplicable y optimizar la visibilidad en buscadores. Con acciones relativamente sencillas como optimizar imágenes y corregir enlaces rotos, el sitio puede obtener mejoras significativas a corto plazo. A mediano plazo, la adopción de prácticas de accesibilidad y legalidad robusta consolidará la reputación de la marca. Finalmente, la adopción de técnicas avanzadas de rendimiento y seguridad asegurará la escalabilidad y confiabilidad del sitio en el futuro.",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())

    def add_references(self):
        """Add references section."""
        self.story.append(Paragraph("Referencias", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        content = [
            "Las siguientes referencias se citaron a lo largo del documento:",
            "",
            "• Google PageSpeed Insights - Análisis de performance y Core Web Vitals",
            "",
            "• Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP)",
            "",
            "• Norma Oficial Mexicana NOM-024-SSA3-2012 - Requisitos para comercio electrónico de medicamentos",
            "",
            "• Web Content Accessibility Guidelines (WCAG) 2.1",
            "",
            "• Schema.org - Marcado estructurado para datos enriquecidos",
            "",
            "• Shopify Theme Documentation - Minimog theme",
        ]
        
        for para in content:
            if para:
                self.story.append(Paragraph(para, self.body_style))
            else:
                self.story.append(Spacer(1, 0.1 * inch))

    def generate(self, data: Dict):
        """Generate complete PDF report."""
        findings_data = data.get("findings", {})
        psi_results = data.get("psi_results", {})
        onpage_results = data.get("onpage_results", {})
        
        # Title page
        self.add_title_page()
        
        # Table of contents
        self.add_table_of_contents()
        
        # Executive summary
        self.add_executive_summary(findings_data)
        
        # Methodology
        self.add_methodology()
        
        # Structure and navigation
        self.add_structure_navigation()
        
        # Technical findings
        self.add_technical_findings(findings_data, psi_results, onpage_results)
        
        # Priority matrix
        self.add_priority_matrix(findings_data)
        
        # Recommendations
        self.add_recommendations()
        
        # Conclusions
        self.add_conclusions()
        
        # References
        self.add_references()
        
        # Build PDF
        doc = SimpleDocTemplate(
            str(self.output_path),
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )
        doc.build(self.story)
        
        print(f"✓ Enhanced PDF report generated: {self.output_path}")


def main():
    """Main function to generate enhanced PDF report."""
    docs_dir = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
    
    # Load findings
    findings_path = docs_dir / "findings.json"
    if not findings_path.exists():
        print(f"Error: Findings file not found at {findings_path}")
        print("Please run findings_generator.py first.")
        return
    
    with open(findings_path, "r", encoding="utf-8") as f:
        findings_data = json.load(f)
    
    # Load PSI results
    psi_summary_path = docs_dir / "perf_runs" / "summary.json"
    psi_results = {}
    if psi_summary_path.exists():
        with open(psi_summary_path, "r", encoding="utf-8") as f:
            psi_results = json.load(f)
    
    # Load on-page results
    onpage_path = docs_dir / "onpage_analysis.json"
    onpage_results = {}
    if onpage_path.exists():
        with open(onpage_path, "r", encoding="utf-8") as f:
            onpage_results = json.load(f)
    
    # Generate PDF
    output_path = docs_dir / "farmaciasmacross-audit-enhanced.pdf"
    generator = EnhancedPDFReportGenerator(output_path)
    generator.generate({
        "findings": findings_data,
        "psi_results": psi_results,
        "onpage_results": onpage_results,
    })
    
    print(f"\n✓ Enhanced PDF report saved to: {output_path}")


if __name__ == "__main__":
    main()

