# 2. Understand OSI & TCP/IP Models

## 📚 Table of Contents

* [a. OSI Model](#a-osi-model)
* [b. TCP/IP Model](#b-tcpip-model)
* [c. Layer Responsibilities](#c-layer-responsibilities)
* [d. Packet Flow](#d-packet-flow)
* [e. Troubleshooting Concepts](#e-troubleshooting-concepts)

---

# a. OSI Model

## What is the OSI Model?

**OSI** stands for **Open Systems Interconnection**.

The **OSI model** is a conceptual framework that divides network communication into **7 layers**.

It helps us understand:

* How devices communicate
* How data moves through a network
* What each layer is responsible for
* Which protocols and devices operate at different layers
* Where network problems occur

### Simple definition

> **The OSI model is a 7-layer framework used to understand and describe how data travels between networked devices.**

---

## The 7 OSI Layers

```text
┌─────────────────────────────┐
│ 7. Application              │
├─────────────────────────────┤
│ 6. Presentation             │
├─────────────────────────────┤
│ 5. Session                  │
├─────────────────────────────┤
│ 4. Transport                │
├─────────────────────────────┤
│ 3. Network                  │
├─────────────────────────────┤
│ 2. Data Link                │
├─────────────────────────────┤
│ 1. Physical                │
└─────────────────────────────┘
```

### Easy memory trick

From Layer 7 to Layer 1:

> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing

| Layer | Name         | Main idea                            |
| ----: | ------------ | ------------------------------------ |
| **7** | Application  | Network services for applications    |
| **6** | Presentation | Data format, encryption, compression |
| **5** | Session      | Manages communication sessions       |
| **4** | Transport    | End-to-end delivery                  |
| **3** | Network      | IP addressing and routing            |
| **2** | Data Link    | Frames and MAC addresses             |
| **1** | Physical     | Bits and physical signals            |

---

## Layer 7 — Application

The **Application layer** provides network services used by applications.

Examples:

* HTTP
* HTTPS
* DNS
* SMTP
* FTP
* SSH

Example:

```text
Web Browser
    ↓
HTTPS
    ↓
Application Layer
```

### Important point

The Application layer does **not** mean the actual application itself.

For example:

```text
Chrome → Application
HTTP/HTTPS → Application-layer protocols
```

---

## Layer 6 — Presentation

The **Presentation layer** deals with how data is represented.

Common responsibilities include:

* Data formatting
* Data translation
* Encryption/decryption
* Compression/decompression

Example:

```text
Data
 ↓
Encryption / Formatting
 ↓
Network communication
```

### Simple idea

> **Presentation = makes data understandable and properly formatted between systems.**

---

## Layer 5 — Session

The **Session layer** manages communication sessions between applications.

It can handle:

* Establishing sessions
* Maintaining sessions
* Ending sessions
* Session synchronization

Simple example:

```text
Device A
   ↕
 Session
   ↕
Device B
```

### Simple idea

> **Session = manages the conversation/session between applications.**

---

## Layer 4 — Transport

The **Transport layer** provides end-to-end transport of data.

Important protocols:

* TCP
* UDP

Responsibilities include:

* Segmentation
* Reliability
* Flow control
* Error recovery
* Port numbers

### TCP

TCP provides reliable, connection-oriented communication.

```text
Sender
  ↓
TCP
  ↓
Receiver
```

TCP can detect missing data and retransmit it.

### UDP

UDP is connectionless and has lower protocol overhead than TCP, but it does not provide TCP's reliability mechanisms.

Examples where UDP may be useful:

* DNS queries
* Streaming
* Online gaming
* Voice/video applications

### Important

> **Transport Layer = TCP/UDP + ports + end-to-end transport.**

---

## Layer 3 — Network

The Network layer is responsible for **logical addressing and routing**.

Important protocol:

* IP

Important concepts:

* IPv4
* IPv6
* IP addresses
* Routing
* Routers

Example:

```text
PC
 ↓
Router
 ↓
Another Network
```

The router uses destination IP information to determine where packets should go.

### Example

```text
Source IP:      192.168.1.10
Destination IP: 8.8.8.8
```

The destination IP helps routers forward the packet toward the destination.

### Important

> **Network Layer = IP addressing + routing.**

---

## Layer 2 — Data Link

The Data Link layer provides communication over a local network link.

Important concepts:

* Ethernet
* MAC addresses
* Frames
* Switches

Example:

```text
PC
 ↓
Ethernet Frame
 ↓
Switch
 ↓
PC
```

A switch uses MAC address information to forward Ethernet frames within a LAN.

### Important

> **Data Link Layer = Frames + MAC addresses + local network delivery.**

---

## Layer 1 — Physical

The Physical layer deals with the actual transmission of bits and signals.

Examples:

* Ethernet cables
* Fiber-optic cables
* Radio signals
* Electrical signals
* Connectors
* Physical network interfaces

Conceptually:

```text
Data
 ↓
Bits
 ↓
Signals
 ↓
Cable / Radio
```

### Important

> **Physical Layer = Bits + signals + physical transmission medium.**

---

# OSI Layer Summary

| Layer | Name         | Main Responsibility                          | Examples             |
| ----: | ------------ | -------------------------------------------- | -------------------- |
| **7** | Application  | Network services for applications            | HTTP, DNS, SMTP      |
| **6** | Presentation | Data representation, encryption, compression | Encoding, encryption |
| **5** | Session      | Manage communication sessions                | Session management   |
| **4** | Transport    | End-to-end transport                         | TCP, UDP, ports      |
| **3** | Network      | IP addressing and routing                    | IP, routers          |
| **2** | Data Link    | Local delivery, frames, MAC                  | Ethernet, switches   |
| **1** | Physical     | Bits and signals                             | Cables, fiber, radio |

---

# b. TCP/IP Model

## What is the TCP/IP Model?

The **TCP/IP model** is a practical networking model used to describe communication across networks and the Internet.

It is named after two important protocols:

* **TCP — Transmission Control Protocol**
* **IP — Internet Protocol**

### Simple definition

> **The TCP/IP model is a practical framework that describes how data is communicated across interconnected networks.**

---

## TCP/IP Model Layers

The commonly used 4-layer TCP/IP model is:

```text
┌──────────────────────────┐
│ Application              │
├──────────────────────────┤
│ Transport                │
├──────────────────────────┤
│ Internet                 │
├──────────────────────────┤
│ Network Access           │
└──────────────────────────┘
```

| TCP/IP Layer       | Main responsibility                     |
| ------------------ | --------------------------------------- |
| **Application**    | Application-level network services      |
| **Transport**      | End-to-end communication                |
| **Internet**       | IP addressing and routing               |
| **Network Access** | Local network and physical transmission |

---

## 1. Application Layer

The TCP/IP Application layer combines functions represented by the OSI:

* Application
* Presentation
* Session

Examples:

* HTTP
* HTTPS
* DNS
* SSH
* SMTP
* FTP

---

## 2. Transport Layer

Responsible for end-to-end communication.

Main protocols:

* TCP
* UDP

Important concepts:

* Ports
* Reliability
* Segmentation
* Flow control

Example:

```text
TCP → Reliable communication
UDP → Connectionless communication
```

---

## 3. Internet Layer

Responsible for:

* IP addressing
* Packet delivery
* Routing

Important protocols:

* IPv4
* IPv6
* ICMP

Routers operate primarily at this layer.

Example:

```text
Network A
   ↓
Router
   ↓
Network B
```

---

## 4. Network Access Layer

The Network Access layer handles communication over the local network and the physical transmission medium.

It covers functions associated with the OSI:

* Data Link
* Physical

Examples:

* Ethernet
* Wi-Fi
* MAC addressing
* Frames
* Physical transmission

---

# OSI vs TCP/IP

The models are related but not identical.

```text
OSI Model                  TCP/IP Model

7 Application ────────┐
6 Presentation ───────┼──→ Application
5 Session ────────────┘

4 Transport ─────────────→ Transport

3 Network ───────────────→ Internet

2 Data Link ──────────┐
1 Physical ───────────┼──→ Network Access
```

### Comparison

| OSI                                             | TCP/IP                                           |
| ----------------------------------------------- | ------------------------------------------------ |
| 7 layers                                        | Commonly 4 layers                                |
| Conceptual reference model                      | Practical Internet networking model              |
| Application, Presentation, Session are separate | Combined into Application                        |
| Data Link and Physical are separate             | Combined into Network Access                     |
| Useful for learning and troubleshooting         | Widely used to describe real Internet networking |

### Easy memory

```text
OSI:
7 → Application
6 → Presentation
5 → Session
4 → Transport
3 → Network
2 → Data Link
1 → Physical

TCP/IP:
Application
Transport
Internet
Network Access
```

---

# c. Layer Responsibilities

Understanding the **job of each layer** is more important than simply memorizing names.

## OSI Layer Responsibilities

|              Layer | Main Question                                               |
| -----------------: | ----------------------------------------------------------- |
|  **7 Application** | What network service does the application need?             |
| **6 Presentation** | How should the data be represented?                         |
|      **5 Session** | How is the communication session managed?                   |
|    **4 Transport** | How should data be delivered end-to-end?                    |
|      **3 Network** | Where should the packet go?                                 |
|    **2 Data Link** | Which device on the local network should receive the frame? |
|     **1 Physical** | How are the bits/signals transmitted?                       |

### Example

Suppose you open:

```text
https://example.com
```

A simplified view:

```text
Application
    ↓
HTTPS
    ↓
Transport
    ↓
TCP
    ↓
Network
    ↓
IP
    ↓
Data Link
    ↓
Ethernet / Wi-Fi
    ↓
Physical
    ↓
Bits / Signals
```

---

# Important Addressing Concepts

Different layers use different types of identifiers.

### MAC Address

Used primarily at the **Data Link layer**.

Example:

```text
00:1A:2B:3C:4D:5E
```

Used for local network communication.

### IP Address

Used at the **Network/Internet layer**.

Example:

```text
192.168.1.10
```

Used for logical addressing and routing between networks.

### Port Number

Used at the **Transport layer**.

Examples:

```text
HTTP  → 80
HTTPS → 443
SSH   → 22
DNS   → 53
```

Ports help identify the destination service/process for transport-layer communication.

---

# d. Packet Flow

## What is Packet Flow?

**Packet flow** describes how data moves from a source device toward a destination across a network.

Example:

```text
Laptop
   ↓
Access Point
   ↓
Switch
   ↓
Router
   ↓
ISP
   ↓
Internet
   ↓
Web Server
```

---

## Example: Opening a Website

You type:

```text
https://example.com
```

Your computer needs to communicate with a web server.

A simplified flow is:

```text
Laptop
  ↓
Wi-Fi
  ↓
Access Point
  ↓
Switch
  ↓
Router
  ↓
ISP
  ↓
Internet
  ↓
Web Server
```

---

## Encapsulation

When the sender sends data, information is added as data moves down the networking layers.

Simplified:

```text
Application Data
      ↓
Transport Header + Data
      ↓
IP Header + Transport Data
      ↓
Frame Header + Packet
      ↓
Bits / Signals
```

Conceptually:

```text
Application
    ↓
   Data
    ↓
Transport
    ↓
 Segment
    ↓
Network
    ↓
 Packet
    ↓
Data Link
    ↓
 Frame
    ↓
Physical
    ↓
 Bits
```

### Common names

| Layer       | Data Unit                      |
| ----------- | ------------------------------ |
| Application | Data                           |
| Transport   | Segment (TCP) / Datagram (UDP) |
| Network     | Packet                         |
| Data Link   | Frame                          |
| Physical    | Bits                           |

---

# Decapsulation

At the destination, the process happens in reverse.

```text
Bits
 ↓
Frame
 ↓
Packet
 ↓
Segment / Datagram
 ↓
Data
```

The receiving system processes the headers and delivers the data to the appropriate application.

### Complete flow

```text
SENDER

Application
    ↓
Transport
    ↓
Network
    ↓
Data Link
    ↓
Physical
    ↓
    NETWORK
    ↓
Physical
    ↓
Data Link
    ↓
Network
    ↓
Transport
    ↓
Application

RECEIVER
```

---

# Switch vs Router During Packet Flow

This distinction is extremely important.

### Switch

A switch primarily operates at **Layer 2**.

It uses MAC address information to forward frames within a LAN.

```text
PC 1
 ↓
Switch
 ↓
PC 2
```

### Router

A router primarily operates at **Layer 3**.

It uses IP addressing and routing information to forward packets between networks.

```text
LAN 1
 ↓
Router
 ↓
LAN 2
```

### Simple memory

> **Switch → MAC → Frame → Layer 2**

> **Router → IP → Packet → Layer 3**

---

# e. Troubleshooting Concepts

## What is Network Troubleshooting?

**Network troubleshooting** is the process of identifying, analyzing, and fixing problems that prevent a network or network service from working correctly.

### Simple definition

> **Network troubleshooting is the systematic process of finding and fixing network problems.**

---

# Layer-by-Layer Troubleshooting

The OSI model helps you troubleshoot problems systematically.

Instead of randomly changing settings, ask:

> **Which layer is causing the problem?**

---

## Layer 1 — Physical

Check:

* Is the cable connected?
* Is the network interface enabled?
* Are link lights present?
* Is the Wi-Fi signal available?
* Is the device powered on?

Example problem:

```text
PC ─────X───── Switch
       Cable
```

Possible solution:

* Replace cable
* Check port
* Enable interface
* Check power

---

## Layer 2 — Data Link

Check:

* Is the network interface working?
* Is the device connected to the correct LAN?
* Is the switch port functioning?
* Are VLAN configurations correct?
* Are there MAC-related issues?

Example:

```text
PC → Switch → ❌
```

The physical cable may work, but the Layer 2 configuration may be incorrect.

---

## Layer 3 — Network

Check:

* IP address
* Subnet mask/prefix
* Default gateway
* Routing
* Reachability

Example:

```text
PC
IP:      192.168.1.10
Gateway: 192.168.1.1
```

If the gateway is incorrect, the device may be unable to reach other networks.

---

## Layer 4 — Transport

Check:

* Is the required port reachable?
* Is TCP/UDP being used correctly?
* Is a firewall blocking the connection?
* Is the service listening?

Example:

```text
Server
   ↓
TCP
   ↓
Port 443
```

If HTTPS is unavailable, investigate whether the expected service is listening and whether traffic to the port is being blocked.

---

## Layer 7 — Application

Check:

* Is the application running?
* Is the correct hostname being used?
* Is the service functioning?
* Are application configurations correct?

Example:

```text
Browser
   ↓
HTTPS
   ↓
Web Server
```

The network may be working correctly while the web application itself is down.

---

# Common Troubleshooting Commands

These commands are useful when learning networking.

### `ping`

Tests basic IP reachability.

```bash
ping 8.8.8.8
```

Example:

```text
PC → Router → Internet
```

If ping fails, investigate connectivity, routing, filtering, or whether the destination responds to ICMP.

---

### `ipconfig` / `ifconfig` / `ip`

Used to inspect network configuration.

Windows:

```cmd
ipconfig
```

Linux:

```bash
ip addr
```

Useful for checking:

* IP address
* Network interface
* Default gateway
* Other interface information

---

### `traceroute` / `tracert`

Shows the path traffic takes through routers toward a destination.

Windows:

```cmd
tracert example.com
```

Linux:

```bash
traceroute example.com
```

Conceptually:

```text
PC
 ↓
Router 1
 ↓
Router 2
 ↓
Router 3
 ↓
Destination
```

---

### `nslookup`

Used to query DNS information.

```bash
nslookup example.com
```

It can help determine whether a hostname is resolving correctly.

---

### `netstat` / `ss`

Used to inspect network connections and listening sockets.

Linux:

```bash
ss -tuln
```

Windows:

```cmd
netstat -ano
```

These can help identify:

* Listening ports
* Active connections
* Network services

---

# Troubleshooting Method

A good troubleshooting process is systematic.

```text
1. Identify the problem
        ↓
2. Gather information
        ↓
3. Check physical connectivity
        ↓
4. Check network configuration
        ↓
5. Test connectivity
        ↓
6. Check routing
        ↓
7. Check ports/services
        ↓
8. Check application
        ↓
9. Apply the fix
        ↓
10. Test again
```

---

# 🛡️ OSI Model and Cybersecurity

Understanding the OSI model is extremely useful in cybersecurity.

Different attacks and security controls can involve different layers.

Examples:

|             Layer | Security-related examples                |
| ----------------: | ---------------------------------------- |
| **7 Application** | Web attacks, application vulnerabilities |
|   **4 Transport** | Port scanning, TCP/UDP traffic           |
|     **3 Network** | IP-based attacks, routing, firewalls     |
|   **2 Data Link** | MAC-based attacks, VLAN-related issues   |
|    **1 Physical** | Physical access, cable/device tampering  |

For example, when analyzing a suspicious connection:

```text
Source IP
    ↓
Destination IP
    ↓
TCP
    ↓
Destination Port 443
    ↓
HTTPS
```

You can use the layered model to understand **what is happening at each stage**.

---

# 🧠 Quick Revision

```text
OSI MODEL
│
├── 7 Application
│     └── Network services
│
├── 6 Presentation
│     └── Data representation / encryption / compression
│
├── 5 Session
│     └── Session management
│
├── 4 Transport
│     └── TCP / UDP / Ports
│
├── 3 Network
│     └── IP / Routing
│
├── 2 Data Link
│     └── MAC / Frames / Ethernet
│
└── 1 Physical
      └── Bits / Signals / Cables
```

```text
TCP/IP MODEL
│
├── Application
│     └── HTTP / HTTPS / DNS / SSH
│
├── Transport
│     └── TCP / UDP
│
├── Internet
│     └── IP / ICMP
│
└── Network Access
      └── Ethernet / Wi-Fi / Physical transmission
```

### Most important things to remember

```text
Layer 7 → Application
Layer 6 → Presentation
Layer 5 → Session
Layer 4 → Transport → TCP/UDP → Ports
Layer 3 → Network → IP → Routing
Layer 2 → Data Link → MAC → Frames → Switch
Layer 1 → Physical → Bits → Signals/Cables
```

### Data flow

```text
Sender
  ↓
Application Data
  ↓
Segment
  ↓
Packet
  ↓
Frame
  ↓
Bits
  ↓
Network
  ↓
Bits
  ↓
Frame
  ↓
Packet
  ↓
Segment
  ↓
Application Data
  ↓
Receiver
```

> **Key idea:** The OSI model helps you understand **where networking functions happen**, while the TCP/IP model provides a practical model for how Internet networking is implemented.
