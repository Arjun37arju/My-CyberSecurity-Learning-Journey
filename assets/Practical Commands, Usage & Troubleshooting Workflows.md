# 1. Understand Linux Fundamentals

## a. Linux Ecosystem

**`uname`**

Shows basic information about the Linux system and kernel.

**How to use:** `uname -a`

**`hostname`**
Displays the system's hostname.
**How to use:** `hostname`

**`hostnamectl`**
Shows detailed information about the operating system and hostname.
**How to use:** `hostnamectl`

**`cat /etc/os-release`**
Displays information about the Linux distribution.
**How to use:** `cat /etc/os-release`

**`uname -r`**
Shows the current Linux kernel version.
**How to use:** `uname -r`

### Workflow

```text
Need to identify the Linux system
       ↓
     uname -a
       ↓
Check kernel + architecture
       ↓
hostname
       ↓
Check system hostname
       ↓
hostnamectl
       ↓
Check OS + hostname details
       ↓
cat /etc/os-release
       ↓
Identify Linux distribution
       ↓
uname -r
       ↓
Confirm kernel version
       ↓
System information identified
```

---

## b. File System Hierarchy

**`pwd`**
Shows the current working directory.
**How to use:** `pwd`

**`ls`**
Lists files and directories.
**How to use:** `ls`

**`ls -l`**
Shows files with detailed information.
**How to use:** `ls -l`

**`cd`**
Changes the current directory.
**How to use:** `cd /home`

**`cd ..`**
Moves to the parent directory.
**How to use:** `cd ..`

**`cd ~`**
Moves to the current user's home directory.
**How to use:** `cd ~`

**`find`**
Searches for files and directories.
**How to use:** `find /home -name "file.txt"`

### Workflow

```text
Need to locate yourself in the filesystem
       ↓
      pwd
       ↓
Check current directory
       ↓
      ls
       ↓
View files and directories
       ↓
     ls -l
       ↓
Check permissions + ownership
       ↓
     cd /home
       ↓
Move to another directory
       ↓
      find
       ↓
Search for required files
       ↓
File/directory location identified
```

---

## c. Users and Groups

**`whoami`**
Shows the username of the current user.
**How to use:** `whoami`

**`id`**
Shows the user's UID, GID, and group membership.
**How to use:** `id`

**`who`**
Shows users currently logged into the system.
**How to use:** `who`

**`groups`**
Shows the groups a user belongs to.
**How to use:** `groups`

**`getent passwd`**
Displays user account information.
**How to use:** `getent passwd`

**`getent group`**
Displays group information.
**How to use:** `getent group`

### Workflow

```text
Need to identify the current user
       ↓
     whoami
       ↓
Check username
       ↓
       id
       ↓
Check UID + GID + groups
       ↓
     groups
       ↓
Check group membership
       ↓
      who
       ↓
Check logged-in users
       ↓
getent passwd
       ↓
Check user account information
       ↓
getent group
       ↓
Check group information
       ↓
User and group information identified
```

---

## d. Processes

**`ps`**
Shows processes associated with the current terminal/session.
**How to use:** `ps`

**`ps aux`**
Shows a detailed list of running processes.
**How to use:** `ps aux`

**`top`**
Displays running processes in real time.
**How to use:** `top`

**`htop`**
Provides an interactive real-time process viewer.
**How to use:** `htop`

**`pgrep`**
Finds the PID of a process by its name.
**How to use:** `pgrep ssh`

**`pidof`**
Finds the PID of a running program.
**How to use:** `pidof bash`

**`kill`**
Sends a signal to a process.
**How to use:** `kill <PID>`

**`kill -9`**
Forces a process to terminate immediately.
**How to use:** `kill -9 <PID>`

### Workflow

```text
Need to investigate running processes
       ↓
       ps
       ↓
Check current processes
       ↓
     ps aux
       ↓
View all running processes
       ↓
       top
       ↓
Monitor CPU + memory in real time
       ↓
      pgrep
       ↓
Find PID of a specific process
       ↓
      pidof
       ↓
Confirm program PID
       ↓
      kill PID
       ↓
Try to terminate the process normally
       ↓
    kill -9 PID
       ↓
Force termination if necessary
       ↓
Process problem resolved
```

