# Build Security-Focused Python Utilities

## Table of Contents

* [1. File Security Utility](#1-file-security-utility)
* [2. Security Log Analyzer](#2-security-log-analyzer)
* [3. JSON Security Dataset Parser](#3-json-security-dataset-parser)
* [4. Reusable Security Functions](#4-reusable-security-functions)
* [5. Automated Security Workflow](#5-automated-security-workflow)


---

## 1. File Security Utility

This utility checks whether a file exists, gets its size, and calculates its SHA-256 hash.

```python
import os
import hashlib

filename = input("Enter file path: ")

if os.path.isfile(filename):

    size = os.path.getsize(filename)

    with open(filename, "rb") as file:
        data = file.read()

    sha256 = hashlib.sha256(data).hexdigest()

    print("\nFile exists")
    print("Size:", size, "bytes")
    print("SHA-256:", sha256)

else:
    print("File not found")
```

---

## 2. Security Log Analyzer

This utility reads a log file and identifies lines containing failed authentication or suspicious login activity.

```python
log_file = input("Enter log file path: ")

failed = 0

try:
    with open(log_file, "r", errors="ignore") as file:

        for line in file:
            if "failed" in line.lower() or "authentication failure" in line.lower():
                print(line.strip())
                failed += 1

    print("\nTotal suspicious lines:", failed)

except FileNotFoundError:
    print("Log file not found")
```

---

## 3. JSON Security Dataset Parser

This utility loads a JSON dataset and displays each record.

### Example `users.json`

```json
[
    {
        "username": "arjun",
        "role": "user"
    },
    {
        "username": "admin",
        "role": "administrator"
    }
]
```

### Python Code

```python
import json

filename = input("Enter JSON file: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("\nJSON data:")

    for item in data:
        print(item)

except FileNotFoundError:
    print("File not found")

except json.JSONDecodeError:
    print("Invalid JSON file")
```

---

## 4. Reusable Security Functions

This utility uses functions to make security-related operations reusable.

```python
import hashlib
import os

def check_file(filename):
    return os.path.isfile(filename)


def get_file_size(filename):
    return os.path.getsize(filename)


def calculate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()

    return hashlib.sha256(data).hexdigest()


filename = input("Enter file path: ")

if check_file(filename):

    print("File exists")
    print("Size:", get_file_size(filename), "bytes")
    print("SHA-256:", calculate_hash(filename))

else:
    print("File not found")
```

---

## 5. Automated Security Workflow

This utility combines file checking, file size calculation, SHA-256 hashing, and automated report generation.

```python
import os
import hashlib
from datetime import datetime

filename = input("Enter file path: ")

if not os.path.isfile(filename):
    print("File not found")
    exit()

size = os.path.getsize(filename)

with open(filename, "rb") as file:
    data = file.read()

sha256 = hashlib.sha256(data).hexdigest()

report = f"""
SECURITY FILE REPORT
--------------------
File: {filename}
Size: {size} bytes
SHA-256: {sha256}
Checked: {datetime.now()}
"""

print(report)

with open("security_report.txt", "w") as file:
    file.write(report)

print("Report saved as security_report.txt")
```

---

## Overall Workflow

```text
Python
   │
   ├── os
   │     └── Files and directories
   │
   ├── hashlib
   │     └── SHA-256 file hashing
   │
   ├── json
   │     └── Security datasets
   │
   ├── Functions
   │     └── Reusable security code
   │
   └── Automation
         └── Security reports and workflows
```
