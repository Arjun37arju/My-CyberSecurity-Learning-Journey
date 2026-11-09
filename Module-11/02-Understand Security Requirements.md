# Understand Security Requirements


- [1. Security Planning](#1-security-planning) 
- [2. Threat Awareness](#2-threat-awareness) 
- [3. Compliance Awareness](#3-compliance-awareness) 
- [4. Secure Design Principles](#4-secure-design-principles) 
- [5. Risk Identification](#5-risk-identification) 


---

## 1. Security Planning

**Security planning** means identifying the security measures an application needs before development begins.

The goal is to ensure security is considered from the beginning of the project.

### Example: Banking Application

Before developing a banking application, the team plans:

- User authentication (secure login).
- Password protection.
- Data encryption.
- Access control.
- Backup and recovery.

**Main Goal:** Decide how to protect the application, its users, and its data.

---

## 2. Threat Awareness

**Threat awareness** means understanding possible security threats that could affect an application or system.

A threat is something that can potentially cause harm to a system.

### Common Security Threats

| Threat | Meaning |
|---|---|
| SQL Injection | Manipulating database queries through user input |
| Phishing | Tricking users into revealing sensitive information |
| Malware | Malicious software designed to harm or compromise systems |
| Brute Force | Repeatedly trying passwords to gain access |
| DDoS | Overwhelming a service with traffic to make it unavailable |
| Data Theft | Stealing sensitive information |

### Example: Brute Force Attack

A login page allows unlimited password attempts.

An attacker repeatedly tries different passwords to gain access to an account.

**Main Goal:** Understand possible attacks before they happen.

---

## 3. Compliance Awareness

**Compliance awareness** means understanding and following applicable security laws, regulations, and industry standards.

Organizations must follow certain rules to protect sensitive information and maintain security.

### Important Security Standards and Regulations

| Standard / Regulation | Purpose |
|---|---|
| GDPR | Protects personal data and privacy in the EU |
| PCI DSS | Protects payment card information |
| HIPAA | Protects health information in the US |
| ISO 27001 | Provides requirements for an information security management system |

### Example

An online shopping application accepts debit and credit card payments.

The organization must follow applicable PCI DSS requirements when handling payment card information.

**Main Goal:** Ensure applications and organizations follow applicable security requirements, laws, and standards.

---

## 4. Secure Design Principles

**Secure design principles** are guidelines used when designing software to make it secure from the beginning.

Instead of fixing security problems after development, developers design the application to prevent them.

### Important Secure Design Principles

| Principle | Meaning |
|---|---|
| Least Privilege | Give users only the permissions they need |
| Defense in Depth | Use multiple layers of security |
| Fail-Safe Defaults | Deny access by default unless permission is granted |
| Separation of Duties | Divide important responsibilities between different people |
| Secure by Default | Start with secure configurations |
| Minimize Attack Surface | Reduce unnecessary entry points attackers could exploit |

### Example: Least Privilege

Imagine a company application has three types of users:

- Employee: Can view normal company records.
- Manager: Can view and manage team records.
- Administrator: Can manage system configurations.

Each user receives only the permissions required for their job.

This reduces the risk of unauthorized access.

**Main Goal:** Build security into the application's design rather than adding it later.

---

## 5. Risk Identification

**Risk identification** means finding possible security risks that could affect an application, system, or organization.

A risk is the possibility that a threat will exploit a vulnerability and cause damage.

### Understanding Threat, Vulnerability, and Risk

| Term | Meaning | Example |
|---|---|---|
| Threat | Something that can cause harm | Attacker |
| Vulnerability | A weakness in a system | Weak password policy |
| Risk | Potential damage when a threat exploits a vulnerability | Attacker gains unauthorized access |

### Example: Banking Application

Imagine a banking application has a weak password policy.

- **Threat:** Attacker attempting to access accounts.
- **Vulnerability:** Weak password requirements.
- **Risk:** Unauthorized access to customer accounts.

### Basic Risk Assessment

Security teams commonly evaluate risks using two important factors:

1. **Likelihood:** How likely is the attack to happen?
2. **Impact:** How much damage could it cause?

### Example

| Risk | Likelihood | Impact |
|---|---|---|
| Weak passwords | High | High |
| Data leakage | Medium | High |
| Website downtime | Medium | Medium |

**Main Goal:** Identify risks early so the organization can prevent or reduce them.

---

## 6. Key Takeaways

| Concept | Description |
|---|---|
| Security Planning | Identify security measures before development |
| Threat Awareness | Understand possible security attacks |
| Compliance Awareness | Follow applicable security laws and standards |
| Secure Design Principles | Design software with security in mind |
| Risk Identification | Find possible security risks before they cause damage |

### Important Differences

- **Threat:** Something that can cause harm.
- **Vulnerability:** A weakness that can be exploited.
- **Risk:** Potential damage when a threat exploits a vulnerability.


**Next Topic:** Understand Secure Software Design and Architecture
