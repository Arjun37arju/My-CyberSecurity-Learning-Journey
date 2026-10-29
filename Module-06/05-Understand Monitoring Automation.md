# Understand Monitoring Automation

## Table of Contents

1. [System Monitoring](#1-system-monitoring)
2. [Service Monitoring](#2-service-monitoring)
3. [File Monitoring](#3-file-monitoring)
4. [Change Detection](#4-change-detection)
5. [Alerting Workflows](#5-alerting-workflows)


---

## 1. System Monitoring

System monitoring means continuously checking the health, performance, and activity of a computer or server.

### What We Monitor

* CPU usage
* Memory usage
* Disk usage
* Running processes
* Network activity

### Python Example

The `psutil` library can be used to monitor system information.

```python
import psutil

print("========== SYSTEM MONITORING ==========")

# CPU
cpu = psutil.cpu_percent(interval=1)
print(f"\nCPU Usage: {cpu}%")

if cpu > 80:
    print("ALERT: High CPU usage!")

# Memory
memory = psutil.virtual_memory()
print(f"\nMemory Usage: {memory.percent}%")

if memory.percent > 80:
    print("ALERT: High memory usage!")

# Disk
disk = psutil.disk_usage("/")
print(f"\nDisk Usage: {disk.percent}%")

if disk.percent > 80:
    print("ALERT: High disk usage!")

# Processes
print("\n========== RUNNING PROCESSES ==========")

for process in psutil.process_iter(["pid", "name"]):
    print(process.info)

# Network connections
print("\n========== NETWORK CONNECTIONS ==========")

connections = psutil.net_connections()

for connection in connections:
    print(connection)

print("\n========== MONITORING COMPLETED ==========")
```

Install `psutil` if it is not installed:

```bash
pip install psutil
```

### Monitoring Flow

```text
Collect System Information
          ↓
Check Values
          ↓
Compare With Threshold
          ↓
Detect Abnormal Condition
          ↓
Generate Alert
```

---

## 2. Service Monitoring

Service monitoring means continuously checking whether important system or network services are running and available.

Examples:

* SSH
* Web server
* Database
* DNS
* Firewall

### Checking a Network Service

```python
import socket

host = "localhost"
port = 22

s = socket.socket()
s.settimeout(2)

result = s.connect_ex((host, port))

if result == 0:
    print("SSH service is available")
else:
    print("ALERT: SSH service is unavailable")

s.close()
```

### Monitoring Flow

```text
Check Service
     ↓
Is it available?
   ↙       ↘
 Yes        No
  ↓          ↓
Continue    Alert
```

---

## 3. File Monitoring

File monitoring means continuously checking files and directories to detect changes.

It can detect:

* File creation
* File deletion
* File modification
* Changes to important files

### File Modification Monitoring

```python
import os
import time

file = "config.txt"

old_time = os.path.getmtime(file)

while True:
    new_time = os.path.getmtime(file)

    if new_time != old_time:
        print("ALERT: File has been modified!")
        old_time = new_time

    time.sleep(2)
```

### How It Works

1. Get the file's original modification time.
2. Check the modification time again.
3. Compare the two values.
4. If they are different, the file was modified.
5. Generate an alert.
6. Wait two seconds and check again.

### Monitoring Flow

```text
Select File
    ↓
Check File
    ↓
Compare Current State
    ↓
Change Detected?
   ↙        ↘
 No         Yes
 ↓           ↓
Continue    Alert
```

---

## 4. Change Detection

Change detection means comparing the previous state of something with its current state to identify changes.

Changes can include:

* File modification
* File creation
* File deletion
* Configuration changes
* User changes
* Permission changes

### Hash-Based Change Detection

A hash can be used to check whether the contents of a file have changed.

```python
import hashlib

def get_hash(file):
    with open(file, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

old_hash = get_hash("config.txt")

print("Original hash:", old_hash)

new_hash = get_hash("config.txt")

if new_hash != old_hash:
    print("ALERT: File has been changed!")
else:
    print("No change detected")
```

### Hash Comparison

```text
Original File
      ↓
   SHA-256
      ↓
Original Hash
      ↓
     Compare
      ↑
Current Hash
      ↑
   SHA-256
      ↑
Modified File
```

If:

```text
Original Hash == Current Hash
        ↓
    No change
```

If:

```text
Original Hash != Current Hash
        ↓
   Change detected
        ↓
       Alert
```

### Change Detection Flow

```text
Collect Original State
        ↓
Collect Current State
        ↓
Compare
        ↓
Change Detected?
    ↙        ↘
  No          Yes
  ↓            ↓
Continue      Alert
```

---

## 5. Alerting Workflows

Alerting workflow is the process of detecting an important event, generating an alert, and following a defined process for investigation and response.

### Basic Workflow

```text
Monitor
   ↓
Detect Event
   ↓
Check Condition
   ↓
Generate Alert
   ↓
Investigate
   ↓
Respond
```

### Example

Suppose five failed login attempts are detected.

```python
failed_logins = 5

if failed_logins >= 5:
    print("CRITICAL ALERT: Possible brute-force activity")
elif failed_logins >= 3:
    print("WARNING: Multiple failed logins")
else:
    print("No alert")
```

Output:

```text
CRITICAL ALERT: Possible brute-force activity
```

### Alert Severity

Alerts can have different severity levels:

| Severity | Meaning                  |
| -------- | ------------------------ |
| Low      | Minor event              |
| Medium   | Needs attention          |
| High     | Important security event |
| Critical | Immediate attention      |

### Security Example

```text
5 Failed Login Attempts
          ↓
Threshold = 3
          ↓
Condition Matched
          ↓
🚨 Alert Generated
          ↓
Investigation
          ↓
Response
```

---

## Conclusion

Monitoring Automation helps continuously monitor systems, services, files, and changes and generate alerts when important conditions are detected.

### Overall Monitoring Automation Flow

```text
System Monitoring
       ↓
Service Monitoring
       ↓
File Monitoring
       ↓
Change Detection
       ↓
Alerting Workflow
```

### Key Idea

> **Monitoring automation = continuously checking systems and automatically detecting and alerting on important changes or abnormal activity.**
