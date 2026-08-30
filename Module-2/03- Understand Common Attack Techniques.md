# Understand Common Attack Techniques

Attack techniques are methods used by attackers to **gain unauthorized access, steal information, deliver malware, manipulate users, or gather information about a target**.

## Table of Contents

* [a. Phishing](#a-phishing)
* [b. Social Engineering](#b-social-engineering)
* [c. Credential Attacks](#c-credential-attacks)
* [d. Malware Delivery](#d-malware-delivery)
* [e. Reconnaissance Activities](#e-reconnaissance-activities)

---

## a. Phishing

### Content

**Phishing** is a technique where an attacker uses **fake messages, websites, or emails** to trick people into providing sensitive information or performing an unsafe action.

```text id="p7x4k2"
Attacker
   ↓
Fake Email / Message
   ↓
Victim
   ↓
Clicks Link / Opens Attachment
   ↓
Information or Access Compromised
```

Phishing can attempt to steal:

* Usernames
* Passwords
* Financial information
* Login credentials

Example:

> A victim receives an email that appears to come from a legitimate company and is asked to log in through a fake website.

**Easy idea:**

> **Phishing = Fake communication used to trick people.**

### Practical Task


### Deliverable

Create a **Phishing Analysis** containing:

```text
Attack:
Target:
Technique:
Attacker's Goal:
Warning Signs:
Prevention:
Source:
```

---

## b. Social Engineering

### Content

**Social engineering** is the use of **psychological manipulation or deception** to influence people into revealing information or performing actions that may compromise security.

Instead of directly attacking technology, attackers may target **human behavior**.

```text id="j8v2m5"
Attacker
   ↓
Manipulates Victim
   ↓
Victim Takes Action
   ↓
Security Is Compromised
```

Common examples include:

* Impersonation
* Pretexting
* Baiting
* Phishing
* Urgency-based scams

Example:

> Someone pretends to be an IT employee and asks a user for information needed to "fix" an account.

**Easy idea:**

> **Social Engineering = Manipulating people to bypass security.**

### Practical Task

Research a real-world social engineering incident.

Identify:

* Who was targeted
* What manipulation technique was used
* Why the victim trusted the attacker
* What information or access was targeted
* How the attack could have been prevented

### Deliverable

Create a **Social Engineering Case Study** explaining the attacker's manipulation method and the security lessons learned.

> Only analyze real examples or use simulated scenarios in your own lab. Do not attempt to manipulate real people.

---

## c. Credential Attacks

### Content

**Credential attacks** are techniques used to **obtain, guess, steal, or misuse usernames, passwords, or other authentication information**.

```text id="k3r7n1"
Credential
     ↓
Obtained / Guessed / Stolen
     ↓
Attacker
     ↓
Unauthorized Access
```

Examples include:

* Password guessing
* Credential stuffing
* Password spraying
* Phishing for credentials
* Using leaked credentials

Example:

> An attacker obtains credentials from a previous data breach and attempts to use the same username and password on another service.

**Easy idea:**

> **Credential Attack = Attempt to obtain or misuse authentication information.**

### Practical Task

Research a real-world credential attack.

Find out:

* What type of credential attack occurred
* How credentials were obtained
* What was targeted
* What was the impact
* How the attack was detected
* How it could have been prevented

### Deliverable

Create a **Credential Attack Analysis**.

Include:

| Item              | Findings |
| ----------------- | -------- |
| Attack Type       |          |
| Target            |          |
| Credential Source |          |
| Impact            |          |
| Detection         |          |
| Prevention        |          |

For practical learning, perform password-security exercises **only in your own authorized lab environment**.

---

## d. Malware Delivery

### Content

**Malware delivery** refers to the methods attackers use to **get malicious software onto a victim's device or environment**.

```text id="z5w8q2"
Attacker
   ↓
Delivery Method
   ↓
Victim
   ↓
Malware Reaches System
   ↓
Malware Executes
```

Common delivery methods can include:

* Malicious email attachments
* Malicious links
* Compromised websites
* Malicious downloads
* Infected files

Example:

> A victim receives a malicious attachment disguised as a legitimate document.

**Easy idea:**

> **Malware Delivery = How malicious software reaches a victim.**

### Practical Task

Research a real-world malware delivery campaign.

Identify:

* Delivery method
* Target
* Type of malware
* How the victim was tricked or exposed
* What happened after delivery
* How the delivery could have been prevented

### Deliverable

Create a **Malware Delivery Analysis**.

```text id="6u4n9p"
Delivery Method
      ↓
Initial Access
      ↓
Malware Execution
      ↓
Impact
      ↓
Prevention
```

For hands-on practice, use **safe simulated files or intentionally vulnerable lab environments** rather than real malware.

---

## e. Reconnaissance Activities

### Content

**Reconnaissance** is the process of **collecting information about a target before attempting further activity**.

Security professionals also use reconnaissance for authorized security assessments.

```text id="w2c7m9"
Target
  ↓
Information Gathering
  ↓
Analyze Information
  ↓
Understand Attack Surface
```

Information may include publicly available details such as:

* Domains
* Subdomains
* Public IP information
* Technologies
* Publicly available documents
* Organization information

Reconnaissance can be:

**Passive reconnaissance**

> Collecting information from publicly available sources without directly interacting with the target.

**Active reconnaissance**

> Interacting with a target to gather information, which should only be performed with proper authorization.

**Easy idea:**

> **Reconnaissance = Gathering information about a target.**

### Practical Task

Perform a **passive reconnaissance exercise** on an organization or domain that you own or are explicitly authorized to research.

Research publicly available information such as:

* Domain information
* Subdomains
* Technologies
* Public documents
* Publicly available organizational information

Organize your findings without attempting unauthorized access.

### Deliverable

Create a **Reconnaissance Report**:

```text id="x6m3v8"
Target:
Scope:
Information Found:
Domains:
Technologies:
Public Information:
Potential Attack Surface:
Sources:
```

**Goal:**

> Learn how information can be collected and organized during the reconnaissance phase of a security assessment.

---

# Final Practical Project

Choose a **fictional organization or an authorized lab environment** and create a report showing how the five attack techniques work at a high level.

```text id="q9k2s5"
Phishing
   ↓
Social Engineering
   ↓
Credential Attack
   ↓
Malware Delivery
   ↓
Reconnaissance
```

Do not perform attacks against real systems without explicit authorization.

### Final Comparison

| Attack Technique   | Main Purpose                 | Common Target           | Basic Defense                    |
| ------------------ | ---------------------------- | ----------------------- | -------------------------------- |
| Phishing           | Trick users                  | People / Accounts       | Awareness, email security        |
| Social Engineering | Manipulate people            | Users                   | Awareness, verification          |
| Credential Attacks | Obtain or misuse credentials | Accounts                | MFA, strong passwords            |
| Malware Delivery   | Deliver malicious software   | Devices                 | Security controls, safe browsing |
| Reconnaissance     | Gather information           | Organizations / Systems | Minimize public exposure         |

### Final Deliverable

Create a GitHub project:

```text id="t8p4w1"
Common-Attack-Techniques/
│
├── README.md
├── phishing.md
├── social-engineering.md
├── credential-attacks.md
├── malware-delivery.md
├── reconnaissance.md
└── comparison.md
```

### Expected Result

After completing this project, you should be able to:

* Explain common attack techniques
* Analyze real-world attack examples
* Identify how attackers target people and systems
* Understand common attack stages at a high level
* Identify basic defensive measures
* Perform safe, authorized reconnaissance
* Document your research professionally

> **Learn → Research → Analyze → Practice Safely → Document**
