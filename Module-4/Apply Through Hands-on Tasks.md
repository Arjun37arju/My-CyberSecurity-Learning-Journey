# Apply Through Hands-on Tasks

Hands-on tasks help you **apply Linux administration and security concepts in practical environments**. Instead of only learning commands and theory, you perform real administrative tasks, analyze logs, write scripts, automate repetitive work, and build basic security monitoring solutions.

---

## a. Administer Linux Systems

### Content

Linux system administration involves managing users, files, permissions, processes, services, storage, and system configuration.

You should practice:

* Creating and managing users
* Creating and managing groups
* Managing file and directory permissions
* Changing file ownership
* Managing processes
* Managing system services
* Checking disk usage
* Monitoring system resources
* Installing and removing packages
* Managing system configuration

### Practical Task

Create a small Linux administration environment and perform basic administrative operations.

For example:

```bash
# Create a user
sudo useradd analyst

# Create a group
sudo groupadd security

# Add user to group
sudo usermod -aG security analyst

# Create a directory
sudo mkdir /security-data

# Change ownership
sudo chown analyst:security /security-data

# Set permissions
sudo chmod 750 /security-data

# Check running processes
ps aux

# Check services
systemctl --type=service
```

Verify that the user, group, permissions, and services are configured correctly.

### Deliverable

Create an **Linux Administration Record**:

| Task                     | Command Used | Result | Observation |
| ------------------------ | ------------ | ------ | ----------- |
| User creation            |              |        |             |
| Group creation           |              |        |             |
| Permission configuration |              |        |             |
| Process monitoring       |              |        |             |
| Service management       |              |        |             |

**Goal:**

> Gain practical experience managing Linux systems, users, permissions, processes, and services.

---

## b. Analyze Security Logs

### Content

Security log analysis involves examining system and authentication logs to identify normal activity, errors, and potential security incidents.

You should practice analyzing:

* Authentication logs
* Login attempts
* Failed login attempts
* Successful logins
* `sudo` activity
* Service logs
* System events
* SSH activity
* Suspicious or repeated events

Common Linux log locations include:

```text
/var/log/auth.log
/var/log/syslog
/var/log/messages
/var/log/secure
```

The exact files available depend on the Linux distribution and logging configuration.

### Practical Task

Analyze a Linux authentication or system log.

Use commands such as:

```bash
cat /var/log/auth.log
```

```bash
grep "Failed" /var/log/auth.log
```

```bash
grep "Accepted" /var/log/auth.log
```

```bash
journalctl
```

Identify:

1. Successful authentication attempts
2. Failed authentication attempts
3. User accounts involved
4. Source IP addresses, where available
5. Repeated failures
6. Unusual activity
7. Relevant timestamps

### Deliverable

Create a **Security Log Analysis Report**:

```text
Log File:

Date / Time:

User:

Source IP:

Event:

Event Type:

Evidence:

Analysis:

Security Concern:

Recommended Action:

Final Conclusion:
```

You can also maintain a table:

| Time | User | Source IP | Event | Status | Observation |
| ---- | ---- | --------- | ----- | ------ | ----------- |
|      |      |           |       |        |             |
|      |      |           |       |        |             |
|      |      |           |       |        |             |

**Goal:**

> Develop the ability to analyze Linux security logs and identify authentication events and potentially suspicious activity.

---

## c. Build Shell Scripts

### Content

Shell scripting allows you to automate Linux operations by combining commands into reusable programs.

You should practice:

* Variables
* User input
* Conditional statements
* Loops
* Functions
* Command execution
* Exit status
* File handling
* Command-line arguments
* Basic error handling

### Practical Task

Create a simple Bash script that performs a useful administrative or security task.

For example, create a script that checks whether important system commands are available:

```bash
#!/bin/bash

commands=("grep" "awk" "sed" "curl" "ss")

for command in "${commands[@]}"
do
    if command -v "$command" >/dev/null 2>&1
    then
        echo "$command: Available"
    else
        echo "$command: Not Available"
    fi
done
```

Save the script:

```bash
nano check_commands.sh
```

Give it execute permission:

```bash
chmod +x check_commands.sh
```

Run it:

```bash
./check_commands.sh
```

### Practical Exercises

Build scripts for:

1. Checking disk usage
2. Checking memory usage
3. Listing logged-in users
4. Checking running processes
5. Checking active network connections
6. Searching logs for failed authentication attempts

### Deliverable

Maintain a **Shell Script Collection**:

| Script | Purpose | Commands Used | Result |
| ------ | ------- | ------------- | ------ |
|        |         |               |        |
|        |         |               |        |
|        |         |               |        |

