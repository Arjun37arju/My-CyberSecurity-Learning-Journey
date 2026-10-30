# Understand Authorization Models

## 📑 Table of Contents
- #1-role-based-access-control-rbac
- #2-principle-of-least-privilege
- #3-access-management
- #4-permission-assignment
- #5-security-implications
- #quick-comparison
- #key-takeaways

---

## Introduction

Authorization determines **what a user, device, or application is allowed to access or perform** after successful authentication.

> **Authentication = Who are you?**  
> **Authorization = What are you allowed to do?**

### Example

A company employee logs in:

- Authentication verifies their identity.
- Authorization determines whether they can:
  - View employee records
  - Modify payroll data
  - Access administrative systems

---

## 1. Role-Based Access Control (RBAC)

Role-Based Access Control (RBAC) is an authorization model where permissions are assigned to roles rather than individual users.

### How RBAC Works

1. Create roles based on job functions.
2. Assign permissions to those roles.
3. Assign users to appropriate roles.

### Example

| Role | Permissions |
|--------|------------|
| Employee | View personal information |
| Manager | View team reports |
| HR Administrator | Manage employee records |
| System Administrator | Full system control |

### Benefits

- Simplifies permission management
- Reduces administrative overhead
- Improves consistency
- Scales well in large organizations

### Real-World Example

A company may create:

- Employee Role
- Manager Role
- IT Support Role
- Administrator Role

Users inherit permissions based on their assigned role.

---

## 2. Principle of Least Privilege

The Principle of Least Privilege (PoLP) states that users should receive **only the minimum permissions necessary** to perform their job functions.

### Goal

Reduce security risks by limiting access.

### Example

A customer support agent may need:

✅ View customer records

❌ Delete customer records

❌ Access financial systems

### Benefits

- Limits damage from compromised accounts
- Reduces insider threats
- Minimizes accidental changes
- Strengthens overall security

### Best Practices

- Grant only required permissions
- Perform regular access reviews
- Remove unnecessary privileges promptly
- Use temporary elevated access when needed

---

## 3. Access Management

Access Management is the process of controlling and monitoring who can access systems, applications, and resources.

### Key Functions

#### User Provisioning

Creating accounts and granting access.

#### User Deprovisioning

Removing access when users leave or change roles.

#### Access Reviews

Regularly verifying that permissions remain appropriate.

#### Monitoring and Auditing

Tracking access activities to identify unauthorized behavior.

### Example Lifecycle

```text
User Joins Organization
            ↓
Account Created
            ↓
Role Assigned
            ↓
Permissions Granted
            ↓
Access Reviewed Regularly
            ↓
Access Removed When No Longer Needed
```

### Benefits

- Improved security
- Regulatory compliance
- Better visibility into user access

---

## 4. Permission Assignment

Permission assignment involves granting specific rights to users, groups, or roles.

### Common Permission Types

| Permission | Description |
|------------|-------------|
| Read | View data |
| Write | Modify data |
| Create | Add new data |
| Delete | Remove data |
| Execute | Run programs or scripts |
| Full Control | Complete access to resources |

### Assignment Methods

#### Direct Assignment

Permissions assigned directly to users.

**Example:**

```text
User: John
Permission: Read Reports
```

#### Group-Based Assignment

Permissions assigned to groups.

**Example:**

```text
Finance Group
 ├── Alice
 ├── Bob
 └── Charlie

Permission: Access Financial Reports
```

#### Role-Based Assignment

Permissions assigned through RBAC roles.

**Example:**

```text
Manager Role
      ↓
View Team Reports
Approve Requests
Generate Reports
```

### Best Practice

Group-based and role-based assignments are preferred over direct user permissions because they are easier to manage and audit.

---

## 5. Security Implications

Poor authorization practices can introduce serious security risks.

### Excessive Privileges

Users receive more permissions than necessary.

#### Risk

- Data theft
- Unauthorized changes
- Increased attack impact

### Privilege Escalation

An attacker gains higher permissions than intended.

#### Example

```text
Standard User
      ↓
Security Vulnerability
      ↓
Administrator Access
```

### Insider Threats

Authorized users intentionally misuse access.

#### Risk

- Data leakage
- Fraud
- System sabotage

### Orphaned Accounts

Accounts remain active after employees leave.

#### Risk

- Unauthorized access
- Compliance violations

### Mitigation Strategies

- Enforce least privilege
- Conduct regular access reviews
- Implement RBAC
- Monitor access logs
- Remove inactive accounts
- Use Multi-Factor Authentication (MFA)

---

## Quick Comparison

| Concept | Purpose | Main Benefit |
|----------|----------|--------------|
| RBAC | Assign permissions through roles | Easier management |
| Least Privilege | Limit access to minimum necessary | Reduced risk |
| Access Management | Control and monitor access | Better security governance |
| Permission Assignment | Grant specific rights | Controlled resource access |
| Security Controls | Protect systems from misuse | Stronger security posture |

---

## Key Takeaways

### Authorization Fundamentals

- Authorization determines what users can access.
- Authentication occurs before authorization.
- RBAC simplifies permission management through roles.
- Least Privilege reduces security risks by minimizing access.
- Access Management ensures users have appropriate permissions throughout their lifecycle.
- Permission Assignment can be direct, group-based, or role-based.
- Poor authorization practices can lead to privilege escalation, insider threats, and unauthorized access.

### Authorization Workflow

```text
User Login
     ↓
Authentication
(Verify Identity)
     ↓
Authorization
(Check Permissions)
     ↓
Access Granted or Denied
```

### Remember

```text
Authentication = Who are you?
Authorization = What can you do?
```

This distinction is one of the most important concepts in cybersecurity, identity management, and access control systems.
