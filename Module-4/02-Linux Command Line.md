# Linux Command Line

## Overview

This task covers the important Linux command-line skills needed for practical Linux usage and cybersecurity.

> **Rule:** Learn up to 15 important commands per section. Do not add unnecessary commands just to reach 15.

---

# 1. Navigation Commands

Navigation commands are used to move around the Linux filesystem.

| Command  | Purpose                                 |
| -------- | --------------------------------------- |
| `pwd`    | Show current directory                  |
| `ls`     | List files and directories              |
| `cd`     | Change directory                        |
| `cd ..`  | Go to parent directory                  |
| `cd -`   | Go to previous directory                |
| `cd ~`   | Go to home directory                    |
| `cd /`   | Go to root directory                    |
| `ls -l`  | Detailed file listing                   |
| `ls -a`  | Show hidden files                       |
| `ls -la` | Detailed listing including hidden files |

### Important examples

```bash
pwd
ls
ls -la
cd /home
cd ..
cd -
cd ~
cd /
```

### Important difference

```text
cd ..  → goes to the parent directory
cd -   → goes to the previous directory
```

---

# 2. File Management

File-management commands are used to create, copy, move, rename, read, and delete files and directories.

| Command | Purpose                          |
| ------- | -------------------------------- |
| `touch` | Create an empty file             |
| `mkdir` | Create a directory               |
| `cp`    | Copy files/directories           |
| `mv`    | Move or rename files/directories |
| `rm`    | Delete files                     |
| `rmdir` | Remove empty directories         |
| `cat`   | Display file contents            |
| `less`  | Read files page by page          |
| `head`  | Show beginning of a file         |
| `tail`  | Show end of a file               |
| `echo`  | Display/write text               |
| `chmod` | Change permissions               |
| `chown` | Change ownership                 |
| `chgrp` | Change group ownership           |

### Examples

Create a file:

```bash
touch abc.txt
```

Create a directory:

```bash
mkdir folder1
```

Copy a file:

```bash
cp abc.txt /home/sioux/folder1/
```

Move a file:

```bash
mv abc.txt /home/sioux/folder1/
```

Rename a file:

```bash
mv old.txt new.txt
```

Delete a file:

```bash
rm abc.txt
```

Read a file:

```bash
cat abc.txt
```

Read a large file:

```bash
less abc.txt
```

Change permissions:

```bash
chmod u+x script.sh
```

Change ownership:

```bash
sudo chown sioux abc.txt
```

### Symbolic links

A symbolic link can point to a file or directory:

```bash
ln -s original.txt shortcut.txt
```

A link to a file can be read like a file:

```bash
cat shortcut.txt
```

A link to a directory can be entered:

```bash
cd mydocs
```

---

# 3. Text Processing

Text-processing commands are used to search, extract, transform, and analyze text.

| Command  | Purpose                             |
| -------- | ----------------------------------- |
| `grep`   | Search for text/patterns            |
| `cut`    | Extract specific fields             |
| `tr`     | Translate/remove characters         |
| `sed`    | Modify/process text                 |
| `awk`    | Process and extract structured data |
| `sort`   | Sort lines                          |
| `uniq`   | Remove duplicate consecutive lines  |
| `wc`     | Count lines/words/characters        |
| `head`   | Show beginning of a file            |
| `tail`   | Show end of a file                  |
| `cat`    | Display file contents               |
| `less`   | Read files page by page             |
| `more`   | Read files page by page             |
| `tee`    | Display and save output             |
| `column` | Format data into columns            |

## `grep`

Search for text inside a file:

```bash
grep "failed" logs.txt
```

Case-insensitive search:

```bash
grep -i "failed" logs.txt
```

`-i` means **ignore case**.

---

## `cut`

Extract specific fields.

Example:

```text
arjun:admin:1001
```

Use `:` as the separator and select field 2:

```bash
cut -d ':' -f 2 users.txt
```

```text
-d → delimiter
-f → fields
```

`-d` = delimiter
`-f` = fields

---

## `tr`

Transform characters:

```bash
echo "hello linux" | tr 'a-z' 'A-Z'
```

Output:

```text
HELLO LINUX
```

Remove numbers:

```bash
echo "abc123xyz" | tr -d '0-9'
```

`-d` = delete.

---

## `sed`

Find and replace text:

```bash
sed 's/admin/ADMIN/' users.txt
```

This displays the modified result without changing the original file.

