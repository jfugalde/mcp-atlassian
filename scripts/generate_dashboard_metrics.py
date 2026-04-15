#!/usr/bin/env python3
"""
Generate dashboard metrics and JQL queries for RYU and SUPA projects.

This script queries the Jira API to generate:
- Summary statistics
- JQL queries for all dashboard filters
- Component breakdown
- Epic progress
- Quarterly distribution
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from mcp_atlassian.jira.client import JiraClient
    from mcp_atlassian.utils.auth import get_auth_config
except ImportError:
    print("Warning: mcp_atlassian not available. Using placeholder data.")
    JiraClient = None


def generate_jql_queries():
    """Generate all JQL queries for dashboard filters."""
    
    queries = {
        "executive_summary": {
            "all_issues": 'project in (RYU, SUPA) ORDER BY updated DESC',
            "to_do": 'project in (RYU, SUPA) AND status = "To Do" ORDER BY priority DESC, created ASC',
            "in_progress": 'project in (RYU, SUPA) AND status = "In Progress" ORDER BY updated DESC',
            "done": 'project in (RYU, SUPA) AND status = Done ORDER BY resolved DESC',
            "by_quarter": 'project in (RYU, SUPA) AND fixVersion in ("2026-Q1", "2026-Q2", "2026-Q3", "2026-Q4") ORDER BY fixVersion ASC, priority DESC',
        },
        "quarterly": {
            "q1": 'project in (RYU, SUPA) AND fixVersion = "2026-Q1" ORDER BY priority DESC, created ASC',
            "q2": 'project in (RYU, SUPA) AND fixVersion = "2026-Q2" ORDER BY priority DESC, created ASC',
            "q3": 'project in (RYU, SUPA) AND fixVersion = "2026-Q3" ORDER BY priority DESC, created ASC',
            "q4": 'project in (RYU, SUPA) AND fixVersion = "2026-Q4" ORDER BY priority DESC, created ASC',
        },
        "epics": {
            "ryu_epics": 'project = RYU AND issuetype = Epic ORDER BY created ASC',
            "supa_epics": 'project = SUPA AND issuetype = Epic ORDER BY created ASC',
            "epic_ryu_01": '"Epic Link" = RYU-46 ORDER BY priority DESC, created ASC',
            "epic_ryu_02": '"Epic Link" = RYU-47 ORDER BY priority DESC, created ASC',
            "epic_ryu_03": '"Epic Link" = RYU-48 ORDER BY priority DESC, created ASC',
            "epic_ryu_04": '"Epic Link" = RYU-49 ORDER BY priority DESC, created ASC',
            "epic_amz_01": '"Epic Link" = SUPA-31 ORDER BY priority DESC, created ASC',
            "epic_amz_02": '"Epic Link" = SUPA-32 ORDER BY priority DESC, created ASC',
            "epic_amz_03": '"Epic Link" = SUPA-33 ORDER BY priority DESC, created ASC',
            "epic_amz_04": '"Epic Link" = SUPA-34 ORDER BY priority DESC, created ASC',
            "epic_amz_05": '"Epic Link" = SUPA-35 ORDER BY priority DESC, created ASC',
            "epic_amz_06": '"Epic Link" = SUPA-36 ORDER BY priority DESC, created ASC',
            "epic_amz_07": '"Epic Link" = SUPA-37 ORDER BY priority DESC, created ASC',
            "epic_amz_08": '"Epic Link" = SUPA-38 ORDER BY priority DESC, created ASC',
            "epic_amz_09": '"Epic Link" = SUPA-39 ORDER BY priority DESC, created ASC',
        },
        "components": {
            "ryu_offer": 'project = RYU AND component = "Offer" ORDER BY priority DESC, created ASC',
            "ryu_client": 'project = RYU AND component = "Client" ORDER BY priority DESC, created ASC',
            "ryu_delivery": 'project = RYU AND component = "Delivery" ORDER BY priority DESC, created ASC',
            "ryu_playbook": 'project = RYU AND component = "Playbook" ORDER BY priority DESC, created ASC',
            "ryu_ops": 'project = RYU AND component = "Ops" ORDER BY priority DESC, created ASC',
            "supa_amazon_account": 'project = SUPA AND component = "Amazon-Account" ORDER BY priority DESC, created ASC',
            "supa_compliance": 'project = SUPA AND component = "Compliance" ORDER BY priority DESC, created ASC',
            "supa_finance": 'project = SUPA AND component = "Finance" ORDER BY priority DESC, created ASC',
            "supa_catalog": 'project = SUPA AND component = "Catalog" ORDER BY priority DESC, created ASC',
            "supa_logistics": 'project = SUPA AND component = "Logistics" ORDER BY priority DESC, created ASC',
            "supa_cx": 'project = SUPA AND component = "CX" ORDER BY priority DESC, created ASC',
            "supa_ads": 'project = SUPA AND component = "Ads" ORDER BY priority DESC, created ASC',
            "supa_brand": 'project = SUPA AND component = "Brand" ORDER BY priority DESC, created ASC',
            "supa_ops": 'project = SUPA AND component = "Ops" ORDER BY priority DESC, created ASC',
        },
        "project_comparison": {
            "ryu_all": 'project = RYU ORDER BY updated DESC',
            "supa_all": 'project = SUPA ORDER BY updated DESC',
            "ryu_by_status": 'project = RYU ORDER BY status ASC, priority DESC',
            "supa_by_status": 'project = SUPA ORDER BY status ASC, priority DESC',
        },
    }
    
    return queries


def query_jira_metrics(client, jql_query):
    """Query Jira for metrics using JQL."""
    if client is None:
        return None
    
    try:
        # This would use the actual Jira client
        # For now, return placeholder
        return {"total": 0, "issues": []}
    except Exception as e:
        print(f"Error querying Jira: {e}", file=sys.stderr)
        return None


def generate_metrics_summary():
    """Generate summary metrics."""
    
    summary = {
        "generated_at": datetime.now().isoformat(),
        "projects": {
            "RYU": {
                "epics": 4,
                "stories": 10,
                "components": ["Offer", "Client", "Delivery", "Playbook", "Ops"],
            },
            "SUPA": {
                "epics": 9,
                "stories": 13,
                "components": [
                    "Amazon-Account",
                    "Compliance",
                    "Finance",
                    "Catalog",
                    "Logistics",
                    "CX",
                    "Ads",
                    "Brand",
                    "Ops",
                ],
            },
        },
        "quarters": {
            "Q1": {"epics": 6, "stories": 8},
            "Q2": {"epics": 5, "stories": 7},
            "Q3": {"epics": 2, "stories": 3},
            "Q4": {"epics": 3, "stories": 3},
        },
    }
    
    return summary


def main():
    """Main function to generate dashboard metrics."""
    
    print("=" * 60)
    print("2026 Year Dashboard - Metrics Generator")
    print("=" * 60)
    print()
    
    # Generate JQL queries
    queries = generate_jql_queries()
    
    # Generate summary metrics
    summary = generate_metrics_summary()
    
    # Output directory
    output_dir = Path(__file__).parent.parent / "docs" / "dashboard"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save JQL queries
    jql_file = output_dir / "jql-queries.json"
    with open(jql_file, "w", encoding="utf-8") as f:
        json.dump(queries, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved JQL queries to: {jql_file}")
    
    # Save summary metrics
    metrics_file = output_dir / "dashboard-metrics.json"
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved metrics summary to: {metrics_file}")
    
    # Generate JQL queries markdown
    jql_md_file = output_dir / "jql-queries.md"
    with open(jql_md_file, "w", encoding="utf-8") as f:
        f.write("# JQL Queries for Dashboard Filters\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for category, category_queries in queries.items():
            f.write(f"## {category.replace('_', ' ').title()}\n\n")
            for name, jql in category_queries.items():
                f.write(f"### {name.replace('_', ' ').title()}\n\n")
                f.write("```jql\n")
                f.write(f"{jql}\n")
                f.write("```\n\n")
    
    print(f"✅ Saved JQL queries markdown to: {jql_md_file}")
    
    # Print summary
    print()
    print("Summary:")
    print(f"  - Total Epics: {summary['projects']['RYU']['epics'] + summary['projects']['SUPA']['epics']}")
    print(f"  - Total Stories: {summary['projects']['RYU']['stories'] + summary['projects']['SUPA']['stories']}")
    print(f"  - RYU Components: {', '.join(summary['projects']['RYU']['components'])}")
    print(f"  - SUPA Components: {', '.join(summary['projects']['SUPA']['components'])}")
    print()
    print("Next steps:")
    print("  1. Review JQL queries in docs/dashboard/jql-queries.md")
    print("  2. Create saved filters in Jira using these queries")
    print("  3. Follow dashboard setup guide: docs/dashboard/2026-year-dashboard-setup.md")
    print()


if __name__ == "__main__":
    main()


