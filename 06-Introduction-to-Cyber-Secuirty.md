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


# Understand Common Attack Techniques

## Table of Contents

* [Introduction](#introduction)
* [1. Phishing](#1-phishing)
* [2. Social Engineering](#2-social-engineering)
* [3. Credential Attacks](#3-credential-attacks)
* [4. Malware Delivery](#4-malware-delivery)
* [5. Reconnaissance Activities](#5-reconnaissance-activities)
* [How These Techniques Are Connected](#how-these-techniques-are-connected)
* [Conclusion](#conclusion)


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


# Understand Common Attack Techniques

---

## Introduction

Cyber attackers use different techniques to gain unauthorized access, steal information, compromise systems, or disrupt organizations.

Some attacks directly target technical weaknesses, while others target **human behavior**. Understanding these common attack techniques helps cybersecurity professionals recognize suspicious activity and apply the right security controls.

The five common techniques covered here are:

* **Phishing**
* **Social Engineering**
* **Credential Attacks**
* **Malware Delivery**
* **Reconnaissance Activities**

---

## 1. Phishing

**Phishing** is a social engineering attack where an attacker pretends to be a trusted person, company, or service to trick someone into revealing sensitive information or performing an unsafe action.

Attackers commonly use **emails, messages, fake websites, or phone calls** to make the victim believe the request is legitimate.

### Common Examples

* Fake bank login pages
* Fake password-reset emails
* Messages pretending to be from a company
* Fake delivery notifications
* Emails containing malicious attachments or links

### Example

A user receives an email saying:

> "Your account will be suspended. Click here to verify your account."

The link leads to a fake login page. When the user enters their username and password, the attacker captures the credentials.

### Common Types of Phishing

| Type               | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| **Email Phishing** | Fake emails designed to trick users                          |
| **Spear Phishing** | Targeted phishing aimed at a specific person or organization |
| **Whaling**        | Phishing targeting high-level executives                     |
| **Smishing**       | Phishing through SMS or text messages                        |
| **Vishing**        | Phishing through voice calls                                 |

### How to Prevent It

* Check the sender and website address carefully
* Avoid clicking suspicious links
* Don't open unexpected attachments
* Use MFA
* Verify unusual requests through another communication channel
* Report suspicious messages

**Purpose of the Attack:**
Usually to steal credentials, financial information, personal data, or deliver malware.

---

## 2. Social Engineering

**Social engineering** is the manipulation of people into revealing information, giving access, or performing an action that benefits an attacker.

Instead of attacking a technical vulnerability directly, the attacker tries to exploit **human trust, fear, curiosity, urgency, or helpfulness**.

### Common Techniques

* **Pretexting:** Creating a believable fake situation to obtain information
* **Baiting:** Offering something attractive to trick someone into taking an unsafe action
* **Tailgating:** Following an authorized person into a restricted area
* **Impersonation:** Pretending to be someone trusted
* **Quid Pro Quo:** Offering something in exchange for information or access

### Example

An attacker calls an employee and pretends to be an IT support technician:

> "We're fixing a security issue with your account. I need you to confirm your login details."

The employee trusts the attacker and provides sensitive information.

### Why It Works

Attackers often take advantage of:

* Trust
* Fear
* Urgency
* Curiosity
* Lack of security awareness

### Prevention

* Verify unusual requests
* Never share passwords or OTPs
* Follow security procedures
* Be careful with unexpected calls and messages
* Provide regular security awareness training

**Main Idea:**
Social engineering attacks the **person**, rather than directly attacking the computer.

---

## 3. Credential Attacks

**Credential attacks** are attempts to obtain, guess, steal, or misuse usernames, passwords, tokens, or other authentication information.

Once attackers obtain valid credentials, they may be able to access accounts without exploiting a software vulnerability.

### Common Credential Attacks

| Attack                  | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| **Brute Force**         | Trying many possible passwords until one works                |
| **Dictionary Attack**   | Trying passwords from a list of common words and passwords    |
| **Password Spraying**   | Trying a few common passwords against many accounts           |
| **Credential Stuffing** | Using leaked username/password combinations on other services |
| **Phishing**            | Tricking users into providing credentials                     |
| **Keylogging**          | Capturing keystrokes to obtain sensitive information          |

### Example

A user's password is leaked from one website. The attacker tries the same username and password on the user's email and other services.

If the user reused the password, the attacker may gain access to multiple accounts.

### Prevention

* Use strong and unique passwords
* Enable MFA
* Avoid password reuse
* Use a password manager
* Implement account lockout or rate limiting
* Monitor unusual login activity
* Use strong authentication methods

**Main Goal of Attackers:**
Gain access to accounts by obtaining valid authentication credentials.

---

## 4. Malware Delivery

**Malware delivery** is the process of getting malicious software onto a victim's device.

Malware can be delivered through different methods, often by convincing the victim to open or install something.

### Common Delivery Methods

* Malicious email attachments
* Fake software downloads
* Malicious websites
* Compromised websites
* USB devices
* Malicious advertisements
* Fake software updates
* Phishing links

### Example

A user receives an email containing an attachment that appears to be an invoice.

The user opens it, and malicious software is installed on the computer.

### Common Types of Malware

* **Virus** – Attaches itself to files and can spread when those files are executed.
* **Worm** – Can spread automatically across systems or networks.
* **Trojan** – Pretends to be legitimate software but performs malicious actions.
* **Ransomware** – Encrypts files or systems and demands payment.
* **Spyware** – Secretly monitors activity or collects information.

### Prevention

* Keep operating systems and applications updated
* Use antivirus/endpoint security
* Avoid unknown downloads
* Don't open unexpected attachments
* Download software from trusted sources
* Use email and web security filters
* Regularly back up important data

**Main Goal of Attackers:**
Get malicious software onto a system so they can steal data, damage systems, maintain access, or disrupt operations.

---

## 5. Reconnaissance Activities

**Reconnaissance** is the process of collecting information about a target before attempting an attack.

Attackers use reconnaissance to understand the target's **people, systems, applications, network, technologies, and publicly available information**.

Reconnaissance can be **passive** or **active**.

### Passive Reconnaissance

The attacker collects information without directly interacting with the target's systems.

**Examples:**

* Searching public websites
* Studying social media
* Looking at company information
* Searching public documents
* Checking publicly available domain information

### Active Reconnaissance

The attacker directly interacts with the target's infrastructure to gather information.

**Examples:**

* Scanning systems
* Identifying open ports
* Checking available services
* Discovering network hosts

### Example

Before attacking a company, an attacker researches:

* Company website
* Employee names and roles
* Email addresses
* Technologies used
* Publicly exposed services
* Domain and network information

This information can later be used to create a more targeted attack.

### Prevention

Organizations can reduce reconnaissance exposure by:

* Limiting unnecessary public information
* Protecting sensitive documents
* Monitoring exposed services
* Using network security controls
* Regularly checking their external attack surface
* Training employees about information sharing

**Main Goal of Attackers:**
Collect enough information to identify weaknesses and plan a more effective attack.

---

## How These Techniques Are Connected

Attackers often combine multiple techniques instead of relying on just one.

A typical attack could look like this:

**Reconnaissance → Social Engineering → Phishing → Credential Theft → Unauthorized Access → Malware Delivery**

### Example Scenario

1. **Reconnaissance:** The attacker researches a company's employees.
2. **Social Engineering:** The attacker creates a believable story.
3. **Phishing:** A fake login message is sent to an employee.
4. **Credential Attack:** The stolen credentials are used to access an account.
5. **Malware Delivery:** Malicious software is delivered to the compromised system.
6. **Further Attack:** The attacker attempts to access additional systems or data.

This shows why cybersecurity requires **multiple layers of protection** rather than relying on a single security tool.

---

## Conclusion

Understanding common attack techniques is an important part of cybersecurity.

* **Phishing** tricks users into revealing information or taking unsafe actions.
* **Social engineering** manipulates human behavior.
* **Credential attacks** target usernames, passwords, and authentication data.
* **Malware delivery** gets malicious software onto a victim's system.
* **Reconnaissance** collects information about a target before an attack.

Security professionals need to understand how these techniques work so they can **identify attacks early, reduce risk, protect users, and strengthen systems**.

---

