"""Generate PDF report from audit findings."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
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


class PDFReportGenerator:
    """Generate PDF audit report."""

    def __init__(self, output_path: Path):
        """
        Initialize PDF generator.
        
        Args:
            output_path: Path to save PDF file.
        """
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
        )
        
        self.heading1_style = ParagraphStyle(
            "CustomHeading1",
            parent=self.styles["Heading1"],
            fontSize=18,
            textColor=colors.HexColor("#2c3e50"),
            spaceAfter=12,
        )
        
        self.heading2_style = ParagraphStyle(
            "CustomHeading2",
            parent=self.styles["Heading2"],
            fontSize=14,
            textColor=colors.HexColor("#34495e"),
            spaceAfter=8,
        )
        
        self.body_style = ParagraphStyle(
            "CustomBody",
            parent=self.styles["BodyText"],
            fontSize=10,
            leading=14,
            spaceAfter=6,
        )

    def add_title_page(self, site_url: str):
        """Add title page."""
        self.story.append(Spacer(1, 2 * inch))
        self.story.append(Paragraph("AUDITORÍA TÉCNICA", self.title_style))
        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(Paragraph(site_url, self.heading1_style))
        self.story.append(Spacer(1, 0.3 * inch))
        self.story.append(
            Paragraph(
                f"Fecha: {datetime.now().strftime('%d de %B de %Y')}",
                self.body_style,
            )
        )
        self.story.append(PageBreak())

    def add_table_of_contents(self, sections: List[str]):
        """Add table of contents."""
        self.story.append(Paragraph("ÍNDICE", self.heading1_style))
        self.story.append(Spacer(1, 0.3 * inch))
        
        for i, section in enumerate(sections, 1):
            self.story.append(
                Paragraph(f"{i}. {section}", self.body_style)
            )
        
        self.story.append(PageBreak())

    def add_section(self, title: str, content: List):
        """Add a section with title and content."""
        self.story.append(Paragraph(title, self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        for item in content:
            if isinstance(item, str):
                self.story.append(Paragraph(item, self.body_style))
            elif isinstance(item, Table):
                self.story.append(item)
                self.story.append(Spacer(1, 0.2 * inch))
            elif isinstance(item, Spacer):
                self.story.append(item)
        
        self.story.append(PageBreak())

    def add_findings_table(self, findings: List[Dict], priority: str):
        """Add findings table for a priority level."""
        if not findings:
            return
        
        data = [["#", "Título", "Prioridad", "Esfuerzo"]]
        
        for i, finding in enumerate(findings, 1):
            data.append(
                [
                    str(i),
                    finding.get("title", ""),
                    finding.get("priority", ""),
                    finding.get("effort", ""),
                ]
            )
        
        table = Table(data, colWidths=[0.5 * inch, 4 * inch, 1 * inch, 1 * inch])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#34495e")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, 0), 10),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
                ]
            )
        )
        
        return table

    def add_finding_detail(self, finding: Dict, number: int):
        """Add detailed finding information."""
        self.story.append(
            Paragraph(f"{number}. {finding.get('title', '')}", self.heading2_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(f"<b>Descripción:</b> {finding.get('description', '')}", self.body_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(f"<b>Impacto:</b> {finding.get('impact', '')}", self.body_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(f"<b>Prioridad:</b> {finding.get('priority', '')}", self.body_style)
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(
                f"<b>Recomendación:</b> {finding.get('recommendation', '')}",
                self.body_style,
            )
        )
        self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(
            Paragraph(
                f"<b>Esfuerzo Estimado:</b> {finding.get('effort', '')}",
                self.body_style,
            )
        )
        
        evidence = finding.get("evidence", [])
        if evidence:
            self.story.append(Spacer(1, 0.1 * inch))
            self.story.append(Paragraph("<b>Evidencia:</b>", self.body_style))
            for ev in evidence[:5]:  # Limit to 5 items
                self.story.append(
                    Paragraph(f"• {ev}", self.body_style)
                )
        
        self.story.append(Spacer(1, 0.2 * inch))

    def generate(self, data: Dict):
        """
        Generate complete PDF report.
        
        Args:
            data: Dictionary containing all analysis data.
        """
        # Title page
        site_url = "https://farmaciasmacross.com.mx"
        self.add_title_page(site_url)
        
        # Table of contents
        sections = [
            "Metodología",
            "Resumen Ejecutivo",
            "URLs Analizadas",
            "Análisis de Performance",
            "Análisis SEO On-Page",
            "Análisis de Seguridad",
            "Matriz de Priorización",
            "Hallazgos Detallados",
            "Recomendaciones y Próximos Pasos",
        ]
        self.add_table_of_contents(sections)
        
        # Methodology
        methodology_content = [
            "Este informe presenta los resultados de una auditoría técnica completa realizada en el sitio web farmaciasmacross.com.mx.",
            "",
            "La auditoría incluye:",
            "• Análisis de performance mediante PageSpeed Insights",
            "• Evaluación de elementos SEO on-page",
            "• Revisión de seguridad y headers HTTP",
            "• Análisis de compliance y documentos legales",
            "• Identificación de problemas técnicos y oportunidades de mejora",
            "",
            "Las pruebas se realizaron en una muestra representativa de URLs del sitio, incluyendo páginas principales, categorías, productos, y páginas legales.",
        ]
        self.add_section("1. Metodología", methodology_content)
        
        # Executive summary
        findings_data = data.get("findings", {})
        findings_list = findings_data.get("findings", [])
        priority_matrix = findings_data.get("priority_matrix", {})
        
        high_count = len(priority_matrix.get("High", []))
        medium_count = len(priority_matrix.get("Medium", []))
        low_count = len(priority_matrix.get("Low", []))
        
        summary_content = [
            f"<b>Total de Hallazgos:</b> {len(findings_list)}",
            "",
            f"<b>Prioridad Alta:</b> {high_count}",
            f"<b>Prioridad Media:</b> {medium_count}",
            f"<b>Prioridad Baja:</b> {low_count}",
            "",
            "Los hallazgos de alta prioridad requieren atención inmediata debido a su impacto en seguridad, performance, o compliance. Los hallazgos de prioridad media y baja representan oportunidades de optimización.",
        ]
        self.add_section("2. Resumen Ejecutivo", summary_content)
        
        # URLs analyzed
        url_set_path = (
            Path(__file__).parent.parent.parent
            / "docs"
            / "shopify-analysis"
            / "url_set.json"
        )
        url_content = []
        if url_set_path.exists():
            with open(url_set_path, "r", encoding="utf-8") as f:
                selected_urls = json.load(f)
            
            url_content.append(f"<b>Total de URLs analizadas:</b> {len(selected_urls)}")
            url_content.append("")
            url_content.append("<b>URLs por categoría:</b>")
            
            by_category = {}
            for item in selected_urls:
                cat = item.get("category", "other")
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(item.get("url", ""))
            
            for cat, urls in sorted(by_category.items()):
                url_content.append(f"• {cat.title()}: {len(urls)} URLs")
        else:
            url_content.append("Información de URLs no disponible.")
        
        self.add_section("3. URLs Analizadas", url_content)
        
        # Performance analysis
        perf_content = [
            "Los resultados de PageSpeed Insights muestran métricas clave de performance incluyendo Core Web Vitals (LCP, CLS, FCP).",
            "",
            "Se analizaron todas las URLs seleccionadas tanto en dispositivos móviles como desktop.",
        ]
        self.add_section("4. Análisis de Performance", perf_content)
        
        # SEO analysis
        seo_content = [
            "El análisis SEO on-page incluye:",
            "• Meta tags (title, description)",
            "• Estructura de headings (H1-H6)",
            "• Schema markup (JSON-LD)",
            "• Open Graph y Twitter Cards",
            "• Canonical tags",
            "• Hreflang tags",
        ]
        self.add_section("5. Análisis SEO On-Page", seo_content)
        
        # Security analysis
        security_content = [
            "El análisis de seguridad incluye:",
            "• Headers HTTP de seguridad (HSTS, X-Frame-Options, etc.)",
            "• Detección de contenido mixto (HTTP sobre HTTPS)",
            "• Redirecciones HTTPS",
            "• Configuración de seguridad general",
        ]
        self.add_section("6. Análisis de Seguridad", security_content)
        
        # Priority matrix
        matrix_content = []
        
        if high_count > 0:
            matrix_content.append(Paragraph("Hallazgos de Alta Prioridad", self.heading2_style))
            matrix_content.append(Spacer(1, 0.1 * inch))
            high_table = self.add_findings_table(priority_matrix.get("High", []), "High")
            if high_table:
                matrix_content.append(high_table)
                matrix_content.append(Spacer(1, 0.3 * inch))
        
        if medium_count > 0:
            matrix_content.append(Paragraph("Hallazgos de Prioridad Media", self.heading2_style))
            matrix_content.append(Spacer(1, 0.1 * inch))
            medium_table = self.add_findings_table(priority_matrix.get("Medium", []), "Medium")
            if medium_table:
                matrix_content.append(medium_table)
                matrix_content.append(Spacer(1, 0.3 * inch))
        
        if low_count > 0:
            matrix_content.append(Paragraph("Hallazgos de Prioridad Baja", self.heading2_style))
            matrix_content.append(Spacer(1, 0.1 * inch))
            low_table = self.add_findings_table(priority_matrix.get("Low", []), "Low")
            if low_table:
                matrix_content.append(low_table)
        
        self.add_section("7. Matriz de Priorización", matrix_content)
        
        # Detailed findings
        detailed_content = []
        for i, finding in enumerate(findings_list, 1):
            self.add_finding_detail(finding, i)
        
        # Add all findings to story
        self.story.append(Paragraph("8. Hallazgos Detallados", self.heading1_style))
        self.story.append(Spacer(1, 0.2 * inch))
        
        for i, finding in enumerate(findings_list, 1):
            self.add_finding_detail(finding, i)
            if i < len(findings_list):
                self.story.append(Spacer(1, 0.1 * inch))
        
        self.story.append(PageBreak())
        
        # Recommendations
        recommendations_content = [
            "<b>Próximos Pasos Recomendados:</b>",
            "",
            "1. Priorizar y abordar los hallazgos de alta prioridad relacionados con seguridad y performance.",
            "2. Implementar mejoras SEO on-page según las recomendaciones detalladas.",
            "3. Realizar pruebas de validación después de cada cambio implementado.",
            "4. Establecer monitoreo continuo de performance y seguridad.",
            "5. Revisar y actualizar documentos legales según requerimientos del sector salud.",
            "",
            "<b>Nota:</b> Las estimaciones de esfuerzo son aproximadas y pueden variar según la complejidad específica de la implementación.",
        ]
        self.add_section("9. Recomendaciones y Próximos Pasos", recommendations_content)
        
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
        
        print(f"✓ PDF report generated: {self.output_path}")


def main():
    """Main function to generate PDF report."""
    docs_dir = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
    
    # Load findings
    findings_path = docs_dir / "findings.json"
    if not findings_path.exists():
        print(f"Error: Findings file not found at {findings_path}")
        print("Please run findings_generator.py first.")
        return
    
    with open(findings_path, "r", encoding="utf-8") as f:
        findings_data = json.load(f)
    
    # Generate PDF
    output_path = docs_dir / "farmaciasmacross-audit.pdf"
    generator = PDFReportGenerator(output_path)
    generator.generate({"findings": findings_data})
    
    print(f"\n✓ PDF report saved to: {output_path}")


if __name__ == "__main__":
    main()

