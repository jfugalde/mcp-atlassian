#!/usr/bin/env python3
"""
Script to help create remaining tasks and link them to stories
This provides the batch JSON for batch_create_issues tool
"""

import json
from pathlib import Path

json_path = Path(__file__).parent.parent / "docs" / "pm" / "farmacias-macross-jira-import.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Story mapping: JSON story key -> Jira story key
story_mapping = {
    "FM-1-1": "FM-5", "FM-1-2": "FM-6", "FM-1-3": "FM-7", "FM-1-4": "FM-8",
    "FM-2-1": "FM-9", "FM-2-2": "FM-10", "FM-2-3": "FM-11", "FM-2-4": "FM-12",
    "FM-3-1": "FM-13", "FM-3-2": "FM-14", "FM-3-3": "FM-15", "FM-3-4": "FM-16", "FM-3-5": "FM-17",
    "FM-4-1": "FM-18", "FM-4-2": "FM-19", "FM-4-3": "FM-20", "FM-4-4": "FM-21"
}

# Tasks already created (first 13)
created_tasks = [
    "FM-1-1-1", "FM-1-1-2", "FM-1-1-3",  # FM-22, FM-23, FM-24
    "FM-1-2-1", "FM-1-2-2", "FM-1-2-3", "FM-1-2-4", "FM-1-2-5", 
    "FM-1-2-6", "FM-1-2-7", "FM-1-2-8", "FM-1-2-9", "FM-1-2-10"  # FM-25 to FM-34
]

# Get remaining tasks
remaining_tasks = [t for t in data['tasks'] if t['key'] not in created_tasks]

print(f"Remaining tasks to create: {len(remaining_tasks)}")
print("\nGrouped by story:\n")

# Group by story
by_story = {}
for task in remaining_tasks:
    story = task['story']
    if story not in by_story:
        by_story[story] = []
    by_story[story].append(task)

# Print batches for easy copy-paste
for story_key, tasks in sorted(by_story.items()):
    jira_story = story_mapping[story_key]
    print(f"\n{story_key} ({jira_story}) - {len(tasks)} tasks:")
    print(f"  Batch JSON for batch_create_issues:")
    batch = []
    for task in tasks:
        batch.append({
            "project_key": "FM",
            "summary": task['summary'],
            "issue_type": "Task",
            "description": task['description']
        })
    print(json.dumps(batch, indent=2, ensure_ascii=False))
    print(f"\n  Then link all to {jira_story} using create_issue_link")





