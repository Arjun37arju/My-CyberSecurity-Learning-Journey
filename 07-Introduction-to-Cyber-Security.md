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



# Understand Web & Internet Security Basics

## Table of Contents

* [a. Surface Web](#a-surface-web)
* [b. Deep Web](#b-deep-web)
* [c. Dark Web](#c-dark-web)
* [d. Anonymous Browsing Concepts](#d-anonymous-browsing-concepts)
* [e. Online Privacy Awareness](#e-online-privacy-awareness)
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

Understanding common attack techniques is important for cybersecurity professionals.


# Understand Web & Internet Security Basics

Web and Internet security basics help us understand how the Internet is organized, how different types of web content work, how anonymous browsing works, and how to protect our personal information online.



---

## a. Surface Web

The **Surface Web** is the part of the Internet that is publicly accessible and can normally be found using search engines such as Google or Bing.

### Examples

* News websites
* Public blogs
* Company websites
* Public social media pages
* Wikipedia
* Public documentation

### How it works

Search engines crawl and index publicly available web pages. When we search for something, the search engine can show these indexed pages in the results.

**Example:**

```text
You → Google → Public Website
```

### Key Point

> **Surface Web = Public and searchable Internet content**

---

## b. Deep Web

The **Deep Web** refers to Internet content that is **not normally indexed by search engines**.

It does **not** mean that the content is illegal or dangerous. A large part of the Deep Web is simply private or login-protected information.

### Examples

* Online banking accounts
* Private email inboxes
* College/student portals
* Company databases
* Private cloud storage
* Content behind a login
* Private social media content

### Example

When you search Google, it normally cannot show the contents of your private Gmail inbox.

But after you log into Gmail, you can access your emails.

Therefore:

```text
Public Google results → Surface Web

Private Gmail inbox → Deep Web
```

### Key Point

> **Deep Web = Content that is not normally indexed by search engines**

---

## c. Dark Web

The **Dark Web** is a small part of the Deep Web that is intentionally hidden and generally requires special software or networks to access.

One commonly known technology used to access parts of the Dark Web is the **Tor network**.

### Legitimate uses

The Dark Web can be used for legitimate purposes such as:

* Protecting privacy
* Anonymous communication
* Journalism
* Whistleblowing
* Bypassing censorship

### Risks

The Dark Web is also associated with:

* Scams
* Stolen data
* Fraud
* Malware
* Illegal marketplaces
* Other criminal activities

### Deep Web vs Dark Web

```text
Internet
│
├── Surface Web
│   └── Publicly searchable websites
│
└── Deep Web
    ├── Private / login-protected content
    │
    └── Dark Web
        └── Intentionally hidden services
```

### Important

**Deep Web ≠ Dark Web**

The **Dark Web is only a small part of the Deep Web**.

### Key Point

> **Dark Web = Intentionally hidden Internet services that require special access methods**

---

## d. Anonymous Browsing Concepts

**Anonymous browsing** means using techniques that try to reduce the amount of information that can be linked to your identity or browsing activity.

It is important to understand that **anonymous browsing does not mean complete invisibility**.

### 1. IP Address Hiding

An IP address can provide information about the network you are connecting from and may reveal your approximate location.

Technologies such as **VPNs** and anonymity networks such as **Tor** can make it harder for websites to see your original IP address.

```text
Without VPN:

You → Website
      ↑
    Your IP


With VPN:

You → VPN → Website
           ↑
        VPN IP
```

### 2. Traffic Encryption

Encryption protects information while it travels between your device and another system.

For example, **HTTPS** encrypts communication between your browser and a website.

```text
Your Browser
     │
     │ Encrypted communication
     ▼
   Website
```

This makes it harder for someone monitoring the network to read the contents of the communication.

### 3. Cookies and Tracking

Websites can use cookies and other tracking technologies to remember users and understand their online activity.

Privacy can be improved by:

* Blocking unnecessary third-party cookies
* Limiting trackers
* Clearing browsing data
* Reviewing browser privacy settings

### 4. Browser Fingerprinting

Browser fingerprinting is a technique that can use characteristics of your browser and device to help distinguish you from other users.

Information may include:

* Browser type
* Operating system
* Screen characteristics
* Language settings
* Installed features

### Important Limitation

Anonymous browsing does **not** make you completely invisible.

You may still be identifiable through:

* Logging into personal accounts
* Cookies
* Browser fingerprinting
* Device information
* Information you voluntarily provide
* Other tracking techniques

### Key Point

> **Anonymous browsing = Reducing traceability, not becoming completely invisible**

---

## e. Online Privacy Awareness

**Online privacy awareness** means understanding what personal information you share online, who can access it, and how that information can be collected, stored, or used.

### Common Personal Information

* Name
* Phone number
* Email address
* Location
* Photos
* Search history
* Browsing activity
* Account information
* Device information

### Common Privacy Risks

| Risk                      | Example                                                  |
| ------------------------- | -------------------------------------------------------- |
| **Oversharing**           | Posting your home address publicly                       |
| **Tracking**              | Websites monitoring your browsing activity               |
| **Phishing**              | Fake websites trying to steal your credentials           |
| **Data Breach**           | A company's database being compromised                   |
| **Weak Passwords**        | Using the same password for multiple accounts            |
| **Excessive Permissions** | Giving an app access to information it doesn't need      |
| **Social Engineering**    | Manipulating someone into revealing personal information |

### Good Privacy Practices

1. Use **strong and unique passwords**.
2. Enable **MFA/2FA** whenever possible.
3. Review your **privacy settings**.
4. Give apps only the **permissions they need**.
5. Avoid publicly sharing sensitive personal information.
6. Be careful with suspicious links and attachments.
7. Keep your operating system, browser, and applications updated.
8. Be careful when using public Wi-Fi.
9. Understand cookies and online tracking.
10. Think before posting or sharing anything online.

---

## Quick Revision

| Topic                        | Simple Meaning                                    |
| ---------------------------- | ------------------------------------------------- |
| **Surface Web**              | Public and searchable Internet content            |
| **Deep Web**                 | Content not normally indexed by search engines    |
| **Dark Web**                 | Intentionally hidden Internet services            |
| **Anonymous Browsing**       | Techniques that reduce online traceability        |
| **Online Privacy Awareness** | Understanding and protecting personal information |

### Easy Way to Remember

```text
Surface → Searchable
Deep → Not normally searchable
Dark → Hidden
Anonymous Browsing → Reduce traceability
Privacy Awareness → Protect your information
```

---

## Conclusion

Understanding the Surface Web, Deep Web, and Dark Web helps us understand how different parts of the Internet work. Learning about anonymous browsing helps us understand online privacy and traceability, while privacy awareness helps us make safer decisions about the information we share online.

> **Think before you click, share, download, or trust.**

