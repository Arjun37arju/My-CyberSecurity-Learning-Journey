# Apply Through Hands-on Tasks


## Table of Contents

* [a. Administer Linux Systems](#a-administer-linux-systems)
* [b. Analyze Security Logs](#b-analyze-security-logs)
* [c. Build Shell Scripts](#c-build-shell-scripts)
* [d. Automate Administrative Tasks](#d-automate-administrative-tasks)
* [e. Create Security Monitoring Scripts](#e-create-security-monitoring-scripts)
* [Hands-on Mini Project](#-hands-on-mini-project)
* [Skills You Should Gain](#-skills-you-should-gain)
* [Overall Workflow](#-overall-workflow)
* [Conclusion](#-conclusion)


This section focuses on **practical Linux administration and cybersecurity tasks**. The goal is to take the commands and concepts learned earlier and apply them in a real Linux lab environment.

> **Practice these tasks only on your own Linux machine or an authorized lab/VM.**

---

## a. Administer Linux Systems

Linux administration involves managing **users, groups, files, permissions, processes, services, storage, and system resources**.

### 1. Check the current user

Check the currently logged-in user:

```bash
whoami
```

Display detailed user and group information:

```bash
id
```

These commands help identify the current username, UID, GID, groups, and privileges.

---

### 2. Create a user

Create a new user with a home directory:

```bash
sudo useradd -m securityuser
```

Set a password:

```bash
sudo passwd securityuser
```

Verify the account:

```bash
id securityuser
```

Check the user's home directory:

```bash
ls -la /home/securityuser
```

---

### 3. Create and manage groups

Create a security-related group:

```bash
sudo groupadd security
```

Add the user to the group:

```bash
sudo usermod -aG security securityuser
```

Verify group membership:

```bash
groups securityuser
```

You can also check:

```bash
id securityuser
```

---

### 4. Manage file permissions

Create a test file:

```bash
touch security.txt
```

Check its permissions:

```bash
ls -l security.txt
```

Change the permissions:

```bash
chmod 600 security.txt
```

Check again:

```bash
ls -l security.txt
```

`600` means:

```text
Owner  → read + write
Group  → no permission
Others → no permission
```

Try another permission:

```bash
chmod 640 security.txt
```

This means:

```text
Owner  → read + write
Group  → read
Others → no permission
```

---

### 5. Manage file ownership

Change the owner:

```bash
sudo chown securityuser security.txt
```

Change both owner and group:

```bash
sudo chown securityuser:security security.txt
```

Verify:

```bash
ls -l security.txt
```

---

### 6. Manage Linux services

Check a service:

```bash
systemctl status ssh
```

Start a service:

```bash
sudo systemctl start ssh
```

Stop a service:

```bash
sudo systemctl stop ssh
```

Restart a service:

```bash
sudo systemctl restart ssh
```

Enable a service at boot:

```bash
sudo systemctl enable ssh
```

Check whether it is enabled:

```bash
systemctl is-enabled ssh
```

> The exact service name can differ between distributions. For example, some systems may use `sshd` instead of `ssh`.

---

### 7. Monitor processes

Display running processes:

```bash
ps aux
```

Search for a specific process:

```bash
ps aux | grep firefox
```

Monitor processes interactively:

```bash
top
```

You can also use:

```bash
htop
```

if it is installed.

---

### 8. Check memory usage

Display memory usage:

```bash
free -h
```

This shows:

```text
Total memory
Used memory
Free memory
Available memory
Swap usage
```

---

### 9. Check disk usage

Check filesystem usage:

```bash
df -h
```

Check the size of a directory:

```bash
du -sh /home
```

Find large directories:

```bash
du -h /home | sort -h | tail
```

---

### 10. Check network configuration

Display IP addresses:

```bash
ip addr
```

Display routing information:

```bash
ip route
```

Check network connectivity:

```bash
ping -c 4 8.8.8.8
```

Check listening ports:

```bash
ss -tuln
```

---

## b. Analyze Security Logs

Security logs provide information about **authentication, user activity, services, errors, and system events**.

Common log locations include:

```text
/var/log/
/var/log/auth.log
/var/log/syslog
/var/log/secure
```

The exact files depend on the Linux distribution and logging configuration.

Systems using `systemd` also provide logs through:

```bash
journalctl
```

---

### 1. View authentication logs

On Debian/Ubuntu/Kali systems, for example:

```bash
sudo cat /var/log/auth.log
```

Search for failed authentication:

```bash
sudo grep -i "failed" /var/log/auth.log
```

Search for successful SSH authentication:

```bash
sudo grep -i "accepted" /var/log/auth.log
```

---

### 2. Count failed authentication attempts

```bash
sudo grep -i "failed" /var/log/auth.log | wc -l
```

This counts the number of matching log lines.

---

### 3. Find failed SSH attempts

```bash
sudo grep "Failed password" /var/log/auth.log
```

Look for information such as:

```text
Username
Source IP address
Date/time
Authentication method
Number of attempts
```

For example, you may see:

```text
Failed password for invalid user test from 192.168.1.50
```

This could indicate an incorrect login attempt. A single failure is not necessarily malicious; repeated failures from an unexpected source deserve investigation.

---

### 4. Find successful SSH logins

```bash
sudo grep "Accepted" /var/log/auth.log
```

Investigate:

```text
Who logged in?
When did they log in?
What was the source IP?
Was the login expected?
```

---

### 5. Search logs using `grep`

Search for SSH activity:

```bash
sudo grep -i "ssh" /var/log/auth.log
```

Search for errors:

```bash
sudo grep -i "error" /var/log/syslog
```

Search for a particular username:

```bash
sudo grep "securityuser" /var/log/auth.log
```

---

### 6. Use `journalctl`

View system logs:

```bash
sudo journalctl
```

Show errors:

```bash
sudo journalctl -p err
```

View SSH logs:

```bash
sudo journalctl -u ssh
```

View recent logs:

```bash
sudo journalctl --since "1 hour ago"
```

View today's logs:

```bash
sudo journalctl --since today
```

---

### 7. Monitor logs in real time

Follow an authentication log:

```bash
sudo tail -f /var/log/auth.log
```

Now new authentication events will appear as they are written.

Press:

```text
Ctrl + C
```

to stop monitoring.

---

### 8. Investigate a security event

When you find a suspicious event, record:

```text
Date / Time:
Username:
Source IP:
Event:
Service:
Number of Attempts:
Expected or Unexpected:
Evidence:
Analysis:
Recommended Action:
```

The goal is not to assume that every failed login is an attack. Instead, **collect evidence and determine whether the activity is normal or suspicious**.

---

## c. Build Shell Scripts

A **shell script** is a file containing Linux commands that can be executed as a single program.

Shell scripts are useful for:

* System administration
* Log analysis
* Monitoring
* Automation
* Security checks
* Report generation

---

### 1. Create a shell script

Create a file:

```bash
nano system-info.sh
```

Add:

```bash
#!/bin/bash

echo "===== System Information ====="

echo
echo "Current User:"
whoami

echo
echo "Hostname:"
hostname

echo
echo "IP Address:"
hostname -I

echo
echo "Disk Usage:"
df -h

echo
echo "Memory Usage:"
free -h

echo
echo "System Uptime:"
uptime
```

Save the file.

---

### 2. Give execute permission

```bash
chmod +x system-info.sh
```

Run the script:

```bash
./system-info.sh
```

---

### 3. Understand the script

```text
#!/bin/bash
     ↓
Specifies Bash as the interpreter

whoami
     ↓
Displays current user

hostname
     ↓
Displays system hostname

hostname -I
     ↓
Displays IP address

df -h
     ↓
Displays disk usage

free -h
     ↓
Displays memory usage

uptime
     ↓
Displays system uptime
```

---

### 4. Practice variables

Create:

```bash
nano variables.sh
```

Example:

```bash
#!/bin/bash

USER_NAME=$(whoami)
HOST_NAME=$(hostname)

echo "User: $USER_NAME"
echo "Hostname: $HOST_NAME"
```

Run:

```bash
chmod +x variables.sh
./variables.sh
```

---

### 5. Practice conditions

```bash
#!/bin/bash

if [ -f /var/log/auth.log ]
then
    echo "Authentication log exists."
else
    echo "Authentication log not found."
fi
```

This introduces basic decision-making in Bash.

---

### 6. Practice loops

```bash
#!/bin/bash

for item in users processes network disk
do
    echo "Checking: $item"
done
```

Loops become useful when you need to perform the same operation on multiple items.

---

## d. Automate Administrative Tasks

Automation means using scripts to perform **repetitive administrative tasks automatically**.

Common tasks include:

* System information collection
* Disk monitoring
* Memory checks
* User auditing
* Log collection
* Service checks
* Network checks
* Report generation
* Backup operations

---

### 1. Create an administration script

Create:

```bash
nano admin-check.sh
```

Add:

```bash
#!/bin/bash

echo "================================"
echo "    LINUX ADMINISTRATION REPORT"
echo "================================"

echo
echo "[1] Current User"
whoami

echo
echo "[2] Hostname"
hostname

echo
echo "[3] Uptime"
uptime

echo
echo "[4] Disk Usage"
df -h

echo
echo "[5] Memory Usage"
free -h

echo
echo "[6] Running Processes"
ps aux | head -10

echo
echo "[7] Listening Ports"
ss -tuln

echo
echo "===== Check Complete ====="
```

Give permission:

```bash
chmod +x admin-check.sh
```

Run:

```bash
./admin-check.sh
```

Now several administrative checks are performed using **one command**.

---

### 2. Save the output to a report

Run:

```bash
./admin-check.sh > admin-report.txt
```

Read the report:

```bash
cat admin-report.txt
```

Or:

```bash
less admin-report.txt
```

Append another result:

```bash
date >> admin-report.txt
```

---

## Automating with `cron`

Linux can execute scripts automatically at scheduled times using **cron**.

Open your user's crontab:

```bash
crontab -e
```

Example:

```text
0 * * * * /home/user/admin-check.sh
```

This runs the script **once every hour**.

Another example:

```text
0 9 * * * /home/user/admin-check.sh
```

This runs the script every day at **9:00 AM**.

Check configured cron jobs:

```bash
crontab -l
```

> Use the correct absolute path and test the script manually before scheduling it.

---

## e. Create Security Monitoring Scripts

A security monitoring script can automatically check important **security indicators** on a Linux system.

You can monitor:

* Authentication failures
* User activity
* Listening ports
* Running processes
* Disk usage
* System errors
* Network connections
* Important log events

---

### 1. Create a security monitoring script

Create:

```bash
nano security-monitor.sh
```

Add:

```bash
#!/bin/bash

echo "================================"
echo "      SECURITY MONITORING"
echo "================================"

echo
echo "[1] Current User"
whoami

echo
echo "[2] Failed Authentication Attempts"

if [ -f /var/log/auth.log ]
then
    grep -i "failed" /var/log/auth.log | tail -10
else
    echo "auth.log not found; check journalctl instead."
fi

echo
echo "[3] Listening Ports"
ss -tuln

echo
echo "[4] Disk Usage"
df -h

echo
echo "[5] Top CPU Processes"
ps aux --sort=-%cpu | head -10

echo
echo "[6] Recent System Errors"
journalctl -p err -n 10 --no-pager

echo
echo "===== Monitoring Complete ====="
```

Give execute permission:

```bash
chmod +x security-monitor.sh
```

Run:

```bash
sudo ./security-monitor.sh
```

---

# 🔍 What the Security Monitoring Script Checks

### 1. Current User

```bash
whoami
```

Identifies the account running the script.

---

### 2. Authentication

```bash
grep -i "failed" /var/log/auth.log
```

Looks for failed authentication events when the authentication log exists.

---

### 3. Network

```bash
ss -tuln
```

Shows listening TCP and UDP ports.

You can investigate:

```text
Port
Protocol
Listening address
Expected service
Unexpected service
```

---

### 4. Storage

```bash
df -h
```

Shows filesystem disk utilization.

High disk usage can cause system problems and may sometimes be an indicator worth investigating.

---

### 5. Processes

```bash
ps aux --sort=-%cpu
```

Sorts processes by CPU usage.

You can investigate processes that consume unusually high resources.

> High CPU usage alone does not mean malware. Always identify the process and determine whether it is expected.

---

### 6. System Errors

```bash
journalctl -p err -n 10 --no-pager
```

Displays recent journal entries with error priority.

These errors should be reviewed to determine whether they are expected system issues or require investigation.

---

# 🧪 Hands-on Mini Project

## Linux Security Monitoring System

Combine the skills from all five sections into one practical project.

### Step 1 — Create the project directory

```bash
mkdir -p ~/security-monitor
cd ~/security-monitor
```

---

### Step 2 — Create the monitoring script

```bash
nano monitor.sh
```

Add:

```bash
#!/bin/bash

REPORT="$HOME/security-monitor/security-report.txt"

echo "=================================" > "$REPORT"
echo "       LINUX SECURITY REPORT" >> "$REPORT"
echo "=================================" >> "$REPORT"

echo >> "$REPORT"
echo "Date:" >> "$REPORT"
date >> "$REPORT"

echo >> "$REPORT"
echo "Current User:" >> "$REPORT"
whoami >> "$REPORT"

echo >> "$REPORT"
echo "Hostname:" >> "$REPORT"
hostname >> "$REPORT"

echo >> "$REPORT"
echo "Disk Usage:" >> "$REPORT"
df -h >> "$REPORT"

echo >> "$REPORT"
echo "Memory Usage:" >> "$REPORT"
free -h >> "$REPORT"

echo >> "$REPORT"
echo "Listening Ports:" >> "$REPORT"
ss -tuln >> "$REPORT"

echo >> "$REPORT"
echo "Top Processes:" >> "$REPORT"
ps aux --sort=-%cpu | head -10 >> "$REPORT"

echo >> "$REPORT"
echo "Recent System Errors:" >> "$REPORT"
journalctl -p err -n 10 --no-pager >> "$REPORT"

echo >> "$REPORT"
echo "Recent Authentication Events:" >> "$REPORT"

if [ -f /var/log/auth.log ]
then
    tail -20 /var/log/auth.log >> "$REPORT"
else
    journalctl -u ssh -n 20 --no-pager >> "$REPORT"
fi

echo
echo "Security report created:"
echo "$REPORT"
```

---

### Step 3 — Give execute permission

```bash
chmod +x monitor.sh
```

---

### Step 4 — Execute the script

```bash
./monitor.sh
```

If access to some logs requires elevated privileges:

```bash
sudo ./monitor.sh
```

---

### Step 5 — Read the report

```bash
cat security-report.txt
```

Or:

```bash
less security-report.txt
```

---

### Step 6 — Investigate the results

Review the report and identify:

```text
Current User
        ↓
System Hostname
        ↓
Disk Usage
        ↓
Memory Usage
        ↓
Listening Ports
        ↓
Running Processes
        ↓
System Errors
        ↓
Authentication Events
```

Ask yourself:

1. Are the users expected?
2. Are the listening ports expected?
3. Are the running processes legitimate?
4. Are there repeated authentication failures?
5. Are there unusual source IP addresses?
6. Are there important system errors?
7. Does anything require further investigation?

---

# 📋 Mini Project Deliverable

Create a report using:

```text
Project Name:
Linux Security Monitoring System

System:
Hostname:

Date:

Current User:

Disk Usage:

Memory Usage:

Listening Ports:

Important Processes:

Authentication Events:

System Errors:

Suspicious Indicators:

Evidence:

Analysis:

Recommended Action:

Final Conclusion:
```

---

# 🎯 Skills You Should Gain

After completing this section, you should be able to:

* Create and manage Linux users
* Create and manage groups
* Configure file permissions
* Change file ownership
* Manage Linux services
* Monitor processes
* Check memory and disk usage
* Check network configuration
* Analyze authentication logs
* Search logs using `grep`
* Use `journalctl`
* Monitor logs in real time
* Write Bash scripts
* Use variables and conditions
* Use loops in shell scripts
* Automate administrative tasks
* Generate system reports
* Schedule scripts using `cron`
* Monitor authentication activity
* Check listening network ports
* Monitor system errors
* Build basic security-monitoring scripts
* Investigate security indicators

---

# 🔄 Overall Workflow

```text
Linux Administration
        ↓
Users / Groups / Permissions
        ↓
Processes / Services / Network
        ↓
Log Analysis
        ↓
Shell Scripting
        ↓
Administrative Automation
        ↓
Security Monitoring
        ↓
Report Generation
        ↓
Investigation
        ↓
Practical Cybersecurity Skills
```

---

# 🏁 Conclusion

The purpose of hands-on Linux security practice is to move from **knowing commands to using them to solve real problems**.

By completing these exercises, you will practice the complete workflow:

```text
Manage
  ↓
Observe
  ↓
Analyze
  ↓
Automate
  ↓
Monitor
  ↓
Investigate
  ↓
Report
```

> **Practice Linux administration → analyze logs → build scripts → automate tasks → monitor security indicators.**

This provides a strong practical foundation for further **Linux security, SOC, Blue Team, and cybersecurity automation** work.

