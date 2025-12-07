"""Main script to run complete technical audit."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from findings_generator import FindingsGenerator, main as generate_findings
from onpage_analysis import OnPageAnalyzer, main as run_onpage
from pdf_generator import PDFReportGenerator, main as generate_pdf
from run_psi_analysis import analyze_urls_from_set, main as run_psi
from url_crawler import SiteCrawler, main as crawl_site
from url_selector import select_representative_urls, save_url_set, main as select_urls


def run_full_audit():
    """Run complete audit workflow."""
    print("=" * 80)
    print("FARMACIAS MACROSS - AUDITORÍA TÉCNICA COMPLETA")
    print("=" * 80)
    print()
    
    docs_dir = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Crawl site
    print("\n" + "=" * 80)
    print("PASO 1: Descubrimiento de URLs")
    print("=" * 80)
    try:
        categorized_urls = crawl_site()
        print("✓ Paso 1 completado\n")
    except Exception as e:
        print(f"❌ Error en Paso 1: {e}")
        return False
    
    # Step 2: Select representative URLs
    print("\n" + "=" * 80)
    print("PASO 2: Selección de URLs Representativas")
    print("=" * 80)
    try:
        selected_urls = select_urls()
        print("✓ Paso 2 completado\n")
    except Exception as e:
        print(f"❌ Error en Paso 2: {e}")
        return False
    
    # Step 3: Run PageSpeed Insights
    print("\n" + "=" * 80)
    print("PASO 3: Análisis de Performance (PageSpeed Insights)")
    print("=" * 80)
    try:
        url_set_path = docs_dir / "url_set.json"
        if url_set_path.exists():
            psi_results = analyze_urls_from_set(url_set_path)
            print("✓ Paso 3 completado\n")
        else:
            print("⚠ URL set not found, skipping PSI analysis")
    except Exception as e:
        print(f"⚠ Error en Paso 3: {e}")
        print("Continuando con análisis on-page...\n")
    
    # Step 4: On-page analysis
    print("\n" + "=" * 80)
    print("PASO 4: Análisis On-Page")
    print("=" * 80)
    try:
        onpage_results = run_onpage()
        print("✓ Paso 4 completado\n")
    except Exception as e:
        print(f"⚠ Error en Paso 4: {e}")
        print("Continuando con generación de hallazgos...\n")
    
    # Step 5: Generate findings
    print("\n" + "=" * 80)
    print("PASO 5: Generación de Hallazgos")
    print("=" * 80)
    try:
        findings = generate_findings()
        print("✓ Paso 5 completado\n")
    except Exception as e:
        print(f"❌ Error en Paso 5: {e}")
        return False
    
    # Step 6: Generate PDF
    print("\n" + "=" * 80)
    print("PASO 6: Generación de Reporte PDF")
    print("=" * 80)
    try:
        generate_pdf()
        print("✓ Paso 6 completado\n")
    except Exception as e:
        print(f"❌ Error en Paso 6: {e}")
        return False
    
    print("\n" + "=" * 80)
    print("✓ AUDITORÍA COMPLETA FINALIZADA")
    print("=" * 80)
    print(f"\nReporte PDF generado en: {docs_dir / 'farmaciasmacross-audit.pdf'}")
    print(f"Hallazgos guardados en: {docs_dir / 'findings.md'}")
    print()
    
    return True


if __name__ == "__main__":
    success = run_full_audit()
    sys.exit(0 if success else 1)

