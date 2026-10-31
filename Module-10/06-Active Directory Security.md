# Active Directory Security

Understanding Active Directory (AD) security is essential for protecting identities, systems, and resources in an enterprise environment. AD security focuses on securing privileged access, protecting credentials, monitoring user activities, applying security standards, and reducing opportunities for attackers.

---

## 📑 Contents

- [Privileged Accounts](#privileged-accounts)
- [Credential Security](#credential-security)
- [Account Monitoring](#account-monitoring)
- [Security Baselines](#security-baselines)
- [Attack Surface Awareness](#attack-surface-awareness)

---

# Privileged Accounts

## What Are Privileged Accounts?

Privileged accounts are accounts with elevated permissions that allow administrative control over systems, users, and resources within Active Directory.

### Examples

- Domain Admins
- Enterprise Admins
- Server Administrators
- Backup Operators

### Capabilities

- Create and manage users
- Reset passwords
- Configure Group Policies
- Manage servers and services
- Access sensitive resources

## Security Risks

If a privileged account is compromised, attackers may gain significant control over the domain and its resources.

## Best Practices

- Follow the Principle of Least Privilege (PoLP)
- Use separate accounts for administration and daily activities
- Enable Multi-Factor Authentication (MFA)
- Regularly review privileged group memberships
- Monitor privileged account activities
- Remove unnecessary administrative permissions

---

# Credential Security

## What Are Credentials?

Credentials are pieces of information used to verify a user's identity.

### Examples

- Username and Password
- PIN
- Smart Card
- Security Token
- Biometric Information

## Common Credential Threats

### Weak Passwords

Short or predictable passwords are easier to crack.

### Password Reuse

Using the same password across multiple systems increases risk.

### Phishing

Attackers trick users into revealing credentials.

### Credential Dumping

Attackers attemptials.

## Security Measures

### Strong Password Policies

- Enforce minimum password length
- Require password complexity
- Prevent common passwords

### Multi-Factor Authentication (MFA)

MFA combines multiple verification methods, such as:

- Something you know (Password)
- Something you have (Token/Phone)
- Something you are (Biometric)

### Secure Storage

Store credentials securely using:

- Password Managers
- Privileged Access Management (PAM) Solutions
- Secure Credential Vaults

---

# Account Monitoring

## What Is Account Monitoring?

Account monitoring involves tracking user activities and authentication events to identify suspicious behavior.

## Activities to Monitor

- Login attempts
- Failed login attempts
- Password changes
- Account lockouts
- Privilege changes
- New account creation
- Group membership modifications

## Benefits

### Early Threat Detection

Helps identify suspicious or malicious activities.

### Incident Investigation

Provides logs that assist during security investigations.

### Compliance Support

Maintains records required for security audits and regulations.

## Monitoring Sources

### Windows Event Logs

Contain authentication and system activity records.

### Active Directory Audit Logs

Provide information on directory-related activities.

### SIEM Platforms

Collect and analyze security events across environments.

### Microsoft Defender

Offers monitoring and threat detection capabilities.

---

# Security Baselines

## What Are Security Baselines?

Security baselines are standardized security configurations designed to establish a secure operating environment.

## Purpose

- Reduce misconfigurations
- Improve consistency
- Enhance overall security posture
- Support compliance requirements

## Common Baseline Settings

### Password Policies

- Strong password requirements
- Password history enforcement
- Password expiration settings

### Account Lockout Policies

Automatically lock accounts after repeated failed login attempts.

### Audit Policies

Enable logging for important security activities.

### System Hardening

- Disable unnecessary services
- Restrict administrative access
- Enforce secure configurations

## Benefits

- Consistent security standards
- Reduced attack opportunities
- Simplified management and auditing
- Improved resilience against common threats

---

# Attack Surface Awareness

## What Is an Attack Surface?

An attack surface is the collection of all possible points where an attacker can attempt to gain unauthorized access.

## Active Directory Attack Surface Examples

- User accounts
- Privileged accounts
- Domain Controllers
- Group Policy Objects (GPOs)
- Shared folders
- Remote access services
- Legacy systems
- Unpatched software

## Common Active Directory Attack Techniques

### Password Spraying

Trying commonly used passwords across many accounts.

### Credential Dumping

Extracting stored credentials from systems.

### Kerberoasting

Requesting service tickets and attempting offline password cracking.

### Pass-the-Hash

Using stolen password hashes for authentication without knowing the actual password.

## Reducing the Attack Surface

- Remove unused accounts
- Disable inactive services
- Apply security patches regularly
- Limit administrative privileges
- Implement MFA
- Monitor suspicious activities
- Review permissions frequently
- Harden Domain Controllers

---
