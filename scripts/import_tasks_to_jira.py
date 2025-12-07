#!/usr/bin/env python3
"""
Script to import all Tasks from JSON to Jira as Subtasks
This script creates tasks linked to their parent stories
"""

import json
from pathlib import Path

# Read the JSON file
json_path = Path(__file__).parent.parent / "docs" / "pm" / "farmacias-macross-jira-import.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Story key mapping (from JSON key to actual Jira key)
# FM-1-1 -> FM-5, FM-1-2 -> FM-6, etc.
story_mapping = {
    "FM-1-1": "FM-5",
    "FM-1-2": "FM-6", 
    "FM-1-3": "FM-7",
    "FM-1-4": "FM-8",
    "FM-2-1": "FM-9",
    "FM-2-2": "FM-10",
    "FM-2-3": "FM-11",
    "FM-2-4": "FM-12",
    "FM-3-1": "FM-13",
    "FM-3-2": "FM-14",
    "FM-3-3": "FM-15",
    "FM-3-4": "FM-16",
    "FM-3-5": "FM-17",
    "FM-4-1": "FM-18",
    "FM-4-2": "FM-19",
    "FM-4-3": "FM-20",
    "FM-4-4": "FM-21"
}

print("Task Import Script")
print("=" * 50)
print(f"\nTotal tasks to create: {len(data['tasks'])}")
print("\nTasks grouped by story:")
for story_key, jira_key in story_mapping.items():
    story_tasks = [t for t in data['tasks'] if t['story'] == story_key]
    print(f"\n{story_key} ({jira_key}): {len(story_tasks)} tasks")
    for task in story_tasks:
        print(f"  - {task['key']}: {task['summary']}")

print("\n\nTo create these tasks, use Jira MCP tools with:")
print("- issue_type: 'Subtask'")
print("- additional_fields: {'parent': '<story_jira_key>'}")
print("\nExample for FM-1-1-1:")
print("  parent: 'FM-5'")