---

## e. System Services

**`systemctl status`**
Shows the current status of a service.
**How to use:** `systemctl status <service>`

**`systemctl start`**
Starts a service.
**How to use:** `sudo systemctl start <service>`

**`systemctl stop`**
Stops a running service.
**How to use:** `sudo systemctl stop <service>`

**`systemctl restart`**
Restarts a service.
**How to use:** `sudo systemctl restart <service>`

**`systemctl enable`**
Enables a service to start automatically at boot.
**How to use:** `sudo systemctl enable <service>`

**`systemctl disable`**
Prevents a service from starting automatically at boot.
**How to use:** `sudo systemctl disable <service>`

**`systemctl is-active`**
Checks whether a service is currently active.
**How to use:** `systemctl is-active <service>`

**`systemctl is-enabled`**
Checks whether a service is enabled at boot.
**How to use:** `systemctl is-enabled <service>`

### Workflow

```text
Service is not working
       ↓
systemctl status SERVICE
       ↓
Check service state
       ↓
systemctl is-active SERVICE
       ↓
Confirm whether service is active
       ↓
systemctl restart SERVICE
       ↓
Restart the service
       ↓
systemctl status SERVICE
       ↓
Verify service recovery
       ↓
journalctl -u SERVICE
       ↓
Investigate errors if service still fails
       ↓
Service problem identified/resolved
```

# 2. Understand Linux Command Line

## a. Navigation Commands

**`pwd`**
Shows the current working directory.
**How to use:** `pwd`

**`ls`**
Lists files and directories.
**How to use:** `ls`

**`ls -l`**
Shows a detailed directory listing.
**How to use:** `ls -l`

**`ls -a`**
Shows hidden files and directories.
**How to use:** `ls -a`

**`cd`**
Changes to a specified directory.
**How to use:** `cd /home/user`

**`cd ..`**
Moves one directory up.
**How to use:** `cd ..`

**`cd ~`**
Moves to the user's home directory.
**How to use:** `cd ~`

**`clear`**
Clears the terminal screen.
**How to use:** `clear`

### Workflow

```text
Open terminal
       ↓
      pwd
       ↓
Identify current location
       ↓
       ls
       ↓
View directory contents
       ↓
     ls -a
       ↓
Check hidden files
       ↓
   cd /home/user
       ↓
Move to required directory
       ↓
      pwd
       ↓
Verify location
       ↓
      cd ..
       ↓
Move to parent directory
       ↓
Navigation completed
```

---

## b. File Management

**`touch`**
Creates an empty file.
**How to use:** `touch file.txt`

**`mkdir`**
Creates a new directory.
**How to use:** `mkdir folder`

**`cp`**
Copies a file or directory.
**How to use:** `cp file.txt backup.txt`

**`mv`**
Moves or renames a file or directory.
**How to use:** `mv old.txt new.txt`

**`rm`**
Removes a file.
**How to use:** `rm file.txt`

**`rmdir`**
Removes an empty directory.
**How to use:** `rmdir folder`

**`cat`**
Displays the contents of a file.
**How to use:** `cat file.txt`

**`less`**
Views a file one screen at a time.
**How to use:** `less file.txt`

**`file`**
Shows the type of a file.
**How to use:** `file file.txt`

**`stat`**
Shows detailed information about a file.
**How to use:** `stat file.txt`

### Workflow

```text
Need to create a file
       ↓
     touch file.txt
       ↓
Create empty file
       ↓
      ls
       ↓
Verify file
       ↓
Need a directory
       ↓
    mkdir folder
       ↓
Create directory
       ↓
      cp
       ↓
Create a backup/copy
       ↓
      mv
       ↓
Move or rename file
       ↓
     cat / less
       ↓
Check file contents
       ↓
      stat
       ↓
Check file metadata
       ↓
      rm
       ↓
Remove unwanted file
       ↓
File management completed
```

---

## c. Text Processing

**`cat`**
Displays the contents of a text file.
**How to use:** `cat file.txt`

