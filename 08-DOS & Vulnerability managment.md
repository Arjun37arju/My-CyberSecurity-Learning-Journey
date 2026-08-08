# Understand Denial of Service Attacks

Denial of Service attacks are attacks that try to make a **website, server, application, or network unavailable or difficult to access** for legitimate users.

The main goal is usually to consume the target's resources such as **bandwidth, CPU, memory, connections, or application resources**.

## Table of Contents

* [a. DoS Attacks](#a-dos-attacks)
* [b. DDoS Attacks](#b-ddos-attacks)
* [c. Botnets](#c-botnets)
* [d. Attack Impact](#d-attack-impact)
* [e. Mitigation Approaches](#e-mitigation-approaches)

---


# Understand Vulnerability Management

**Vulnerability Management** is the continuous process of **identifying, evaluating, prioritizing, fixing, and monitoring security vulnerabilities** in systems, applications, networks, and devices.

The goal is to reduce the risk that vulnerabilities can be exploited by attackers.

## Table of Contents

* [a. Vulnerability Lifecycle](#a-vulnerability-lifecycle)
* [b. CVEs](#b-cves)
* [c. Severity Ratings](#c-severity-ratings)
* [d. Patch Management](#d-patch-management)
* [e. Risk Prioritization](#e-risk-prioritization)

  ---
## a. DoS Attacks

**DoS (Denial of Service)** is an attack where an attacker attempts to make a service unavailable to legitimate users.

The attacker sends excessive or specially crafted requests to a target. If the target cannot handle the traffic or requests, its resources may become exhausted.

### Simple Example

Imagine a small shop that can serve **10 customers at a time**.

If hundreds of fake customers continuously occupy the shop without buying anything, real customers cannot enter or get service.

The same basic idea can happen with a server:

```text
Attacker
   │
   │ Large number of requests
   ▼
Server
   │
   ├── Resources consumed
   ├── Performance decreases
   └── Legitimate users cannot access service
```

### Common DoS Categories

* **Network attacks** – Attempt to overwhelm network resources.
* **Protocol attacks** – Abuse weaknesses in network protocols.
* **Application-layer attacks** – Target applications or web servers with large numbers of requests.

### Effects of a DoS Attack

* Website becomes slow
* Server may stop responding
* Users cannot access services
* Network resources become exhausted
* Business operations may be interrupted

### Key Point

> **DoS = Trying to make a service unavailable by overwhelming or exhausting its resources.**

---

## b. DDoS Attacks

**DDoS (Distributed Denial of Service)** is similar to a DoS attack, but the attack traffic comes from **many different systems** instead of a single source.

```text
             ┌── Device 1 ──┐
             ├── Device 2 ──┤
             ├── Device 3 ──┤
             ├── Device 4 ──┤
             └── Device 5 ──┘
                     │
                     ▼
                  Target
```

Because the traffic comes from many sources, DDoS attacks can be much larger and harder to block using simple source-based filtering.

### DoS vs DDoS

| Feature    | DoS                            | DDoS                             |
| ---------- | ------------------------------ | -------------------------------- |
| Full Form  | Denial of Service              | Distributed Denial of Service    |
| Sources    | Usually one or limited sources | Many distributed sources         |
| Scale      | Usually smaller                | Can be very large                |
| Detection  | Often easier                   | Can be more difficult            |
| Mitigation | Relatively simpler             | Often requires multiple defenses |

### Key Point

> **DoS = One/few sources**
> **DDoS = Many distributed sources**

---

## c. Botnets

A **botnet** is a group of compromised devices that are controlled by an attacker.

These devices may include:

* Computers
* Servers
* Smartphones
* Routers
* IoT devices

The owner of the device may not even know that their device has been compromised.

### How a Botnet Can Be Used

```text
                Attacker
                   │
                   ▼
             Botnet Control
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
    Device 1    Device 2    Device 3
       │           │           │
       └───────────┼───────────┘
                   ▼
                 Target
```

During a DDoS attack, compromised devices can be instructed to send traffic or requests toward a target.

### How Devices Become Part of Botnets

Devices can become compromised through:

* Malware
* Weak or default passwords
* Unpatched software
* Vulnerable services
* Phishing
* Poorly secured IoT devices

### Key Point

> **Botnet = A network of compromised devices controlled by an attacker.**

---

## d. Attack Impact

A successful DoS or DDoS attack can cause significant technical and business problems.

### 1. Service Downtime

The website or application may become unavailable.

```text
Normal:

User → Website → Response ✓


During Attack:

Users → Website
          ↓
     Overloaded
          ↓
    No Response ✗
```

### 2. Performance Problems

Even if the service does not completely go offline, it may become extremely slow.

### 3. Financial Loss

Organizations may lose money because customers cannot use their services.

For example:

* Online stores may lose sales.
* Banking services may become unavailable.
* Businesses may lose customers.

### 4. Reputation Damage

Frequent outages can reduce customer trust in an organization.

### 5. Operational Disruption

Employees may be unable to access important applications, systems, or network resources.

### 6. Security Team Workload

Security and IT teams may need to spend significant time:

* Investigating the attack
* Filtering malicious traffic
* Restoring services
* Monitoring infrastructure

### Key Point

> **DDoS impact is not only technical; it can also affect money, reputation, customers, and business operations.**

---

## e. Mitigation Approaches

**DDoS mitigation** means using security controls and infrastructure to detect, absorb, filter, or reduce malicious traffic.

There is no single solution that works for every attack. Organizations usually use **multiple layers of protection**.

### 1. Traffic Monitoring

Monitor network traffic to identify unusual increases or suspicious patterns.

```text
Normal Traffic
      │
      ▼
 Monitoring
      │
      ├── Normal → Allow
      │
      └── Suspicious → Investigate / Filter
```

### 2. Rate Limiting

Rate limiting controls how many requests a user, IP address, or client can make within a specific period.

This helps prevent systems from being overwhelmed by excessive requests.

### 3. Firewalls

Firewalls can filter traffic according to predefined security rules.

They can help block known malicious or unwanted traffic.

### 4. Web Application Firewall (WAF)

A **WAF** protects web applications by inspecting HTTP/HTTPS traffic and blocking suspicious requests.

It can help protect against certain application-layer attacks.

### 5. Load Balancing

Load balancers distribute traffic across multiple servers.

```text
              Users
                │
                ▼
          Load Balancer
          /      |      \
         ▼       ▼       ▼
      Server 1 Server 2 Server 3
```

This can improve availability and prevent a single server from becoming a bottleneck.

### 6. CDN

A **Content Delivery Network (CDN)** distributes content across multiple locations.

CDNs can help absorb and distribute large amounts of traffic before it reaches the origin server.

### 7. DDoS Protection Services

Organizations can use specialized DDoS protection services that detect and filter malicious traffic before it reaches their infrastructure.

### 8. Redundancy

Having multiple servers, network paths, and infrastructure components can improve availability when one system becomes overloaded or unavailable.

### 9. Incident Response Plan

Organizations should have a predefined plan for responding to DDoS attacks.

The plan can include:

* Who should be contacted
* How traffic should be analyzed
* Which systems should be protected first
* How services should be restored
* How the incident should be documented

---

## DoS/DDoS Attack Flow

```text
                Attacker
                   │
                   ▼
             Attack Source
                   │
          ┌────────┴────────┐
          │                 │
        DoS               DDoS
     Single source     Many sources
          │                 │
          └────────┬────────┘
                   ▼
                 Target
                   │
                   ▼
          Resources exhausted
                   │
                   ▼
       Service becomes slow/unavailable
```

---

## Quick Revision

| Topic             | Simple Meaning                                                                         |
| ----------------- | -------------------------------------------------------------------------------------- |
| **DoS**           | Attempts to make a service unavailable by overwhelming or exhausting resources         |
| **DDoS**          | A DoS attack using many distributed sources                                            |
| **Botnet**        | A group of compromised devices controlled by an attacker                               |
| **Attack Impact** | Downtime, slow services, financial loss, reputation damage, and operational disruption |
| **Mitigation**    | Techniques used to detect, filter, absorb, and reduce malicious traffic                |

### Easy Way to Remember

```text
DoS → One/Few Sources
DDoS → Many Sources
Botnet → Compromised Devices
Impact → Service Disruption
Mitigation → Detect + Filter + Absorb + Recover
```

## Conclusion

DoS and DDoS attacks focus on **availability**. Instead of trying to steal information directly, attackers attempt to prevent legitimate users from accessing a service.

Understanding **DoS, DDoS, botnets, attack impact, and mitigation techniques** is important for cybersecurity because availability is one of the three main goals of the **CIA Triad**:

```text
C → Confidentiality
I → Integrity
A → Availability
```

> **DDoS attacks target Availability — the "A" in the CIA Triad.**


# Understand Vulnerability Management

**Vulnerability Management** is the continuous process of **identifying, evaluating, prioritizing, fixing, and monitoring security vulnerabilities** in systems, applications, networks, and devices.

The goal is to reduce the risk that vulnerabilities can be exploited by attackers.

## Table of Contents

* [a. Vulnerability Lifecycle](#a-vulnerability-lifecycle)
* [b. CVEs](#b-cves)
* [c. Severity Ratings](#c-severity-ratings)
* [d. Patch Management](#d-patch-management)
* [e. Risk Prioritization](#e-risk-prioritization)

---

## a. Vulnerability Lifecycle

The **vulnerability lifecycle** describes the different stages involved in managing a vulnerability from discovery to resolution and continuous monitoring.

### Main Stages

```text
Discovery
    ↓
Assessment
    ↓
Prioritization
    ↓
Remediation
    ↓
Verification
    ↓
Continuous Monitoring
    ↺
```

### 1. Discovery

Identify vulnerabilities in:

* Operating systems
* Applications
* Websites
* Networks
* Servers
* Cloud environments
* Hardware and IoT devices

Tools such as vulnerability scanners can help discover security weaknesses.

### 2. Assessment

After discovering a vulnerability, security teams analyze:

* What is affected?
* How serious is it?
* Can it be exploited?
* What systems are exposed?
* What could happen if it is exploited?

### 3. Prioritization

Not every vulnerability needs to be fixed at the same time.

Security teams prioritize vulnerabilities based on factors such as:

* Severity
* Exploitability
* Asset importance
* Exposure to the Internet
* Availability of known exploits
* Potential business impact

### 4. Remediation

The vulnerability is addressed by applying an appropriate solution.

Examples:

* Installing a security patch
* Updating software
* Changing configuration
* Removing vulnerable software
* Applying compensating security controls

### 5. Verification

After remediation, security teams verify that the vulnerability has actually been fixed.

This may involve:

* Rescanning the system
* Testing the affected application
* Checking the installed software version
* Reviewing configuration

### 6. Continuous Monitoring

New vulnerabilities can appear even after a system has been secured.

Therefore, organizations continuously monitor their systems and repeat the vulnerability management process.

### Key Point

> **Vulnerability management is a continuous cycle, not a one-time task.**

---

## b. CVEs

**CVE (Common Vulnerabilities and Exposures)** is a standardized identification system for publicly known cybersecurity vulnerabilities.

A CVE provides a unique identifier that security professionals can use to refer to a specific vulnerability.

### CVE Example

A CVE identifier looks like:

```text
CVE-2024-XXXX
```

The general format is:

```text
CVE-YEAR-NUMBER
```

For example:

```text
CVE-2021-44228
```

This identifier is associated with the well-known **Log4Shell** vulnerability in Apache Log4j.

### Why CVEs Are Important

CVEs help organizations:

* Identify specific vulnerabilities
* Search for vulnerability information
* Track security issues
* Communicate about vulnerabilities consistently
* Determine whether their systems are affected
* Find available remediation information

### CVE vs Vulnerability

These terms are related but different:

```text
Vulnerability
     ↓
A security weakness

CVE
     ↓
A standardized identifier for a publicly known vulnerability
```

### Key Point

> **CVE = A unique identifier used to track a publicly known vulnerability.**

---

## c. Severity Ratings

A vulnerability's **severity rating** indicates how serious the vulnerability could be from a technical security perspective.

One commonly used system is **CVSS (Common Vulnerability Scoring System)**.

CVSS provides a numerical score from **0.0 to 10.0**.

### Common CVSS Severity Levels

|     CVSS Score | Severity |
| -------------: | -------- |
|        **0.0** | None     |
|  **0.1 – 3.9** | Low      |
|  **4.0 – 6.9** | Medium   |
|  **7.0 – 8.9** | High     |
| **9.0 – 10.0** | Critical |

### Example

Suppose a vulnerability has a CVSS score of:

```text
CVSS: 9.8
```

This is classified as **Critical** severity.

It should generally receive urgent attention, especially if the affected system is exposed and the vulnerability is actively exploitable.

### Important

A high CVSS score does **not automatically mean it should be fixed before every other vulnerability**.

Organizations should also consider:

* Whether the system is exposed
* Whether an exploit exists
* Whether attackers are actively exploiting it
* How important the affected asset is
* What data or services could be affected

### Key Point

> **Severity tells you how serious a vulnerability is; risk prioritization considers the real-world context.**

---

## d. Patch Management

**Patch management** is the process of identifying, testing, deploying, and verifying software updates that fix security vulnerabilities, bugs, or other issues.

### Patch Management Process

```text
Identify Updates
       ↓
Assess Risk
       ↓
Test Patch
       ↓
Deploy Patch
       ↓
Verify Installation
       ↓
Monitor
```

### 1. Identify Updates

Organizations monitor vendors and security sources for available updates.

### 2. Assess Risk

Determine which systems require immediate patching based on factors such as:

* Vulnerability severity
* System exposure
* Exploit availability
* Business importance

### 3. Test the Patch

Before deploying a patch everywhere, organizations may test it in a controlled environment.

This helps identify compatibility or stability problems.

### 4. Deploy the Patch

After testing, the patch is deployed to affected systems.

For large environments, patch deployment may be performed in stages.

### 5. Verify

Security teams confirm that:

* The patch was successfully installed.
* The vulnerable version is no longer present.
* The system continues to work correctly.

### 6. Monitor

After deployment, systems should continue to be monitored for problems or new vulnerabilities.

### Why Patch Management Is Important

Without proper patch management:

```text
Unpatched System
       ↓
Known Vulnerability
       ↓
Possible Exploitation
       ↓
Security Incident
```

### Key Point

> **Patch management helps reduce security risk by keeping systems updated and fixing known vulnerabilities.**

---

## e. Risk Prioritization

Organizations may discover **hundreds or thousands of vulnerabilities**.

It is usually impossible to fix everything immediately, so security teams must determine **which vulnerabilities need attention first**.

This process is called **risk prioritization**.

### Factors Used for Prioritization

#### 1. Severity

Higher-severity vulnerabilities generally require more attention.

#### 2. Exploitability

A vulnerability that is easy to exploit may represent greater risk.

#### 3. Active Exploitation

If attackers are actively exploiting a vulnerability, it may require urgent remediation.

#### 4. Asset Criticality

A vulnerability on a critical production server may be more important than the same vulnerability on an isolated test system.

#### 5. Internet Exposure

Internet-facing systems are generally more exposed to attacks.

#### 6. Business Impact

Consider what could happen if the vulnerability is exploited.

For example:

* Data theft
* Service disruption
* Financial loss
* Unauthorized access
* Reputation damage

### Simple Risk Example

```text
Vulnerability A
Severity: High
Internet-facing: Yes
Known exploit: Yes
Critical server: Yes

          ↓

      HIGH PRIORITY
```

```text
Vulnerability B
Severity: Medium
Internal test system: Yes
Known exploit: No
Low business impact: Yes

          ↓

     LOWER PRIORITY
```

### Risk-Based Approach

A simple way to think about vulnerability risk is:

```text
Risk
  ↓
Severity
+ Exploitability
+ Exposure
+ Asset Criticality
+ Business Impact
```

This is not a formal risk calculation, but it helps explain why **severity alone should not determine remediation priority**.

### Key Point

> **Risk prioritization = Fix the vulnerabilities that pose the greatest real-world risk first.**

---

## Vulnerability Management Flow

```text
              Discover
                 ↓
              Assess
                 ↓
            Prioritize
                 ↓
             Remediate
                 ↓
              Verify
                 ↓
          Monitor Continuously
                 │
                 └──────────→ New Vulnerabilities
```

---

## CVE, CVSS, and Risk

These concepts are related but have different purposes:

| Term            | Meaning                                                           |
| --------------- | ----------------------------------------------------------------- |
| **CVE**         | Identifies a specific publicly known vulnerability                |
| **CVSS**        | Provides a standardized severity score                            |
| **Risk**        | Considers the vulnerability's real-world impact and context       |
| **Patch**       | A software update that may fix a vulnerability                    |
| **Remediation** | The overall action taken to reduce or eliminate the vulnerability |

### Example

```text
CVE
 ↓
Identifies the vulnerability
 ↓
CVSS
 ↓
Provides severity information
 ↓
Risk Assessment
 ↓
Considers environment and business impact
 ↓
Prioritization
 ↓
Decides how urgently to fix it
 ↓
Patch / Remediation
 ↓
Verify
```

---

## Quick Revision

| Topic                       | Simple Meaning                                                                          |
| --------------------------- | --------------------------------------------------------------------------------------- |
| **Vulnerability Lifecycle** | Process of discovering, assessing, prioritizing, fixing, and monitoring vulnerabilities |
| **CVE**                     | Unique identifier for a publicly known vulnerability                                    |
| **Severity Ratings**        | Indicate how serious a vulnerability is                                                 |
| **Patch Management**        | Process of testing, deploying, and verifying security updates                           |
| **Risk Prioritization**     | Deciding which vulnerabilities should be fixed first based on real-world risk           |

### Easy Way to Remember

```text
Lifecycle → Discover → Assess → Prioritize → Fix → Verify → Monitor

CVE → Identifies the vulnerability

CVSS → Measures technical severity

Patch → Fixes the vulnerability

Risk → Considers the real-world situation

Priority → Decides what to fix first
```

## Conclusion

Vulnerability management helps organizations continuously identify and reduce security weaknesses. Understanding the **vulnerability lifecycle, CVEs, severity ratings, patch management, and risk prioritization** helps security teams focus their resources on the vulnerabilities that create the greatest risk.

> **Find it → Understand it → Prioritize it → Fix it → Verify it → Monitor it**

