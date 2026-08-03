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

🔎 Reconnaissance Techniques
Table of Contents
1. Subdomain Finding
2. WHOIS Lookup
3. Technology Detection
4. robots.txt Check
5. DNS Enumeration
6. Port Scanning
7. IP Address Information
8. Certificate Transparency Logs
9. Search Engine Dorking
10. Wayback Machine (Archive)
11. Social Media & Public Information
12. Email Harvesting
Conclusion
1. Subdomain Finding

Subdomain finding is the process of discovering subdomains associated with a target domain.

Example
site:example.com

Search engines can reveal indexed subdomains such as:

learn.example.com
blog.example.com
mail.example.com
Tools & Techniques
Google search
Subfinder
Amass
Assetfinder
Why It Is Useful

Subdomains can reveal additional applications, development environments, APIs, or other publicly accessible assets.

2. WHOIS Lookup

WHOIS lookup provides information about a domain's registration and ownership details.

Example

Search for:

example.com

using a WHOIS lookup service.

Information You May Find
Domain registrar
Registration date
Expiration date
Name servers
Domain status
Organization information
Tools
WHOIS
Whois.com
WhoisDomainTools
Why It Is Useful

WHOIS information can help understand the domain's registration and infrastructure.

Note: Privacy protection may hide the actual registrant's personal information.

3. Technology Detection

Technology detection identifies the technologies and services used by a website.

Tools
Wappalyzer — Browser extension for detecting web technologies
BuiltWith — Online technology profiling service
WhatWeb — Command-line technology fingerprinting tool
Information You May Find
Web server
Programming language
Framework
CMS
JavaScript libraries
Analytics platforms
Web technologies
Example

A website might use:

Web Server: Nginx
CMS: WordPress
Framework: React
Analytics: Google Analytics
Why It Is Useful

Knowing the technologies in use helps security professionals understand the target's technology stack and identify areas that need security testing.

4. robots.txt Check

The robots.txt file tells search engine crawlers which parts of a website they should or should not crawl.

Example
https://example.com/robots.txt

A file might contain:

User-agent: *
Disallow: /admin/
Disallow: /private/
Disallow: /backup/
What It Can Reveal

It may reveal paths such as:

/admin/
/private/
/backup/
/test/
Important

robots.txt does not provide security or prevent users from accessing these paths. It is simply a crawler instruction file.

Why It Is Useful

During authorized reconnaissance, it can provide clues about interesting website paths.

5. DNS Enumeration

DNS enumeration involves gathering information from the Domain Name System (DNS) to understand how a domain and its services are configured.

Common DNS Records
Record	Purpose
A	Maps a domain to an IPv4 address
AAAA	Maps a domain to an IPv6 address
MX	Identifies mail servers
NS	Identifies authoritative name servers
TXT	Stores text information such as SPF records
CNAME	Creates an alias for another domain
Tools
dig
nslookup
dnsrecon
dnsenum
Example
nslookup example.com

or:

dig example.com
Why It Is Useful

DNS information can help identify:

IP addresses
Mail servers
Name servers
Subdomains
Other connected infrastructure
6. Port Scanning

Port scanning is used to identify open network ports and the services listening on them.

Common Tools
Nmap
RustScan
Masscan
Example

For an authorized target:

nmap <target-ip>

Service detection:

nmap -sV <target-ip>
Common Ports
Port	Common Service
22	SSH
25	SMTP
53	DNS
80	HTTP
443	HTTPS
3389	RDP
Why It Is Useful

Port scanning helps security professionals understand which network services are exposed and whether unnecessary services are accessible.

7. IP Address Information

An IP address can provide information about the network and organization associated with an internet-facing system.

Useful Information
ISP
Autonomous System (AS)
Approximate geographic location
Hostname
Network range
Organization
Tools
ipinfo.io
ViewDNS
WHOIS
Regional Internet Registries
Example
Target Domain
      ↓
IP Address
      ↓
ISP / Organization
      ↓
Network Information
Why It Is Useful

This can help map publicly exposed infrastructure belonging to an organization.

8. Certificate Transparency Logs

Certificate Transparency (CT) logs contain records of publicly issued SSL/TLS certificates.

These certificates can sometimes reveal domain names and subdomains.

Tool
crt.sh

Search for:

example.com
Example Information

A certificate might contain:

example.com
www.example.com
api.example.com
mail.example.com
Why It Is Useful

CT logs can help discover subdomains that may not appear in normal search-engine results.

