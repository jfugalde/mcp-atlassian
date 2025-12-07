"""Deep analysis of installed apps - performance, security, cost impact."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from query_apps import query_installed_apps, format_apps_data


# High-risk scopes that could impact performance or security
HIGH_RISK_SCOPES = {
    "write_themes": "Can modify theme code - security risk",
    "write_script_tags": "Can inject JavaScript - performance & security risk",
    "write_products": "Can modify product data - data integrity risk",
    "write_orders": "Can modify orders - financial risk",
    "write_customers": "Can access/modify customer data - privacy risk",
    "read_all_orders": "Access to all order data - privacy risk",
    "read_all_customers": "Access to all customer data - privacy risk",
}


def analyze_app_security(app: Dict) -> Dict:
    """
    Analyze security aspects of an app installation.
    
    Args:
        app: App installation data.
    
    Returns:
        Security analysis dictionary.
    """
    granted_scopes = app.get("granted_scopes", [])
    requested_scopes = app.get("requested_scopes", [])
    
    high_risk_granted = [
        scope for scope in granted_scopes
        if scope in HIGH_RISK_SCOPES
    ]
    
    security_score = 100
    if high_risk_granted:
        security_score -= len(high_risk_granted) * 15
    
    # Check for excessive permissions
    if len(granted_scopes) > 10:
        security_score -= 10
    
    warnings = []
    if high_risk_granted:
        warnings.append(
            f"High-risk permissions granted: {', '.join(high_risk_granted)}"
        )
    
    return {
        "security_score": max(0, security_score),
        "granted_scopes_count": len(granted_scopes),
        "requested_scopes_count": len(requested_scopes),
        "high_risk_scopes": high_risk_granted,
        "warnings": warnings,
        "scope_details": {
            scope: HIGH_RISK_SCOPES.get(scope, "Standard permission")
            for scope in granted_scopes
        },
    }


def calculate_app_cost(app: Dict) -> Dict:
    """
    Calculate total cost of an app including subscriptions and usage.
    
    Args:
        app: App installation data.
    
    Returns:
        Cost analysis dictionary.
    """
    subscriptions = app.get("subscriptions", [])
    total_monthly = 0.0
    total_annual = 0.0
    usage_costs = []
    currency = "USD"
    
    for sub in subscriptions:
        # This would need to be enhanced with actual subscription data
        # from the enhanced query
        status = sub.get("status", "").upper()
        if status == "ACTIVE":
            # Placeholder - actual pricing comes from lineItems
            pass
    
    return {
        "total_monthly_cost": total_monthly,
        "total_annual_cost": total_annual,
        "currency": currency,
        "active_subscriptions": len([s for s in subscriptions if s.get("status") == "ACTIVE"]),
        "usage_costs": usage_costs,
    }


def analyze_app_performance_impact(app: Dict) -> Dict:
    """
    Analyze potential performance impact of an app.
    
    Args:
        app: App installation data.
    
    Returns:
        Performance impact analysis.
    """
    impact_score = 50  # Neutral starting point
    
    # Embedded apps typically have more impact
    if app.get("embedded", False):
        impact_score -= 10
    
    # Script tags can slow down page load
    if "write_script_tags" in app.get("granted_scopes", []):
        impact_score -= 15
    
    # Theme modifications can affect performance
    if "write_themes" in app.get("granted_scopes", []):
        impact_score -= 10
    
    recommendations = []
    if impact_score < 40:
        recommendations.append(
            "Consider monitoring page load times - this app may impact performance"
        )
    if "write_script_tags" in app.get("granted_scopes", []):
        recommendations.append(
            "App can inject scripts - monitor for performance degradation"
        )
    
    return {
        "impact_score": max(0, min(100, impact_score)),
        "is_embedded": app.get("embedded", False),
        "can_modify_theme": "write_themes" in app.get("granted_scopes", []),
        "can_inject_scripts": "write_script_tags" in app.get("granted_scopes", []),
        "recommendations": recommendations,
    }


def generate_app_recommendations(app: Dict, security: Dict, cost: Dict, performance: Dict) -> List[str]:
    """
    Generate actionable recommendations for an app.
    
    Args:
        app: App installation data.
        security: Security analysis.
        cost: Cost analysis.
        performance: Performance analysis.
    
    Returns:
        List of recommendation strings.
    """
    recommendations = []
    
    # Security recommendations
    if security["security_score"] < 60:
        recommendations.append(
            f"⚠️  Security: Review permissions for {app['name']} - "
            f"high-risk scopes detected"
        )
    
    # Cost recommendations
    if cost["total_monthly_cost"] > 50:
        recommendations.append(
            f"💰 Cost: {app['name']} costs ${cost['total_monthly_cost']:.2f}/month - "
            f"review if value justifies cost"
        )
    
    # Performance recommendations
    if performance["impact_score"] < 40:
        recommendations.append(
            f"⚡ Performance: {app['name']} may impact storefront performance - "
            f"monitor page load times"
        )
    
    # Unused apps
    if not app.get("subscriptions") and not app.get("launch_url"):
        recommendations.append(
            f"🗑️  Unused: {app['name']} appears unused - consider uninstalling"
        )
    
    return recommendations


def deep_analyze_apps(
    shop_domain: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Dict:
    """
    Perform deep analysis on all installed apps.
    
    Args:
        shop_domain: Shop domain. If None, reads from environment.
        access_token: Access token. If None, reads from environment.
    
    Returns:
        Comprehensive analysis dictionary.
    """
    print("🔍 Performing deep app analysis...")
    
    # Query apps
    apps_data = query_installed_apps(shop_domain, access_token)
    apps = format_apps_data(apps_data)
    
    analysis_results = {
        "total_apps": len(apps),
        "analysis_date": datetime.now().isoformat(),
        "apps": [],
        "summary": {
            "total_monthly_cost": 0.0,
            "high_risk_apps": 0,
            "performance_concerns": 0,
            "security_issues": 0,
        },
    }
    
    for app in apps:
        security = analyze_app_security(app)
        cost = calculate_app_cost(app)
        performance = analyze_app_performance_impact(app)
        recommendations = generate_app_recommendations(app, security, cost, performance)
        
        app_analysis = {
            "app": app,
            "security": security,
            "cost": cost,
            "performance": performance,
            "recommendations": recommendations,
            "overall_score": (
                security["security_score"] * 0.4 +
                performance["impact_score"] * 0.3 +
                (100 if cost["total_monthly_cost"] < 50 else 70) * 0.3
            ),
        }
        
        analysis_results["apps"].append(app_analysis)
        
        # Update summary
        analysis_results["summary"]["total_monthly_cost"] += cost["total_monthly_cost"]
        if security["security_score"] < 60:
            analysis_results["summary"]["high_risk_apps"] += 1
        if performance["impact_score"] < 40:
            analysis_results["summary"]["performance_concerns"] += 1
        if security["security_score"] < 70:
            analysis_results["summary"]["security_issues"] += 1
    
    # Sort by overall score (lower is worse)
    analysis_results["apps"].sort(key=lambda x: x["overall_score"])
    
    return analysis_results


def format_analysis_report(analysis: Dict) -> str:
    """
    Format analysis results as a readable report.
    
    Args:
        analysis: Analysis results dictionary.
    
    Returns:
        Formatted markdown report.
    """
    report = []
    report.append("# Deep App Analysis Report\n")
    report.append(f"**Analysis Date:** {analysis['analysis_date']}\n")
    report.append(f"**Total Apps Analyzed:** {analysis['total_apps']}\n\n")
    
    # Summary
    summary = analysis["summary"]
    report.append("## Summary\n")
    report.append(f"- **Total Monthly Cost:** ${summary['total_monthly_cost']:.2f}")
    report.append(f"- **High-Risk Apps:** {summary['high_risk_apps']}")
    report.append(f"- **Performance Concerns:** {summary['performance_concerns']}")
    report.append(f"- **Security Issues:** {summary['security_issues']}\n\n")
    
    # Detailed app analysis
    report.append("## App Details\n\n")
    
    for app_analysis in analysis["apps"]:
        app = app_analysis["app"]
        report.append(f"### {app['name']}\n")
        report.append(f"**Developer:** {app['developer']}  \n")
        report.append(f"**Category:** {app.get('category', 'N/A')}  \n")
        report.append(f"**Overall Score:** {app_analysis['overall_score']:.1f}/100\n\n")
        
        # Security
        security = app_analysis["security"]
        report.append(f"**Security Score:** {security['security_score']}/100  \n")
        if security["high_risk_scopes"]:
            report.append(f"⚠️  **High-Risk Scopes:** {', '.join(security['high_risk_scopes'])}\n")
        
        # Performance
        perf = app_analysis["performance"]
        report.append(f"**Performance Impact:** {perf['impact_score']}/100  \n")
        
        # Cost
        cost = app_analysis["cost"]
        if cost["total_monthly_cost"] > 0:
            report.append(f"**Monthly Cost:** ${cost['total_monthly_cost']:.2f} {cost['currency']}\n")
        
        # Recommendations
        if app_analysis["recommendations"]:
            report.append("\n**Recommendations:**\n")
            for rec in app_analysis["recommendations"]:
                report.append(f"- {rec}\n")
        
        report.append("\n---\n\n")
    
    return "\n".join(report)


def main():
    """Main function to run deep app analysis."""
    try:
        analysis = deep_analyze_apps()
        
        # Save JSON
        output_path = Path(__file__).parent.parent.parent / "docs" / "shopify-analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        json_file = output_path / "deep_app_analysis.json"
        
        with open(json_file, "w") as f:
            json.dump(analysis, f, indent=2, default=str)
        
        print(f"✅ Analysis saved to: {json_file}")
        
        # Generate and save report
        report = format_analysis_report(analysis)
        report_file = output_path / "deep_app_analysis_report.md"
        
        with open(report_file, "w") as f:
            f.write(report)
        
        print(f"✅ Report saved to: {report_file}")
        
        # Print summary to console
        print("\n" + "=" * 60)
        print("ANALYSIS SUMMARY")
        print("=" * 60)
        summary = analysis["summary"]
        print(f"Total Apps: {analysis['total_apps']}")
        print(f"Total Monthly Cost: ${summary['total_monthly_cost']:.2f}")
        print(f"High-Risk Apps: {summary['high_risk_apps']}")
        print(f"Performance Concerns: {summary['performance_concerns']}")
        print(f"Security Issues: {summary['security_issues']}")
        print("=" * 60)
        
        return analysis
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        raise


if __name__ == "__main__":
    main()

