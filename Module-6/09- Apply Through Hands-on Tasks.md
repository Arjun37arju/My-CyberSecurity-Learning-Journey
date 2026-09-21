# Apply Through Hands-on Tasks

## Table of Contents

1. [Build Log Analysis Scripts](#1-build-log-analysis-scripts)
2. [Create Monitoring Tools](#2-create-monitoring-tools)
3. [Develop Automation Workflows](#3-develop-automation-workflows)
4. [Generate Security Reports](#4-generate-security-reports)
5. [Build Incident-Support Utilities](#5-build-incident-support-utilities)
6. [Complete Hands-on Workflow](#complete-hands-on-workflow)

---

## 1. Build Log Analysis Scripts

### What is Log Analysis?

**Log analysis** means reading security logs and finding useful or suspicious events.

A script can automatically:

* Read log files
* Find failed login attempts
* Find errors
* Extract IP addresses
* Count events
* Detect suspicious patterns

### Example

```python
logs = [
    "Failed login from 192.168.1.10",
    "Successful login from 192.168.1.20",
    "Failed login from 192.168.1.10",
    "ERROR: Database connection failed"
]

failed_logins = []

for log in logs:
    if "Failed login" in log:
        failed_logins.append(log)

print("Failed login attempts:", len(failed_logins))
```

### Practical Goal

Build a script that reads a log file and identifies important security events.

---

## 2. Create Monitoring Tools

### What is a Monitoring Tool?

A **monitoring tool** continuously checks a system, service, file, or network activity.

It can monitor:

* CPU usage
* Memory usage
* Disk usage
* Running processes
* Services
* Files
* Network connections

### Example

```python
import psutil

cpu = psutil.cpu_percent(interval=1)

print("CPU Usage:", cpu, "%")

if cpu > 80:
    print("ALERT: High CPU usage!")
```

### Practical Goal

Build a simple monitoring tool that checks system resources and generates alerts when a threshold is exceeded.

---

## 3. Develop Automation Workflows

### What is an Automation Workflow?

An **automation workflow** connects multiple security tasks and performs them in a specific order.

### Example Workflow

```text
Detect Event
     ↓
Analyze Event
     ↓
Check Condition
     ↓
Generate Alert
     ↓
Create Ticket
     ↓
Generate Report
```

### Example

```python
failed_logins = 5

if failed_logins >= 5:
    print("1. Incident detected")
    print("2. Alert generated")
    print("3. Security ticket created")
    print("4. Investigation required")
```

### Practical Goal

Combine multiple security automation tasks into one workflow.

---

## 4. Generate Security Reports

### What is a Security Report?

A **security report** summarizes important security events and findings.

A report can include:

* Total log entries
* Failed logins
* Errors
* Suspicious events
* Alerts
* Incident status

### Example

```python
total_logs = 100
failed_logins = 12
errors = 5
alerts = 3

report = f"""
========== SECURITY REPORT ==========

Total logs       : {total_logs}
Failed logins    : {failed_logins}
Errors           : {errors}
Security alerts  : {alerts}

======================================
"""

print(report)
```

### Practical Goal

Create a script that analyzes security data and automatically generates a readable report.

---

## 5. Build Incident-Support Utilities

### What is an Incident-Support Utility?

An **incident-support utility** is a small tool that helps security professionals investigate or respond to security incidents.

### Examples

* IP information checker
* Log search tool
* File hash checker
* Port checker
* Process viewer
* System information collector
* Failed-login counter

### Example: File Hash Checker

```python
import hashlib

def get_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

filename = "sample.txt"

print("SHA-256:", get_hash(filename))
```

A file hash can be used to compare a file's current content with a known reference.

### Practical Goal

Build small utilities that make common incident investigation tasks faster.

---

# Complete Hands-on Workflow

The five tasks can be combined into one security automation project:

```text
             Security Logs
                  ↓
          Log Analysis Script
                  ↓
          Detect Security Event
                  ↓
           Monitoring Tool
                  ↓
           Generate Alert
                  ↓
        Automation Workflow
                  ↓
       Incident-Support Utility
                  ↓
          Generate Report
```

---

# Example Mini Project

## Security Log Monitoring and Reporting Tool

### Features

```text
1. Read security logs
2. Find failed login attempts
3. Count security events
4. Detect suspicious activity
5. Generate alerts
6. Create a security report
```

### Basic Structure

```python
def analyze_logs(logs):
    failed_logins = []

    for log in logs:
        if "Failed login" in log:
            failed_logins.append(log)

    return failed_logins


def generate_report(logs, failed_logins):
    print("========== SECURITY REPORT ==========")
    print("Total logs:", len(logs))
    print("Failed logins:", len(failed_logins))


logs = [
    "Failed login from 192.168.1.10",
    "Successful login from 192.168.1.20",
    "Failed login from 192.168.1.10",
    "ERROR: Database connection failed"
]

failed_logins = analyze_logs(logs)

if len(failed_logins) >= 2:
    print("ALERT: Multiple failed login attempts detected!")

generate_report(logs, failed_logins)
```

---

# Quick Revision

| Task                             | Purpose                              |
| -------------------------------- | ------------------------------------ |
| Build Log Analysis Scripts       | Analyze security logs                |
| Create Monitoring Tools          | Monitor systems and services         |
| Develop Automation Workflows     | Connect security tasks               |
| Generate Security Reports        | Summarize security information       |
| Build Incident-Support Utilities | Help with investigation and response |

---
