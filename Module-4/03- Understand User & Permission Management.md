#  Understand User & Permission Management

## Contents

* [a. User Accounts](#a-user-accounts)
* [b. Groups](#b-groups)
* [c. File Permissions](#c-file-permissions)
* [d. Ownership](#d-ownership)
* [e. Privilege Management](#e-privilege-management)

---

## a. User Accounts

### View Current User

```bash
whoami
```

Shows the current username.

### View User Information

```bash
id username
```

Shows the user's UID, GID, and groups.

### List Logged-in Users

```bash
who
```

Shows users currently logged into the system.

### Create a User

```bash
sudo useradd username
```

Creates a user account.

### Create User with Home Directory

```bash
sudo useradd -m username
```

Creates a user and a home directory.

### Set User Password

```bash
sudo passwd username
```

Sets or changes the user's password.

### Modify a User

```bash
sudo usermod [options] username
```

Modifies an existing user account.

### Delete a User

```bash
sudo userdel username
```

Deletes a user account.

### Delete User and Home Directory

```bash
sudo userdel -r username
```

Deletes the user and their home directory.

### Lock User Account

```bash
sudo usermod -L username
```

Locks the user's account.

### Unlock User Account

```bash
sudo usermod -U username
```

Unlocks the user's account.

---

## b. Groups

### View User's Groups

```bash
groups username
```

Shows the groups a user belongs to.

### View Detailed Group Information

```bash
id username
```

Shows the user's UID, GID, and group memberships.

### Create a Group

```bash
sudo groupadd groupname
```

Creates a new group.

### Add User to Group

```bash
sudo usermod -aG groupname username
```

Adds a user to a supplementary group.

### Remove User from Group

```bash
sudo gpasswd -d username groupname
```

Removes a user from a group.

### Change User's Primary Group

```bash
sudo usermod -g groupname username
```

Changes the user's primary group.

### Delete a Group

```bash
sudo groupdel groupname
```

Deletes a group.

### View Group Information

```bash
getent group groupname
```

Displays information about a group and its members.

---

## c. File Permissions

### View File Permissions

```bash
ls -l
```

Displays file permissions, owner, and group.

### Change Permissions — Numeric

```bash
chmod 755 filename
```

Changes file permissions using numeric notation.

Common values:

```text
7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---
```

### Change Permissions — Symbolic

```bash
chmod u+x filename
```

Adds execute permission for the owner.

```bash
chmod u-w filename
```

Removes write permission from the owner.

```bash
chmod g+w filename
```

Adds write permission for the group.

```bash
chmod o-r filename
```

Removes read permission from others.

### Change Permissions Recursively

```bash
chmod -R 755 directory/
```

Changes permissions for a directory and its contents.

---

## d. Ownership

### View File Ownership

```bash
ls -l
```

Shows the owner and group associated with files.

### Change File Owner

```bash
sudo chown username filename
```

Changes the owner of a file.

### Change File Owner and Group

```bash
sudo chown username:groupname filename
```

Changes both the owner and group.

### Change Group Ownership

```bash
sudo chgrp groupname filename
```

Changes the group ownership of a file.

### Change Ownership Recursively

```bash
sudo chown -R username:groupname directory/
```

Changes ownership of a directory and its contents.

---

## e. Privilege Management

### Run Command with Elevated Privileges

```bash
sudo command
```

Runs a command with elevated privileges.

### Check sudo Permissions

```bash
sudo -l
```

Shows commands the current user is allowed to run with `sudo`.

### Switch User

```bash
su username
```

Switches to another user account.

### Switch to Root Shell

```bash
sudo -i
```

Opens a root shell using `sudo`.

### Edit sudo Configuration

```bash
sudo visudo
```

Safely edits the `sudoers` configuration.

### Add User to sudo Group

```bash
sudo usermod -aG sudo username
```

Adds a user to the `sudo` group on Debian-based systems.

---

# Quick Command Reference

| Topic                | Command       | Purpose                      |
| -------------------- | ------------- | ---------------------------- |
| User Accounts        | `whoami`      | Show current user            |
| User Accounts        | `id username` | Show user information        |
| User Accounts        | `useradd`     | Create user                  |
| User Accounts        | `passwd`      | Set password                 |
| User Accounts        | `usermod`     | Modify user                  |
| User Accounts        | `userdel`     | Delete user                  |
| Groups               | `groups`      | Show user's groups           |
| Groups               | `groupadd`    | Create group                 |
| Groups               | `usermod -aG` | Add user to group            |
| Groups               | `gpasswd -d`  | Remove user from group       |
| Groups               | `groupdel`    | Delete group                 |
| File Permissions     | `ls -l`       | View permissions             |
| File Permissions     | `chmod`       | Change permissions           |
| Ownership            | `chown`       | Change owner                 |
| Ownership            | `chgrp`       | Change group                 |
| Privilege Management | `sudo`        | Run with elevated privileges |
| Privilege Management | `sudo -l`     | View sudo permissions        |
| Privilege Management | `su`          | Switch user                  |
| Privilege Management | `visudo`      | Edit sudo configuration      |
