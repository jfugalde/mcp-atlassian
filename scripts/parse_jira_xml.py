#!/usr/bin/env python3
"""
Script to parse Jira XML export and generate markdown documentation
similar to the FM project structure.
"""

import argparse
import html
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


def clean_text(text: str) -> str:
    """Clean and format text from Jira XML.
    
    Handles HTML entities, tags, and formatting.
    """
    if not text:
        return ""
    
    # Unescape HTML/XML entities
    text = html.unescape(text)
    
    # Convert common HTML entities to markdown-friendly text
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;", '"')
    text = text.replace("&#39;", "'")
    
    # Remove HTML tags but preserve structure
    # Convert <p> to double newlines
    text = re.sub(r"<p[^>]*>", "\n\n", text)
    text = re.sub(r"</p>", "", text)
    
    # Convert <br/> to single newline
    text = re.sub(r"<br\s*/?>", "\n", text)
    
    # Convert <b> and <strong> to **bold**
    text = re.sub(r"<(b|strong)[^>]*>(.*?)</(b|strong)>", r"**\2**", text, flags=re.DOTALL)
    
    # Convert <i> and <em> to *italic*
    text = re.sub(r"<(i|em)[^>]*>(.*?)</(i|em)>", r"*\2*", text, flags=re.DOTALL)
    
    # Convert <ul><li> to markdown lists
    text = re.sub(r"<ul[^>]*>", "", text)
    text = re.sub(r"</ul>", "", text)
    text = re.sub(r"<li[^>]*>", "- ", text)
    text = re.sub(r"</li>", "", text)
    
    # Convert <ol><li> to numbered lists
    text = re.sub(r"<ol[^>]*>", "", text)
    text = re.sub(r"</ol>", "", text)
    # Note: Numbered lists need special handling, keeping as bullets for now
    
    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    
    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)  # Max 2 consecutive newlines
    text = re.sub(r"[ \t]+", " ", text)  # Multiple spaces to single
    text = text.strip()
    
    return text


def format_description(description: str, max_length: int = 500) -> str:
    """Format description for markdown display.
    
    Args:
        description: Raw description text
        max_length: Maximum length before truncation
        
    Returns:
        Formatted description
    """
    if not description:
        return ""
    
    desc = clean_text(description)
    
    # Truncate if too long, but try to break at sentence
    if len(desc) > max_length:
        # Try to break at last sentence before max_length
        truncated = desc[:max_length]
        last_period = truncated.rfind(".")
        last_newline = truncated.rfind("\n")
        break_point = max(last_period, last_newline)
        
        if break_point > max_length * 0.7:  # If we found a good break point
            desc = desc[:break_point + 1]
        else:
            desc = desc[:max_length]
        desc += "..."
    
    return desc