**Goal:**

> Develop practical Bash scripting skills for Linux administration and security-related tasks.

---

## d. Automate Administrative Tasks

### Content

Linux administration often involves repetitive tasks. Automation allows these tasks to be performed consistently and efficiently.

You should practice automating:

* Log collection
* Temporary file cleanup
* Disk usage checks
* System information collection
* User auditing
* Service status checks
* Backup operations
* Report generation

### Practical Task

Create a Bash script that collects basic system information and saves it into a report.

Example:

```bash
#!/bin/bash

REPORT="system_report.txt"

echo "Linux System Report" > "$REPORT"
echo "===================" >> "$REPORT"

echo "Hostname:" >> "$REPORT"
hostname >> "$REPORT"

echo "" >> "$REPORT"

echo "Current User:" >> "$REPORT"
whoami >> "$REPORT"

echo "" >> "$REPORT"

echo "Disk Usage:" >> "$REPORT"
df -h >> "$REPORT"

echo "" >> "$REPORT"

echo "Memory Usage:" >> "$REPORT"
free -h >> "$REPORT"

echo "" >> "$REPORT"

echo "Logged-in Users:" >> "$REPORT"
who >> "$REPORT"

echo "Report saved to $REPORT"
```

Run the script:

```bash
chmod +x system_report.sh
./system_report.sh
```

Check the generated report:

```bash
cat system_report.txt
```

### Practical Exercises

Automate tasks such as:

```text
System information collection
        ↓
Log collection
        ↓
Disk usage check
        ↓
User audit
        ↓
Service status check
        ↓
Generate report
```

### Deliverable

Create an **Automation Task Report**:

| Task               | Script | Frequency | Output |
| ------------------ | ------ | --------- | ------ |
| System information |        |           |        |
| Log collection     |        |           |        |
| User audit         |        |           |        |
| Disk monitoring    |        |           |        |
| Service check      |        |           |        |

**Goal:**

> Learn how to automate repetitive Linux administration tasks and generate consistent results using shell scripts.

---

## e. Create Security Monitoring Scripts

### Content

Security monitoring scripts can continuously or periodically check a Linux system for events that may require investigation.

You should practice monitoring:

* Failed login attempts
* Successful logins
* Logged-in users
* Running processes
* Listening network ports
* Active connections
* Disk usage
* Important system files
* Suspicious log entries

### Practical Task

Create a Bash script that checks for failed SSH authentication attempts.

Example:

```bash
#!/bin/bash

LOG="/var/log/auth.log"

echo "===== Failed Authentication Attempts ====="

if [ -f "$LOG" ]
then
    grep "Failed password" "$LOG"
else
    echo "Authentication log not found."
fi
```

You can extend the script to count failed attempts:

```bash
grep "Failed password" "$LOG" | wc -l
```

You can also check listening network services:

```bash
ss -tuln
```

And monitor disk usage:

```bash
df -h
```

### Practical Monitoring Workflow

```text
Linux System
     │
     ▼
Collect Events
     │
     ├── Authentication Logs
     ├── Processes
     ├── Network Connections
     ├── Disk Usage
     └── User Activity
     │
     ▼
Analyze Events
     │
     ▼
Identify Suspicious Activity
     │
     ▼
Generate Alert / Report
     │
     ▼
Investigate
```

### Deliverable

Create a **Linux Security Monitoring Report**:

```text
Monitoring Period:

System:

Authentication Events:

Failed Login Attempts:

Active Users:

Running Processes:

Listening Ports:

Disk Usage:

Suspicious Activity:

Evidence:

Recommended Action:

Final Conclusion:
```

You can also maintain a monitoring table:

| Check          | Command/Script | Result | Security Observation |
| -------------- | -------------- | ------ | -------------------- |
| Authentication |                |        |                      |
| Users          |                |        |                      |
| Processes      |                |        |                      |
| Network Ports  |                |        |                      |
| Disk Usage     |                |        |                      |

**Goal:**

> Develop practical skills in monitoring Linux systems, identifying security indicators, and creating simple automated security checks.

---

## Conclusion

Hands-on Linux tasks transform theoretical knowledge into **practical system administration and security skills**.

By completing these exercises, you should be able to:

* Administer Linux users, groups, permissions, and services
* Analyze authentication and system logs
* Write Bash scripts
* Automate repetitive administrative tasks
* Monitor Linux systems for security indicators
* Generate useful security reports
* Investigate suspicious system activity

> **Practice → Automate → Monitor → Analyze → Improve**
