# 🔐 Understand Authorization Models

## 📚 Table of Contents

- [Introduction](#-introduction)
- [1. Role-Based Access Control (RBAC)](#1-role-based-access-control-rbac)
- [2. Principle of Least Privilege](#2-principle-of-least-privilege)
- [3. Access Management](#3-access-management)
- [4. Permission Assignment](#4-permission-assignment)
- [5. Security Implications](#5-security-implications)


---

## 📖 Introduction

**Authorization** is the process of determining what an authenticated user is allowed to access or perform within a system.

> **Authentication = Who are you?**  
> **Authorization = What are you allowed to do?**

### Example

A user logs into a company network:

- Authentication verifies the user's identity.
- Authorization determines whether the user can:
  - View records
  - Edit files
  - Delete data
  - Access administrative functions

---

# 1. Role-Based Access Control (RBAC)

Role-Based Access Control (RBAC) is an authorization model where permissions are assigned to **roles** rather than directly to individual users.

## How RBAC Works

```text
Permissions
      ↓
    Roles
      ↓
    Users
```

### Example

| Role | Permissions |
|--------|------------|
| Employee | View Documents |
| Manager | View & Approve Documents |
| HR Admin | Manage Employee Records |
| System Admin | Full System Access |

### Benefits

- Simplifies permission management
- Reduces administrative effort
- Improves consistency
- Scales efficiently in large organizations

### Real-World Example

```text
User: Alice
Role: Manager

Inherited Permissions:
✅ View Reports
✅ Approve Requests
✅ Manage Team Data
```

---

# 2. Principle of Least Privilege

The Principle of Least Privilege (PoLP) states that users should be granted **only the minimum permissions necessary** to perform their job responsibilities.

## Example

Customer Support Staff:

```text
✅ View Customer Records
✅ Reset Passwords

❌ Access Payroll Data
❌ Modify Financial Systems
❌ Change Security Settings
```

## Benefits

- Reduces attack surface
- Limits damage from compromised accounts
- Prevents accidental errors
- Minimizes insider threats

## Best Practices

- Grant only required permissions.
- Review permissions regularly.
- Remove unused privileges.
- Use temporary elevated access when necessary.

---

# 3. Access Management

Access Management is the process of controlling, monitoring, and reviewing user access to resources.

## Core Activities

### User Provisioning

Creating accounts and granting appropriate access.

### Access Modification

Updating permissions when responsibilities change.

### User Deprovisioning

Removing access when employees leave an organization.

### Access Reviews

Periodically verifying that permissions remain appropriate.

### Auditing & Monitoring

Tracking user activities and access attempts.

## User Access Lifecycle

```text
User Joins
     ↓
Account Created
     ↓
Role Assigned
     ↓
Permissions Granted
     ↓
Periodic Access Reviews
     ↓
Access Removed When Needed
```

## Benefits

- Improved security
- Better compliance
- Easier administration
- Enhanced visibility and control

---

# 4. Permission Assignment

Permission Assignment is the process of granting specific rights to users, groups, or roles.

## Common Permission Types

| Permission | Description |
|------------|-------------|
| Read | View information |
| Write | Modify information |
| Create | Add new data |
| Delete | Remove data |
| Execute | Run programs or scripts |
| Full Control | Complete access |

## Methods of Permission Assignment

### 1. Direct Assignment

```text
John
 └── Read Reports
```

Assigned directly to a user.

### 2. Group-Based Assignment

```text
Finance Group
├── Alice
├── Bob
└── Charlie

Permission:
✅ Access Financial Reports
```

Permissions are assigned to a group rather than individuals.

### 3. Role-Based Assignment

```text
Manager Role
├── View Reports
├── Approve Requests
└── Manage Team Resources
```

Users obtain permissions by belonging to a role.

## Best Practice

✅ Use **Role-Based** and **Group-Based** assignments whenever possible.

❌ Avoid assigning permissions directly to individual users in large environments.

---

# 5. Security Implications

Improper authorization can create serious security vulnerabilities.

## Excessive Privileges

Users receive more permissions than necessary.

### Risks

- Data exposure
- Unauthorized changes
- Greater damage during attacks

---

## Privilege Escalation

An attacker gains higher privileges than intended.

### Example

```text
Standard User
      ↓
Exploits Vulnerability
      ↓
Administrator Access
```

### Risks

- Full system compromise
- Sensitive data theft
- Service disruption

---

## Insider Threats

Authorized users intentionally misuse their access.

### Risks

- Data theft
- Fraud
- Sabotage
- Information leaks

---

## Orphaned Accounts

Accounts remain active after an employee leaves.

### Risks

- Unauthorized access
- Security breaches
- Compliance violations

---

## Security Controls

To minimize authorization risks:

- Implement RBAC
- Apply Least Privilege
- Conduct regular access reviews
- Monitor user activities
- Remove inactive accounts
- Enable Multi-Factor Authentication (MFA)

---

# 📊 Quick Comparison

| Concept | Purpose | Main Benefit |
|----------|----------|--------------|
| RBAC | Assign permissions through roles | Easier management |
| Least Privilege | Limit access to what is necessary | Reduced risk |
| Access Management | Control user access lifecycle | Improved governance |
| Permission Assignment | Define user rights | Controlled access |
| Security Controls | Protect systems from misuse | Stronger security |

---

# ✅ Key Takeaways

### Remember

```text
Authentication = Who are you?

Authorization = What are you allowed to do?
```

### Key Points

- RBAC assigns permissions through roles.
- Least Privilege grants only required access.
- Access Management controls the user access lifecycle.
- Permission Assignment determines user rights.
- Poor authorization can lead to:
  - Privilege escalation
  - Insider threats
  - Data breaches
  - Unauthorized access

## Authorization Workflow

```text
User Logs In
      ↓
Authentication
(Identity Verified)
      ↓
Authorization
(Permissions Checked)
      ↓
Access Granted or Denied
```


✅ RBAC = Permissions assigned to roles

✅ Least Privilege = Minimum required access

✅ Access Management = Control and review access

✅ Permission Assignment = Read, Write, Execute, Delete, etc.

✅ Security Risks = Excessive privileges, privilege escalation, insider threats, orphaned accounts
