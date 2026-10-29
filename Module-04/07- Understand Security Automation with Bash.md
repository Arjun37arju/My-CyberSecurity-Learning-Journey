#  Understand Security Automation with Bash

## Table of Contents

* [Introduction](#introduction)
* [a. Log Parsing](#a-log-parsing)
* [b. User Auditing](#b-user-auditing)
* [c. System Monitoring](#c-system-monitoring)
* [d. Automated Reporting](#d-automated-reporting)
* [e. Security Administration Tasks](#e-security-administration-tasks)
* [Practical Security Automation Script](#practical-security-automation-script)


---

## Introduction

**Security automation with Bash** means using Bash scripts to automatically perform repetitive security-related tasks on a Linux system.

Instead of manually checking logs, users, processes, disk usage, and system activity, we can write scripts that collect information and identify suspicious activity.

### Why Bash for Security Automation?

Bash is useful because it can interact directly with Linux commands and system files.

Common commands used in security automation:

```bash
grep
awk
sed
cut
sort
uniq
find
ps
ss
df
du
who
last
id
systemctl
journalctl
```

A basic automation flow is:

```text
System Data
     ↓
Bash Script
     ↓
Collect Information
     ↓
Analyze / Filter
     ↓
Detect Security Indicators
     ↓
Generate Report
     ↓
Administrator Action
```

---

# a. Log Parsing

## What is Log Parsing?

**Log parsing** is the process of reading system logs and extracting useful security information.

Linux systems generate logs for:

* User authentication
* SSH connections
* System services
* Kernel events
* Applications
* Security events

Common locations include:

```text
/var/log/
```

For example:

```bash
ls /var/log/
```

You may see files such as:

```text
auth.log
syslog
kern.log
apache2/
```

> The exact log files depend on the Linux distribution and logging configuration.

---

## Searching Logs with `grep`

`grep` is one of the most important tools for security log analysis.

Example:

```bash
grep "Failed password" /var/log/auth.log
```

This searches for failed SSH/password authentication attempts.

Count failed attempts:

```bash
grep -c "Failed password" /var/log/auth.log
```

Find successful logins:

```bash
grep "Accepted password" /var/log/auth.log
```

---

## Extracting IP Addresses

Suppose a log contains:

```text
Failed password for root from 192.168.1.50 port 42123 ssh2
```

We can extract the IP using tools such as `awk`.

Example:

```bash
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}'
```

A more robust approach depends on the exact log format, so always verify the fields before automating extraction.

---

## Finding Repeated Attack Sources

```bash
grep "Failed password" /var/log/auth.log |
awk '{print $(NF-3)}' |
sort |
uniq -c |
sort -nr
```

This helps identify IP addresses generating many failed authentication attempts.

Example output:

```text
25 192.168.1.50
12 192.168.1.20
 4 192.168.1.15
```

This could indicate:

```text
Repeated authentication failures
          ↓
Possible brute-force activity
          ↓
Investigate source IP
```

---

## Important Security Indicators in Logs

Look for:

* Multiple failed logins
* Successful login after many failures
* Login from unusual accounts
* Login at unusual times
* Repeated SSH connection attempts
* Account creation
* Privilege changes
* Service failures
* Unexpected commands
* Changes to security configuration

---

# b. User Auditing

## What is User Auditing?

**User auditing** means checking accounts, groups, privileges, login activity, and authentication information on a Linux system.

This helps identify:

* Unauthorized accounts
* Suspicious users
* Excessive privileges
* Inactive accounts
* Unexpected administrative access

---

## List Users

Linux user information is stored in:

```text
/etc/passwd
```

View users:

```bash
cat /etc/passwd
```

A cleaner approach:

```bash
cut -d: -f1 /etc/passwd
```

---

## Check a Specific User

```bash
id username
```

Example:

```bash
id arjun
```

Output may contain:

```text
uid=1000(arjun) gid=1000(arjun) groups=1000(arjun),27(sudo)
```

This tells you the user's UID, primary group, and supplementary groups.

---

## Check Logged-In Users

```bash
who
```

More detailed:

```bash
w
```

These can help identify unexpected active sessions.

---

## Check Login History

```bash
last
```

This provides historical login information.

For failed login attempts, depending on the system:

```bash
lastb
```

may be available and require administrative privileges.

---

## Check Privileged Users

On many Linux systems, members of the `sudo` group can perform administrative actions.

```bash
getent group sudo
```

On systems using different privilege-management groups, the relevant group may differ.

---

## Security Questions During User Auditing

Ask:

```text
Who are the users?
        ↓
Who is currently logged in?
        ↓
Who has administrative privileges?
        ↓
Are there unexpected accounts?
        ↓
Are there suspicious login attempts?
```

---

# c. System Monitoring

## What is System Monitoring?

**System monitoring** means continuously checking system resources, processes, network connections, and services.

Security monitoring can detect:

* Suspicious processes
* Resource exhaustion
* Unexpected network connections
* Failed services
* Disk-space problems
* Possible denial-of-service conditions

---

## Monitor Processes

```bash
ps aux
```

For an interactive view:

```bash
top
```

If installed:

```bash
htop
```

Look for:

* Unknown processes
* Processes running as root unexpectedly
* High CPU usage
* High memory usage
* Suspicious command lines

---

## Monitor Network Connections

```bash
ss -tuln
```

This displays listening TCP/UDP sockets.

For more information:

```bash
ss -tunap
```

This can help identify:

```text
Process
   ↓
Network connection
   ↓
Local port
   ↓
Remote IP
```

---

## Monitor Disk Usage

```bash
df -h
```

Find large directories:

```bash
du -sh /*
```

High disk usage may affect system availability and can sometimes indicate:

* Large log generation
* Unwanted files
* Application problems
* Possible compromise

---

## Monitor Services

List services:

```bash
systemctl --type=service
```

Check a specific service:

```bash
systemctl status ssh
```

Find failed services:

```bash
systemctl --failed
```

---

## Automated Monitoring Example

```bash
#!/bin/bash

echo "===== SYSTEM MONITORING ====="

echo
echo "CPU / Processes:"
ps aux --sort=-%cpu | head

echo
echo "Memory:"
free -h

echo
echo "Disk:"
df -h

echo
echo "Listening Ports:"
ss -tuln

echo
echo "Failed Services:"
systemctl --failed
```

---

# d. Automated Reporting

## What is Automated Reporting?

**Automated reporting** means collecting security information automatically and presenting it in a readable report.

Instead of running:

```bash
who
df -h
ss -tuln
grep ...
```

manually every day, a Bash script can collect everything automatically.

---

## Basic Report Structure

A security report can contain:

```text
========================
SECURITY REPORT
========================

System Information

User Information

Failed Login Attempts

Active Users

Running Processes

Network Connections

Disk Usage

Failed Services

========================
END OF REPORT
========================
```

---

## Creating a Report File

```bash
#!/bin/bash

REPORT="security_report.txt"

echo "===== SECURITY REPORT =====" > "$REPORT"

echo >> "$REPORT"
echo "===== SYSTEM =====" >> "$REPORT"
hostname >> "$REPORT"
date >> "$REPORT"

echo >> "$REPORT"
echo "===== USERS =====" >> "$REPORT"
who >> "$REPORT"

echo >> "$REPORT"
echo "===== DISK =====" >> "$REPORT"
df -h >> "$REPORT"

echo >> "$REPORT"
echo "===== NETWORK =====" >> "$REPORT"
ss -tuln >> "$REPORT"

echo >> "$REPORT"
echo "===== FAILED SERVICES =====" >> "$REPORT"
systemctl --failed >> "$REPORT"

echo "Report created: $REPORT"
```

---

## Why Reporting Matters

Automated reports provide:

* Consistent security checks
* Historical records
* Faster investigation
* Easier incident detection
* Evidence for administrators
* Reduced manual work

Reports can also be scheduled using **cron**.

Example:

```bash
crontab -e
```

A daily script could be scheduled with an appropriate cron entry, for example:

```text
0 9 * * * /home/user/security_report.sh
```

This means the script runs every day at approximately **09:00** according to the system's local time.

---

# e. Security Administration Tasks

Bash can automate many routine Linux security administration tasks.

## 1. Check File Permissions

```bash
ls -l
```

Find world-writable files:

```bash
find / -type f -perm -0002 2>/dev/null
```

World-writable files can sometimes create security risks, so they should be reviewed rather than automatically changed.

---

## 2. Find SUID Files

SUID programs execute with the permissions of their file owner.

Find SUID files:

```bash
find / -perm -4000 -type f 2>/dev/null
```

These should be reviewed because unexpected or vulnerable SUID binaries can create privilege-escalation opportunities.

---

## 3. Check SSH Configuration

Common SSH configuration:

```bash
/etc/ssh/sshd_config
```

View relevant settings:

```bash
grep -E "^(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication)" /etc/ssh/sshd_config
```

The exact configuration and security recommendations depend on the environment.

---

## 4. Check Firewall Status

For systems using UFW:

```bash
sudo ufw status
```

For systems using another firewall framework, use the appropriate administration command.

---

## 5. Check System Updates

On Debian/Ubuntu-based systems:

```bash
sudo apt update
```

To see available upgrades:

```bash
apt list --upgradable
```

Keeping software updated helps reduce exposure to known vulnerabilities.

---

## 6. Check Failed Services

```bash
systemctl --failed
```

Detailed service status:

```bash
systemctl status service_name
```

---

## 7. Automate Account Checks

Example:

```bash
#!/bin/bash

echo "===== USER AUDIT ====="

echo
echo "Users:"
cut -d: -f1 /etc/passwd

echo
echo "Logged-in users:"
who

echo
echo "Sudo group:"
getent group sudo
```

---

# Practical Security Automation Script

Here is a small beginner-friendly Bash script combining the concepts:

```bash
#!/bin/bash

REPORT="security_report.txt"

echo "==================================" > "$REPORT"
echo "       LINUX SECURITY REPORT      " >> "$REPORT"
echo "==================================" >> "$REPORT"

echo >> "$REPORT"
echo "[1] SYSTEM INFORMATION" >> "$REPORT"
echo "Hostname: $(hostname)" >> "$REPORT"
echo "Date: $(date)" >> "$REPORT"

echo >> "$REPORT"
echo "[2] LOGGED-IN USERS" >> "$REPORT"
who >> "$REPORT"

echo >> "$REPORT"
echo "[3] FAILED LOGIN ATTEMPTS" >> "$REPORT"
if [ -f /var/log/auth.log ]; then
    grep "Failed password" /var/log/auth.log | tail -20 >> "$REPORT"
else
    echo "auth.log not found; check journalctl or distro-specific logs." >> "$REPORT"
fi

echo >> "$REPORT"
echo "[4] DISK USAGE" >> "$REPORT"
df -h >> "$REPORT"

echo >> "$REPORT"
echo "[5] LISTENING PORTS" >> "$REPORT"
ss -tuln >> "$REPORT"

echo >> "$REPORT"
echo "[6] TOP CPU PROCESSES" >> "$REPORT"
ps aux --sort=-%cpu | head -10 >> "$REPORT"

echo >> "$REPORT"
echo "[7] FAILED SERVICES" >> "$REPORT"
systemctl --failed >> "$REPORT"

echo >> "$REPORT"
echo "==================================" >> "$REPORT"
echo "Report completed." >> "$REPORT"

echo "Security report saved to: $REPORT"
```

Run it:

```bash
chmod +x security_report.sh
```

Then:

```bash
./security_report.sh
```

View the report:

```bash
cat security_report.txt
```

---

# Security Automation Workflow

```text
             Linux System
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
      Logs      Users      System
       │          │          │
       ↓          ↓          ↓
    Parsing    Auditing   Monitoring
       │          │          │
       └──────────┼──────────┘
                  ↓
             Bash Script
                  ↓
          Security Analysis
                  ↓
             Report
                  ↓
          Administrator
                  ↓
        Investigation / Action
```

---

# Important Bash Tools for Security

| Tool         | Security Use               |
| ------------ | -------------------------- |
| `grep`       | Search logs                |
| `awk`        | Extract/transform fields   |
| `sed`        | Modify/filter text         |
| `cut`        | Extract columns            |
| `sort`       | Sort results               |
| `uniq`       | Find/count repeated values |
| `find`       | Search files               |
| `ps`         | Process monitoring         |
| `ss`         | Network/socket monitoring  |
| `df`         | Disk monitoring            |
| `du`         | File/directory size        |
| `who`        | Current users              |
| `last`       | Login history              |
| `id`         | User/group information     |
| `systemctl`  | Service management         |
| `journalctl` | Systemd journal analysis   |
| `cron`       | Schedule automation        |

---

# Key Things to Remember

### Log Parsing

```text
Collect logs → Search → Filter → Extract → Analyze
```

### User Auditing

```text
Users → Groups → Privileges → Login activity
```

### System Monitoring

```text
Processes → Memory → Disk → Network → Services
```

### Automated Reporting

```text
Collect → Analyze → Save → Schedule
```

### Security Administration

```text
Permissions → Accounts → Services → Firewall → Updates
```