9. Search Engine Dorking

Search engine dorking uses advanced search operators to find publicly indexed information.

It is also called Google hacking.

Common Operators
site:

Search within a specific domain.

site:example.com

Find pages containing a specific word:

site:example.com inurl:login

Find specific file types:

site:example.com filetype:pdf

Find pages with a specific title:

site:example.com intitle:"login"
Why It Is Useful

Security professionals can use search operators to identify publicly exposed information and help organizations discover accidental exposure.

Important: Only investigate information you are authorized to assess. Do not attempt to access restricted information.

10. Wayback Machine (Archive)

The Wayback Machine stores historical snapshots of websites.

Tool
https://web.archive.org/

Search for:

example.com
What It Can Reveal

Older versions of websites may show:

Removed pages
Previous technologies
Old URLs
Previous website structure
Historical content
Why It Is Useful

Historical information can help security professionals understand how an organization's public-facing infrastructure has changed over time.

11. Social Media & Public Information

Publicly available information from social media and other websites can provide useful information during reconnaissance.

Sources
LinkedIn
GitHub
Company websites
Public documentation
Job postings
Technical blogs
Information That May Be Found
Employee names and roles
Technologies used
Programming languages
Projects
Company structure
Email naming patterns
Public repositories
Example

A company's job posting may mention:

AWS
Docker
Kubernetes
Python
React
Linux

This can provide clues about the organization's technology environment.

Why It Is Useful

Security teams can use this information to understand their organization's public exposure and reduce unnecessary information leakage.

12. Email Harvesting

Email harvesting is the process of finding publicly available email addresses associated with a domain or organization.

Tools
Hunter
theHarvester
Search engines
Public company websites
Example

A company may publicly expose addresses such as:

info@example.com
support@example.com
admin@example.com
employee@example.com
Information That May Be Useful
Public email addresses
Email naming patterns
Employee names
Associated domains
Why It Is Useful

Security teams can use this information to assess their organization's exposure to phishing and other social-engineering attacks.

🔗 How Reconnaissance Techniques Connect

Reconnaissance is usually performed as a process, rather than using only one technique.

A simplified workflow can look like:

Domain
   ↓
Subdomain Discovery
   ↓
DNS Enumeration
   ↓
IP Address Discovery
   ↓
Technology Detection
   ↓
Port & Service Discovery
   ↓
Public Information Gathering
   ↓
Attack Surface Mapping

For example:

example.com
     ↓
api.example.com
     ↓
IP Address
     ↓
Open Ports
     ↓
Running Services
     ↓
Technology Stack

This helps security professionals build a clearer picture of the organization's attack surface.

🛡️ Defensive Importance of Reconnaissance

Reconnaissance is not only useful for attackers. Defenders and penetration testers also use it to find weaknesses before attackers do.

Organizations should regularly check:

Publicly exposed subdomains
Unnecessary open ports
Outdated technologies
Exposed documents
Publicly available employee information
Old website versions
DNS configuration
Forgotten or unused assets

The goal is to reduce unnecessary exposure and strengthen the organization's security.

⚠️ Important Note

Reconnaissance should always be performed legally and ethically.

Only scan, enumerate, or test systems that you own or have explicit permission to assess.

For learning, use authorized labs such as:

TryHackMe
Hack The Box
PortSwigger Web Security Academy
OWASP WebGoat
Conclusion

Reconnaissance is one of the first stages of many cyber attacks. It involves collecting information about a target's domains, subdomains, IP addresses, technologies, services, employees, and publicly available data.

Important reconnaissance techniques include:

Subdomain Finding
WHOIS Lookup
Technology Detection
robots.txt Checking
DNS Enumeration
Port Scanning
IP Information Gathering
Certificate Transparency
Search Engine Dorking
Wayback Machine
Social Media Research
Email Harvesting

Understanding these techniques helps cybersecurity professionals discover an organization's attack surface and exposed information so that weaknesses can be fixed before they are exploited.

## Conclusion

Understanding common attack techniques is an important part of cybersecurity.

* **Phishing** tricks users into revealing information or taking unsafe actions.
* **Social engineering** manipulates human behavior.
* **Credential attacks** target usernames, passwords, and authentication data.
* **Malware delivery** gets malicious software onto a victim's system.
* **Reconnaissance** collects information about a target before an attack.

Security professionals need to understand how these techniques work so they can **identify attacks early, reduce risk, protect users, and strengthen systems**.

---