To modify the file itself:

```bash
sed -i 's/admin/ADMIN/' users.txt
```

`-i` = edit the file in place.

---

## `awk`

Extract fields from structured data:

```bash
awk -F ':' '{print $1}' users.txt
```

```text
-F ':' → use : as separator
$1     → field 1
$2     → field 2
$3     → field 3
```

Example:

```bash
awk -F ':' '{print $1, $3}' users.txt
```

---

## `sort`

Sort lines:

```bash
sort users.txt
```

---

## `uniq`

Remove duplicate consecutive lines:

```bash
uniq users.txt
```

For reliable duplicate removal, sorting is often used first:

```bash
sort users.txt | uniq
```

---

## `wc`

Count information.

Count lines:

```bash
wc -l users.txt
```

Count words:

```bash
wc -w users.txt
```

Count characters:

```bash
wc -m users.txt
```

---

## `head`

Show the beginning:

```bash
head users.txt
```

Show the first 10 lines by default.

---

## `tail`

Show the end:

```bash
tail users.txt
```

Useful for logs:

```bash
tail -f /var/log/syslog
```

`-f` follows new entries as they appear.

---

## `more`

Read a file page by page:

```bash
more largefile.txt
```

Useful keys:

```text
Space → next page
Enter → next line
q     → quit
```

---

## `tee`

Display output and save it at the same time:

```bash
echo "Linux security" | tee security.txt
```

Append instead of overwrite:

```bash
echo "New line" | tee -a security.txt
```

```text
>       → save to file
tee     → display + save
tee -a  → display + append
```

---

## `column`

Format separated data into readable columns:

```bash
column -t -s ':' users.txt
```

```text
-s ':' → separator is :
-t     → format as a table
```

---

# 4. Search Operations

Search commands help locate files, commands, and information on a Linux system.

| Command      | Purpose                                     |
| ------------ | ------------------------------------------- |
| `find`       | Find files/directories                      |
| `locate`     | Quickly find files using a database         |
| `which`      | Find an executable                          |
| `whereis`    | Find executable and related files           |
| `grep`       | Search text                                 |
| `type`       | Identify the type of a command              |
| `command -v` | Find what the shell will execute            |
| `apropos`    | Search commands by description              |
| `xargs`      | Pass output as arguments to another command |

---

## `find`

Find files/directories:

```bash
find . -name "abc.txt"
```

```text
.          → start from current directory
-name      → search by name
"abc.txt"  → filename
```

Example:

```bash
find /home/sioux -name "abc.txt"
```

---

## `locate`

Search for files using its file-path database:

```bash
locate abc.txt
```

### `find` vs `locate`

```text
find   → searches the filesystem directly
locate → searches a database
```

`locate` is usually faster, but its database may not contain very recently created files.

---

## `which`

Find where an executable is located:

```bash
which bash
```

Example output:

```text
/usr/bin/bash
```

---

## `whereis`

Find an executable and related locations:

```bash
whereis bash
```

It may show:

```text
/usr/bin/bash
/usr/share/man/...
```

### Difference

```text
which   → executable location
whereis → executable + related locations
```

---

## `type`

Identify what kind of command something is:

```bash
type cd
```

Possible result:

```text
cd is a shell builtin
```

Check another:

```bash
type ls
```

It can identify aliases, builtins, functions, or executables.

---

## `command -v`

Find what the shell will execute:

```bash
command -v ls
```

It can also identify shell builtins:

```bash
command -v cd
```

---

## `apropos`

Search for commands based on descriptions:

```bash
apropos network
```

Useful when you know **what you want to do but don't know the command name**.

---

## `xargs`

Pass the output of one command as arguments to another command:

```bash
find . -name "*.txt" | xargs wc -l
```

Concept:

```text
find
  ↓
find files
  ↓
xargs
  ↓
give filenames to wc
  ↓
count lines
```

Be careful when using `xargs` with commands that modify or delete files.

---

# 5. Administrative Commands

Administrative commands are used for users, privileges, processes, services, and system management.

