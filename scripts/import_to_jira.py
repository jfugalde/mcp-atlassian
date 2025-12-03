#!/usr/bin/env python3
"""
Script to import all Epics, Stories, and Tasks from JSON to Jira
Uses Jira REST API via MCP or direct API calls
"""

import json
import sys
from pathlib import Path

# Read the JSON file
json_path = Path(__file__).parent.parent / "docs" / "pm" / "farmacias-macross-jira-import.json"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data['epics'])} epics, {len(data['stories'])} stories, {len(data['tasks'])} tasks")
print("\nThis script would create:")
print(f"- {len(data['epics'])} Epics")
print(f"- {len(data['stories'])} Stories") 
print(f"- {len(data['tasks'])} Tasks")
print("\nTotal: {len(data['epics']) + len(data['stories']) + len(data['tasks'])} issues")
print("\nNote: This requires manual execution via Jira MCP tools or Jira API")



