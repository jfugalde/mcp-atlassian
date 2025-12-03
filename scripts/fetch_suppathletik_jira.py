#!/usr/bin/env python3
"""
Script to fetch all Jira issues from a project
and generate markdown documentation files similar to the FM project structure.

Supports multiple Jira instances via environment variable prefixes.
Example .env:
  # Default instance
  JIRA_URL=https://default.atlassian.net
  JIRA_USERNAME=user@example.com
  JIRA_API_TOKEN=token123

  # Suppathletik instance
  JIRA_URL_suppathletik=https://suppathletik.atlassian.net
  JIRA_USERNAME_suppathletik=user@example.com
  JIRA_API_TOKEN_suppathletik=token456

Usage:
  uv run scripts/fetch_suppathletik_jira.py --project suppathletik --instance suppathletik
  uv run scripts/fetch_suppathletik_jira.py --project FM  # Uses default JIRA_* vars
"""

import argparse
import sys
from pathlib import Path
from typing import Any

# Load environment variables from .env file
from dotenv import load_dotenv

# Load .env file from project root
project_root = Path(__file__).parent.parent
env_file = project_root / ".env"
if env_file.exists():
    load_dotenv(env_file, override=True)
else:
    # Try to load from default location
    load_dotenv(override=True)

# Add src to path to import mcp_atlassian
sys.path.insert(0, str(project_root / "src"))

from mcp_atlassian.jira import JiraConfig, JiraFetcher


def fetch_all_project_issues(
    jira: JiraFetcher, project_key: str
) -> list[dict[str, Any]]:
    """Fetch all issues from a project with pagination.

    Args:
        jira: JiraFetcher instance
        project_key: The project key to fetch issues from

    Returns:
        List of all issues as dictionaries
    """
    all_issues = []
    start_at = 0
    limit = 50

    print(f"Fetching issues from project '{project_key}'...")

    while True:
        print(f"  Fetching batch starting at {start_at}...")
        result = jira.get_project_issues(
            project_key=project_key, start=start_at, limit=limit
        )

        if not result or not result.issues:
            break

        # Convert issues to dictionaries
        for issue in result.issues:
            issue_dict = issue.to_simplified_dict()
            all_issues.append(issue_dict)

        print(
            f"  Fetched {len(result.issues)} issues (total so far: {len(all_issues)})"
        )

        # Check if we've fetched all issues
        if result.total > 0 and len(all_issues) >= result.total:
            break

        if len(result.issues) < limit:
            break

        start_at += limit

    print(f"Total issues fetched: {len(all_issues)}")
    return all_issues


def organize_issues(issues: list[dict[str, Any]]) -> dict[str, Any]:
    """Organize issues by type and relationships.

    Args:
        issues: List of issue dictionaries

    Returns:
        Dictionary with organized issues
    """
    epics = []
    stories = []
    tasks = []
    other_issues = []

    # Issue lookup by key
    issues_by_key: dict[str, dict[str, Any]] = {}

    for issue in issues:
        key = issue.get("key", "")
        issues_by_key[key] = issue

        issue_type = issue.get("issuetype", {}).get("name", "").lower()

        if issue_type == "epic":
            epics.append(issue)
        elif issue_type in ["story", "user story"]:
            stories.append(issue)
        elif issue_type in ["task", "subtask"]:
            tasks.append(issue)
        else:
            other_issues.append(issue)

    # Map relationships
    # Epic links: stories/tasks linked to epics
    # Epic link can be in various places: epicLink field, epic field, or custom fields
    epic_links: dict[str, list[dict[str, Any]]] = {}
    for story in stories + tasks + other_issues:
        epic_key = None
        # Try different ways to get epic link
        if "epicLink" in story:
            epic_key = story.get("epicLink")
        elif "epic" in story:
            epic = story.get("epic")
            if isinstance(epic, dict):
                epic_key = epic.get("key")
            elif isinstance(epic, str):
                epic_key = epic
        # Check custom fields (common patterns: customfield_10011, etc.)
        for field_name, field_value in story.items():
            if "epic" in field_name.lower() and field_value:
                if isinstance(field_value, dict):
                    epic_key = field_value.get("key")
                elif isinstance(field_value, str):
                    epic_key = field_value
                break

        if epic_key:
            if epic_key not in epic_links:
                epic_links[epic_key] = []
            epic_links[epic_key].append(story)

    # Parent-child relationships (subtasks)
    parent_children: dict[str, list[dict[str, Any]]] = {}
    for task in tasks + stories + other_issues:
        parent = task.get("parent")
        parent_key = None
        if isinstance(parent, dict):
            parent_key = parent.get("key")
        elif isinstance(parent, str):
            parent_key = parent

        if parent_key:
            if parent_key not in parent_children:
                parent_children[parent_key] = []
            parent_children[parent_key].append(task)

    return {
        "epics": epics,
        "stories": stories,
        "tasks": tasks,
        "other_issues": other_issues,
        "issues_by_key": issues_by_key,
        "epic_links": epic_links,
        "parent_children": parent_children,
    }


