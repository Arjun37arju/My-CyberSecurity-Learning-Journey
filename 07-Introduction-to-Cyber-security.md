# Understand Common Attack Techniques

## Table of Contents

- [Introduction](#introduction)
- [1. Phishing](#1-phishing)
- [2. Social Engineering](#2-social-engineering)
- [3. Credential Attacks](#3-credential-attacks)
- [4. Malware Delivery](#4-malware-delivery)
- [5. Reconnaissance Activities](#5-reconnaissance-activities)
- [How They Are Connected](#how-they-are-connected)
- [Conclusion](#conclusion)

---

## Introduction

Cyber attacks use different techniques to trick users, steal information, or gain unauthorized access.

Attackers may first collect information about a target and then use phishing, social engineering, credential attacks, or malware to compromise the system.

The main techniques are **Phishing, Social Engineering, Credential Attacks, Malware Delivery, and Reconnaissance Activities.**

---

## 1. Phishing

**Phishing** is a technique where an attacker pretends to be a trusted person or organization to trick a victim into sharing sensitive information or clicking a malicious link.

For example, a victim may receive an email saying:

> Your account will be blocked. Click here to verify your account.

The link may lead to a fake login page designed to steal the user's username and password.

### Common Types

- **Email Phishing** – Fake emails sent to victims.
- **Spear Phishing** – A targeted attack against a specific person or organization.
- **Smishing** – Phishing through SMS.
- **Vishing** – Phishing through phone calls.

### Protection

- Check the sender and URL carefully.
- Avoid clicking unknown links.
- Don't open unexpected attachments.
- Use MFA.
- Verify suspicious requests through official channels.

---

## 2. Social Engineering

**Social engineering** is the use of psychological manipulation to trick people into giving information or performing an action that helps an attacker.

For example, an attacker may pretend to be an IT employee and say:

> Your account has a security issue. Please provide your password so I can fix it.

The attacker is not technically hacking the system. Instead, they are manipulating the person.

### Common Techniques

- **Pretexting** – Creating a believable story to obtain information.
- **Baiting** – Offering something attractive to make a victim perform an unsafe action.
- **Impersonation** – Pretending to be someone trustworthy.
- **Tailgating** – Following an authorized person into a restricted area.

### Protection

- Verify someone's identity before sharing information.
- Never share passwords.
- Be careful with urgent requests.
- Follow company security procedures.
- Don't allow unknown people into restricted areas.

---

## 3. Credential Attacks

**Credential attacks** are attempts to steal or abuse usernames, passwords, authentication tokens, or other login information.

### Common Techniques

- **Brute Force** – Trying many possible passwords until the correct one is found.
- **Password Spraying** – Trying one common password against many accounts.
- **Credential Stuffing** – Using stolen username and password combinations from one service on another service.
- **Keylogging** – Recording the keys typed by a user to capture sensitive information.

For example, if someone uses the same password on multiple websites and one website is breached, attackers may try the same password on other accounts.

### Protection

- Use strong and unique passwords.
- Enable MFA.
- Never reuse passwords.
- Use a password manager.
- Monitor unusual login attempts.
- Use rate limiting and account protection.

---

## 4. Malware Delivery

**Malware delivery** is the process of getting malicious software onto a victim's device.

Malware can include:

- Viruses
- Worms
- Trojans
- Ransomware
- Spyware
- Keyloggers

### Common Delivery Methods

- Malicious email attachments
- Malicious links
- Fake software
- Compromised websites
- Infected USB devices

For example, an attacker may send a file named:

`Invoice.pdf.exe`

It may look like a normal document, but it could actually execute malicious software.

### Protection

- Keep systems and applications updated.
- Use endpoint protection.
- Download software from trusted sources.
- Avoid pirated or cracked software.
- Don't open unexpected attachments.
- Maintain regular backups.

---

## 5. Reconnaissance Activities

**Reconnaissance** is the information-gathering stage of a cyber attack.

Attackers may collect information about:

- Domains
- Subdomains
- IP addresses
- Technologies
- DNS information
- Public documents
- Employees
- Publicly exposed services

Think of reconnaissance as **learning about the target before making a move**.

Reconnaissance can be:

- **Passive Reconnaissance** – Gathering information without directly interacting with the target.
- **Active Reconnaissance** – Directly interacting with the target's systems.

> Always perform reconnaissance only on systems you own or have explicit permission to test.

### Subdomain Finding

Subdomain finding is used to discover subdomains connected to a main domain.

For example:

```text
example.com
www.example.com
mail.example.com
learn.example.com
dev.example.com
