# Understand Security Principles

## Table of Contents

- [Defense in Depth](#a-defense-in-depth)
- [Least Privilege (PoLP)](#b-least-privilege-polp)
- [Zero Trust Concepts](#c-zero-trust-concepts)
- [Security Layers](#d-security-layers)
- [Risk Reduction Strategies](#e-risk-reduction-strategies)

---

# Understand Security Principles

## a. Defense in Depth

### Definition
Defense in Depth is a security strategy that uses multiple layers of protection to secure systems, networks, and data. If one security control fails, other layers continue to provide protection.

### Key Points
- Multiple security layers
- No single point of failure
- Prevent, detect, respond, and recover from attacks

### Example
A company uses:
- Firewall
- Antivirus
- Multi-Factor Authentication (MFA)
- Data Encryption
- Security Monitoring

Even if an attacker bypasses the firewall, the remaining controls help stop the attack.

---

## b. Least Privilege (PoLP)

### Definition
The Principle of Least Privilege (PoLP) means users, applications, and systems should have only the minimum permissions required to perform their tasks.

### Benefits
- Reduces unauthorized access
- Limits damage if an account is compromised
- Improves overall security

### Example
A receptionist can view visitor records but cannot access payroll or server settings.

---

## c. Zero Trust Concepts

### Definition
Zero Trust is a security model based on the principle:

> **"Never Trust, Always Verify."**

No user or device is trusted automatically, whether inside or outside the network.

### Core Principles
- Verify every user and device
- Use Multi-Factor Authentication (MFA)
- Apply Least Privilege
- Assume a breach can happen
- Continuously monitor activity

### Example
Before accessing company data, a user must:
1. Verify identity.
2. Complete MFA.
3. Use a compliant device.
4. Receive only the required level of access.

---

## d. Security Layers

Security uses multiple layers to protect an organization.

1. Physical Security
2. Perimeter Security
3. Network Security
4. Endpoint Security
5. Application Security
6. Identity & Access Management (IAM)
7. Data Security
8. Monitoring & Incident Response
9. Backup & Disaster Recovery
10. Security Awareness

### Example
A phishing email bypasses the email filter, but antivirus, EDR, and security monitoring detect and stop the attack before significant damage occurs.

---

## e. Risk Reduction Strategies

### Definition
Risk reduction strategies are methods used to lower the likelihood or impact of security threats.

### Common Strategies
- Keep systems updated (Patch Management)
- Use strong passwords and MFA
- Encrypt sensitive data
- Perform regular backups
- Conduct security awareness training
- Use firewalls and antivirus software
- Implement Least Privilege
- Monitor logs and respond to incidents
- Perform regular vulnerability assessments
- Develop an incident response plan

### Example
A company regularly updates software, trains employees to identify phishing emails, and backs up critical data. These measures reduce the risk of cyberattacks and minimize business impact.

---

# Quick Revision

| Principle | Purpose |
|-----------|---------|
| Defense in Depth | Use multiple layers of security |
| Least Privilege | Give only the minimum required access |
| Zero Trust | Never trust, always verify |
| Security Layers | Protect systems using different security controls |
| Risk Reduction Strategies | Reduce the likelihood and impact of cyber threats |