**`head`**
Displays the beginning of a file.
**How to use:** `head file.txt`

**`tail`**
Displays the end of a file.
**How to use:** `tail file.txt`

**`tail -f`**
Continuously displays new lines added to a file.
**How to use:** `tail -f logfile.txt`

**`grep`**
Searches for matching text in a file.
**How to use:** `grep "error" logfile.txt`

**`sort`**
Sorts lines of text.
**How to use:** `sort names.txt`

**`uniq`**
Removes or identifies repeated adjacent lines.
**How to use:** `uniq names.txt`

**`wc`**
Counts lines, words, and characters.
**How to use:** `wc file.txt`

**`cut`**
Extracts selected sections from each line.
**How to use:** `cut -d: -f1 /etc/passwd`

**`tr`**
Translates or replaces characters.
**How to use:** `tr 'a-z' 'A-Z' < file.txt`

### Workflow

```text
Need to inspect a text/log file
       ↓
      cat
       ↓
Read complete file
       ↓
     head
       ↓
Check beginning
       ↓
     tail
       ↓
Check latest entries
       ↓
    tail -f
       ↓
Monitor new log entries
       ↓
     grep
       ↓
Search for errors/patterns
       ↓
     sort
       ↓
Organize results
       ↓
     uniq
       ↓
Remove repeated adjacent entries
       ↓
      wc
       ↓
Count lines/words/bytes
       ↓
     cut / tr
       ↓
Extract or transform data
       ↓
Text analysis completed
```

---

## d. Search Operations

**`find`**
Searches for files and directories.
**How to use:** `find /home -name "file.txt"`

**`grep`**
Searches for text patterns.
**How to use:** `grep "error" logfile.txt`

**`locate`**
Quickly searches for files using a database.
**How to use:** `locate file.txt`

**`which`**
Shows the location of an executable command.
**How to use:** `which python`

**`whereis`**
Finds the binary, source, and manual locations of a command.
**How to use:** `whereis bash`

**`grep -r`**
Recursively searches for text inside directories.
**How to use:** `grep -r "password" /home/user`

**`history`**
Shows previously executed commands.
**How to use:** `history`

### Workflow

```text
Need to find a file
       ↓
      find
       ↓
Search filesystem
       ↓
Need to find text
       ↓
      grep
       ↓
Search inside files
       ↓
Need a faster filename search
       ↓
     locate
       ↓
Search the locate database
       ↓
Need command location
       ↓
      which
       ↓
Find executable path
       ↓
     whereis
       ↓
Find binary + manual locations
       ↓
Need previous command
       ↓
     history
       ↓
Review command history
       ↓
Required information found
```

---

## e. Administrative Commands

**`sudo`**
Runs a command with elevated privileges.
**How to use:** `sudo <command>`

**`su`**
Switches to another user account.
**How to use:** `su <username>`

**`passwd`**
Changes a user's password.
**How to use:** `sudo passwd <username>`

**`useradd`**
Creates a new user account.
**How to use:** `sudo useradd <username>`

**`userdel`**
Deletes a user account.
**How to use:** `sudo userdel <username>`

**`groupadd`**
Creates a new group.
**How to use:** `sudo groupadd <groupname>`

**`apt`**
Manages software packages on Debian-based systems.
**How to use:** `sudo apt install <package>`

**`man`**
Displays the manual page for a command.
**How to use:** `man <command>`

**`history`**
Displays previously executed commands.
**How to use:** `history`

### Workflow

```text
Need administrative privileges
       ↓
      sudo
       ↓
Run authorized command
       ↓
Need to switch user
       ↓
       su
       ↓
Switch account
       ↓
Need to manage password
       ↓
     passwd
       ↓
Change password
       ↓
Need a new user
       ↓
    useradd
       ↓
Create account
       ↓
Need a new group
       ↓
   groupadd
       ↓
Create group
       ↓
Need software
       ↓
      apt
       ↓
Install/update/remove packages
       ↓
Need command documentation
       ↓
       man
       ↓
Read manual
       ↓
Administrative task completed
```

# 3. Understand User & Permission Management

## a. User Accounts

**`whoami`**
Shows the current username.
**How to use:** `whoami`