def get_field_value(issue: dict[str, Any], field_name: str, default: Any = None) -> Any:
    """Safely get a field value from an issue.

    Args:
        issue: Issue dictionary
        field_name: Name of the field to get
        default: Default value if field not found

    Returns:
        Field value or default
    """
    return issue.get(field_name, default)


def format_description(description: str | None) -> str:
    """Format issue description for markdown.

    Args:
        description: Raw description text

    Returns:
        Formatted description
    """
    if not description:
        return ""

    # Remove HTML tags if present (basic cleanup)
    import re  # noqa: E402

    description = re.sub(r"<[^>]+>", "", description)

    return description.strip()


def generate_epics_markdown(
    organized: dict[str, Any], project_key: str, project_name: str = ""
) -> str:
    """Generate the epics markdown file.

    Args:
        organized: Organized issues dictionary
        project_key: Project key
        project_name: Project name (optional)

    Returns:
        Markdown content
    """
    epics = organized["epics"]
    stories = organized["stories"]
    tasks = organized["tasks"]
    epic_links = organized["epic_links"]
    parent_children = organized["parent_children"]
    issues_by_key = organized["issues_by_key"]

    lines = []
    lines.append(f"# {project_name or project_key} - Jira Epic Structure")
    lines.append("")
    lines.append(f"**Project Key**: {project_key}")
    if project_name:
        lines.append(f"**Project Name**: {project_name}")
    lines.append("")

    # Summary statistics
    lines.append("**Estructura en Jira:**")
    lines.append(
        f"- **{len(epics)} Epics**: {', '.join([e.get('key', '') for e in epics])}"
    )
    lines.append(f"- **{len(stories)} Stories**")
    lines.append(f"- **{len(tasks)} Tasks**")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sort epics by key
    epics_sorted = sorted(epics, key=lambda x: x.get("key", ""))

    for epic_idx, epic in enumerate(epics_sorted, 1):
        epic_key = epic.get("key", "")
        epic_summary = epic.get("summary", "")
        epic_status = epic.get("status", {}).get("name", "Unknown")
        epic_description = format_description(epic.get("description"))

        # Get custom fields that might be useful
        priority = epic.get("priority", {}).get("name", "")

        lines.append(f"## EPIC {epic_idx}: {epic_summary}")
        lines.append("")
        lines.append(f"**Epic Key**: {epic_key}")
        lines.append(f"**Summary**: {epic_summary}")
        lines.append(f"**Status**: {epic_status}")
        if priority:
            lines.append(f"**Priority**: {priority}")
        if epic_description:
            lines.append(f"**Description**: {epic_description}")
        lines.append("")

        # Get stories/tasks linked to this epic
        epic_stories = epic_links.get(epic_key, [])

        if epic_stories:
            # Separate stories and tasks
            epic_stories_list = [
                s
                for s in epic_stories
                if s.get("issuetype", {}).get("name", "").lower()
                in ["story", "user story"]
            ]
            epic_tasks_list = [
                t
                for t in epic_stories
                if t.get("issuetype", {}).get("name", "").lower() in ["task", "subtask"]
            ]

            # Sort by key
            epic_stories_list = sorted(
                epic_stories_list, key=lambda x: x.get("key", "")
            )
            epic_tasks_list = sorted(epic_tasks_list, key=lambda x: x.get("key", ""))

            # Process stories
            for story in epic_stories_list:
                story_key = story.get("key", "")
                story_summary = story.get("summary", "")
                story_status = story.get("status", {}).get("name", "Unknown")
                story_priority = story.get("priority", {}).get("name", "")
                story_description = format_description(story.get("description"))

                lines.append(f"### Story {story_key}: {story_summary}")
                lines.append("")
                lines.append(f"**Story Key**: {story_key}")
                lines.append(f"**Summary**: {story_summary}")
                lines.append(f"**Status**: {story_status}")
                if story_priority:
                    lines.append(f"**Priority**: {story_priority}")
                if story_description:
                    lines.append(f"**Description**: {story_description}")
                lines.append("")

                # Get tasks linked to this story (as parent)
                story_tasks = parent_children.get(story_key, [])
                story_tasks = sorted(story_tasks, key=lambda x: x.get("key", ""))

                if story_tasks:
                    lines.append("#### Tasks:")
                    for task in story_tasks:
                        task_key = task.get("key", "")
                        task_summary = task.get("summary", "")
                        task_status = task.get("status", {}).get("name", "Unknown")
                        task_priority = task.get("priority", {}).get("name", "")
                        task_description = format_description(task.get("description"))

                        lines.append(
                            f"- **{task_key}**: {task_summary} (Status: {task_status})"
                        )
                        if task_priority:
                            lines.append(f"  - **Priority**: {task_priority}")
                        if task_description:
                            # Truncate long descriptions
                            desc = (
                                task_description[:200] + "..."
                                if len(task_description) > 200
                                else task_description
                            )
                            lines.append(f"  - **Description**: {desc}")
                        lines.append("")

                lines.append("---")
                lines.append("")

            # Process standalone tasks (not linked to stories as subtasks)
            # A task is standalone if it has no parent, or its parent is not a story
            standalone_tasks = []
            for t in epic_tasks_list:
                parent = t.get("parent")
                if not parent:
                    standalone_tasks.append(t)
                else:
                    parent_key = (
                        parent.get("key") if isinstance(parent, dict) else parent
                    )
                    # Check if parent is a story - if not, it's standalone
                    if parent_key and parent_key in issues_by_key:
                        parent_issue = issues_by_key[parent_key]
                        parent_type = (
                            parent_issue.get("issuetype", {}).get("name", "").lower()
                        )
                        if parent_type not in ["story", "user story"]:
                            standalone_tasks.append(t)
                    else:
                        standalone_tasks.append(t)
            if standalone_tasks:
                lines.append("### Standalone Tasks:")
                for task in standalone_tasks:
                    task_key = task.get("key", "")
                    task_summary = task.get("summary", "")
                    task_status = task.get("status", {}).get("name", "Unknown")
                    lines.append(
                        f"- **{task_key}**: {task_summary} (Status: {task_status})"
                    )
                lines.append("")

        lines.append("")

    return "\n".join(lines)


