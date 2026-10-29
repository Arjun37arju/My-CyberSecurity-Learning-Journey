# Identity & Access Management (IAM) Fundamentals

A beginner-friendly guide to understanding Identity and Access Management (IAM), including authentication, authorization, identity lifecycle management, and access governance.

---

## 📚 Table of Contents

- [1. What is IAM?](#1-what-is-iam)
- [2. Authentication Concepts](#2-authentication-concepts)
- [3. Authorization Concepts](#3-authorization-concepts)
- [4. Identity Lifecycle](#4-identity-lifecycle)
- [5. Access Governance](#5-access-governance)
- [Quick Summary](#quick-summary)

---

# 1. What is IAM?

Identity and Access Management (IAM) is a framework of policies, processes, and technologies used to ensure that the **right people have the right access to the right resources at the right time**.

IAM helps organizations:

- Identify users (employees, customers, vendors)
- Authenticate users
- Authorize access to resources
- Monitor and manage user identities throughout their lifecycle

## Example

A company employee logs into the company portal:

1. IAM verifies who they are.
2. IAM determines what resources they can access.
3. IAM tracks and audits their actions.

---

# 2. Authentication Concepts

Authentication is the process of verifying the identity of a user or system.

### Key Question

> Who are you?

## Authentication Factors

### Something You Know

- Password
- PIN
- Security Questions

### Something You Have

- Smartphone
- Hardware Token
- Smart Card

### Something You Are

- Fingerprint
- Facial Recognition
- Iris Scan

## Multi-Factor Authentication (MFA)

MFA combines two or more authentication factors.

### Example

- Password + Mobile OTP
- Password + Fingerprint

### Benefits

- Stronger Security
- Reduced Risk of Account Compromise
- Improved Identity Verification

## Common Authentication Methods

- Username and Password
- One-Time Password (OTP)
- Biometrics
- Digital Certificates
- Single Sign-On (SSO)

---

# 3. Authorization Concepts

Authorization determines what an authenticated user is allowed to do.

### Key Question

> What are you allowed to access?

## Example

| User Type | Access |
|------------|----------|
| HR Employee | Employee Records |
| Finance Employee | Financial Data |
| IT Administrator | System Configuration |

## Authorization Models

### Role-Based Access Control (RBAC)

Permissions are assigned based on roles.

Examples:

- HR Manager
- Accountant
- Network Administrator

### Attribute-Based Access Control (ABAC)

Access decisions are made using attributes such as:

- Department
- Location
- Device Type
- Time of Access

### Principle of Least Privilege

Users should receive only the minimum permissions necessary to perform their job responsibilities.

#### Benefits

- Reduced Attack Surface
- Stronger Security Posture
- Lower Risk of Misuse

---

# 4. Identity Lifecycle

Identity Lifecycle refers to managing user identities from creation to removal.

## Stages of the Identity Lifecycle

### 1. Provisioning

Creating user accounts and assigning required permissions.

#### Example

A new employee joins the organization:

- Email account created
- Applications assigned
- Initial permissions granted

### 2. Modification

Updating user information and permissions.

#### Example

An employee changes departments.

Actions:

- New permissions assigned
- Unnecessary permissions removed

### 3. Review and Certification

Periodic validation of user access rights.

#### Questions Asked

- Does the user still require this access?
- Are permissions appropriate?

### 4. Deprovisioning

Removing user access when no longer needed.

#### Example

An employee leaves the company:

- User account disabled
- Access tokens revoked
- Permissions removed

## Why Identity Lifecycle Management Matters

- Prevents Unauthorized Access
- Reduces Orphaned Accounts
- Supports Compliance Requirements
- Improves Operational Efficiency

---

# 5. Access Governance

Access Governance ensures that access rights are controlled, reviewed, and monitored throughout the organization.

## Goals

- Appropriate Access
- Secure Access
- Regulatory Compliance
- Accountability

## Key Components

### Access Reviews

Regular reviews of user permissions.

#### Example

Managers review employee access every quarter.

### Segregation of Duties (SoD)

Prevents users from holding conflicting permissions.

#### Example

A user who creates payments should not also approve them.

### Audit and Compliance

Tracks:

- Who accessed a resource
- When they accessed it
- What actions they performed

### Policy Enforcement

Ensures organizational security policies are followed consistently.

---

# Quick Summary

| IAM Component | Purpose |
|--------------|---------|
| Identity | Represents a user or system |
| Authentication | Verifies user identity |
| Authorization | Determines user permissions |
| Identity Lifecycle | Manages users from creation to removal |
| Access Governance | Reviews and controls access |

---

## 🧠 Memory Trick

**IAM = IAA + G**

- **I** → Identity
- **A** → Authentication (*Who are you?*)
- **A** → Authorization (*What can you do?*)
- **G** → Governance (*Who should have access?*)

---

### Key Takeaway

Identity and Access Management (IAM) ensures that the right users have the right access to the right resources while maintaining security, compliance, and operational efficiency.
