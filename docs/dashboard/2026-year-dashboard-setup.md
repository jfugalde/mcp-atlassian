# 2026 Year Dashboard Setup Guide - RYU & SUPA

This guide provides step-by-step instructions for creating a comprehensive Jira dashboard to track progress across RYU and SUPA projects for 2026.

## Dashboard Overview

The dashboard tracks:
- **Quarterly Milestones**: Q1-Q4 2026 deliverables
- **Epic Progress**: All epics across both projects
- **Component Breakdown**: Issues organized by component
- **Project Comparison**: RYU vs SUPA side-by-side metrics

## Step 1: Create Saved Filters

Create the following saved filters in Jira (Issues → Search for issues → Save as filter):

### Executive Summary Filters

**All RYU & SUPA Issues**
```
project in (RYU, SUPA) ORDER BY updated DESC
```

**Issues by Status - To Do**
```
project in (RYU, SUPA) AND status = "To Do" ORDER BY priority DESC, created ASC
```

**Issues by Status - In Progress**
```
project in (RYU, SUPA) AND status = "In Progress" ORDER BY updated DESC
```

**Issues by Status - Done**
```
project in (RYU, SUPA) AND status = Done ORDER BY resolved DESC
```

**All Issues by Quarter**
```
project in (RYU, SUPA) AND fixVersion in ("2026-Q1", "2026-Q2", "2026-Q3", "2026-Q4") ORDER BY fixVersion ASC, priority DESC
```

### Quarterly Filters

**Q1 2026 Issues**
```
project in (RYU, SUPA) AND fixVersion = "2026-Q1" ORDER BY priority DESC, created ASC
```

**Q2 2026 Issues**
```
project in (RYU, SUPA) AND fixVersion = "2026-Q2" ORDER BY priority DESC, created ASC
```

**Q3 2026 Issues**
```
project in (RYU, SUPA) AND fixVersion = "2026-Q3" ORDER BY priority DESC, created ASC
```

**Q4 2026 Issues**
```
project in (RYU, SUPA) AND fixVersion = "2026-Q4" ORDER BY priority DESC, created ASC
```

### Epic Progress Filters

**All RYU Epics**
```
project = RYU AND issuetype = Epic ORDER BY created ASC
```

**All SUPA Epics**
```
project = SUPA AND issuetype = Epic ORDER BY created ASC
```

**EPIC-RYU-01 Issues**
```
"Epic Link" = RYU-46 ORDER BY priority DESC, created ASC
```

**EPIC-RYU-02 Issues**
```
"Epic Link" = RYU-47 ORDER BY priority DESC, created ASC
```

**EPIC-RYU-03 Issues**
```
"Epic Link" = RYU-48 ORDER BY priority DESC, created ASC
```

**EPIC-RYU-04 Issues**
```
"Epic Link" = RYU-49 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-01 Issues**
```
"Epic Link" = SUPA-31 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-02 Issues**
```
"Epic Link" = SUPA-32 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-03 Issues**
```
"Epic Link" = SUPA-33 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-04 Issues**
```
"Epic Link" = SUPA-34 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-05 Issues**
```
"Epic Link" = SUPA-35 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-06 Issues**
```
"Epic Link" = SUPA-36 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-07 Issues**
```
"Epic Link" = SUPA-37 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-08 Issues**
```
"Epic Link" = SUPA-38 ORDER BY priority DESC, created ASC
```

**EPIC-AMZ-09 Issues**
```
"Epic Link" = SUPA-39 ORDER BY priority DESC, created ASC
```

### Component Filters

**RYU - Offer Component**
```
project = RYU AND component = "Offer" ORDER BY priority DESC, created ASC
```

**RYU - Client Component**
```
project = RYU AND component = "Client" ORDER BY priority DESC, created ASC
```

**RYU - Delivery Component**
```
project = RYU AND component = "Delivery" ORDER BY priority DESC, created ASC
```

**RYU - Playbook Component**
```
project = RYU AND component = "Playbook" ORDER BY priority DESC, created ASC
```

**RYU - Ops Component**
```
project = RYU AND component = "Ops" ORDER BY priority DESC, created ASC
```

**SUPA - Amazon-Account Component**
```
project = SUPA AND component = "Amazon-Account" ORDER BY priority DESC, created ASC
```

**SUPA - Compliance Component**
```
project = SUPA AND component = "Compliance" ORDER BY priority DESC, created ASC
```

**SUPA - Finance Component**
```
project = SUPA AND component = "Finance" ORDER BY priority DESC, created ASC
```

**SUPA - Catalog Component**
```
project = SUPA AND component = "Catalog" ORDER BY priority DESC, created ASC
```

**SUPA - Logistics Component**
```
project = SUPA AND component = "Logistics" ORDER BY priority DESC, created ASC
```

**SUPA - CX Component**
```
project = SUPA AND component = "CX" ORDER BY priority DESC, created ASC
```

**SUPA - Ads Component**
```
project = SUPA AND component = "Ads" ORDER BY priority DESC, created ASC
```

**SUPA - Brand Component**
```
project = SUPA AND component = "Brand" ORDER BY priority DESC, created ASC
```

**SUPA - Ops Component**
```
project = SUPA AND component = "Ops" ORDER BY priority DESC, created ASC
```

### Project Comparison Filters

**All RYU Issues**
```
project = RYU ORDER BY updated DESC
```

**All SUPA Issues**
```
project = SUPA ORDER BY updated DESC
```

**RYU Issues by Status**
```
project = RYU ORDER BY status ASC, priority DESC
```

**SUPA Issues by Status**
```
project = SUPA ORDER BY status ASC, priority DESC
```

