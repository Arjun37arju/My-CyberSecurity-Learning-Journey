# Understand Log Processing Automation

## Table of Contents

1. [Log Collection](#1-log-collection)
2. [Log Parsing](#2-log-parsing)
3. [Event Extraction](#3-event-extraction)
4. [Event Correlation](#4-event-correlation)
5. [Automated Reporting](#5-automated-reporting)

---

## 1. Log Collection

**Log collection** means gathering log information from different sources so it can be analyzed.

Logs can come from:

* Operating systems
* Applications
* Web servers
* Network devices
* Security tools

Example Linux command:

```bash
journalctl
```

It can be used to view system logs.

### Why collect logs?

* Investigate what happened
* Detect suspicious activity
* Find failed login attempts
* Troubleshoot problems
* Create security reports

> **Log collection = gathering logs from different sources for further analysis.**

---

## 2. Log Parsing

**Log parsing** means breaking raw log data into useful information.

Example:

```text
2026-09-16 10:20:15 Failed login from 192.168.1.10 user arjun
```

The information can be separated into:

```text
Date   → 2026-09-16
Time   → 10:20:15
Event  → Failed login
IP     → 192.168.1.10
User   → arjun
```

### Why parse logs?

Parsing makes raw log data easier for a program to understand and analyze.

> **Log parsing = converting raw log text into useful information.**

---

## 3. Event Extraction

**Event extraction** means finding important events from logs.

Example:

```text
User arjun logged in
Failed login for user arjun
File report.txt was modified
Server started
```

A security program may extract:

```text
Failed login
File modified
```

Common events to look for:

```text
Failed login
Unauthorized
Permission denied
File modified
Connection refused
```

Example:

```python
log = "Failed login for user arjun"

if "Failed login" in log:
    print("Security event detected")
```

> **Event extraction = identifying important events from logs.**

---

## 4. Event Correlation

**Event correlation** means connecting multiple related events to understand a larger activity or pattern.

Example:

```text
10:01 → Failed login from 192.168.1.10
10:02 → Failed login from 192.168.1.10
10:03 → Failed login from 192.168.1.10
10:04 → Successful login from 192.168.1.10
```

These events are related because they involve the same IP address and occur close together.

```text
Failed login
      ↓
Failed login
      ↓
Failed login
      ↓
Successful login
      ↓
Related activity
```

### Why is correlation useful?

* Connect events from the same user or IP
* Identify patterns
* Understand the sequence of activity
* Help detect potentially suspicious activity

### Difference

```text
Event Extraction
→ Find important events

Event Correlation
→ Connect related events
```

> **Event correlation = connecting related events to understand a larger activity or pattern.**

---

## 5. Automated Reporting

**Automated reporting** means using a program to automatically create a summary of important information found in logs.

### Reporting Flow

```text
Collect Logs
     ↓
Parse Logs
     ↓
Extract Events
     ↓
Correlate Events
     ↓
Generate Report
```

### Example

The program can automatically calculate:

```text
Failed logins: 15
Error events: 3
```

and generate a report.

### Python Automated Log Report

```python
def generate_report(logs):
    total_logs = len(logs)
    failed_logins = [line for line in logs if "Failed password" in line]
    errors = [line for line in logs if "ERROR" in line]

    report = f"""
    === Automated Log Report ===
    Total log entries: {total_logs}
    Failed login attempts: {len(failed_logins)}
    Error events: {len(errors)}
    """
    return report


# Example usage
logs = [
    "Sep 16 10:20:31 server1 sshd[1234]: Failed password for root from 192.168.1.10",
    "Sep 16 10:21:02 server1 app[5678]: ERROR: Database connection failed",
    "Sep 16 10:22:15 server1 sshd[1234]: Failed password for admin from 192.168.1.30"
]

print(generate_report(logs))
```

### Expected Output

```text
=== Automated Log Report ===
Total log entries: 3
Failed login attempts: 2
Error events: 1
```

### Why automate reporting?

* Saves time
* Reduces manual work
* Creates consistent reports
* Makes important events easier to understand
* Can generate reports regularly

> **Automated reporting = automatically generating a useful summary from processed log data.**

---

## Conclusion

Log Processing Automation helps process large amounts of log data automatically.

```text
Log Collection
      ↓
Log Parsing
      ↓
Event Extraction
      ↓
Event Correlation
      ↓
Automated Reporting
```

These steps help security teams collect, understand, identify, connect, and report important log events.
