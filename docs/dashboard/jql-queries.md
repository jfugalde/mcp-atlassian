# JQL Queries for Dashboard Filters

Generated: 2025-12-21 16:00:11

## Executive Summary

### All Issues

```jql
project in (RYU, SUPA) ORDER BY updated DESC
```

### To Do

```jql
project in (RYU, SUPA) AND status = "To Do" ORDER BY priority DESC, created ASC
```

### In Progress

```jql
project in (RYU, SUPA) AND status = "In Progress" ORDER BY updated DESC
```

### Done

```jql
project in (RYU, SUPA) AND status = Done ORDER BY resolved DESC
```

### By Quarter

```jql
project in (RYU, SUPA) AND fixVersion in ("2026-Q1", "2026-Q2", "2026-Q3", "2026-Q4") ORDER BY fixVersion ASC, priority DESC
```

## Quarterly

### Q1

```jql
project in (RYU, SUPA) AND fixVersion = "2026-Q1" ORDER BY priority DESC, created ASC
```

### Q2

```jql
project in (RYU, SUPA) AND fixVersion = "2026-Q2" ORDER BY priority DESC, created ASC
```

### Q3

```jql
project in (RYU, SUPA) AND fixVersion = "2026-Q3" ORDER BY priority DESC, created ASC
```

### Q4

```jql
project in (RYU, SUPA) AND fixVersion = "2026-Q4" ORDER BY priority DESC, created ASC
```

## Epics

### Ryu Epics

```jql
project = RYU AND issuetype = Epic ORDER BY created ASC
```

### Supa Epics

```jql
project = SUPA AND issuetype = Epic ORDER BY created ASC
```

### Epic Ryu 01

```jql
"Epic Link" = RYU-46 ORDER BY priority DESC, created ASC
```

### Epic Ryu 02

```jql
"Epic Link" = RYU-47 ORDER BY priority DESC, created ASC
```

### Epic Ryu 03

```jql
"Epic Link" = RYU-48 ORDER BY priority DESC, created ASC
```

### Epic Ryu 04

```jql
"Epic Link" = RYU-49 ORDER BY priority DESC, created ASC
```

### Epic Amz 01

```jql
"Epic Link" = SUPA-31 ORDER BY priority DESC, created ASC
```

### Epic Amz 02

```jql
"Epic Link" = SUPA-32 ORDER BY priority DESC, created ASC
```

### Epic Amz 03

```jql
"Epic Link" = SUPA-33 ORDER BY priority DESC, created ASC
```

### Epic Amz 04

```jql
"Epic Link" = SUPA-34 ORDER BY priority DESC, created ASC
```

### Epic Amz 05

```jql
"Epic Link" = SUPA-35 ORDER BY priority DESC, created ASC
```

### Epic Amz 06

```jql
"Epic Link" = SUPA-36 ORDER BY priority DESC, created ASC
```

### Epic Amz 07

```jql
"Epic Link" = SUPA-37 ORDER BY priority DESC, created ASC
```

### Epic Amz 08

```jql
"Epic Link" = SUPA-38 ORDER BY priority DESC, created ASC
```

### Epic Amz 09

```jql
"Epic Link" = SUPA-39 ORDER BY priority DESC, created ASC
```

## Components

### Ryu Offer

```jql
project = RYU AND component = "Offer" ORDER BY priority DESC, created ASC
```

### Ryu Client

```jql
project = RYU AND component = "Client" ORDER BY priority DESC, created ASC
```

### Ryu Delivery

```jql
project = RYU AND component = "Delivery" ORDER BY priority DESC, created ASC
```

### Ryu Playbook

```jql
project = RYU AND component = "Playbook" ORDER BY priority DESC, created ASC
```

### Ryu Ops

```jql
project = RYU AND component = "Ops" ORDER BY priority DESC, created ASC
```

### Supa Amazon Account

```jql
project = SUPA AND component = "Amazon-Account" ORDER BY priority DESC, created ASC
```

### Supa Compliance

```jql
project = SUPA AND component = "Compliance" ORDER BY priority DESC, created ASC
```

### Supa Finance

```jql
project = SUPA AND component = "Finance" ORDER BY priority DESC, created ASC
```

### Supa Catalog

```jql
project = SUPA AND component = "Catalog" ORDER BY priority DESC, created ASC
```

### Supa Logistics

```jql
project = SUPA AND component = "Logistics" ORDER BY priority DESC, created ASC
```

### Supa Cx

```jql
project = SUPA AND component = "CX" ORDER BY priority DESC, created ASC
```

### Supa Ads

```jql
project = SUPA AND component = "Ads" ORDER BY priority DESC, created ASC
```

### Supa Brand

```jql
project = SUPA AND component = "Brand" ORDER BY priority DESC, created ASC
```

### Supa Ops

```jql
project = SUPA AND component = "Ops" ORDER BY priority DESC, created ASC
```

## Project Comparison

### Ryu All

```jql
project = RYU ORDER BY updated DESC
```

### Supa All

```jql
project = SUPA ORDER BY updated DESC
```

### Ryu By Status

```jql
project = RYU ORDER BY status ASC, priority DESC
```

### Supa By Status

```jql
project = SUPA ORDER BY status ASC, priority DESC
```

