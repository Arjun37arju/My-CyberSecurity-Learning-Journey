# Understand Active Directory Administration

## Contents
1. [User Management](#1-user-management)
2. [Group Management](#2-group-management)
3. [Access Control](#3-access-control)
4. [Security Configuration](#4-security-configuration)
5. [Administrative Practices](#5-administrative-practices)

---

## 1. User Management

**User management** means creating, modifying, disabling, and deleting user accounts in Active Directory.

**Main activities:**
- Create accounts for new employees.
- Modify user details.
- Reset forgotten passwords.
- Disable inactive or compromised accounts.
- Delete accounts when no longer required, following retention policies.

**Security importance:** Regularly review user accounts and disable unnecessary accounts to reduce security risks.

## 2. Group Management

**Group management** means organizing multiple user accounts into groups to manage permissions easily.

Instead of assigning permissions to each employee individually, administrators can assign permissions to a group.

### Types of Groups

**1. Security Group**
- Used to assign permissions to resources.
- Controls access to shared folders and files.
- Example: Give the IT Group access to an IT folder.

**2. Distribution Group**
- Used mainly for email distribution.
- Does not assign resource access permissions.
- Example: Send an email to all HR employees using the HR group.

**Benefits:**
- Easy administration.
- Centralized permission management.
- Better security.
- Less manual work.

**Security importance:** Regularly review group membership and remove unnecessary access.

## 3. Access Control

**Access control** determines what an authenticated user is allowed to access and what actions they can perform.

**Important concepts:**
- **Authentication:** Verifies who you are.
- **Authorization:** Determines what you are allowed to do.
- **Permissions:** Define allowed actions such as read, write, and modify.
- **Access Control List (ACL):** Specifies which users or groups can access a resource and their permissions.
- **Least Privilege:** Gives users only the permissions required for their jobs.

**Example:** An HR employee can access HR files but cannot access confidential Finance files.

**Security importance:** Incorrect permissions can expose confidential information or allow unauthorized changes.

## 4. Security Configuration

**Security configuration** means setting up security policies and controls to protect Active Directory.

**Important security configurations:**

1. **Password Policy:** Enforces password requirements.
2. **Account Lockout Policy:** Locks accounts after a configured number of failed login attempts.
3. **Multi-Factor Authentication (MFA):** Requires additional verification beyond a password, where supported.
4. **Group Policy:** Centrally configures security settings on users and computers.
5. **Audit Policies:** Record important security events, such as login attempts and account changes.

**Security importance:** Proper configuration helps reduce unauthorized access and security attacks.

## 5. Administrative Practices

**Administrative practices** are procedures administrators follow to maintain Active Directory securely and reliably.

**Important practices:**
- **Regular monitoring:** Review login activities and security events.
- **Account auditing:** Identify inactive accounts and unnecessary privileges.
- **Backup:** Regularly back up Active Directory data.
- **Patch management:** Keep Domain Controllers and Windows systems updated.
- **Privileged account protection:** Restrict and monitor administrator accounts.
- **Documentation:** Record configuration changes and administrative activities.

**Security importance:** Good administrative practices help prevent security incidents and maintain system availability.

---

## Quick Revision

| Topic | Main Purpose |
|---|---|
| User Management | Manage individual user accounts |
| Group Management | Organize users and manage permissions |
| Access Control | Decide who can access resources |
| Security Configuration | Apply security policies and controls |
| Administrative Practices | Maintain and protect Active Directory |
