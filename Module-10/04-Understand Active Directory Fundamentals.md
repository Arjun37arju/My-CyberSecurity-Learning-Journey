# 🔐 Understand Active Directory Fundamentals

## 📑 Table of Contents

- [What is Active Directory?](#1-what-is-active-directory)
- [Domains](#2-domains)
- [Domain Controllers](#3-domain-controllers)
- [Organizational Units (OUs)](#4-organizational-units-ous)
- [Group Policies](#5-group-policies)



---

# 1. What is Active Directory?

**Active Directory (AD)** is Microsoft's directory service that stores and manages information about users, computers, groups, printers, and other network resources in a centralized environment.

It allows administrators to manage authentication, authorization, and resource access across an organization.

## Main Functions

- Centralized user management
- Authentication and authorization
- Resource management
- Security policy enforcement
- Single Sign-On (SSO)

## Example

A company with 500 employees uses Active Directory to:

- Store employee accounts
- Manage computers
- Control access to files and printers
- Apply security policies

## Benefits

✅ Centralized administration

✅ Improved security

✅ Simplified user management

✅ Scalability for large organizations

---

# 2. Domains

A **Domain** is a logical grouping of users, computers, and resources that share a common Active Directory database and security policies.

## Example Domain Structure

```text
company.local
│
├── Users
├── Computers
├── Servers
└── Printers
```

In this example, **company.local** is the domain.

## Features of a Domain

- Centralized authentication
- Shared security policies
- Common database
- Simplified administration

## Real-World Example

```text
sales.company.local
hr.company.local
it.company.local
```

Each domain can have its own resources while remaining part of the overall organization.

---

# 3. Domain Controllers

A **Domain Controller (DC)** is a server that hosts Active Directory and performs authentication and authorization services.

It contains a copy of the Active Directory database.

## Responsibilities

- Verify user credentials
- Process logon requests
- Manage security policies
- Store Active Directory information
- Replicate data to other Domain Controllers

## Authentication Process

```text
User Login
     ↓
Domain Controller
     ↓
Verify Credentials
     ↓
Grant or Deny Access
```

## Why Multiple Domain Controllers?

Organizations commonly deploy multiple DCs for:

- High Availability
- Fault Tolerance
- Load Balancing

## Example

```text
DC01.company.local
DC02.company.local
```

If one Domain Controller fails, another can continue handling authentication requests.

---

# 4. Organizational Units (OUs)

An **Organizational Unit (OU)** is a container used to organize Active Directory objects such as users, computers, and groups.

OUs provide a logical structure for administration and policy management.

## Example

```text
company.local
│
├── HR
│   ├── Users
│   └── Computers
│
├── Sales
│   ├── Users
│   └── Computers
│
└── IT
    ├── Users
    └── Computers
```

## Benefits

- Better organization
- Easier administration
- Delegation of control
- Targeted policy application

## Delegation Example

The HR administrator can be given permission to manage only the HR OU without affecting other departments.

---

# 5. Group Policies

**Group Policy** is a feature that allows administrators to configure and enforce settings for users and computers across a domain.

These settings are applied using **Group Policy Objects (GPOs).**

## Common Uses of Group Policy

### Security Settings

- Password requirements
- Account lockout policies
- User access restrictions

### System Configuration

- Windows updates
- Firewall settings
- Software installation

### User Environment Settings

- Desktop backgrounds
- Control Panel restrictions
- Login scripts

## Example Password Policy

```text
Minimum Password Length: 12 Characters
Password Expiry: 90 Days
Account Lockout: 5 Failed Attempts
```

## Group Policy Workflow

```text
Administrator Creates GPO
          ↓
Link GPO to Domain or OU
          ↓
Policy Applied
          ↓
Settings Enforced Automatically
```

## Benefits

✅ Consistent configurations

✅ Improved security

✅ Automated system management

✅ Reduced administrative effort

---

# Key Concepts Relationship

```text
Active Directory
        │
        ├── Domains
        │
        ├── Domain Controllers
        │
        ├── Organizational Units (OUs)
        │
        └── Group Policies (GPOs)
