# Understand OSI & TCP/IP Models

The **OSI and TCP/IP models** help us understand **how data travels between devices over a network** and what each layer is responsible for.

## Table of Contents

* [a. OSI Model](#a-osi-model)
* [b. TCP/IP Model](#b-tcpip-model)
* [c. Layer Responsibilities](#c-layer-responsibilities)
* [d. Packet Flow](#d-packet-flow)
* [e. Troubleshooting Concepts](#e-troubleshooting-concepts)

---

## a. OSI Model

### Content

**OSI (Open Systems Interconnection) Model** is a **7-layer model** used to understand how network communication works.

```text
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical
```

Each layer has a specific responsibility.

| Layer | Name         | Main Responsibility                              |
| ----: | ------------ | ------------------------------------------------ |
|     7 | Application  | Provides network services to applications        |
|     6 | Presentation | Handles data format, encryption, and compression |
|     5 | Session      | Establishes and manages communication sessions   |
|     4 | Transport    | Provides end-to-end data delivery                |
|     3 | Network      | Handles logical addressing and routing           |
|     2 | Data Link    | Handles communication within a local network     |
|     1 | Physical     | Transmits bits through physical media            |

**Easy idea:**

> **OSI = 7 layers that explain how network communication works.**

---

## b. TCP/IP Model

### Content

The **TCP/IP model** is the practical networking model used to describe how Internet communication works.

It commonly has **4 layers**:

```text
4. Application
3. Transport
2. Internet
1. Network Access
```

| TCP/IP Layer   | Main Responsibility                     |
| -------------- | --------------------------------------- |
| Application    | Network applications and services       |
| Transport      | End-to-end communication                |
| Internet       | IP addressing and routing               |
| Network Access | Local network and physical transmission |

Examples:

```text
Application     → HTTP, DNS, SSH
Transport       → TCP, UDP
Internet        → IP
Network Access  → Ethernet, Wi-Fi
```

**Easy idea:**

> **TCP/IP = Practical model used to understand Internet communication.**

### OSI and TCP/IP Mapping

```text
OSI                    TCP/IP

Application  ─┐
Presentation  ├──→ Application
Session       ┘

Transport     ───→ Transport

Network       ───→ Internet

Data Link     ─┐
Physical      ─┴──→ Network Access
```

---

## c. Layer Responsibilities

### Content

Each network layer performs a different job.

```text
Application  → Network services
Presentation → Data format
Session      → Communication sessions
Transport    → End-to-end delivery
Network      → Addressing and routing
Data Link    → Local network communication
Physical     → Transmission of bits
```

### Example

When you open a website:

```text
Application
HTTP request

     ↓

Transport
TCP

     ↓

Network
IP

     ↓

Data Link
Ethernet / Wi-Fi

     ↓

Physical
Electrical / Radio / Light signals
```

**Easy idea:**

> **Each layer performs a specific part of the communication process.**

---

## d. Packet Flow

### Content

**Packet flow** describes how data travels from a source device to a destination device through a network.

For example:

```text
Your Computer
      ↓
   Router
      ↓
   Internet
      ↓
Web Server
```

At a high level, data moves down through the networking layers before being transmitted.

```text
Application Data
      ↓
Transport Segment
      ↓
Network Packet
      ↓
Data Link Frame
      ↓
Physical Bits
```

At the destination, the process happens in reverse.

```text
Bits
 ↓
Frame
 ↓
Packet
 ↓
Segment
 ↓
Application Data
```

This process is commonly called **encapsulation and decapsulation**.

**Easy idea:**

> **Packet Flow = How data moves from one device to another through the network.**

---

## e. Troubleshooting Concepts

### Content

**Network troubleshooting** is the process of finding and fixing problems that prevent network communication from working correctly.

A basic troubleshooting approach is:

```text
Identify Problem
      ↓
Check Physical Connection
      ↓
Check Network Configuration
      ↓
Test Connectivity
      ↓
Check DNS / Services
      ↓
Find Cause
      ↓
Fix Problem
      ↓
Verify
```

Common problems include:

* No network connection
* Incorrect IP address
* DNS problems
* Gateway problems
* Cable problems
* Wi-Fi problems
* Firewall restrictions
* Service unavailable

### Example

If you cannot open a website:

```text
Check Wi-Fi
    ↓
Check IP Address
    ↓
Check Gateway
    ↓
Test Connectivity
    ↓
Test DNS
    ↓
Check Website / Service
```

**Easy idea:**

> **Troubleshooting = Find the problem → identify the cause → fix it → verify the solution.**
