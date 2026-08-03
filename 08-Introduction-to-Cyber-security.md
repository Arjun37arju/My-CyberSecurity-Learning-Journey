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
