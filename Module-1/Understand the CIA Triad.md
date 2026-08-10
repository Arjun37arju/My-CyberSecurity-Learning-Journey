# Understand the CIA Triad

The **CIA Triad** is a basic security model used to understand the main goals of protecting information and systems.

## Table of Contents

* [a. Confidentiality](#a-confidentiality)
* [b. Integrity](#b-integrity)
* [c. Availability](#c-availability)
* [d. Real-World Examples](#d-real-world-examples)
* [e. Security Objectives](#e-security-objectives)

---

## a. Confidentiality

**Confidentiality** means making sure that **only authorized people can access information**.

```text
Information
     ↓
Access Control
     ↓
Authorized User
```

Example:

> Only authorized employees can access a company's customer database.

If an unauthorized person gets access to private information, **confidentiality is compromised**.

**Easy idea:**

> **Confidentiality = Keep information private.**

---

## b. Integrity

**Integrity** means making sure that **information remains accurate, complete, and is not changed without authorization**.

```text
Original Data
     ↓
Security Controls
     ↓
Accurate Data
```

Example:

> A student's exam marks should not be changed by an unauthorized person.

If someone changes information without permission, **integrity is compromised**.

**Easy idea:**

> **Integrity = Keep information accurate and unchanged.**

---

## c. Availability

**Availability** means making sure that **systems and information are accessible when authorized users need them**.

```text
User
 ↓
System
 ↓
Available
```

Example:

> An online banking service should be available when customers need to access their accounts.

If a system becomes unavailable because of an attack or technical failure, **availability is compromised**.

**Easy idea:**

> **Availability = Keep systems and information accessible.**

---

## d. Real-World Examples

The CIA Triad can be understood through everyday examples.

### Online Banking

**Confidentiality**

> Only you should be able to access your bank account.

**Integrity**

> Your account balance should not be changed incorrectly.

**Availability**

> The banking service should be available when you need it.

```text
Online Banking
      ↓
Confidentiality → Protect account information
Integrity       → Protect account data from unauthorized changes
Availability    → Keep banking service accessible
```

---

### Hospital

**Confidentiality**

> Only authorized medical staff should access a patient's records.

**Integrity**

> Patient records should remain accurate.

**Availability**

> Doctors should be able to access records when needed.

---

### Company

**Confidentiality**

> Only authorized employees can access confidential company information.

**Integrity**

> Company data should not be changed without authorization.

**Availability**

> Employees should be able to access required systems when needed.

---

## e. Security Objectives

The three parts of the CIA Triad represent the main **security objectives** for protecting information and systems.

```text
              CIA TRIAD
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
Confidentiality Integrity Availability
       ↓         ↓         ↓
    Private    Accurate   Accessible
```

### Confidentiality

**Objective:**

> Prevent unauthorized access to information.

### Integrity

**Objective:**

> Prevent unauthorized modification or destruction of information.

### Availability

**Objective:**

> Ensure authorized users can access systems and information when needed.

---

## Quick Revision

| CIA Principle       | Meaning                   | Main Goal                    |
| ------------------- | ------------------------- | ---------------------------- |
| **Confidentiality** | Keep information private  | Prevent unauthorized access  |
| **Integrity**       | Keep information accurate | Prevent unauthorized changes |
| **Availability**    | Keep systems accessible   | Ensure access when needed    |

### Easy Way to Remember

```text
C → Confidentiality → Keep it PRIVATE
I → Integrity       → Keep it CORRECT
A → Availability    → Keep it ACCESSIBLE
```

> **CIA Triad = Private + Correct + Accessible**
