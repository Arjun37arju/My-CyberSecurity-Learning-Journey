#  Understand OSI & TCP/IP Models

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

```text id="osi7l"
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical
```

Each layer has a specific responsibility.

### The 7 Layers

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

### Practical Task

Create your own **OSI Model diagram**.

For every layer, write:

* Layer number
* Layer name
* Main responsibility
* One example protocol or technology

### Deliverable

Create:

```text
osi-model.md
```

with a complete OSI layer table and diagram.

**Goal:**

> Understand the purpose of all seven OSI layers.

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
Application → HTTP, DNS, SSH
Transport   → TCP, UDP
Internet    → IP
Network Access → Ethernet, Wi-Fi
```

**Easy idea:**

> **TCP/IP = Practical model used to understand Internet communication.**

### Practical Task

Research the TCP/IP model and compare it with the OSI model.

Create a mapping:

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

### Deliverable

Create:

```text
tcp-ip-model.md
```

including the model, layer responsibilities, and OSI-to-TCP/IP mapping.

**Goal:**

> Understand how the OSI and TCP/IP models relate to each other.

---

## c. Layer Responsibilities

### Content

Each network layer performs a different job.

A simple way to remember them:

```text
Application → What service?
Presentation → What format?
Session → What connection/session?
Transport → How to deliver?
Network → Where to send?
Data Link → Which local device?
Physical → How are bits transmitted?
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

### Practical Task

Choose one activity:

> Opening a website.

Explain what happens at each OSI layer.

Create a table:

| OSI Layer    | What Happens? |
| ------------ | ------------- |
| Application  |               |
| Presentation |               |
| Session      |               |
| Transport    |               |
| Network      |               |
| Data Link    |               |
| Physical     |               |

### Deliverable

Create:

```text
layer-responsibilities.md
```

with your explanation.

**Goal:**

> Understand what each layer does during real network communication.

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

### Practical Task

Create a packet-flow diagram for:

> **Your computer opening a website.**

Show:

```text
Computer
   ↓
Router
   ↓
Internet
   ↓
Web Server
```

Then show the data format at different layers:

```text
Application Data
       ↓
TCP Segment
       ↓
IP Packet
       ↓
Ethernet Frame
       ↓
Bits
```

### Deliverable

Create:

```text
packet-flow.md
```

and include a packet-flow diagram.

**Goal:**

> Understand how data is encapsulated and transmitted across a network.

---

## e. Troubleshooting Concepts

### Content

**Network troubleshooting** is the process of finding and fixing problems that prevent network communication from working correctly.

A simple troubleshooting process is:

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

### Practical Task

Create **5 network troubleshooting scenarios**.

Example:

> **Scenario:** Computer is connected to Wi-Fi but cannot access websites.

Investigate possible causes such as:

* Wi-Fi connection
* IP configuration
* Default gateway
* DNS
* Internet connection

For each scenario, document:

```text
Problem:
Possible Cause:
Test:
Finding:
Solution:
Verification:
```

### Deliverable

Create:

```text
troubleshooting.md
```

containing your five scenarios and solutions.

**Goal:**

> Develop a structured approach to identifying and solving common network problems.

---

# Final Practical Project

Create a **OSI & TCP/IP Networking Project** combining all five topics.

```text
OSI Model
    ↓
TCP/IP Model
    ↓
Layer Responsibilities
    ↓
Packet Flow
    ↓
Troubleshooting
```

### Final Challenge

Take this scenario:

> **A user can connect to Wi-Fi but cannot open websites.**

Analyze the problem using the OSI model.

```text
Application
    ↓
Is the website/service working?

Transport
    ↓
Is the connection reaching the service?

Network
    ↓
Does the device have a valid IP and gateway?

Data Link
    ↓
Is the device connected to the local network?

Physical
    ↓
Is the network connection working?
```

Then document:

1. What you checked
2. Which layer was involved
3. What you found
4. What caused the problem
5. How you fixed it
6. How you verified the solution

### Final GitHub Structure

```text
OSI-TCPIP-Models/
│
├── README.md
├── osi-model.md
├── tcp-ip-model.md
├── layer-responsibilities.md
├── packet-flow.md
├── troubleshooting.md
└── diagrams/
    ├── osi-model.png
    └── packet-flow.png
```

### Expected Result

After completing this project, you should be able to:

* Explain the OSI model
* Explain the TCP/IP model
* Understand the responsibility of each layer
* Explain packet flow
* Understand encapsulation and decapsulation
* Troubleshoot basic network problems
* Use OSI layers to locate possible network issues
* Document networking concepts professionally

> **Understand the layers → Follow the data → Find the problem → Fix it → Document it**