**`id`**
Shows UID, GID, and group membership.
**How to use:** `id`

**`who`**
Shows currently logged-in users.
**How to use:** `who`

**`w`**
Shows logged-in users and their current activity.
**How to use:** `w`

**`useradd`**
Creates a new user account.
**How to use:** `sudo useradd <username>`

**`passwd`**
Sets or changes a user's password.
**How to use:** `sudo passwd <username>`

**`userdel`**
Deletes a user account.
**How to use:** `sudo userdel <username>`

**`usermod`**
Modifies an existing user account.
**How to use:** `sudo usermod <options> <username>`

### Workflow

```text
Need to identify current user
       ↓
     whoami
       ↓
Check username
       ↓
       id
       ↓
Check UID + GID + groups
       ↓
       who
       ↓
Check logged-in users
       ↓
        w
       ↓
Check user activity
       ↓
Need new account
       ↓
     useradd
       ↓
Create user
       ↓
     passwd
       ↓
Set password
       ↓
     usermod
       ↓
Modify account
       ↓
    userdel
       ↓
Remove account when required
       ↓
User management completed
```

---

## b. Groups

**`groups`**
Shows the groups a user belongs to.
**How to use:** `groups <username>`

**`getent group`**
Displays group information.
**How to use:** `getent group`

**`groupadd`**
Creates a new group.
**How to use:** `sudo groupadd <groupname>`

**`groupdel`**
Deletes a group.
**How to use:** `sudo groupdel <groupname>`

**`usermod -aG`**
Adds a user to a supplementary group.
**How to use:** `sudo usermod -aG <group> <username>`

**`id`**
Shows the groups associated with a user.
**How to use:** `id <username>`

### Workflow

```text
Need to check group membership
       ↓
     groups
       ↓
View user's groups
       ↓
       id
       ↓
Confirm group IDs
       ↓
Need a new group
       ↓
    groupadd
       ↓
Create group
       ↓
Need to add user
       ↓
   usermod -aG
       ↓
Add user to supplementary group
       ↓
     groups
       ↓
Verify membership
       ↓
Need to remove group
       ↓
    groupdel
       ↓
Delete group if appropriate
       ↓
Group management completed
```

---

## c. File Permissions

**`ls -l`**
Displays file permissions and ownership.
**How to use:** `ls -l file.txt`

**`chmod`**
Changes file or directory permissions.
**How to use:** `chmod 755 script.sh`

**`chmod u+x`**
Adds execute permission for the owner.
**How to use:** `chmod u+x script.sh`

**`chmod g+w`**
Adds write permission for the group.
**How to use:** `chmod g+w file.txt`

**`chmod o-r`**
Removes read permission from others.
**How to use:** `chmod o-r file.txt`

**`umask`**
Shows or sets the default permission mask for new files.
**How to use:** `umask`

### Workflow

```text
Need to check file permissions
       ↓
      ls -l
       ↓
Check owner + group + permissions
       ↓
Need to change permissions
       ↓
      chmod
       ↓
Modify permission bits
       ↓
Need owner execution permission
       ↓
   chmod u+x
       ↓
Add execute permission
       ↓
Need group write permission
       ↓
   chmod g+w
       ↓
Add group write permission
       ↓
Need to restrict others
       ↓
   chmod o-r
       ↓
Remove read permission
       ↓
      ls -l
       ↓
Verify new permissions
       ↓
Permissions configured
```

---

## d. Ownership

**`ls -l`**
Shows the owner and group of a file.
**How to use:** `ls -l file.txt`

**`chown`**
Changes the owner of a file or directory.
**How to use:** `sudo chown <user> file.txt`

**`chown user:group`**
Changes both owner and group.
**How to use:** `sudo chown user:group file.txt`

**`chgrp`**
Changes the group ownership of a file.
**How to use:** `sudo chgrp <group> file.txt`

**`stat`**
Displays detailed ownership and permission information.
**How to use:** `stat file.txt`

### Workflow

