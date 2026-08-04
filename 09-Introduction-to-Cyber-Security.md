# Understand OSINT Fundamentals

**OSINT (Open-Source Intelligence)** is the process of collecting, analyzing, and using information that is **legally available from public or authorized sources**.

OSINT is widely used in cybersecurity, threat intelligence, journalism, investigations, and security research.

The goal is not simply to collect information, but to **turn publicly available information into useful intelligence**.

## Table of Contents

* [a. Open-Source Intelligence](#a-open-source-intelligence)
* [b. Public Information Gathering](#b-public-information-gathering)
* [c. Search Techniques](#c-search-techniques)
* [d. Threat Research](#d-threat-research)
* [e. Investigation Workflows](#e-investigation-workflows)

---

## a. Open-Source Intelligence

**Open-Source Intelligence (OSINT)** is intelligence produced by collecting and analyzing information from publicly available sources.

The word **"open-source"** here means information that is publicly accessible. It does **not** mean open-source software.

### Common OSINT Sources

* Search engines
* Public websites
* News websites
* Social media
* Public reports
* Government websites
* Security advisories
* Public databases
* Technical documentation
* Public code repositories
* Domain and DNS information

### OSINT Process

```text
Public Information
       ↓
   Collection
       ↓
    Analysis
       ↓
   Verification
       ↓
   Intelligence
```

### Example

Suppose a security researcher wants to understand a company's public attack surface.

They may research:

```text
Company
  ↓
Official website
  ↓
Public domains
  ↓
Public technologies
  ↓
Security information
  ↓
Potential exposure
```

The researcher is not automatically attacking the company. They are **collecting and analyzing publicly available information**.

### Key Point

> **OSINT = Collect + Analyze + Verify publicly available information.**

---

## b. Public Information Gathering

**Public information gathering** means collecting relevant information from publicly accessible sources.

The first step is to define **what information you actually need**.

### Types of Information

#### 1. Organization Information

* Company name
* Official domains
* Public websites
* Business locations
* Public contact information
* Public technology information

#### 2. Technical Information

* Domain names
* DNS records
* Public IP information
* Technologies used by websites
* Public security advisories
* Public documentation

#### 3. Threat Information

* Known malware
* Threat actors
* Indicators of compromise
* Vulnerabilities
* Attack techniques
* Security reports

### Important Principle

Only collect information that is:

* Publicly available
* Relevant to your investigation
* Legally accessible
* Appropriate for your purpose

### Avoid

OSINT should not involve:

* Unauthorized account access
* Password theft
* Bypassing authentication
* Exploiting systems
* Obtaining private information illegally

### Key Point

> **OSINT focuses on publicly available information, not unauthorized access.**

---

## c. Search Techniques

Good search skills are one of the most important parts of OSINT.

Instead of making very broad searches, investigators use **specific keywords and search operators** to find relevant information.

### 1. Exact Phrase Search

Use quotation marks to search for an exact phrase.

```text
"cyber security analyst"
```

This can help find pages containing the exact phrase.

### 2. Site Search

The `site:` operator limits results to a particular website or domain.

```text
site:example.com security
```

This can help locate security-related pages on a specific domain.

### 3. File Type Search

The `filetype:` operator can help locate specific document types.

```text
filetype:pdf cybersecurity report
```

For example, this can help find publicly available PDF reports.

### 4. Excluding Terms

The `-` operator can exclude a term from search results.

```text
cybersecurity -course
```

This can reduce results related to courses.

### 5. Combining Search Operators

Search operators can be combined to make searches more precise.

```text
site:example.com "security policy" filetype:pdf
```

### 6. Search Multiple Sources

Do not depend on a single search engine or website.

Compare information from:

* Search engines
* Official websites
* Security advisories
* News sources
* Technical reports
* Public databases

### Verify Information

Search results are not automatically trustworthy.

Before using information:

```text
Find
 ↓
Check source
 ↓
Compare with other sources
 ↓
Verify
 ↓
Use
```

### Key Point

> **Good OSINT searching is about finding the right information, not simply finding more information.**

---

## d. Threat Research

**Threat research** involves studying cybersecurity threats to understand how attackers operate and how organizations can defend against them.

### What Can Be Studied?

* Malware
* Vulnerabilities
* Threat actors
* Attack techniques
* Campaigns
* Indicators of compromise
* Exploitation methods
* Security incidents

### Example

Suppose a security team wants to understand a particular malware family.

They may research:

```text
Malware
   ↓
Who uses it?
   ↓
How is it delivered?
   ↓
What systems does it target?
   ↓
What behavior does it show?
   ↓
What indicators are available?
   ↓
How can defenders detect it?
```

### Common Threat Intelligence Information

#### Indicators of Compromise (IOCs)

Examples include:

* Malicious IP addresses
* Malicious domains
* File hashes
* Suspicious URLs
* Malware filenames

#### Tactics, Techniques, and Procedures (TTPs)

These describe how attackers operate.

For example:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Exfiltration
```

Security teams can use frameworks such as **MITRE ATT&CK** to understand and categorize adversary techniques.

### Important

Threat research should be performed for **defensive and authorized purposes**.

### Key Point

> **Threat research = Study threats to understand, detect, and defend against them.**

---

## e. Investigation Workflows

An **OSINT investigation workflow** is a structured process used to collect, verify, analyze, and document information.

A good workflow helps prevent random searching and keeps the investigation organized.

### Basic OSINT Workflow

```text
1. Define Objective
        ↓
2. Identify Sources
        ↓
3. Collect Information
        ↓
4. Organize Data
        ↓
5. Verify Information
        ↓
6. Analyze
        ↓
7. Document Findings
        ↓
8. Review Conclusions
```

### 1. Define the Objective

First determine what you are trying to discover.

Example:

> "Identify publicly exposed information about an organization's web presence."

### 2. Identify Sources

Determine which public sources may contain useful information.

Examples:

* Official websites
* Search engines
* Security databases
* Public reports
* Public repositories

### 3. Collect Information

Gather relevant information while recording where each piece of information came from.

### 4. Organize Data

Keep information structured.

For example:

| Information       | Source               | Verified? |
| ----------------- | -------------------- | --------- |
| Domain            | Public website       | Yes       |
| Technology        | Public documentation | Yes       |
| Security advisory | Security database    | Yes       |

### 5. Verify Information

Cross-check important findings with reliable sources.

```text
Source A
   │
   ├──── Compare ──── Source B
   │
   └──── Compare ──── Source C
              ↓
          Verified Finding
```

### 6. Analyze

Look for:

* Connections
* Patterns
* Relationships
* Security risks
* Inconsistencies
* Important findings

### 7. Document Findings

Record:

* What was discovered
* Where it was found
* When it was found
* How it was verified
* Why it matters

### 8. Review Conclusions

Before finalizing an investigation, ask:

* Is the information accurate?
* Is the source reliable?
* Could the information be outdated?
* Did I make assumptions?
* Can the finding be independently verified?

### Key Point

> **A good OSINT investigation is structured, evidence-based, and repeatable.**

---

## OSINT Investigation Example

Imagine you are performing authorized research on a company's public security posture.

```text
Objective
   ↓
Identify official domains
   ↓
Research public websites
   ↓
Review DNS / public technical information
   ↓
Search public security reports
   ↓
Check known vulnerabilities
   ↓
Verify findings
   ↓
Document results
   ↓
Create security recommendations
```

The focus is on **information gathering and analysis**, not unauthorized exploitation.

---

## OSINT vs Intelligence

These terms are related but slightly different.

| Term             | Meaning                                                 |
| ---------------- | ------------------------------------------------------- |
| **Data**         | Raw information collected from sources                  |
| **Information**  | Organized or processed data                             |
| **Intelligence** | Analyzed information that provides useful understanding |
| **OSINT**        | Intelligence created from publicly available sources    |

### Simple Example

```text
Public Website
      ↓
Raw Information
      ↓
Collect & Organize
      ↓
Analyze & Verify
      ↓
Useful Intelligence
```

---

## Quick Revision

| Topic                            | Simple Meaning                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------- |
| **Open-Source Intelligence**     | Intelligence created from publicly available information                               |
| **Public Information Gathering** | Collecting relevant information from public sources                                    |
| **Search Techniques**            | Methods used to find information efficiently                                           |
| **Threat Research**              | Studying threats, attackers, vulnerabilities, and techniques                           |
| **Investigation Workflows**      | A structured process for collecting, verifying, analyzing, and documenting information |

### Easy Way to Remember

```text
OSINT → Collect + Analyze + Verify

Public Gathering → Find public information

Search Techniques → Search smarter

Threat Research → Understand threats

Investigation → Objective → Collect → Verify → Analyze → Document
```

## Conclusion

OSINT is an important cybersecurity skill because security professionals often need to understand what information is publicly available about organizations, technologies, threats, and vulnerabilities.

By learning **public information gathering, search techniques, threat research, and investigation workflows**, you can perform more organized and reliable security research while staying within legal and ethical boundaries.

> **Good OSINT is not about collecting everything — it is about finding relevant information, verifying it, and turning it into useful intelligence.**