## Step 2: Create Dashboard

1. Go to **Dashboards** → **Create dashboard**
2. Name: **"2026 Year Dashboard - RYU & SUPA"**
3. Description: **"Comprehensive tracking dashboard for RYU and SUPA projects across 2026"**
4. Share with: Your team/workspace

## Step 3: Add Dashboard Gadgets

### Executive Summary Section

**1. Filter Results - All Issues**
- Gadget: **Filter Results**
- Filter: "All RYU & SUPA Issues"
- Columns: Key, Summary, Status, Assignee, Fix Version, Component
- Max issues: 50

**2. Created vs Resolved Chart**
- Gadget: **Created vs Resolved Chart**
- Filter: "All RYU & SUPA Issues"
- Period: Last 12 months

**3. Pie Chart - Issues by Status**
- Gadget: **Pie Chart**
- Filter: "All RYU & SUPA Issues"
- Group by: **Status**

**4. Pie Chart - Issues by Project**
- Gadget: **Pie Chart**
- Filter: "All RYU & SUPA Issues"
- Group by: **Project**

### Quarterly Milestones Section

**5. Filter Results - Q1 2026**
- Gadget: **Filter Results**
- Filter: "Q1 2026 Issues"
- Columns: Key, Summary, Status, Assignee, Epic Link, Component
- Max issues: 30

**6. Filter Results - Q2 2026**
- Gadget: **Filter Results**
- Filter: "Q2 2026 Issues"
- Columns: Key, Summary, Status, Assignee, Epic Link, Component
- Max issues: 30

**7. Filter Results - Q3 2026**
- Gadget: **Filter Results**
- Filter: "Q3 2026 Issues"
- Columns: Key, Summary, Status, Assignee, Epic Link, Component
- Max issues: 30

**8. Filter Results - Q4 2026**
- Gadget: **Filter Results**
- Filter: "Q4 2026 Issues"
- Columns: Key, Summary, Status, Assignee, Epic Link, Component
- Max issues: 30

### Epic Progress Section

**9. Filter Results - RYU Epics**
- Gadget: **Filter Results**
- Filter: "All RYU Epics"
- Columns: Key, Summary, Status, Fix Version
- Max issues: 10

**10. Filter Results - SUPA Epics**
- Gadget: **Filter Results**
- Filter: "All SUPA Epics"
- Columns: Key, Summary, Status, Fix Version
- Max issues: 10

**11. Two Dimensional Filter Statistics - Epic Progress**
- Gadget: **Two Dimensional Filter Statistics**
- Filter: "All RYU & SUPA Issues"
- First dimension: **Epic Link**
- Second dimension: **Status**

### Component Breakdown Section

**12. Pie Chart - Issues by Component (RYU)**
- Gadget: **Pie Chart**
- Filter: "All RYU Issues"
- Group by: **Component**

**13. Pie Chart - Issues by Component (SUPA)**
- Gadget: **Pie Chart**
- Filter: "All SUPA Issues"
- Group by: **Component**

**14. Two Dimensional Filter Statistics - Component vs Status**
- Gadget: **Two Dimensional Filter Statistics**
- Filter: "All RYU & SUPA Issues"
- First dimension: **Component**
- Second dimension: **Status**

### Project Comparison Section

**15. Filter Results - RYU Issues**
- Gadget: **Filter Results**
- Filter: "All RYU Issues"
- Columns: Key, Summary, Status, Assignee, Fix Version
- Max issues: 25

**16. Filter Results - SUPA Issues**
- Gadget: **Filter Results**
- Filter: "All SUPA Issues"
- Columns: Key, Summary, Status, Assignee, Fix Version
- Max issues: 25

**17. Two Dimensional Filter Statistics - Project vs Status**
- Gadget: **Two Dimensional Filter Statistics**
- Filter: "All RYU & SUPA Issues"
- First dimension: **Project**
- Second dimension: **Status**

**18. Two Dimensional Filter Statistics - Project vs Quarter**
- Gadget: **Two Dimensional Filter Statistics**
- Filter: "All RYU & SUPA Issues"
- First dimension: **Project**
- Second dimension: **Fix Version**

### Additional Useful Gadgets

**19. Assigned to Me**
- Gadget: **Assigned to Me**
- Filter: "All RYU & SUPA Issues"
- Max issues: 20

**20. Activity Stream**
- Gadget: **Activity Stream**
- Filter: "All RYU & SUPA Issues"
- Max items: 20

## Step 4: Arrange Dashboard Layout

Recommended layout:
- **Row 1**: Executive Summary (gadgets 1-4)
- **Row 2**: Quarterly Milestones (gadgets 5-8)
- **Row 3**: Epic Progress (gadgets 9-11)
- **Row 4**: Component Breakdown (gadgets 12-14)
- **Row 5**: Project Comparison (gadgets 15-18)
- **Row 6**: Personal & Activity (gadgets 19-20)

## Step 5: Configure Gadget Refresh

- Set auto-refresh interval: **5 minutes** (or as needed)
- Enable notifications for critical updates

## Links to Jira Boards

- **RYU Board**: [FM board](https://ryu-technologies.atlassian.net/jira/software/projects/RYU/boards)
- **SUPA Board**: [SUPA board](https://ryu-technologies.atlassian.net/jira/software/projects/SUPA/boards)

## Notes

- All filters are saved and can be shared with your team
- Dashboard gadgets auto-update from Jira data
- Filters can be modified to add additional criteria (e.g., assignee, labels)
- Use the dashboard to track progress and identify blockers
- Run the `generate_dashboard_metrics.py` script periodically to get updated statistics


