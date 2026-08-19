#  Understand System Monitoring

## Table of Contents

* [Introduction](#introduction)
* [a. Process Monitoring](#a-process-monitoring)
* [b. Memory Usage](#b-memory-usage)
* [c. Disk Utilization](#c-disk-utilization)
* [d. Service Management](#d-service-management)
* [e. Performance Observation](#e-performance-observation)
* [Conclusion](#conclusion)

---

## Introduction

System monitoring is the process of observing a computer system to understand its current state, resource usage, running processes, services, and overall performance. In cybersecurity and system administration, monitoring helps identify abnormal behavior, resource exhaustion, failures, and potential security incidents.

---

## a. Process Monitoring

A **process** is a running instance of a program. Process monitoring helps identify which programs are running, how much CPU and memory they consume, and whether any suspicious or unnecessary processes are active.

### Important Commands

```bash
ps
ps aux
ps -ef
top
htop
pgrep <process_name>
pidof <process_name>
pstree
```

### Examples

```bash
ps aux
```

Displays currently running processes with CPU and memory usage.

```bash
top
```

Provides a real-time view of running processes and system resource usage.

```bash
pgrep ssh
```

Finds the process ID of a process named `ssh`.

### Cybersecurity Relevance

Process monitoring can help detect:

* Unknown processes
* Suspicious programs
* Processes consuming excessive CPU
* Unexpected background applications
* Potential malware activity

---

## b. Memory Usage

Memory monitoring helps determine how much RAM is being used, available, cached, and allocated to processes.

### Important Commands

```bash
free -h
cat /proc/meminfo
top
htop
vmstat
```

### Examples

```bash
free -h
```

Displays RAM and swap usage in a human-readable format.

```bash
cat /proc/meminfo
```

Displays detailed information about system memory.

```bash
vmstat
```

Displays information about memory, processes, CPU, and other system resources.

### What to Observe

* Total RAM
* Used RAM
* Available RAM
* Free RAM
* Swap usage
* Processes consuming large amounts of memory

### Cybersecurity Relevance

Unusual memory consumption can indicate:

* Memory-intensive applications
* Resource exhaustion
* Denial-of-service conditions
* Suspicious or malicious processes

---

## c. Disk Utilization

Disk monitoring involves checking available storage space and identifying directories or files consuming large amounts of disk space.

### Important Commands

```bash
df -h
du -sh <directory>
du -h --max-depth=1
lsblk
```

### Examples

```bash
df -h
```

Displays disk-space usage for mounted file systems.

```bash
du -sh /var/log
```

Shows the total size of the `/var/log` directory.

```bash
lsblk
```

Displays available block devices and storage partitions.

### What to Observe

* Total disk space
* Used space
* Available space
* Mounted partitions
* Large directories
* Log file growth

### Cybersecurity Relevance

Disk monitoring can help identify:

* Excessive log generation
* Unexpected files
* Storage exhaustion
* Suspicious file creation
* Potential log-based attacks

---

## d. Service Management

A **service** is a background program that provides a specific function to the operating system or other applications.

Linux systems commonly use `systemd` to manage services.

### Important Commands

```bash
systemctl status <service>
systemctl start <service>
systemctl stop <service>
systemctl restart <service>
systemctl enable <service>
systemctl disable <service>
systemctl list-units --type=service
```

### Examples

```bash
systemctl status ssh
```

Checks the current status of the SSH service.

```bash
systemctl restart ssh
```

Restarts the SSH service.

```bash
systemctl list-units --type=service
```

Lists active services.

### What to Observe

* Running services
* Failed services
* Services starting automatically
* Unexpected services
* Service failures

### Cybersecurity Relevance

Service monitoring helps identify:

* Unauthorized services
* Suspicious network services
* Disabled security services
* Failed services
* Unexpected changes to system configuration

---

## e. Performance Observation

Performance observation involves monitoring the overall behavior of the system, including CPU, memory, disk, processes, and system load.

### Important Commands

```bash
uptime
top
htop
vmstat
iostat
sar
```

### Examples

```bash
uptime
```

Displays how long the system has been running and shows the system load average.

```bash
top
```

Provides a real-time overview of CPU, memory, processes, and system load.

```bash
vmstat
```

Provides information about processes, memory, CPU, and system activity.

```bash
iostat
```

Displays CPU and input/output statistics.

### What to Observe

* CPU utilization
* Memory utilization
* System load
* Disk I/O
* Running processes
* System responsiveness

### Cybersecurity Relevance

Performance observation can help identify:

* Resource exhaustion
* Abnormal system activity
* Denial-of-service conditions
* Resource-heavy malicious processes
* Unexpected system behavior

---


### Key Commands to Remember

```bash
ps aux
top
free -h
df -h
du -sh
lsblk
systemctl status
systemctl list-units --type=service
uptime
vmstat
iostat
```

---

## 📚 Additional Resources

### Linux Commands Reference



👉 [Open Linux Fundamentals Commands Reference](../assets/Linux_Fundamentals_Task_1_.pdf)