def parse_jira_xml(xml_path: Path) -> list[dict[str, Any]]:
    """Parse Jira XML export file and extract all issues.

    Args:
        xml_path: Path to the Jira XML export file

    Returns:
        List of issue dictionaries
    """
    print(f"Parsing Jira XML file: {xml_path}")
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the channel element (RSS structure)
    channel = root.find("channel")
    if channel is None:
        raise ValueError("Invalid XML structure: no <channel> element found")

    issues = []
    items = channel.findall("item")

    print(f"Found {len(items)} issues in XML")

    for item in items:
        issue = {}

        # Extract basic fields
        key_elem = item.find("key")
        issue["key"] = key_elem.text if key_elem is not None else ""

        summary_elem = item.find("summary")
        issue["summary"] = clean_text(summary_elem.text) if summary_elem is not None else ""

        type_elem = item.find("type")
        issue["issuetype"] = {
            "name": type_elem.text if type_elem is not None else "Unknown"
        }

        status_elem = item.find("status")
        issue["status"] = {
            "name": status_elem.text if status_elem is not None else "Unknown"
        }

        priority_elem = item.find("priority")
        issue["priority"] = {
            "name": priority_elem.text if priority_elem is not None else ""
        }

        description_elem = item.find("description")
        issue["description"] = (
            clean_text(description_elem.text) if description_elem is not None else ""
        )

        # Extract parent (for subtasks)
        parent_elem = item.find("parent")
        if parent_elem is not None:
            parent_key = parent_elem.text if parent_elem.text else None
            if parent_key:
                issue["parent"] = {"key": parent_key}

        # Extract Epic Link from customfields
        epic_link = None
        customfields = item.find("customfields")
        if customfields is not None:
            for customfield in customfields.findall("customfield"):
                field_name = customfield.find("customfieldname")
                if field_name is not None and "Epic Link" in field_name.text:
                    values = customfield.find("customfieldvalues")
                    if values is not None:
                        value_elem = values.find("customfieldvalue")
                        if value_elem is not None:
                            epic_link = value_elem.text
                            break

        if epic_link:
            issue["epicLink"] = epic_link

        # Extract project info
        project_elem = item.find("project")
        if project_elem is not None:
            issue["project"] = {
                "key": project_elem.get("key", ""),
                "name": project_elem.text or "",
            }

        # Extract assignee
        assignee_elem = item.find("assignee")
        if assignee_elem is not None and assignee_elem.text:
            issue["assignee"] = {"displayName": assignee_elem.text}

        # Extract created/updated dates
        created_elem = item.find("created")
        issue["created"] = created_elem.text if created_elem is not None else ""

        updated_elem = item.find("updated")
        issue["updated"] = updated_elem.text if updated_elem is not None else ""
        
        resolved_elem = item.find("resolved")
        issue["resolved"] = resolved_elem.text if resolved_elem is not None else ""
        
        # Extract time tracking
        time_original_estimate = item.find("timeoriginalestimate")
        if time_original_estimate is not None and time_original_estimate.text:
            issue["time_original_estimate"] = time_original_estimate.text
        
        time_spent = item.find("timespent")
        if time_spent is not None and time_spent.text:
            issue["time_spent"] = time_spent.text

        # Extract labels
        labels_elem = item.find("labels")
        labels = []
        if labels_elem is not None:
            for label in labels_elem.findall("label"):
                if label.text:
                    labels.append(label.text)
        issue["labels"] = labels

        issues.append(issue)

    print(f"Successfully parsed {len(issues)} issues")
    return issues


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
    # Epic links can be by key or by name (summary)
    epic_links: dict[str, list[dict[str, Any]]] = {}
    # Create a mapping from epic name to epic key
    epic_name_to_key: dict[str, str] = {}
    for epic in epics:
        epic_key = epic.get("key", "")
        epic_name = epic.get("summary", "")
        if epic_name:
            epic_name_to_key[epic_name] = epic_key

    for story in stories + tasks + other_issues:
        epic_link = story.get("epicLink")
        if epic_link:
            # Try to find epic by name first, then by key
            epic_key = None
            if epic_link in epic_name_to_key:
                epic_key = epic_name_to_key[epic_link]
            elif epic_link in issues_by_key:
                epic_key = epic_link

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
    epic_keys = [e.get("key", "") for e in epics]
    lines.append(f"- **{len(epics)} Epics**: {', '.join(epic_keys)}")
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
        epic_description = epic.get("description", "")

        # Get custom fields that might be useful
        priority = epic.get("priority", {}).get("name", "")
        assignee = epic.get("assignee", {}).get("displayName", "")
        created = epic.get("created", "")
        updated = epic.get("updated", "")

        lines.append(f"## EPIC {epic_idx}: {epic_summary}")
        lines.append("")
        lines.append(f"**Epic Key**: {epic_key}")
        lines.append(f"**Summary**: {epic_summary}")
        lines.append(f"**Status**: {epic_status}")
        if priority:
            lines.append(f"**Priority**: {priority}")
        if assignee and assignee != "Unassigned":
            lines.append(f"**Assignee**: {assignee}")
        if created:
            # Format date nicely
            try:
                from datetime import datetime
                dt = datetime.strptime(created.split(",")[1].strip(), "%d %b %Y %H:%M:%S %z")
                lines.append(f"**Created**: {dt.strftime('%Y-%m-%d')}")
            except Exception:
                lines.append(f"**Created**: {created}")
        
        # Count linked issues
        epic_stories = epic_links.get(epic_key, [])
        if epic_stories:
            stories_count = len([s for s in epic_stories if s.get("issuetype", {}).get("name", "").lower() in ["story", "user story"]])
            tasks_count = len([t for t in epic_stories if t.get("issuetype", {}).get("name", "").lower() in ["task", "subtask"]])
            if stories_count > 0 or tasks_count > 0:
                counts = []
                if stories_count > 0:
                    counts.append(f"{stories_count} Stories")
                if tasks_count > 0:
                    counts.append(f"{tasks_count} Tasks")
                lines.append(f"**Linked Issues**: {', '.join(counts)}")
        
        lines.append("")
        
        if epic_description:
            desc = format_description(epic_description, max_length=400)
            if desc:
                lines.append("**Description**:")
                lines.append("")
                # Indent description for better readability
                for line in desc.split("\n"):
                    if line.strip():
                        lines.append(f"  {line}")
                    else:
                        lines.append("")
                lines.append("")

        # Get stories/tasks linked to this epic
        epic_stories = epic_links.get(epic_key, [])

        if epic_stories:
            # Separate stories and tasks
            epic_stories_list = [
                s
                for s in epic_stories
                if s.get("issuetype", {}).get("name", "").lower() in ["story", "user story"]
            ]
            epic_tasks_list = [
                t
                for t in epic_stories
                if t.get("issuetype", {}).get("name", "").lower() in ["task", "subtask"]
            ]

            # Sort by key
            epic_stories_list = sorted(epic_stories_list, key=lambda x: x.get("key", ""))
            epic_tasks_list = sorted(epic_tasks_list, key=lambda x: x.get("key", ""))

            # Process stories
            for story in epic_stories_list:
                story_key = story.get("key", "")
                story_summary = story.get("summary", "")
                story_status = story.get("status", {}).get("name", "Unknown")
                story_priority = story.get("priority", {}).get("name", "")
                story_description = story.get("description", "")

                story_assignee = story.get("assignee", {}).get("displayName", "")
                story_labels = story.get("labels", [])
                
                lines.append(f"### Story {story_key}: {story_summary}")
                lines.append("")
                lines.append(f"**Story Key**: {story_key}")
                lines.append(f"**Summary**: {story_summary}")
                lines.append(f"**Status**: {story_status}")
                if story_priority:
                    lines.append(f"**Priority**: {story_priority}")
                if story_assignee and story_assignee != "Unassigned":
                    lines.append(f"**Assignee**: {story_assignee}")
                if story_labels:
                    lines.append(f"**Labels**: {', '.join(story_labels)}")
                
                # Get task count for this story
                story_tasks = parent_children.get(story_key, [])
                if story_tasks:
                    done_count = len([t for t in story_tasks if t.get("status", {}).get("name", "").lower() == "done"])
                    total_count = len(story_tasks)
                    lines.append(f"**Tasks**: {total_count} total ({done_count} done)")
                
                lines.append("")
                
                if story_description:
                    desc = format_description(story_description, max_length=300)
                    if desc:
                        lines.append("**Description**:")
                        lines.append("")
                        for line in desc.split("\n"):
                            if line.strip():
                                lines.append(f"  {line}")
                            else:
                                lines.append("")
                        lines.append("")

                # Get tasks linked to this story (as parent)
                story_tasks = parent_children.get(story_key, [])
                story_tasks = sorted(story_tasks, key=lambda x: x.get("key", ""))

                if story_tasks:
                    # Group tasks by status for better organization
                    tasks_by_status: dict[str, list[dict[str, Any]]] = {}
                    for task in story_tasks:
                        status = task.get("status", {}).get("name", "Unknown")
                        if status not in tasks_by_status:
                            tasks_by_status[status] = []
                        tasks_by_status[status].append(task)
                    
                    # Sort statuses: Done first, then others
                    status_order = ["Done", "In Progress", "To Do", "In Review", "Blocked"]
                    sorted_statuses = sorted(
                        tasks_by_status.keys(),
                        key=lambda x: (
                            status_order.index(x) if x in status_order else 999,
                            x
                        )
                    )
                    
                    lines.append("#### Tasks:")
                    lines.append("")
                    
                    for status in sorted_statuses:
                        status_tasks = sorted(tasks_by_status[status], key=lambda x: x.get("key", ""))
                        if len(sorted_statuses) > 1:
                            lines.append(f"**{status}** ({len(status_tasks)}):")
                            lines.append("")
                        
                        for task in status_tasks:
                            task_key = task.get("key", "")
                            task_summary = task.get("summary", "")
                            task_status = task.get("status", {}).get("name", "Unknown")
                            task_priority = task.get("priority", {}).get("name", "")
                            task_assignee = task.get("assignee", {}).get("displayName", "")
                            task_labels = task.get("labels", [])
                            
                            # Build task line with key info
                            task_parts = [f"**{task_key}**: {task_summary}"]
                            if task_status != status or len(sorted_statuses) == 1:
                                task_parts.append(f"Status: {task_status}")
                            if task_priority:
                                task_parts.append(f"Priority: {task_priority}")
                            
                            lines.append(f"- {', '.join(task_parts)}")
                            
                            # Add additional info if available
                            if task_assignee and task_assignee != "Unassigned":
                                lines.append(f"  - Assignee: {task_assignee}")
                            if task_labels:
                                lines.append(f"  - Labels: {', '.join(task_labels)}")
                            
                            # Add time tracking if available
                            if task.get("time_spent"):
                                lines.append(f"  - Time Spent: {task.get('time_spent')}")
                            
                            lines.append("")

                lines.append("---")
                lines.append("")

            # Process standalone tasks (not linked to stories as subtasks)
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
                # Group standalone tasks by status
                standalone_by_status: dict[str, list[dict[str, Any]]] = {}
                for task in standalone_tasks:
                    status = task.get("status", {}).get("name", "Unknown")
                    if status not in standalone_by_status:
                        standalone_by_status[status] = []
                    standalone_by_status[status].append(task)
                
                # Sort statuses
                status_order = ["Done", "In Progress", "To Do", "In Review", "Blocked"]
                sorted_statuses = sorted(
                    standalone_by_status.keys(),
                    key=lambda x: (
                        status_order.index(x) if x in status_order else 999,
                        x
                    )
                )
                
                lines.append("### Standalone Tasks:")
                lines.append("")
                
                for status in sorted_statuses:
                    status_tasks = sorted(standalone_by_status[status], key=lambda x: x.get("key", ""))
                    if len(sorted_statuses) > 1:
                        lines.append(f"**{status}** ({len(status_tasks)}):")
                        lines.append("")
                    
                    for task in status_tasks:
                        task_key = task.get("key", "")
                        task_summary = task.get("summary", "")
                        task_status = task.get("status", {}).get("name", "Unknown")
                        task_priority = task.get("priority", {}).get("name", "")
                        task_assignee = task.get("assignee", {}).get("displayName", "")
                        
                        task_parts = [f"**{task_key}**: {task_summary}"]
                        if task_status != status or len(sorted_statuses) == 1:
                            task_parts.append(f"Status: {task_status}")
                        if task_priority:
                            task_parts.append(f"Priority: {task_priority}")
                        
                        lines.append(f"- {', '.join(task_parts)}")
                        
                        if task_assignee and task_assignee != "Unassigned":
                            lines.append(f"  - Assignee: {task_assignee}")
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
    today = datetime.now().strftime("%Y-%m-%d")
    lines.append("| Document | Purpose | Last Updated |")
    lines.append("|----------|---------|--------------|")
    lines.append(
        f"| [Epic Structure](./suppathletik-epics.md) | Complete breakdown of all "
        f"epics, stories, and tasks | {today} |"
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
    
    # Calculate status breakdown
    status_counts: dict[str, int] = {}
    for issue in epics + stories + tasks:
        status = issue.get("status", {}).get("name", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
    
    if status_counts:
        lines.append("### Status Breakdown")
        lines.append("")
        for status in sorted(status_counts.keys()):
            count = status_counts[status]
            percentage = (count / (len(epics) + len(stories) + len(tasks))) * 100
            lines.append(f"- **{status}**: {count} issues ({percentage:.1f}%)")
        lines.append("")

    if epics:
        lines.append("### Epics")
        lines.append("")
        for epic in sorted(epics, key=lambda x: x.get("key", "")):
            epic_key = epic.get("key", "")
            epic_summary = epic.get("summary", "")
            epic_status = epic.get("status", {}).get("name", "Unknown")
            epic_priority = epic.get("priority", {}).get("name", "")
            
            epic_info = f"- **{epic_key}**: {epic_summary}"
            epic_info += f" (Status: {epic_status}"
            if epic_priority:
                epic_info += f", Priority: {epic_priority}"
            epic_info += ")"
            lines.append(epic_info)
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Esta documentación se genera automáticamente desde Jira XML export")
    lines.append(
        "- Para actualizar, ejecutar el script `scripts/parse_jira_xml.py`"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    today = datetime.now().strftime("%Y-%m-%d")
    lines.append(f"**Última actualización**: {today}")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main function to parse XML and generate markdown files."""
    parser = argparse.ArgumentParser(
        description="Parse Jira XML export and generate markdown documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "xml_file",
        type=str,
        help="Path to Jira XML export file",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="docs/suppathletik",
        help="Output directory for markdown files (default: docs/suppathletik)",
    )

    args = parser.parse_args()

    xml_path = Path(args.xml_file)
    if not xml_path.exists():
        print(f"Error: XML file not found: {xml_path}")
        sys.exit(1)

    # Parse XML
    try:
        issues = parse_jira_xml(xml_path)
        if not issues:
            print("No issues found in XML file")
            sys.exit(0)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

    # Organize issues
    print("\nOrganizing issues...")
    organized = organize_issues(issues)

    print(f"  Found {len(organized['epics'])} epics")
    print(f"  Found {len(organized['stories'])} stories")
    print(f"  Found {len(organized['tasks'])} tasks")
    print(f"  Found {len(organized['other_issues'])} other issues")

    # Get project info from first issue
    project_key = "SD"
    project_name = "SUPP-DIGITAL"
    if issues:
        project_info = issues[0].get("project", {})
        project_key = project_info.get("key", "SD")
        project_name = project_info.get("name", "SUPP-DIGITAL")

    # Generate markdown files
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating markdown files in {output_dir}...")

    # Generate epics markdown
    epics_md = generate_epics_markdown(organized, project_key, project_name)
    epics_file = output_dir / "suppathletik-epics.md"
    epics_file.write_text(epics_md, encoding="utf-8")
    print(f"  Generated: {epics_file}")

    # Generate index markdown
    index_md = generate_index_markdown(organized, project_key, project_name)
    index_file = output_dir / "suppathletik-index.md"
    index_file.write_text(index_md, encoding="utf-8")
    print(f"  Generated: {index_file}")

    print("\nDone!")


if __name__ == "__main__":
    main()

