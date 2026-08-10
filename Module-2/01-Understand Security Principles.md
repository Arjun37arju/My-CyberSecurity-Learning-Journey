# Understand Security Principles

## Table of Contents

* [a. Defense in Depth](#a-defense-in-depth)
* [b. Least Privilege](#b-least-privilege)
* [c. Zero Trust Concepts](#c-zero-trust-concepts)
* [d. Security Layers](#d-security-layers)
* [e. Risk Reduction Strategies](#e-risk-reduction-strategies)

---

## a. Defense in Depth

### Content

**Defense in Depth** means using multiple layers of security to protect systems instead of depending on a single security control.

```text
Attacker
   ↓
Firewall
   ↓
Authentication
   ↓
Access Control
   ↓
Endpoint Security
   ↓
Data Protection
```

**Easy idea:**

> **Defense in Depth = Multiple security layers working together.**

### Practical Task

Design a basic security system for a small organization using multiple security layers.

Include:

* Network protection
* Authentication
* Access control
* Endpoint protection
* Data protection

### Deliverable

Create:

1. Defense in Depth diagram
2. Explanation of each layer
3. GitHub documentation

---

## b. Least Privilege

### Content

**Least Privilege** means giving a user, application, or system only the permissions required to perform its task.

Example:

> An employee who only needs to read a document should not have permission to delete it.

**Easy idea:**

> **Least Privilege = Give only the access that is needed.**

### Practical Task

Create a fictional organization with different users.

For example:

```text
Employee
Manager
Administrator
```

Decide what each user needs to access.

| User          | Required Access | Unnecessary Access |
| ------------- | --------------- | ------------------ |
| Employee      |                 |                    |
| Manager       |                 |                    |
| Administrator |                 |                    |

### Deliverable

Create:

1. User access table
2. Explanation of your permission decisions
3. GitHub documentation

---

## c. Zero Trust Concepts

### Content

**Zero Trust** is a security approach where access is not automatically trusted.

A user or device should be verified before access is granted.

```text
User
 ↓
Verify Identity
 ↓
Check Access
 ↓
Check Device / Context
 ↓
Allow or Deny
```

**Easy idea:**

> **Zero Trust = Verify before allowing access.**

### Practical Task

Create a Zero Trust access scenario.

Example:

> An employee wants to access a company's internal application.

Create a workflow showing how the user's access is verified.

### Deliverable

Create:

1. Zero Trust workflow diagram
2. Explanation of each verification step
3. Example access scenario
4. GitHub documentation

---

## d. Security Layers

### Content

**Security layers** are different parts of a system where security controls are applied.

```text
Network Layer
      ↓
Application Layer
      ↓
Endpoint Layer
      ↓
Data Layer
```

Each layer protects a different part of the environment.

**Easy idea:**

> **Security Layers = Protect different parts of a system with appropriate security controls.**

### Practical Task

Create a simple security architecture containing different security layers.

| Security Layer | Protects | Security Control | Possible Problem |
| -------------- | -------- | ---------------- | ---------------- |
| Network        |          |                  |                  |
| Application    |          |                  |                  |
| Endpoint       |          |                  |                  |
| Data           |          |                  |                  |

### Deliverable

Create:

1. Security layers diagram
2. Comparison table
3. Explanation of each layer
4. GitHub documentation

---

## e. Risk Reduction Strategies

### Content

**Risk reduction strategies** are actions used to reduce the likelihood or impact of security risks.

```text
Identify Risk
     ↓
Understand Threat
     ↓
Find Vulnerability
     ↓
Choose Security Control
     ↓
Reduce Risk
```

Example:

> A company has an outdated server. Updating the software can reduce the risk associated with known vulnerabilities.

**Easy idea:**

> **Risk Reduction = Take actions that reduce security risk.**

### Practical Task

Create a fictional security scenario and identify:

```text
Threat
   ↓
Vulnerability
   ↓
Risk
   ↓
Security Control
   ↓
Risk Reduction
```

Create a table:

| Threat | Vulnerability | Risk | Security Control | How Risk Is Reduced |
| ------ | ------------- | ---- | ---------------- | ------------------- |
|        |               |      |                  |                     |
|        |               |      |                  |                     |
|        |               |      |                  |                     |

### Deliverable

Create:

1. Risk analysis table
2. Risk reduction explanation
3. Security control diagram
4. GitHub documentation

---

# Final Practical Project

Combine all five principles into one security design for a fictional organization.

```text
Defense in Depth
       ↓
Security Layers
       ↓
Least Privilege
       ↓
Zero Trust
       ↓
Risk Reduction
```

### Final Deliverable

Create a GitHub project containing:

```text
Security-Principles/
│
├── README.md
├── defense-in-depth.md
├── least-privilege.md
├── zero-trust.md
├── security-layers.md
├── risk-reduction.md
└── diagrams/
```

> **Learn → Understand → Practice → Design → Document**
