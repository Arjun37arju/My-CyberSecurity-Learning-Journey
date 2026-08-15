# Understand Linux Fundamentals

**Linux fundamentals** cover the basic concepts needed to understand, use, and manage a Linux system. This includes the Linux ecosystem, filesystem, users and groups, processes, and system services.

## Table of Contents

* [a. Linux Ecosystem](#a-linux-ecosystem)
* [b. File System Hierarchy](#b-file-system-hierarchy)
* [c. Users and Groups](#c-users-and-groups)
* [d. Processes](#d-processes)
* [e. System Services](#e-system-services)

---

## a. Linux Ecosystem

### Content

**Linux** is an open-source kernel. The kernel is the core component that manages system resources and provides a foundation for applications to interact with hardware.

```text
Application
     ↓
Linux Kernel
     ↓
Hardware
```

### Linux Kernel

The kernel manages important system resources such as:

* Process management
* Memory management
* File/system management
* Network management
* Device/hardware management

**Easy idea:**

> **Kernel = The core of Linux that manages system resources and hardware.**

### Linux Distribution

A **Linux distribution** is a complete operating system built around the Linux kernel.

It includes:

* Linux kernel
* System utilities
* Libraries
* Package management
* Applications
* Configuration

Examples:

* Ubuntu
* Kali Linux
* Linux Mint
* Debian
* Fedora

```text
Linux Kernel
     +
System Utilities
     +
Libraries
     +
Applications
     ↓
Linux Distribution
```

**Easy idea:**

> **Linux = Kernel. Linux distribution = Complete operating system built around the Linux kernel.**

### Kali Linux

**Kali Linux** is an open-source, Debian-based Linux distribution designed for cybersecurity and security testing.

It includes cybersecurity tools and utilities along with the Linux operating system.

**Easy idea:**

> **Kali Linux = Debian-based Linux distribution used for cybersecurity.**

### Shell

A **shell** is a program that allows users to interact with the operating system by entering commands.

```text
User
 ↓
Shell
 ↓
Linux Kernel
 ↓
Hardware
```

Examples of shells include:

* Bash
* Zsh
* Fish
* Dash

### Bash

**Bash** stands for **Bourne Again SHell**.

Bash is one specific type of shell used to execute commands and create shell scripts.

```text
Shell = Category
Bash  = One type of shell
```

**Easy idea:**

> **Shell = Command interpreter. Bash = A specific shell.**

---

## b. File System Hierarchy

### Content

Linux uses a hierarchical filesystem where everything starts from the root directory:

```text
/
```

The filesystem can be visualized as:

```text
/
├── home
├── root
├── etc
├── var
├── tmp
├── usr
├── bin
├── sbin
├── dev
├── proc
└── sys
```

### Important Directories

| Directory | Purpose                                   |
| --------- | ----------------------------------------- |
| `/`       | Root of the filesystem                    |
| `/home`   | Normal users' home directories            |
| `/root`   | Root user's home directory                |
| `/etc`    | Configuration files                       |
| `/var`    | Variable data, including logs             |
| `/tmp`    | Temporary files                           |
| `/usr`    | Programs, libraries, and shared resources |
| `/bin`    | Essential commands                        |
| `/sbin`   | System administration commands            |
| `/dev`    | Device interfaces                         |
| `/proc`   | Process and kernel information            |
| `/sys`    | System and hardware information           |

### Security-Focused Locations

```text
/etc       → Configuration
/var/log   → Logs
/home      → User files
/root      → Root user's home
/tmp       → Temporary files
/proc      → Process/system information
/dev       → Devices
```

### Absolute Path

An **absolute path** gives the complete location starting from `/`.

Example:

```text
/home/user/Documents
/etc/ssh/sshd_config
```

**Easy idea:**

> **Absolute path = Complete path starting from `/`.**

### Relative Path

A **relative path** describes a location from the current directory.

Example:

```bash
cd Documents
```

If you are currently in:

```text
/home/user
```

then:

```text
Documents
```

refers to:

```text
/home/user/Documents
```

**Easy idea:**

> **Relative path = Path based on your current location.**

### Important Path Shortcuts

```text
/   → Filesystem root
.   → Current directory
..  → Parent directory
~   → Current user's home directory
```

Example:

```text
../logs
```

means:

> Go one directory up, then enter `logs`.

### Navigation Commands

#### `pwd`

Shows the current working directory.

```bash
pwd
```

**Easy idea:**

> `pwd` = **Where am I?**

#### `ls`

Lists files and directories.

```bash
ls
```

Useful options:

```bash
ls -l
ls -a
ls -la
ls -lh
```

**Easy idea:**

> `ls` = **What is here?**

#### `cd`

Changes the current directory.

```bash
cd Documents
```

Go one directory up:

```bash
cd ..
```

Go home:

```bash
cd ~
```

Go to filesystem root:

```bash
cd /
```

**Easy idea:**

> `cd` = **Move to another directory.**

---

## c. Users and Groups

### Content

Linux is a **multi-user operating system**. Different users can have different permissions and privileges.

### User

A **user** is an account or identity that represents a person or process interacting with Linux.

A user can have:

* Username
* User ID (UID)
* Home directory
* Group membership
* Permissions
* Authentication information

Example:

```text
Username: arjun
UID:      1000
Home:     /home/arjun
```

### Root User

`root` is the highly privileged administrative user.

Root can generally:

* Modify system configuration
* Install/remove software
* Manage users
* Change permissions
* Start/stop services
* Access protected files

**Easy idea:**

> **Root = Highly privileged Linux administrator account.**

### UID

**UID** means **User ID**.

Linux internally identifies users using numeric IDs.

```text
Username → arjun
UID      → 1000
```

Check your UID with:

```bash
id
```

### `/etc/passwd`

Local user account information is stored in:

```text
/etc/passwd
```

View it with:

```bash
cat /etc/passwd
```

### Group

A **group** is a collection of users.

Groups make permission management easier.

```text
security
├── arjun
├── alice
└── bob
```

### GID

**GID** means **Group ID**.

```text
UID → Identifies a user
GID → Identifies a group
```

### `/etc/group`

Local group information can be found in:

```text
/etc/group
```

View it with:

```bash
cat /etc/group
```

### File Ownership

Every file has:

* An owner
* A group
* Permissions

```text
File
 ↓
Owner + Group
 ↓
Permissions
```

Example:

```text
File:  report.txt
Owner: arjun
Group: security
```

### `chown`

Changes the owner of a file.

```bash
sudo chown arjun report.txt
```

Change both owner and group:

```bash
sudo chown arjun:security report.txt
```

**Easy idea:**

> `chown` = **Change owner.**

### `chgrp`

Changes the group of a file.

```bash
sudo chgrp security report.txt
```

**Easy idea:**

> `chgrp` = **Change group.**

### File Permissions

Linux uses three basic permissions:

```text
r = Read
w = Write
x = Execute
```

These permissions apply to:

```text
Owner | Group | Others
```

Example:

```text
-rwxr-xr--
```

means:

```text
Owner  → rwx
Group  → r-x
Others → r--
```

### Numeric Permissions

```text
r = 4
w = 2
x = 1
```

Examples:

```text
rwx = 4 + 2 + 1 = 7
r-x = 4 + 0 + 1 = 5
r-- = 4 + 0 + 0 = 4
```

Therefore:

```text
755 = rwxr-xr-x
644 = rw-r--r--
700 = rwx------
600 = rw-------
```

### `chmod`

Changes file or directory permissions.

```bash
chmod 755 script.sh
```

Another example:

```bash
chmod 600 secret.txt
```

**Easy idea:**

> `chmod` = **Change permissions.**

### Permission Summary

```text
UID
 ↓
User

GID
 ↓
Group

File
 ↓
Owner + Group
 ↓
Permissions
 ↓
r / w / x
```

---

## d. Processes

### Content

A **process** is a running instance of a program.

```text
Program = Stored software
Process = Running program
```

Example:

```text
Firefox
   ↓
Started
   ↓
Process
```

A process uses system resources such as:

* CPU
* Memory
* Files
* Network resources

### PID

**PID** means **Process ID**.

Linux assigns each running process a unique PID.

Example:

```text
PID     Program
1012    firefox
2050    bash
3100    python3
```

Find the PID of your current shell:

```bash
echo $$
```

**Easy idea:**

> **PID = Unique ID of a running process.**

### `ps`

Shows processes.

```bash
ps
```

For a broader process list:

```bash
ps aux
```

**Easy idea:**

> `ps` = **View processes.**

### `top`

Provides a live view of running processes and resource usage.

```bash
top
```

Press:

```text
q
```

to exit.

### `htop`

Provides an interactive process viewer when installed.

```bash
htop
```

### Foreground Process

A foreground process uses the current terminal.

Example:

```bash
ping 8.8.8.8
```

### Background Process

The `&` symbol runs a command in the background.

```bash
ping 8.8.8.8 &
```

You can continue using the terminal while it runs.

### Parent and Child Processes

Processes can create other processes.

```text
Parent Process
      │
      ├── Child Process
      └── Child Process
```

### Process States

| State | Meaning               |
| ----- | --------------------- |
| `R`   | Running               |
| `S`   | Sleeping              |
| `D`   | Uninterruptible sleep |
| `T`   | Stopped               |
| `Z`   | Zombie                |

View process states with:

```bash
ps aux
```

Look at the `STAT` column.

### `kill`

`kill` sends a signal to a process.

```bash
kill 1234
```

### Important Signals

Graceful termination:

```bash
kill -15 1234
```

Force termination:

```bash
kill -9 1234
```

Stop a process:

```bash
kill -STOP 1234
```

Continue a stopped process:

```bash
kill -CONT 1234
```

### Shell Job Commands

```bash
jobs
```

Shows background jobs.

```bash
fg
```

Brings a job to the foreground.

```bash
bg
```

Continues a stopped job in the background.

**Easy idea:**

> **Process = Running program identified by a PID.**

---

## e. System Services

### Content

A **system service** is a program/process that runs in the background to provide a specific function to the system or other applications.

Examples:

* SSH
* Web server
* DNS service
* Network services
* Logging services

```text
Linux starts
    ↓
Services start
    ↓
Services run in background
    ↓
They provide system functions
```

### Service vs Process

A **process** is any running program.

A **service** is generally a background program designed to provide an ongoing system function.

```text
Firefox
   ↓
Process

SSH Server
   ↓
Background Service
```

### systemd

Modern Linux distributions commonly use **systemd** as the system and service manager.

It helps:

* Start services
* Stop services
* Restart services
* Manage services
* Start services during boot
* Manage service dependencies

### `systemctl`

`systemctl` is the main command used to interact with systemd services.

Check service status:

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

Disable automatic startup:

```bash
sudo systemctl disable ssh
```

Check whether a service is active:

```bash
systemctl is-active ssh
```

Enable and start immediately:

```bash
sudo systemctl enable --now ssh
```

### Start vs Enable

This distinction is important:

```text
start
  ↓
Start the service NOW

enable
  ↓
Start the service automatically during BOOT
```

**Easy idea:**

> `systemctl` = **Manage Linux system services.**

---

# Task 1 Summary

By completing **Linux Fundamentals**, you should understand:

```text
Linux
  ↓
Kernel
  ↓
Filesystem
  ↓
Users & Groups
  ↓
Permissions
  ↓
Processes
  ↓
Services
```

### Important Commands

```bash
pwd
ls
cd
id
cat /etc/passwd
cat /etc/group
chmod
chown
chgrp
ps
top
htop
kill
jobs
fg
bg
systemctl
```

---

## 📚 Additional Resources

### Linux Commands Reference

Finished Task 1?

👉 [Open Linux Fundamentals Commands Reference](../assets/Linux_Fundamentals_Task_1_.pdf)



**Easy idea:**

> **Linux Fundamentals = Understand how Linux is structured, where files are stored, who can access them, what is running, and which services are operating.**