| #  | Command      | Purpose                                |
| -- | ------------ | -------------------------------------- |
| 1  | `sudo`       | Run a command with elevated privileges |
| 2  | `whoami`     | Show current username                  |
| 3  | `id`         | Show UID, GID, and groups              |
| 4  | `groups`     | Show group membership                  |
| 5  | `passwd`     | Change a password                      |
| 6  | `su`         | Switch user                            |
| 7  | `useradd`    | Create a user                          |
| 8  | `usermod`    | Modify a user                          |
| 9  | `userdel`    | Delete a user                          |
| 10 | `ps`         | Show processes                         |
| 11 | `top`        | Monitor processes in real time         |
| 12 | `kill`       | Send a signal to a process             |
| 13 | `systemctl`  | Manage system services                 |
| 14 | `journalctl` | View system logs                       |
| 15 | `shutdown`   | Shut down/restart the system           |

---

## `sudo`

Run a command with administrator privileges:

```bash
sudo command
```

Example:

```bash
sudo apt update
```

`sudo` does not permanently turn you into root.

---

## `whoami`

Show the current user:

```bash
whoami
```

With sudo:

```bash
sudo whoami
```

The result is normally:

```text
root
```

---

## `id`

Show identity information:

```bash
id
```

Important terms:

```text
UID → User ID
GID → Group ID
groups → groups the user belongs to
```

Show only UID:

```bash
id -u
```

Show primary GID:

```bash
id -g
```

---

## `groups`

Show group membership:

```bash
groups
```

---

## `passwd`

Change your password:

```bash
passwd
```

Administrator changing another user's password:

```bash
sudo passwd username
```

---

## `su`

Switch user:

```bash
su username
```

Switch to root login shell where configured:

```bash
su -
```

Return to the previous shell:

```bash
exit
```

### Difference

```text
su user       → switch to another user
sudo command  → run one command with elevated privileges
```

---

## `useradd`

Create a user:

```bash
sudo useradd testuser
```

Set a password:

```bash
sudo passwd testuser
```

---

## `usermod`

Modify an existing user.

Add a user to a supplementary group:

```bash
sudo usermod -aG group username
```

Important:

```text
-a → append
-G → supplementary group
```

---

## `userdel`

Delete a user:

```bash
sudo userdel username
```

Delete the user and their home directory:

```bash
sudo userdel -r username
```

Be careful with `-r` because files in the user's home directory can be removed.

---

# Process Management

## `ps`

Show running processes:

```bash
ps
```

Detailed process list:

```bash
ps aux
```

Important information includes:

```text
USER
PID
%CPU
%MEM
COMMAND
```

**PID = Process ID**

---

## `top`

Show processes in real time:

```bash
top
```

Press:

```text
q
```

to quit.

### Difference

```text
ps → process snapshot
top → live process monitoring
```

---

## `kill`

Send a signal to a process:

```bash
kill PID
```

Force termination:

```bash
kill -9 PID
```

Use `-9` only when necessary.

Always identify the process before terminating it.

---

# Services

## `systemctl`

Check a service:

```bash
systemctl status ssh
```

Start:

```bash
sudo systemctl start ssh
```

Stop:

```bash
sudo systemctl stop ssh
```

Restart:

```bash
sudo systemctl restart ssh
```

Enable at boot:

```bash
sudo systemctl enable ssh
```

Disable at boot:

```bash
sudo systemctl disable ssh
```

---

# Logs

## `journalctl`

View system logs:

```bash
journalctl
```

Show the last 20 entries:

```bash
journalctl -n 20
```

Follow logs in real time:

```bash
journalctl -f
```

View logs for a service:

```bash
journalctl -u ssh
```

### Cybersecurity importance

Logs can contain information about:

* Login attempts
* SSH activity
* Service failures
* System events
* Errors
* Suspicious activity

---

# System Shutdown

## `shutdown`

Shut down:

```bash
sudo shutdown now
```

Restart:

```bash
sudo shutdown -r now
```

Schedule shutdown:

```bash
sudo shutdown +10
```

Cancel scheduled shutdown:

```bash
sudo shutdown -c
```

> Do not run shutdown commands on your main system just for practice.

---

# Cybersecurity-Focused Commands to Prioritize

If you need to revise quickly, prioritize these:

```text
grep
find
cut
awk
sed
sort
uniq
wc
ps
top
kill
sudo
id
systemctl
journalctl
chmod
chown
```

These commands are particularly useful for **Linux administration, log analysis, system investigation, permissions, and cybersecurity work**.

---

# Task 2 Completion Checklist

* [x] Navigation Commands
* [x] File Management
* [x] Text Processing
* [x] Search Operations
* [x] Administrative Commands

## Task 2 — COMPLETE ✅