```text
Need to check file ownership
       ↓
      ls -l
       ↓
Identify owner + group
       ↓
Need to change owner
       ↓
      chown
       ↓
Change file owner
       ↓
Need to change owner + group
       ↓
   chown user:group
       ↓
Update both ownership values
       ↓
Need only group changed
       ↓
      chgrp
       ↓
Change group ownership
       ↓
      stat
       ↓
Verify ownership + permissions
       ↓
Ownership configured
```

---

## e. Privilege Management

**`sudo`**
Runs a command with elevated privileges.
**How to use:** `sudo <command>`

**`sudo -l`**
Shows commands the current user can run with sudo.
**How to use:** `sudo -l`

**`su`**
Switches to another user account.
**How to use:** `su <username>`

**`whoami`**
Shows the current effective username.
**How to use:** `whoami`

**`id`**
Shows the current user's identity and groups.
**How to use:** `id`

**`visudo`**
Safely edits the sudoers configuration.
**How to use:** `sudo visudo`

### Workflow

```text
Need to perform an administrative task
       ↓
      sudo
       ↓
Run command with elevated privileges
       ↓
Need to check sudo permissions
       ↓
     sudo -l
       ↓
View allowed sudo commands
       ↓
Need another user account
       ↓
       su
       ↓
Switch user
       ↓
      whoami
       ↓
Verify effective user
       ↓
       id
       ↓
Verify UID + GID + groups
       ↓
Need to safely edit sudo configuration
       ↓
     visudo
       ↓
Validate and save configuration
       ↓
Privilege management completed
```

# 4. Understand System Monitoring

## a. Process Monitoring

**`ps`**
Shows processes associated with the current terminal/session.
**How to use:** `ps`

**`ps aux`**
Shows detailed information about running processes.
**How to use:** `ps aux`

**`top`**
Monitors processes live in real time.
**How to use:** `top`

**`htop`**
Provides an interactive live process viewer.
**How to use:** `htop`

**`pgrep`**
Finds processes by name.
**How to use:** `pgrep <process-name>`

**`pidof`**
Finds the PID of a running program.
**How to use:** `pidof <program>`

**`kill`**
Sends a signal to a process.
**How to use:** `kill <PID>`

**`kill -9`**
Forces a process to terminate immediately.
**How to use:** `kill -9 <PID>`

**`pstree`**
Displays processes in a tree structure.
**How to use:** `pstree`

### Workflow

```text
System/process is behaving strangely
       ↓
       ps
       ↓
Check current processes
       ↓
     ps aux
       ↓
View all running processes
       ↓
       top
       ↓
Identify high CPU/memory processes
       ↓
      htop
       ↓
Interactively investigate processes
       ↓
     pgrep
       ↓
Find PID by process name
       ↓
     pidof
       ↓
Confirm program PID
       ↓
      kill PID
       ↓
Terminate process normally
       ↓
   kill -9 PID
       ↓
Force termination only if necessary
       ↓
      pstree
       ↓
Check parent/child process relationships
       ↓
Process issue investigated
```

---

## b. Memory Usage

**`free -h`**
Shows RAM and swap memory usage in human-readable format.
**How to use:** `free -h`

**`top`**
Shows memory usage of running processes in real time.
**How to use:** `top`

**`htop`**
Provides an interactive view of memory and process usage.
**How to use:** `htop`

**`ps aux --sort=-%mem`**
Lists processes sorted by memory usage.
**How to use:** `ps aux --sort=-%mem`

**`vmstat`**
Displays memory and overall system performance information.
**How to use:** `vmstat`

### Workflow

```text
System is slow or applications are freezing
       ↓
     free -h
       ↓
Check RAM + swap
       ↓
       top
       ↓
Check memory usage by processes
       ↓
      htop
       ↓
Interactively identify memory-heavy processes
       ↓
ps aux --sort=-%mem
       ↓
Find processes consuming the most memory
       ↓
     vmstat
       ↓
Check memory + system activity
       ↓
Identify memory-heavy process
       ↓
Investigate or manage process
       ↓
Memory problem identified
```

---

## c. Disk Utilization

**`df -h`**
Shows available and used disk space on filesystems.
**How to use:** `df -h`

**`du -h`**
Shows disk usage of files and directories.
**How to use:** `du -h <directory>`

