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

# AI-Assisted Security Research

**AI-Assisted Security Research** means using Artificial Intelligence (AI) tools to help security professionals **analyze information, research threats, understand vulnerabilities, summarize security news, and assess risks**.

AI can make security research faster, but its output should **always be reviewed and validated by a human**.

## Table of Contents

* [a. Use AI For](#a-use-ai-for)

  * [i. Threat Analysis](#i-threat-analysis)
  * [ii. Malware Research](#ii-malware-research)
  * [iii. Security News Summarization](#iii-security-news-summarization)
  * [iv. CVE Analysis](#iv-cve-analysis)
  * [v. Risk Assessments](#v-risk-assessments)
* [b. Validate Outputs](#b-validate-outputs)

  * [i. Verify Findings](#i-verify-findings)
  * [ii. Confirm Technical Details](#ii-confirm-technical-details)
  * [iii. Review Threat Information](#iii-review-threat-information)

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




# AI-Assisted Security Research



# a. Use AI For

AI can assist security researchers with many tasks. It is especially useful when dealing with **large amounts of technical information**.

---

## i. Threat Analysis

**Threat analysis** is the process of studying potential threats to understand how they work, what they target, and what risks they create.

AI can help analyze:

* Threat reports
* Attack techniques
* Threat actor information
* Indicators of compromise (IOCs)
* Attack patterns
* Security incidents
* Tactics, Techniques, and Procedures (TTPs)

### Example

A security researcher provides a threat report to an AI tool and asks it to identify:

```text
Threat Actor
     ↓
Target
     ↓
Attack Technique
     ↓
Indicators
     ↓
Potential Impact
     ↓
Recommended Defenses
```

AI can help organize the information and highlight important findings.

### Important

AI-generated threat analysis should be checked against **trusted security sources** before being treated as accurate.

### Key Point

> **AI can help organize and analyze threat information faster, but the findings must be verified.**

---

## ii. Malware Research

AI can assist with **malware research** by helping researchers understand malware behavior and technical reports.

AI can help with:

* Explaining malware terminology
* Summarizing malware reports
* Identifying observed behaviors
* Organizing Indicators of Compromise (IOCs)
* Comparing malware families
* Explaining defensive techniques
* Mapping behaviors to security frameworks

### Example

A researcher has a technical malware report.

Instead of reading hundreds of lines immediately, AI can help organize the report:

```text
Malware
   ↓
Delivery Method
   ↓
Execution
   ↓
Persistence
   ↓
Behavior
   ↓
Indicators
   ↓
Detection Opportunities
```

The researcher can then manually verify the important technical details.

### Key Point

> **AI can help researchers understand and organize malware information, but it should not replace technical analysis and verification.**

---

## iii. Security News Summarization

Cybersecurity produces a large amount of information every day.

AI can help summarize:

* Security news
* Data breach reports
* Vulnerability announcements
* Threat intelligence reports
* Vendor security advisories
* Incident reports

### Example

Instead of reading several long security articles, AI can create a structured summary:

```text
Title
  ↓
What happened?
  ↓
Who is affected?
  ↓
What vulnerability or threat was involved?
  ↓
Impact
  ↓
Recommended action
```

### Benefits

* Saves time
* Reduces information overload
* Makes long reports easier to understand
* Helps identify important developments quickly

### Important

AI summaries can leave out important context or contain incorrect information.

Always check the **original article or official advisory** for important claims.

### Key Point

> **Use AI to summarize security news, but verify important information using the original source.**

---

## iv. CVE Analysis

AI can help security professionals analyze **CVE (Common Vulnerabilities and Exposures)** information.

AI can help explain:

* What the vulnerability is
* What software is affected
* How the vulnerability works at a high level
* CVSS severity
* Potential impact
* Affected versions
* Available patches or mitigations
* Whether additional investigation is required

### Example

```text
CVE
 ↓
Affected Product
 ↓
Vulnerability Type
 ↓
Severity
 ↓
Potential Impact
 ↓
Affected Systems
 ↓
Patch / Mitigation
```

### Example Research Questions

A researcher could ask AI:

> "Explain this CVE in simple terms."

> "What systems could be affected by this vulnerability?"

> "What factors should I consider when prioritizing this CVE?"

AI can help explain the information, but the researcher should confirm it using authoritative vulnerability databases, vendor advisories, and other trusted sources.

### Key Point

> **AI can simplify CVE research, but vulnerability details should be confirmed using reliable sources.**

---

## v. Risk Assessments

A **risk assessment** identifies potential security risks and evaluates their likelihood and impact.

AI can help organize risk assessments by considering:

* Threats
* Vulnerabilities
* Assets
* Potential impact
* Likelihood
* Existing security controls
* Possible mitigations

### Simple Risk Model

```text
Threat
  +
Vulnerability
  +
Asset
  ↓
Potential Risk
  ↓
Impact + Likelihood
  ↓
Risk Assessment
  ↓
Mitigation
```

### Example

Suppose an organization has a critical Internet-facing server with a known vulnerability.

AI can help organize the assessment:

| Factor            | Example                                   |
| ----------------- | ----------------------------------------- |
| **Asset**         | Internet-facing server                    |
| **Vulnerability** | Known security weakness                   |
| **Threat**        | Potential attacker exploitation           |
| **Impact**        | Service disruption or unauthorized access |
| **Likelihood**    | Depends on exposure and exploitability    |
| **Risk**          | Potentially high                          |
| **Mitigation**    | Patch, configuration changes, monitoring  |

### Key Point

> **AI can help structure risk assessments, but the final risk decision should consider the organization's actual environment and business context.**

---

# b. Validate Outputs

AI is useful, but it can produce **incorrect, outdated, incomplete, or misleading information**.

This is why security professionals should always validate AI-generated results.

```text
AI Output
    ↓
Human Review
    ↓
Verify Sources
    ↓
Check Technical Details
    ↓
Confirm Threat Information
    ↓
Final Finding
```

---

## i. Verify Findings

When AI produces a security finding, do not immediately assume it is correct.

Check:

* Where did the information come from?
* Is the source reliable?
* Is the information current?
* Can the finding be reproduced or confirmed?
* Do other trusted sources support it?

### Example

AI says:

> "This vulnerability affects version X."

The researcher should check:

```text
AI Finding
    ↓
Vendor Advisory
    ↓
CVE Database
    ↓
Security Research
    ↓
Confirmed Finding
```

### Key Point

> **Never treat an AI-generated security finding as confirmed until it has been verified.**

---

## ii. Confirm Technical Details

Security research often involves highly technical information.

AI can make mistakes involving:

* CVE numbers
* Software versions
* Vulnerability types
* Network protocols
* Attack techniques
* Malware behavior
* Security configurations
* Commands or technical procedures

### Example

If AI says:

> "CVE-XXXX affects version 2.1."

The researcher should verify:

1. The CVE identifier.
2. The affected product.
3. The affected versions.
4. The vulnerability description.
5. The official vendor information.

### Key Point

> **Technical details should be confirmed using authoritative documentation and trusted security sources.**

---

## iii. Review Threat Information

Threat intelligence changes quickly.

A threat actor may change:

* Infrastructure
* Malware
* Attack techniques
* Domains
* IP addresses
* Delivery methods
* Campaigns

Therefore, AI-generated threat information may become outdated.

### Review Process

```text
AI Threat Information
         ↓
Check Source
         ↓
Check Date
         ↓
Compare Multiple Sources
         ↓
Analyze Context
         ↓
Confirm Finding
```

### Questions to Ask

Before accepting threat information, ask:

* Is the information recent?
* What is the original source?
* Is the source trustworthy?
* Has another security organization reported the same information?
* Is the information relevant to my environment?
* Could the information be outdated?

### Key Point

> **Threat information should be reviewed for accuracy, reliability, relevance, and freshness.**

---

# AI-Assisted Security Research Workflow

A practical workflow can look like this:

```text
                 Security Data
                      ↓
                  AI Analysis
                      ↓
              AI-Generated Findings
                      ↓
                Human Review
                      ↓
              Source Verification
                      ↓
          Technical Detail Validation
                      ↓
             Threat Information Review
                      ↓
               Final Conclusion
```

The most important principle is:

> **AI assists the researcher; it does not replace the researcher.**

---

# AI vs Human Responsibilities

| Task                   | AI Can Help With                  | Human Should                           |
| ---------------------- | --------------------------------- | -------------------------------------- |
| **Threat Analysis**    | Organize and summarize threats    | Verify findings and context            |
| **Malware Research**   | Explain and organize reports      | Confirm technical behavior             |
| **News Summarization** | Summarize long articles           | Check original sources                 |
| **CVE Analysis**       | Explain vulnerability information | Confirm affected versions and severity |
| **Risk Assessment**    | Structure risk information        | Make the final risk decision           |
| **Validation**         | Identify information to check     | Verify and approve findings            |

---

# Common Risks of Using AI in Security Research

AI-assisted research also has limitations.

### 1. Hallucinations

AI may generate information that sounds correct but is actually false.

### 2. Outdated Information

AI may not always have the latest information about a vulnerability or threat.

### 3. Incorrect Technical Details

AI can sometimes confuse:

* CVE identifiers
* Versions
* Commands
* Vulnerability types
* Attack techniques

### 4. Missing Context

A summary may leave out important details from the original report.

### 5. False Confidence

A well-written AI response can appear authoritative even when it is incorrect.

### Key Point

> **The more important the security decision, the more important human verification becomes.**

---

# Quick Revision

| Topic                         | Simple Meaning                                                |
| ----------------------------- | ------------------------------------------------------------- |
| **Threat Analysis**           | Use AI to organize and analyze threat information             |
| **Malware Research**          | Use AI to understand and organize malware research            |
| **Security News**             | Use AI to summarize security news and reports                 |
| **CVE Analysis**              | Use AI to understand and analyze vulnerability information    |
| **Risk Assessment**           | Use AI to organize threats, vulnerabilities, impact, and risk |
| **Verify Findings**           | Check AI results against reliable sources                     |
| **Confirm Technical Details** | Verify technical claims and specifications                    |
| **Review Threat Information** | Check threat information for accuracy, context, and freshness |

## Easy Way to Remember

```text
AI Security Research
        ↓
Analyze
        ↓
Summarize
        ↓
Explain
        ↓
Assess
        ↓
        VALIDATE
        ↓
Verify Findings
        ↓
Confirm Technical Details
        ↓
Review Threat Information
        ↓
Final Decision
```

## Conclusion

AI can significantly improve the speed and efficiency of cybersecurity research. It can help with **threat analysis, malware research, security news summarization, CVE analysis, and risk assessments**.

However, AI should be treated as an **assistant rather than an authoritative source**. Security professionals must verify findings, confirm technical details, and review threat information before using AI-generated results for security decisions.

> **Use AI to research faster — validate to research correctly.**
