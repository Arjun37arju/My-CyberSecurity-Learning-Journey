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



---