**`du -sh`**
Shows the total size of a directory in a readable format.
**How to use:** `du -sh <directory>`

**`ls -lh`**
Shows file sizes in human-readable format.
**How to use:** `ls -lh`

**`df -i`**
Shows filesystem inode usage.
**How to use:** `df -i`

### Workflow

```text
System reports low disk space
       ↓
      df -h
       ↓
Check filesystem capacity
       ↓
      df -i
       ↓
Check inode usage
       ↓
      du -sh *
       ↓
Find large items in current directory
       ↓
      du -h DIRECTORY
       ↓
Inspect directory disk usage
       ↓
      ls -lh
       ↓
Check individual file sizes
       ↓
Identify unnecessary large files/directories
       ↓
Clean or move data safely
       ↓
      df -h
       ↓
Verify available disk space
       ↓
Disk problem resolved
```

---

## d. Service Management

**`systemctl status`**
Shows the current status of a service.
**How to use:** `systemctl status <service>`

**`systemctl start`**
Starts a service.
**How to use:** `sudo systemctl start <service>`

**`systemctl stop`**
Stops a service.
**How to use:** `sudo systemctl stop <service>`

**`systemctl restart`**
Restarts a service.
**How to use:** `sudo systemctl restart <service>`

**`systemctl enable`**
Enables a service to start automatically at boot.
**How to use:** `sudo systemctl enable <service>`

**`systemctl disable`**
Disables automatic service startup.
**How to use:** `sudo systemctl disable <service>`

**`systemctl is-active`**
Checks whether a service is currently active.
**How to use:** `systemctl is-active <service>`

**`systemctl is-enabled`**
Checks whether a service is enabled at boot.
**How to use:** `systemctl is-enabled <service>`

### Workflow

```text
Application/service is not working
       ↓
systemctl status SERVICE
       ↓
Check service state
       ↓
systemctl is-active SERVICE
       ↓
Confirm active/inactive status
       ↓
systemctl restart SERVICE
       ↓
Restart the service
       ↓
systemctl status SERVICE
       ↓
Verify service after restart
       ↓
Still not working?
       ↓
journalctl -u SERVICE
       ↓
Check service logs
       ↓
Identify configuration/error
       ↓
Fix the problem
       ↓
systemctl restart SERVICE
       ↓
Verify again
       ↓
Service working normally
```

---

## e. Performance Observation

**`uptime`**
Shows system uptime and load average.
**How to use:** `uptime`

**`vmstat`**
Displays CPU, memory, processes, and system activity.
**How to use:** `vmstat`

**`vmstat 2`**
Continuously monitors system activity every 2 seconds.
**How to use:** `vmstat 2`

**`top`**
Provides real-time CPU and process monitoring.
**How to use:** `top`

**`free -h`**
Checks overall RAM and swap usage.
**How to use:** `free -h`

**`df -h`**
Checks filesystem disk utilization.
**How to use:** `df -h`

**`ps aux --sort=-%mem | head`**
Shows processes using the most memory.
**How to use:** `ps aux --sort=-%mem | head`

**`ps aux --sort=-%cpu | head`**
Shows processes using the most CPU.
**How to use:** `ps aux --sort=-%cpu | head`

### Workflow

```text
System feels slow
       ↓
     uptime
       ↓
Check load average
       ↓
      top
       ↓
Check CPU + processes
       ↓
    free -h
       ↓
Check RAM + swap
       ↓
     df -h
       ↓
Check disk capacity
       ↓
    du -sh *
       ↓
Find large directories/files
       ↓
systemctl status SERVICE
       ↓
Check important services
       ↓
journalctl -u SERVICE
       ↓
Investigate service problems
       ↓
Identify the bottleneck
       ↓
Take corrective action
       ↓
Re-check system performance
       ↓
System performance confirmed
```

# Quick Learning Pattern

For every command, remember:

```text
COMMAND
   ↓ 
What does it do?
   ↓
How do I use it?
   ↓
Practice it in Linux
```

**Main goal:** Don't just memorize the commands. Run each command yourself in your Linux/Kali environment and observe the output.
