# Understand Denial of Service Attacks

Denial of Service attacks are attacks that attempt to **make a service, website, server, or network unavailable to legitimate users**.

## Table of Contents

* [a. DoS Attacks](#a-dos-attacks)
* [b. DDoS Attacks](#b-ddos-attacks)
* [c. Botnets](#c-botnets)
* [d. Attack Impact](#d-attack-impact)
* [e. Mitigation Approaches](#e-mitigation-approaches)

---

## a. DoS Attacks

### Content

**DoS (Denial of Service)** is an attack where an attacker attempts to **overwhelm or disrupt a service**, preventing legitimate users from accessing it.

```text id="d0s4k8"
Attacker
    ↓
Large Amount of Requests / Traffic
    ↓
Server
    ↓
Resources Exhausted
    ↓
Service Becomes Unavailable
```

The target may run out of resources such as:

* CPU
* Memory
* Network bandwidth
* Connection capacity

Example:

> A server receives an excessive number of requests and becomes too busy to respond normally to legitimate users.

**Easy idea:**

> **DoS = One main source attempts to make a service unavailable.**

### Practical Task

Research a **real-world DoS attack**.

Find out:

* What was targeted?
* What type of DoS attack occurred?
* How did the attack affect the service?
* How long did the disruption last?
* What was the impact?
* How was the incident handled?

### Deliverable

Create a **DoS Attack Analysis**:

```text id="k5v9q2"
Target:
Attack Type:
Cause:
Impact:
Response:
Security Lesson:
Sources:
```

**Goal:**

> Understand how DoS attacks can disrupt the availability of services.

---

## b. DDoS Attacks

### Content

**DDoS (Distributed Denial of Service)** is similar to DoS, but the attack traffic comes from **many systems or sources**.

```text id="d2d8x5"
System 1 ──┐
System 2 ──┤
System 3 ──┤
System 4 ──┼──→ Target Server
System 5 ──┤
System 6 ──┘
```

Because traffic comes from many sources, DDoS attacks can be more difficult to handle.

**Easy idea:**

> **DDoS = Many sources → One target → Service disruption.**

### Practical Task

Research a **real-world DDoS incident**.

Identify:

* Target
* Date
* Type of attack
* Sources of traffic
* Impact
* How the organization responded
* Security lessons

### Deliverable

Create a **DDoS Incident Report** and include a simple diagram showing how distributed sources can affect a target.

**Goal:**

> Understand the difference between DoS and DDoS and how distributed attacks can increase the scale of an attack.

---

## c. Botnets

### Content

A **botnet** is a group of compromised devices that can be controlled by an attacker.

These devices may include:

* Computers
* Servers
* Routers
* IoT devices

```text id="b8n3m6"
             Attacker
                ↓
        Command / Control
                ↓
      ┌─────────┼─────────┐
      ↓         ↓         ↓
   Device    Device    Device
      ↓         ↓         ↓
      └─────────┼─────────┘
                ↓
             Target
```

A botnet can be used for different malicious activities, including DDoS attacks.

**Easy idea:**

> **Botnet = Group of compromised devices controlled by an attacker.**

### Practical Task

Research a **real-world botnet**.

Find out:

* Botnet name
* How devices became infected
* Types of devices affected
* How the botnet was controlled
* What it was used for
* How it was disrupted or removed

### Deliverable

Create a **Botnet Research Report** with a diagram showing:

```text id="r3p7c1"
Compromised Devices
        ↓
      Botnet
        ↓
 Attacker Control
        ↓
 Malicious Activity
```

**Goal:**

> Understand how compromised devices can be organized into a botnet and used for attacks.

---

## d. Attack Impact

### Content

A DoS or DDoS attack can affect an organization in several ways.

Possible impacts include:

* Website downtime
* Service disruption
* Loss of availability
* Financial losses
* Customer dissatisfaction
* Business interruption
* Increased recovery costs

```text id="i6x9v2"
DDoS Attack
     ↓
Service Disruption
     ↓
Users Cannot Access Service
     ↓
Business Impact
```

**Easy idea:**

> **Attack Impact = The damage or disruption caused by the attack.**

### Practical Task

Choose a real-world DoS or DDoS incident and analyze its impact.

Identify:

* Technical impact
* Business impact
* User impact
* Financial impact, if publicly reported
* Recovery process

### Deliverable

Create an **Attack Impact Analysis**:

| Impact Area          | Findings |
| -------------------- | -------- |
| Technical Impact     |          |
| Service Availability |          |
| User Impact          |          |
| Business Impact      |          |
| Financial Impact     |          |
| Recovery             |          |

**Goal:**

> Understand that availability attacks can affect both technology and business operations.

---

## e. Mitigation Approaches

### Content

**Mitigation approaches** are security measures used to **reduce the likelihood or impact of DoS and DDoS attacks**.

Common approaches include:

* Traffic filtering
* Rate limiting
* Firewalls
* Load balancing
* DDoS protection services
* Network monitoring
* Incident response planning
* Redundant infrastructure

```text id="m7q4z9"
Incoming Traffic
       ↓
Traffic Filtering
       ↓
Rate Limiting
       ↓
DDoS Protection
       ↓
Legitimate Traffic
       ↓
Server
```

The exact defense depends on the type and scale of the attack.

**Easy idea:**

> **Mitigation = Measures used to reduce the impact of an attack.**

### Practical Task

Create a mitigation plan for a fictional website.

Scenario:

> An online store experiences a large amount of unwanted traffic and legitimate customers are unable to access the website.

Design a basic mitigation plan.

Include:

* Traffic filtering
* Rate limiting
* Monitoring
* DDoS protection
* Incident response
* Recovery

### Deliverable

Create a **DDoS Mitigation Plan**:

| Security Measure  | Purpose |
| ----------------- | ------- |
| Traffic Filtering |         |
| Rate Limiting     |         |
| Monitoring        |         |
| DDoS Protection   |         |
| Incident Response |         |
| Recovery          |         |

**Goal:**

> Understand how organizations can prepare for, detect, and reduce the impact of DoS and DDoS attacks.

---

# Final Practical Project

Create a **Denial of Service Attack Research Report** combining all five topics.

```text id="n5c8r2"
DoS
 ↓
DDoS
 ↓
Botnets
 ↓
Attack Impact
 ↓
Mitigation
```

### Final Challenge

Choose **one real-world DDoS incident** and analyze it from beginning to end.

Document:

```text id="p4x7m1"
1. What was targeted?
        ↓
2. DoS or DDoS?
        ↓
3. How was the attack distributed?
        ↓
4. Was a botnet involved?
        ↓
5. What was the impact?
        ↓
6. How was it mitigated?
        ↓
7. What security lessons were learned?
```

### Final Deliverable

Create a GitHub project:

```text id="c8v2n6"
Denial-of-Service/
│
├── README.md
├── dos-attacks.md
├── ddos-attacks.md
├── botnets.md
├── attack-impact.md
├── mitigation.md
└── incident-analysis.md
```

**Important:** For hands-on practice, use only **authorized labs or controlled environments**. Do not send DoS/DDoS traffic against real websites, servers, or networks.

### Expected Result

After completing this project, you should be able to:

* Explain DoS attacks
* Explain DDoS attacks
* Understand what botnets are
* Analyze the impact of availability attacks
* Identify common mitigation approaches
* Analyze real-world DoS/DDoS incidents
* Document security findings professionally

> **Learn → Research → Analyze → Understand Defense → Document**
