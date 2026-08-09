# 📚 Table of Contents

1. [Understand Network Fundamentals](#1-understand-network-fundamentals)

## Quick Navigation

| Section | Topic                                             |
| ------- | ------------------------------------------------- |
| **1.a** | [What is Networking](#a-what-is-networking)       |
| **1.b** | [Network Communication](#b-network-communication) |
| **1.c** | [Network Architecture](#c-network-architecture)   |
| **1.d** | [Network Components](#d-network-components)       |
| **1.e** | [Data Transmission](#e-data-transmission)         |





# 1. Understand Network Fundamentals

## a. What is Networking?

### Definition

A **computer network** is a group of two or more devices connected together so they can **communicate, exchange data, and share resources**.

In simple words:

> **Networking is the process of connecting devices so they can communicate and share data or resources.**

### Example

A simple home network can look like this:

```text
                Internet
                   │
                 Router
                   │
                Switch
             ┌─────┼─────┐
             │     │     │
            PC   Laptop Printer
```

The devices can communicate with each other through the network.

### Main purposes of networking

* **Communication** — Allows devices to send and receive data.
* **Resource sharing** — Allows devices to share printers, files, storage, etc.
* **Internet access** — Allows devices to communicate with external networks.
* **Centralized management** — Allows organizations to manage users, devices, and services.
* **Data sharing** — Allows information to be transferred between systems.

---

## Network Types

### LAN — Local Area Network

**LAN** stands for **Local Area Network**.

A LAN connects devices within a **limited geographical area**, such as:

* Home
* Office
* School
* Computer laboratory
* Building

Example:

```text
              LAN
        ┌───────────────┐
        │               │
      PC 1            PC 2
        │               │
        └──── Switch ───┘
               │
             PC 3
```

If PC 1 wants to communicate with PC 3:

```text
PC 1 → Switch → PC 3
```

The switch forwards the data to the correct device within the local network.

### Key point

> **LAN = Local network covering a limited physical area.**

---

### WLAN — Wireless Local Area Network

**WLAN** stands for **Wireless Local Area Network**.

A WLAN is a type of LAN where devices connect using **wireless communication, usually Wi-Fi**.

Example:

```text
              Router / Access Point
                    📡
               ))   ))   ))
              📱    💻    📺
```

The devices communicate wirelessly with the wireless access point.

In a larger network, an access point may connect to a switch:

```text
Internet
   │
Router
   │
Switch
   │
Access Point
   ))))  ))))  ))))
  Phone Laptop  TV
```

Here:

* **Switch** provides wired connectivity to the Access Point.
* **Access Point** provides wireless connectivity.
* **Router** connects the local network to other networks.

### Key point

> **WLAN = A LAN that uses wireless communication.**

---

### WAN — Wide Area Network

**WAN** stands for **Wide Area Network**.

A WAN connects multiple networks across a **large geographical area**, such as different:

* Cities
* States
* Countries
* Continents

Example:

```text
Bangalore LAN
      │
    Router
      │
      │
     WAN
      │
      │
    Router
      │
Mumbai LAN
```

Each office has its own LAN, while the WAN connects those LANs.

A company with offices in Bangalore, Mumbai, and Delhi could use a WAN to connect the different office networks.

```text
                 WAN
        ┌─────────┼─────────┐
        │         │         │
    Bangalore   Mumbai     Delhi
       LAN        LAN        LAN
```

### Key point

> **WAN = Connects networks across a large geographical area.**

---

### Internet

The **Internet** is a global system of **interconnected networks** that communicate using standardized networking protocols.

It is not one single network. It is made up of many interconnected networks.

```text
Home Network
     │
    ISP
     │
Internet
     │
Destination Network
     │
Server
```

For example, when you open a website:

```text
Laptop
  ↓
Wi-Fi
  ↓
Router
  ↓
ISP
  ↓
Internet
  ↓
Web Server
```

### Key point

> **Internet = A global network of interconnected networks.**

### Network types summary

| Network      | Meaning                        | Typical scope           | Example                       |
| ------------ | ------------------------------ | ----------------------- | ----------------------------- |
| **LAN**      | Local Area Network             | Small/local area        | Office network                |
| **WLAN**     | Wireless Local Area Network    | Small/local area        | Home Wi-Fi                    |
| **WAN**      | Wide Area Network              | Large geographical area | Company offices across cities |
| **Internet** | Global interconnected networks | Worldwide               | World Wide Internet           |

### Geographical Meaning

**Geographical** means **related to a physical place or location**.

Therefore:

> **Geographical area = A particular physical area or location.**

For example:

```text
Room → Building → City → State → Country → World
```

---

## b. Network Communication

### Definition

**Network communication** is the process of **exchanging data between two or more devices over a network**.

In simple words:

> **Network communication is how devices send and receive data through a network.**

Example:

```text
Sender
  │
  ↓
Network
  │
  ↓
Receiver
```

For example, when a computer sends a file to another computer:

```text
PC 1
 ↓
Switch
 ↓
PC 2
```

PC 1 is the **sender**, and PC 2 is the **receiver**.

### Main elements of network communication

Network communication involves:

1. **Sender** — Device that sends the data.
2. **Receiver** — Device that receives the data.
3. **Data** — Information being transmitted.
4. **Communication medium** — The path used to carry the data.
5. **Network devices** — Devices such as switches and routers that forward traffic.
6. **Protocols** — Rules that define how devices communicate.

Example:

```text
Sender
  ↓
Data
  ↓
Communication Medium
  ↓
Network Devices
  ↓
Receiver
```

### Communication media

#### Wired

```text
PC ───── Ethernet Cable ───── Switch
```

Examples:

* Ethernet cable
* Fiber-optic cable

#### Wireless

```text
Phone
  )))
  ))) Wi-Fi
  )))
Access Point
```

Examples:

* Wi-Fi
* Bluetooth
* Cellular networks
* Satellite communication

### Protocols

Protocols are **rules that define how devices communicate**.

Common networking protocols include:

| Protocol  | Purpose                                      |
| --------- | -------------------------------------------- |
| **IP**    | Addressing and routing                       |
| **TCP**   | Reliable transport                           |
| **UDP**   | Connectionless transport                     |
| **DNS**   | Resolves domain names                        |
| **HTTP**  | Web communication                            |
| **HTTPS** | Secure web communication                     |
| **DHCP**  | Provides network configuration automatically |

### Example: Website communication

When you open a website:

```text
Laptop
  ↓
Wi-Fi
  ↓
Access Point
  ↓
Switch / Router
  ↓
ISP
  ↓
Internet
  ↓
Web Server
```

Different protocols work together to make this communication possible.

### Exam definition

> **Network communication is the process of transmitting and receiving data between two or more devices over a network using communication media, network devices, and standardized protocols.**

---

## c. Network Architecture

### Definition

**Network architecture** is the **overall design and structure of a network**, including its devices, connections, communication methods, services, and security mechanisms.

In simple words:

> **Network architecture is the blueprint of a network.**

It describes how different components are organized and how they communicate.

### Example

A company network may look like:

```text
                    Internet
                       │
                   Firewall
                       │
                    Router
                       │
                    Switch
              ┌────────┼────────┐
              │        │        │
             PC       PC      Server
                                │
                             Database
```

This overall design is the network's architecture.

### Network architecture includes

* Network devices
* End devices
* Connections
* Communication protocols
* Servers
* Network services
* Security controls
* Network structure

---

### Client-Server Architecture

In a **client-server architecture**, clients request services or resources from a server.

```text
Client 1 ──┐
Client 2 ──┼── Network ── Server
Client 3 ──┘
```

Example:

```text
Employee PC
     ↓
Network
     ↓
File Server
     ↓
Company Files
```

The employee's computer is the **client**, while the system providing the files is the **server**.

Examples include:

* Web servers
* File servers
* Database servers
* DNS servers
* Mail servers

---

### Peer-to-Peer Architecture

In **Peer-to-Peer (P2P)** architecture, devices can communicate directly with each other and may act as both clients and servers.

```text
       PC 1
      /    \
     /      \
   PC 2 ─── PC 3
```

There is not necessarily a central server controlling all communication.

### Client-Server vs P2P

| Feature        | Client-Server       | Peer-to-Peer                            |
| -------------- | ------------------- | --------------------------------------- |
| Central server | Usually present     | Not required                            |
| Management     | Centralized         | Distributed                             |
| Scalability    | Generally better    | Usually limited for large organizations |
| Example        | Company file server | Direct file sharing                     |

---

### Network Architecture vs Network Topology

These terms are related but different.

**Network Architecture**:

> Overall design of the network.

**Network Topology**:

> Arrangement of network devices and their connections.

Examples of topology include:

* Star
* Bus
* Ring
* Mesh
* Tree
* Hybrid

---

## d. Network Components

### Definition

**Network components** are the hardware, software, and communication elements that work together to connect devices, transmit data, provide services, and manage network traffic.

In simple words:

> **Network components are the different parts that allow a network to operate.**

### Main network components

| Component              | Main function                                     |
| ---------------------- | ------------------------------------------------- |
| **End Device**         | Sends or receives data                            |
| **NIC**                | Provides network connectivity                     |
| **Switch**             | Connects devices within a LAN                     |
| **Router**             | Connects different networks                       |
| **Access Point**       | Provides wireless connectivity                    |
| **Modem**              | Connects local equipment to an ISP access network |
| **Firewall**           | Controls and filters network traffic              |
| **Server**             | Provides services and resources                   |
| **Transmission Media** | Carries data                                      |
| **Protocols**          | Define communication rules                        |

---

### 1. End Devices

End devices are devices at the edge of a network that send or receive data.

Examples:

* Computer
* Laptop
* Smartphone
* Printer
* IP camera
* Server
* IoT device

```text
Laptop ───── Network ───── Server
```

---

### 2. NIC

**NIC = Network Interface Card/Controller**

A NIC allows a device to connect to a network.

Examples:

```text
Laptop
  ↓
Ethernet NIC
  ↓
Ethernet Cable
  ↓
Switch
```

Or:

```text
Laptop
  ↓
Wi-Fi NIC
  )))
Access Point
```

NICs are associated with **MAC addresses**, which are used for communication at the data-link layer.

---

### 3. Switch

A **switch connects devices within a LAN**.

```text
PC 1 ──┐
PC 2 ──┤
PC 3 ──┼── Switch
Printer┘
```

A switch primarily uses **MAC addresses** to forward Ethernet frames.

Example:

```text
PC 1 → Switch → PC 3
```

---

### 4. Router

A **router connects different networks**.

```text
Home LAN
   ↓
Router
   ↓
ISP
   ↓
Internet
```

Routers use **IP addresses and routing information** to determine where packets should go.

---

### 5. Access Point

An **Access Point (AP)** provides wireless network connectivity.

```text
Switch
   │
   │ Ethernet
   ↓
Access Point
  )))  )))  )))
 📱    💻    📺
```

The wireless devices connect to the AP using Wi-Fi.

---

### 6. Modem

A modem is equipment that provides a connection between local network equipment and an ISP's access network, depending on the Internet technology being used.

Example:

```text
Home Network
     ↓
  Router
     ↓
   Modem
     ↓
    ISP
```

Modern home devices often combine modem, router, switch, and wireless access point functions into one device.

---

### 7. Firewall

A firewall controls network traffic according to security rules.

```text
Internet
   ↓
Firewall
   ↓
Internal Network
```

It can allow or block traffic based on configured policies.

Firewalls are an important security control for protecting networks.

---

### 8. Server

A server provides services or resources to other systems called clients.

Examples:

* Web server
* DNS server
* File server
* Database server
* Mail server

```text
Client 1 ──┐
Client 2 ──┼── Network ── Server
Client 3 ──┘
```

---

### 9. Transmission Media

Transmission media provide the path through which data travels.

#### Wired

```text
PC ───── Ethernet ───── Switch
```

Examples:

* Copper Ethernet
* Fiber optic

#### Wireless

```text
Phone )))))) Wi-Fi )))))) Access Point
```

---

### 10. Protocols

Protocols are rules that define how network communication occurs.

Examples:

* IP
* TCP
* UDP
* DNS
* HTTP
* HTTPS
* DHCP
* Ethernet

---

## e. Data Transmission

### Definition

**Data transmission** is the process of transferring digital data from a sender to a receiver through a communication medium using established communication protocols.

In simple words:

> **Data transmission is the process of sending data from one device to another through a network.**

Example:

```text
Sender
  ↓
Network
  ↓
Receiver
```

---

### Sender and Receiver

```text
Sender                 Receiver
  💻 ───── Network ───── 🖥️
```

When uploading a file:

```text
Phone
  ↓
Network
  ↓
Server
```

The phone is the sender and the server is the receiver.

When downloading:

```text
Server
  ↓
Network
  ↓
Phone
```

The server becomes the sender and the phone becomes the receiver.

---

### Transmission Media

#### Wired Transmission

Data travels through physical media.

```text
PC ───────── Switch
      Ethernet
```

Examples:

* Ethernet
* Fiber optic

#### Wireless Transmission

Data is transmitted using wireless signals.

```text
Laptop
  )))
  ))) Wi-Fi
  )))
Access Point
```

Examples:

* Wi-Fi
* Bluetooth
* Cellular
* Satellite

---

### Data as Bits

Computers represent digital data using **bits**, which have values of 0 or 1.

Conceptually:

```text
Data
 ↓
Binary
 ↓
01001000...
```

As data moves through the networking stack, it is encapsulated into different units.

A simplified view is:

```text
Application Data
      ↓
Transport Segment / Datagram
      ↓
IP Packet
      ↓
Data-Link Frame
      ↓
Bits / Signals
      ↓
Transmission Medium
```

---

### Data is Divided Into Smaller Units

Large amounts of data are transferred using smaller units.

Conceptually:

```text
Large Data
    ↓
┌────┬────┬────┬────┬────┐
│ P1 │ P2 │ P3 │ P4 │ P5 │
└────┴────┴────┴────┴────┘
```

These units are transmitted through the network and processed/reassembled as needed at the destination.

---

### Data Transmission Modes

There are three common transmission modes.

#### Simplex

Communication occurs in **one direction only**.

```text
A ─────────→ B
```

Example:

```text
TV Station ─────→ TV
```

---

#### Half-Duplex

Communication can occur in **both directions, but not simultaneously**.

```text
A ─────→ B
A ←───── B
```

Example:

**Walkie-talkie**

One person communicates at a time.

---

#### Full-Duplex

Communication can occur in **both directions simultaneously**.

```text
A ─────────→ B
A ←───────── B
```

Example:

**Telephone conversation**

Both people can speak and listen at the same time.

---

### Bandwidth

**Bandwidth** refers to the capacity of a network link to carry data.

Examples:

```text
100 Mbps
1 Gbps
10 Gbps
```

A higher-capacity link can generally carry more data per second.

---

### Latency

**Latency** is the delay involved in communication.

For example:

```text
Computer → Server
```

If the communication takes 20 ms, that represents lower latency than 200 ms, assuming comparable measurements.

Low latency is important for:

* Online gaming
* Video calls
* Real-time applications

---

### Throughput

**Throughput** is the actual amount of data successfully transferred over a network in a given period.

Example:

```text
Link capacity: 100 Mbps
Actual throughput: 85 Mbps
```

Throughput can be lower than the theoretical link capacity due to:

* Network congestion
* Protocol overhead
* Interference
* Hardware limitations
* Packet loss

---

### Bandwidth vs Throughput vs Latency

| Term           | Meaning                            |
| -------------- | ---------------------------------- |
| **Bandwidth**  | Capacity of a network link         |
| **Throughput** | Actual data transfer rate achieved |
| **Latency**    | Delay in communication             |

A simple analogy:

```text
Bandwidth  = Number of lanes on a highway
Throughput = Number of cars actually passing
Latency    = Time taken for a car to reach the destination
```

---

# 🛡️ Networking Fundamentals and Cybersecurity

Understanding networking fundamentals is essential for cybersecurity.

A security professional needs to understand how traffic moves:

```text
Device
  ↓
LAN / WLAN
  ↓
Switch
  ↓
Router
  ↓
Firewall
  ↓
Internet
  ↓
Server
```

This helps security professionals understand:

* Source and destination IP addresses
* MAC addresses
* Ports
* Protocols
* Network traffic
* Network boundaries
* Routing
* Firewalls
* Suspicious communication

For example:

```text
Employee PC
     ↓
192.168.1.20
     ↓
TCP
     ↓
Port 443
     ↓
Internet
```

A SOC analyst can investigate whether this communication is expected or suspicious.

---

# 🧠 Quick Revision

```text
NETWORKING
│
├── What is Networking?
│      └── Connecting devices to communicate/share resources
│
├── Network Communication
│      └── Devices exchanging data
│
├── Network Architecture
│      └── Overall network design/blueprint
│
├── Network Components
│      ├── End Devices
│      ├── NIC
│      ├── Switch
│      ├── Router
│      ├── Access Point
│      ├── Modem
│      ├── Firewall
│      ├── Server
│      ├── Transmission Media
│      └── Protocols
│
└── Data Transmission
       ├── Sender
       ├── Receiver
       ├── Wired
       ├── Wireless
       ├── Simplex
       ├── Half-Duplex
       ├── Full-Duplex
       ├── Bandwidth
       ├── Throughput
       └── Latency
```
