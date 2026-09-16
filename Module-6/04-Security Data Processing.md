# Security Data Processing

## Table of Contents

1. [Structured Data](#1-structured-data)
2. [CSV Analysis](#2-csv-analysis)
3. [JSON Analysis](#3-json-analysis)
4. [Event Categorization](#4-event-categorization)
5. [Alert Generation](#5-alert-generation)
6. [Combined Security Data Processing Program](#6-combined-security-data-processing-program)

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

Simple example:

```python
failed_logins = 5

if failed_logins >= 3:
    print("ALERT: Multiple failed login attempts detected!")
```

Output:

```text
ALERT: Multiple failed login attempts detected!
```

Alerts can help security systems identify events that require attention.

---

## 6. Combined Security Data Processing Program

This program combines **Event Categorization** and **Alert Generation**.

```python
def categorize_event(event):
    if "Failed login" in event or "Successful login" in event:
        return "Authentication"

    elif "port scan" in event or "connection" in event:
        return "Network"

    elif "ERROR" in event or "crash" in event:
        return "System"

    elif "malware" in event or "virus" in event:
        return "Threat"

    else:
        return "Other"


def generate_alert(event, category):
    if "Failed login" in event:
        return "ALERT: Failed login detected"

    if category == "Threat":
        return "ALERT: Possible security threat detected"

    if category == "System":
        return "ALERT: System error detected"

    return "No alert"


logs = [
    "Failed login from 192.168.1.10",
    "Firewall detected port scan from 192.168.1.20",
    "ERROR: Database connection failed",
    "Antivirus detected malware in file.exe",
    "User arjun logged in successfully"
]


for log in logs:
    category = categorize_event(log)
    alert = generate_alert(log, category)

    print(f"Event    : {log}")
    print(f"Category : {category}")
    print(f"Alert    : {alert}")
    print("-----------------------------")
```

### Program Flow

```text
Log
 ↓
Categorize Event
 ↓
Check Security Condition
 ↓
Generate Alert
 ↓
Display Result
```

### Example Output

```text
Event    : Failed login from 192.168.1.10
Category : Authentication
Alert    : ALERT: Failed login detected
-----------------------------

Event    : Firewall detected port scan from 192.168.1.20
Category : Network
Alert    : No alert
-----------------------------

Event    : ERROR: Database connection failed
Category : System
Alert    : ALERT: System error detected
-----------------------------

Event    : Antivirus detected malware in file.exe
Category : Threat
Alert    : ALERT: Possible security threat detected
-----------------------------
```

---

## Conclusion

Security Data Processing helps security automation systems **organize, analyze, categorize, and respond to security data**.

The overall process is:

```text
Structured Data
      ↓
CSV / JSON Analysis
      ↓
Event Categorization
      ↓
Alert Generation
```

This provides a foundation for building automated security monitoring and analysis tools.
