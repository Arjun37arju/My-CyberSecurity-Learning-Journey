# Understand Security Principles

## Table of Contents

- [Defense in Depth](#a-defense-in-depth)
- [Least Privilege (PoLP)](#b-least-privilege-polp)
- [Zero Trust Concepts](#c-zero-trust-concepts)
- [Security Layers](#d-security-layers)
- [Risk Reduction Strategies](#e-risk-reduction-strategies)

---
# 🦠 Understand Malware Fundamentals


## 📚 Table of Contents

1. [What is Malware?](#1-what-is-malware)
2. [Viruses](#2-viruses)
3. [Worms](#3-worms)
4. [Trojans](#4-trojans)
5. [Ransomware](#5-ransomware)
6. [Spyware](#6-spyware)
7. [Malware Comparison](#7-malware-comparison)
8. [Basic Prevention](#8-basic-prevention)

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






**Malware (Malicious Software)** is software designed to harm systems, steal information, gain unauthorized access, disrupt operations, or perform other malicious activities.

---

# 1. What is Malware?

Malware is software created with malicious intent. It can be used to:

* Steal information
* Damage or delete files
* Gain unauthorized access
* Monitor users
* Disrupt systems
* Encrypt data

---

# 2. Viruses 🦠

A **virus** is malware that attaches itself to a file or program and can infect other files when the infected file is executed.

### How It Works

```text
Infected File
     ↓
User Runs File
     ↓
Virus Activates
     ↓
Other Files Become Infected
```

### Example

An attacker distributes an infected `game.exe`. When the user runs it, the virus activates and may infect other executable files.

**Main Purpose:** Infect files and spread.

> **Virus = Infect**

---

# 3. Worms 🪱

A **worm** is malware that can replicate itself and spread from one computer to another, often through networks.

### How It Works

```text
Computer A 🪱
     ↓
Finds Vulnerable Computer
     ↓
Computer B 🪱
     ↓
Searches for More Systems
```

Unlike a traditional virus, a worm does not need to attach itself to another file to replicate.

**Main Purpose:** Spread quickly between systems.

> **Worm = Spread**

---

# 4. Trojans 🐴

A **Trojan** is malware that pretends to be legitimate software or a useful file to trick the user into running it.

### How It Works

```text
Fake Software
     ↓
User Downloads It
     ↓
User Runs It
     ↓
Malicious Code Executes
```

### Example

A fake application looks like a useful tool, but after installation it secretly performs malicious actions.

**Main Purpose:** Trick users and gain access or perform malicious actions.

> **Trojan = Trick**

---

# 5. Ransomware 🔒

**Ransomware** is malware that usually encrypts files or prevents access to systems and demands a ransom.

### How It Works

```text
Ransomware Enters System
        ↓
Malware Executes
        ↓
Files Are Encrypted
        ↓
Victim Loses Access
        ↓
Ransom Demand
```

### Example

```text
report.docx → 🔒 Encrypted
photo.jpg   → 🔒 Encrypted
```

**Main Purpose:** Extortion and financial gain.

> **Ransomware = Lock**

---

# 6. Spyware 🕵️

**Spyware** is malware that secretly monitors a user's activity and collects information.

### How It Works

```text
Spyware Enters System
        ↓
Runs Secretly
        ↓
Monitors Activity
        ↓
Collects Information
        ↓
May Send Information to Attacker
```

It may collect:

* Login credentials
* Keystrokes
* Browsing activity
* Personal information
* Files

**Main Purpose:** Secretly collect information.

> **Spyware = Spy**

---

# 7. Malware Comparison

| Malware       | Main Behavior           | Main Goal                   |
| ------------- | ----------------------- | --------------------------- |
| 🦠 Virus      | Infects files           | Spread/infection            |
| 🪱 Worm       | Spreads between systems | Rapid propagation           |
| 🐴 Trojan     | Tricks the user         | Unauthorized actions/access |
| 🔒 Ransomware | Encrypts/locks data     | Extortion                   |
| 🕵️ Spyware   | Monitors activity       | Information collection      |

### 🧠 Easy Memory Trick

> **Virus → Infect** 🦠
> **Worm → Spread** 🪱
> **Trojan → Trick** 🐴
> **Ransomware → Lock** 🔒
> **Spyware → Spy** 🕵️

---

# 8. Basic Prevention

* 🔄 Keep operating systems and applications updated.
* 🛡️ Use reliable endpoint/security software.
* 🔑 Enable MFA for important accounts.
* 📧 Avoid suspicious links and attachments.
* 💾 Keep regular backups of important data.
* 🧑‍🏫 Learn to recognize phishing and social engineering.
* 👁️ Monitor systems for unusual activity.

> **The best protection is a layered approach rather than relying on one security control.**