def generate_index_markdown(
    organized: dict[str, Any], project_key: str, project_name: str = ""
) -> str:
    """Generate the index markdown file.

    Args:
        organized: Organized issues dictionary
        project_key: Project key
        project_name: Project name (optional)

    Returns:
        Markdown content
    """
    epics = organized["epics"]
    stories = organized["stories"]
    tasks = organized["tasks"]

    lines = []
    lines.append(f"# {project_name or project_key} - Project Documentation Index")
    lines.append("")
    lines.append(f"**Project Key**: {project_key}")
    if project_name:
        lines.append(f"**Project Name**: {project_name}")
    lines.append(f"**Total Issues**: {len(epics) + len(stories) + len(tasks)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Quick Reference")
    lines.append("")
    lines.append("| Document | Purpose | Last Updated |")
    lines.append("|----------|---------|--------------|")
    lines.append(
        "| [Epic Structure](./suppathletik-epics.md) | Complete breakdown of all epics, stories, and tasks | [Fecha] |"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Project Overview")
    lines.append("")
    lines.append("### Structure Summary")
    lines.append("")
    lines.append(f"- **{len(epics)} Epics**")
    lines.append(f"- **{len(stories)} Stories**")
    lines.append(f"- **{len(tasks)} Tasks**")
    lines.append("")

    if epics:
        lines.append("### Epics")
        lines.append("")
        for epic in sorted(epics, key=lambda x: x.get("key", "")):
            epic_key = epic.get("key", "")
            epic_summary = epic.get("summary", "")
            epic_status = epic.get("status", {}).get("name", "Unknown")
            lines.append(f"- **{epic_key}**: {epic_summary} (Status: {epic_status})")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Esta documentación se genera automáticamente desde Jira")
    lines.append(
        "- Para actualizar, ejecutar el script `scripts/fetch_suppathletik_jira.py`"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**Última actualización**: [Fecha]")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main function to fetch issues and generate markdown files."""
    parser = argparse.ArgumentParser(
        description="Fetch Jira issues and generate markdown documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default Jira instance
  %(prog)s --project FM

  # Use specific Jira instance with prefix
  %(prog)s --project suppathletik --instance suppathletik

Environment Variables:
  For default instance:
    JIRA_URL=https://your-domain.atlassian.net
    JIRA_USERNAME=your.email@example.com
    JIRA_API_TOKEN=your_token

  For prefixed instance (e.g., --instance suppathletik):
    JIRA_URL_suppathletik=https://suppathletik.atlassian.net
    JIRA_USERNAME_suppathletik=user@example.com
    JIRA_API_TOKEN_suppathletik=token
        """,
    )
    parser.add_argument(
        "--project",
        default="suppathletik",
        help="Jira project key to fetch issues from (default: suppathletik)",
    )
    parser.add_argument(
        "--instance",
        default=None,
        help="Jira instance prefix for environment variables (e.g., 'suppathletik' for JIRA_URL_suppathletik). If not provided, uses default JIRA_* variables.",
    )
    parser.add_argument(
        "--list-projects",
        action="store_true",
        help="List all available Jira projects and exit",
    )

    args = parser.parse_args()
    project_key = args.project
    instance_prefix = args.instance

    # Initialize Jira client
    try:
        config = JiraConfig.from_env(prefix=instance_prefix)
        jira = JiraFetcher(config=config)
        instance_info = f" (instance: {instance_prefix})" if instance_prefix else ""
        print(f"Connected to Jira at {config.url}{instance_info}")
    except Exception as e:
        print(f"Error initializing Jira client: {e}")
        print("\nMake sure Jira credentials are configured:")
        print("  1. Create a .env file in the project root, or")
        if instance_prefix:
            print(f"  2. Set environment variables with prefix '{instance_prefix}':")
            print(f"     JIRA_URL_{instance_prefix}")
            print(f"     JIRA_USERNAME_{instance_prefix}")
            print(f"     JIRA_API_TOKEN_{instance_prefix}")
        else:
            print(
                "  2. Set environment variables: JIRA_URL, JIRA_USERNAME, JIRA_API_TOKEN"
            )
        print(f"\n.env file location: {project_root / '.env'}")
        if not env_file.exists():
            print(f"  (Note: .env file not found at {env_file})")
        sys.exit(1)

    # List projects if requested
    if args.list_projects:
        try:
            print("\nFetching available projects...")
            projects = jira.get_all_projects(include_archived=False)
            if projects:
                print(f"\nFound {len(projects)} project(s):\n")
                for project in sorted(projects, key=lambda x: x.get("key", "")):
                    key = project.get("key", "N/A")
                    name = project.get("name", "N/A")
                    project_type = project.get("projectTypeKey", "N/A")
                    print(f"  {key:15} - {name} ({project_type})")
            else:
                print("No projects found or no access to projects.")
            sys.exit(0)
        except Exception as e:
            print(f"Error listing projects: {e}")
            import traceback

            traceback.print_exc()
            sys.exit(1)

    # Verify project exists
    try:
        print(f"\nVerifying project '{project_key}' exists...")
        project_info = jira.get_project(project_key)
        if not project_info:
            print(f"\nError: Project '{project_key}' not found or no access.")
            print("\nAvailable projects:")
            try:
                projects = jira.get_all_projects(include_archived=False)
                if projects:
                    for project in sorted(projects, key=lambda x: x.get("key", "")):
                        key = project.get("key", "N/A")
                        name = project.get("name", "N/A")
                        print(f"  {key} - {name}")
                else:
                    print("  (No projects accessible)")
            except Exception:
                print("  (Could not fetch project list)")
            print("\nTip: Use --list-projects to see all available projects")
            sys.exit(1)
        else:
            project_name = project_info.get("name", "")
            print(f"  ✓ Project found: {project_name}")
    except Exception as e:
        print(f"Warning: Could not verify project: {e}")
        print("  Continuing anyway...")

    # Fetch all issues
    try:
        all_issues = fetch_all_project_issues(jira, project_key)

        if not all_issues:
            print(f"No issues found in project '{project_key}'")
            sys.exit(0)

        # Organize issues
        print("\nOrganizing issues...")
        organized = organize_issues(all_issues)

        print(f"  Found {len(organized['epics'])} epics")
        print(f"  Found {len(organized['stories'])} stories")
        print(f"  Found {len(organized['tasks'])} tasks")
        print(f"  Found {len(organized['other_issues'])} other issues")

        # Get project info (try to get from first issue or use defaults)
        project_name = ""
        if all_issues:
            project_info = all_issues[0].get("project", {})
            project_name = project_info.get("name", "")

        # Generate markdown files
        docs_dir = Path(__file__).parent.parent / "docs" / "pm"
        docs_dir.mkdir(parents=True, exist_ok=True)

        print("\nGenerating markdown files...")

        # Generate epics markdown
        epics_md = generate_epics_markdown(organized, project_key, project_name)
        epics_file = docs_dir / "suppathletik-epics.md"
        epics_file.write_text(epics_md, encoding="utf-8")
        print(f"  Generated: {epics_file}")

        # Generate index markdown
        index_md = generate_index_markdown(organized, project_key, project_name)
        index_file = docs_dir / "suppathletik-index.md"
        index_file.write_text(index_md, encoding="utf-8")
        print(f"  Generated: {index_file}")

        print("\nDone!")

    except Exception as e:
        print(f"Error fetching issues: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
