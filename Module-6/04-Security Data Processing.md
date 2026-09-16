# Security Data Processing

## Table of Contents

1. [Structured Data](#1-structured-data)
2. [CSV Analysis](#2-csv-analysis)
3. [JSON Analysis](#3-json-analysis)
4. [Event Categorization](#4-event-categorization)
5. [Alert Generation](#5-alert-generation)

---

## 1. Structured Data

Structured data is data organized in a fixed and predictable format.

Examples:

* CSV
* JSON
* Database tables

In security, structured data makes it easier to search, filter, analyze, and process security events.

---

## 2. CSV Analysis

CSV stands for **Comma-Separated Values**.

It stores data in rows and columns.

Example:

```csv
Time,User,IP,Event
10:20,arjun,192.168.1.10,Failed login
10:25,priya,192.168.1.15,Login success
```

Python provides the `csv` module for working with CSV files.

```python
import csv

with open("logs.csv", "r") as file:
    logs = csv.DictReader(file)

    for row in logs:
        if row["Event"] == "Failed login":
            print(row)
```

`DictReader()` allows us to access columns using their names.

---

## 3. JSON Analysis

JSON stands for **JavaScript Object Notation**.

It stores data using key-value pairs.

Example:

```json
{
    "user": "arjun",
    "ip": "192.168.1.10",
    "event": "Failed login"
}
```

Python uses the `json` module to work with JSON data.

```python
import json

data = '{"user": "arjun", "event": "Failed login"}'

logs = json.loads(data)

print(logs["user"])
print(logs["event"])
```

JSON is commonly used when security tools exchange structured information.

---

## 4. Event Categorization

Event categorization means **grouping security events into meaningful categories**.

Example:

| Event                      | Category          |
| -------------------------- | ----------------- |
| Failed login               | Authentication    |
| Unauthorized access        | Access Violation  |
| Database connection failed | System Error      |
| Suspicious executable      | Malware           |
| High CPU usage             | System Monitoring |

Simple Python example:

```python
event = "Failed login attempt"

if "Failed login" in event:
    category = "Authentication"
elif "Unauthorized" in event:
    category = "Access Violation"
elif "ERROR" in event:
    category = "System Error"
else:
    category = "Other"

print(category)
```

Output:

```text
Authentication
```

Categorization makes large amounts of security data easier to analyze.

---

## 5. Alert Generation

Alert generation means **automatically creating a warning when a security condition is detected**.

Example:

```python
failed_logins = 5

if failed_logins >= 3:
    print("ALERT: Multiple failed login attempts detected!")
```

Output:

```text
ALERT: Multiple failed login attempts detected!
```

A basic security automation flow is:

```text
Log Data
    ↓
Analyze
    ↓
Categorize Event
    ↓
Check Condition
    ↓
Generate Alert
```

For example, if five failed login attempts are detected and the threshold is three, the system can generate an alert.

---

## Conclusion

Security Data Processing helps security automation systems organize, analyze, categorize, and respond to security data.

The basic process is:

```text
Structured Data
      ↓
CSV / JSON Analysis
      ↓
Event Categorization
      ↓
Alert Generation
```

This format will let you click the **Table of Contents** items in GitHub to jump directly to each topic.
