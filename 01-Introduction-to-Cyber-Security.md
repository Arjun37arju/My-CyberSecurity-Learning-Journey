## Table of Contents

- [What is Cybersecurity?](#what-is-cybersecurity)
  - [Objectives of Cybersecurity](#objectives-of-cybersecurity)
- [Why is Cybersecurity Important?](#why-is-cybersecurity-important)
  - [Importance of Cybersecurity](#importance-of-cybersecurity)
- [Information Security vs Cybersecurity](#information-security-vs-cybersecurity)
- [Cybersecurity Domains](#cybersecurity-domains)
  - [1. Network Security](#1-network-security)
  - [2. Information Security](#2-information-security)
  - [3. Application Security](#3-application-security)
  - [4. Cloud Security](#4-cloud-security)
  - [5. Endpoint Security](#5-endpoint-security)
  - [6. Identity and Access Management (IAM)](#6-identity-and-access-management-iam)
  - [7. Operational Security (OPSEC)](#7-operational-security-opsec)
  - [8. Disaster Recovery and Business Continuity](#8-disaster-recovery-and-business-continuity)
- [Modern Threat Landscape](#modern-threat-landscape)
  - [Common Modern Threats](#common-modern-threats)
    - [Phishing](#phishing)
    - [Malware](#malware)
    - [Ransomware](#ransomware)
    - [Data Breach](#data-breach)
    - [DDoS (Distributed Denial of Service)](#ddos-distributed-denial-of-service)
    - [Insider Threat](#insider-threat)
    - [Zero-Day Attack](#zero-day-attack)
    - [Social Engineering](#social-engineering)
- [Security Objectives and CIA Triad](#security-objectives-and-cia-triad)
  - [A. Confidentiality](#a-confidentiality)
  - [B. Integrity](#b-integrity)
  - [C. Availability](#c-availability)
  - [D. Real-World Example (ATM Banking System)](#d-real-world-example-atm-banking-system)
  - [E. Security Objectives](#e-security-objectives)
- [Summary](#summary)
- [Cybersecurity Basics](#cybersecurity-basics)
  - [1. Threat](#1-threat)
  - [2. Vulnerability](#2-vulnerability)
  - [3. Risk](#3-risk)
  - [4. Exploit](#4-exploit)
  - [5. Attack Vector](#5-attack-vector)
  - [Relationship Between Them](#relationship-between-them)
  - [Quick Comparison](#quick-comparison)
  - [Real-World Example](#real-world-example)
- [Types of Attackers](#types-of-attackers)
  - [A. Script Kiddies](#a-script-kiddies)
  - [B. Cyber Criminals](#b-cyber-criminals)
  - [C. Insider Threat](#c-insider-threat)
  - [D. Hacktivists](#d-hacktivists)
  - [E. Nation-State Actors](#e-nation-state-actors)
- [Interview Summary](#interview-summary)

---


# Introduction to Cybersecurity

## What is Cybersecurity?

Cybersecurity is the practice of protecting digital assets, including computers, networks, systems, applications, and data, from cyber attacks, unauthorized access, theft, damage, and disruption.

It involves implementing technologies, processes, and security controls to ensure the confidentiality, integrity, and availability of information.

### Objectives of Cybersecurity

- Protect sensitive information
- Prevent unauthorized access
- Detect and respond to cyber threats
- Ensure business continuity
- Protect digital infrastructure

---

# Why is Cybersecurity Important?

Cybersecurity has become essential because organizations and individuals depend on digital technology for communication, banking, healthcare, education, and business operations.

Without cybersecurity, attackers can steal sensitive information, disrupt services, and cause financial losses.

## Importance of Cybersecurity

- Protects sensitive and confidential data
- Prevents unauthorized access
- Secures computer systems and networks
- Protects online banking and financial transactions
- Prevents cyber attacks such as malware and phishing
- Ensures business continuity
- Protects customer privacy
- Maintains trust and reputation
- Helps organizations comply with security regulations

---

# Information Security vs Cybersecurity

Although Information Security and Cybersecurity are related, they are not the same.

| Information Security | Cybersecurity |
|----------------------|---------------|
| Protects all forms of information | Protects digital systems and information |
| Covers both physical and digital data | Covers only digital assets |
| Focuses on confidentiality, integrity, and availability | Focuses on defending against cyber attacks |
| Includes paper documents, digital files, and databases | Includes computers, networks, applications, cloud, and devices |

### Example

Information Security:
- Locking confidential paper documents inside a secure cabinet.

Cybersecurity:
- Protecting a company's server using a firewall and antivirus.

---

# Cybersecurity Domains

Cybersecurity consists of several specialized domains.

## 1. Network Security

Protects computer networks from unauthorized access, attacks, and misuse.

Examples:
- Firewalls
- IDS/IPS
- VPN
- Network Monitoring

---

## 2. Information Security

Protects sensitive information from unauthorized access, disclosure, modification, or destruction.

Examples:
- Encryption
- Access Control
- Data Classification

---

## 3. Application Security

Protects software applications throughout their development and deployment.

Examples:
- Secure Coding
- Vulnerability Assessment
- Penetration Testing

---

## 4. Cloud Security

Protects cloud platforms, cloud applications, and cloud data.

Examples:
- AWS Security
- Microsoft Azure Security
- Google Cloud Security

---

## 5. Endpoint Security

Protects endpoint devices such as laptops, desktops, mobile phones, and servers.

Examples:
- Antivirus
- EDR (Endpoint Detection and Response)

---

## 6. Identity and Access Management (IAM)

Ensures only authorized users can access systems and resources.

Examples:
- Multi-Factor Authentication (MFA)
- Role-Based Access Control (RBAC)

---

## 7. Operational Security (OPSEC)

Protects operational processes and organizational security procedures.

Examples:
- Security Policies
- Risk Management

---

## 8. Disaster Recovery and Business Continuity

Ensures organizations can recover quickly after cyber attacks or disasters.

Examples:
- Data Backup
- Disaster Recovery Plan

---

# Modern Threat Landscape

The Modern Threat Landscape refers to the constantly evolving cyber threats, attack techniques, and vulnerabilities that target organizations, governments, and individuals.

Attackers continuously develop new methods to bypass security controls.

## Common Modern Threats

### Phishing

Fraudulent emails or messages designed to steal sensitive information such as usernames, passwords, or banking details.

---

### Malware

Malicious software designed to damage, disrupt, or gain unauthorized access to computer systems.

Examples:
- Virus
- Worm
- Trojan

---

### Ransomware

A type of malware that encrypts files and demands payment to restore access.

---

### Data Breach

Unauthorized access to confidential or sensitive information.

---

### DDoS (Distributed Denial of Service)

An attack that floods a server or website with traffic, making it unavailable to legitimate users.

---

### Insider Threat

Security threats caused by employees, contractors, or trusted individuals.

---

### Zero-Day Attack

An attack that exploits a software vulnerability before developers release a security patch.

---

### Social Engineering

Psychological manipulation used to trick users into revealing confidential information.

Examples:
- Phishing
- Baiting
- Pretexting
- Tailgating

---



# Security Objectives and CIA Triad

## A. Confidentiality

**Definition:**
Confidentiality ensures that sensitive information is accessible only to authorized users and is protected from unauthorized access.

**How it is achieved:**
- Passwords
- Multi-Factor Authentication (MFA)
- Encryption
- Access Control
- Biometric Authentication

**Example:**
Only you can access your Gmail account using your password and OTP.

---

## B. Integrity

**Definition:**
Integrity ensures that data remains accurate, complete, and is modified only by authorized users.

**How it is achieved:**
- Hashing
- Digital Signatures
- Checksums
- Access Permissions
- Version Control

**Example:**
When you transfer ₹5,000 through online banking, the amount should not be changed during the transaction.

---

## C. Availability

**Definition:**
Availability ensures that systems, applications, and data are accessible whenever authorized users need them.

**How it is achieved:**
- Regular Backups
- Redundant Servers
- UPS (Backup Power)
- Disaster Recovery
- Load Balancing

**Example:**
An ATM should be available 24/7 so customers can withdraw money whenever they need it.

---

## D. Real-World Example (ATM Banking System)

The ATM banking system is a great example of the CIA Triad.

### Confidentiality
Only the account owner can access the account using an ATM card and PIN.

### Integrity
The bank balance and transaction records remain accurate and cannot be altered by unauthorized users.

### Availability
The ATM and banking network should be available whenever customers need to withdraw cash.

---

## E. Security Objectives

Security objectives are the goals of protecting information and systems from unauthorized access, modification, or disruption. The primary security objectives are represented by the **CIA Triad**.

### Objectives
- **Confidentiality** – Protect sensitive information from unauthorized access.
- **Integrity** – Ensure data remains accurate and trustworthy.
- **Availability** – Ensure systems and data are accessible when needed.

### Why Security Objectives are Important
- Protect sensitive information
- Prevent unauthorized access
- Maintain data accuracy
- Ensure continuous business operations
- Build trust with users and customers
- Reduce the risk of cyber attacks

# Summary

Cybersecurity is essential for protecting digital systems, networks, applications, and sensitive information from cyber threats. Understanding cybersecurity fundamentals, security domains, and modern attack techniques provides a strong foundation for learning advanced cybersecurity concepts.

# Cybersecurity Basics

This document explains five fundamental cybersecurity concepts: **Threat, Vulnerability, Risk, Exploit, and Attack Vector**.

---

## 1. Threat

### Definition
A **threat** is any potential danger that can exploit a vulnerability to harm a system, network, application, or data.

### Examples
- Hacker
- Malware
- Ransomware
- Insider attack
- Natural disasters

---

## 2. Vulnerability

### Definition
A **vulnerability** is a weakness or flaw in a system, application, network, or device that attackers can exploit.

### Examples
- Weak passwords
- Outdated software
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Security misconfiguration

---

## 3. Risk

### Definition
A **risk** is the possibility that a threat will exploit a vulnerability and cause damage, data loss, or financial loss.

### Examples
- Data breach
- Financial loss
- Service disruption
- Reputation damage

---

## 4. Exploit

### Definition
An **exploit** is a tool, code, or technique used to take advantage of a vulnerability.

### Examples
- SQL Injection exploit
- Buffer Overflow exploit
- Remote Code Execution (RCE) exploit
- Zero-day exploit

---

## 5. Attack Vector

### Definition
An **attack vector** is the method or path an attacker uses to gain unauthorized access to a system.

### Examples
- Phishing email
- Malicious website
- USB device
- Open ports
- Weak passwords
- Remote Desktop Protocol (RDP)

---

# Relationship Between Them

```
Threat
   │
   ▼
Finds a Vulnerability
   │
   ▼
Uses an Exploit
   │
   ▼
Through an Attack Vector
   │
   ▼
Creates a Risk
```

---

# Quick Comparison

| Term | Meaning |
|------|---------|
| **Threat** | Potential danger that can cause harm. |
| **Vulnerability** | Weakness in a system. |
| **Risk** | Chance that a threat exploits a vulnerability. |
| **Exploit** | Tool or technique used to attack a vulnerability. |
| **Attack Vector** | Path or method used to launch an attack. |

---

# Real-World Example

- **Threat:** Hacker
- **Vulnerability:** Weak password
- **Exploit:** Password brute-force attack
- **Attack Vector:** Login page
- **Risk:** Unauthorized access and data theft



# Types of Attackers

## A. Script Kiddies

**Definition:**  
Script kiddies are inexperienced attackers who use ready-made hacking tools or scripts created by others instead of developing their own.

**Example:**  
A student downloads a password-cracking tool from the internet and tries to hack a friend's Wi-Fi without understanding how the tool works.

---

## B. Cyber Criminals

**Definition:**  
Cyber criminals are attackers who commit cybercrimes for financial gain by stealing money, personal information, or valuable data.

**Example:**  
A hacker sends fake bank emails (phishing) to steal users' login credentials and transfer money.

---

## C. Insider Threat

**Definition:**  
An insider threat is a trusted employee, contractor, or partner who intentionally or accidentally causes harm to an organization's systems or data.

**Example:**  
An employee copies confidential customer information and shares it with a competitor.

---

## D. Hacktivists

**Definition:**  
Hacktivists are attackers who hack systems to promote political, social, or ideological causes.

**Example:**  
A group hacks a government website and replaces the homepage with a protest message.

---

## E. Nation-State Actors

**Definition:**  
Nation-state actors are highly skilled hackers supported or sponsored by a government to conduct cyber espionage, sabotage, or cyber warfare.

**Example:**  
A government-backed hacking group targets another country's military or power grid to steal sensitive information.

---

# Interview Summary

| Attacker Type | Simple Definition |
|---------------|-------------------|
| Script Kiddies | Inexperienced hackers who use ready-made tools. |
| Cyber Criminals | Attackers who hack for financial gain. |
| Insider Threat | Trusted insiders who intentionally or accidentally cause harm. |
| Hacktivists | Hackers motivated by political or social causes. |
| Nation-State Actors | Government-backed hackers involved in espionage or cyber warfare. |
