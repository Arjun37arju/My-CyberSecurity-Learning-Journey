# Understand Network Devices

Network devices are hardware or security systems that **connect devices, control network traffic, and help protect networks**.

## Table of Contents

* [a. Routers](#a-routers)
* [b. Switches](#b-switches)
* [c. Firewalls](#c-firewalls)
* [d. IDS](#d-ids)
* [e. IPS](#e-ips)

---

## a. Routers

### Content

A **router** connects **different networks** and forwards data between them.

For example, your home router connects your **local network** to the **Internet**.

```text
Your Devices
     ↓
  Switch / Wi-Fi
     ↓
   Router
     ↓
  Internet
```

A router uses **IP addresses** to determine where network traffic should go.

**Easy idea:**

> **Router = Connects different networks and forwards traffic between them.**

### Practical Task

Create a simple network using a router in a **lab environment**.

Research:

* What a router does
* IP addresses
* Default gateway
* Routing
* How a home router connects to the Internet

### Deliverable

Create a router diagram:

```text
Internet
    ↓
 Router
    ↓
Local Network
 ┌──┼──┐
PC  PC Phone
```

Explain how data travels from a local device to the Internet.

**Goal:**

> Understand how routers connect networks and forward traffic.

---

## b. Switches

### Content

A **switch** connects multiple devices within a **local network (LAN)**.

```text
       Switch
      /  |  \
     ↓   ↓   ↓
    PC  PC  Printer
```

A switch uses **MAC addresses** to forward Ethernet frames to the appropriate device on the local network.

Example:

> If Computer A wants to communicate with Computer B on the same LAN, the switch helps deliver the frame to Computer B.

**Easy idea:**

> **Switch = Connects devices within a local network.**

### Practical Task

Research how a switch forwards traffic.

Understand:

* LAN
* MAC address
* Ethernet frame
* Switch ports
* MAC address table

### Deliverable

Create a diagram:

```text
PC 1 ──┐
PC 2 ──┤
PC 3 ──┼── Switch
Printer─┘
```

Then explain how the switch determines where to send a frame.

**Goal:**

> Understand how switches connect devices and forward traffic within a LAN.

---

## c. Firewalls

### Content

A **firewall** is a security system that **monitors and controls network traffic based on defined security rules**.

```text
Internet
    ↓
Firewall
    ↓
Internal Network
```

A firewall can evaluate traffic based on rules such as:

* Source IP
* Destination IP
* Port
* Protocol
* Connection state

Example:

```text
Internet
   ↓
Firewall
   ↓
Allowed Traffic → Internal Network
Blocked Traffic → ❌
```

A firewall can help prevent unauthorized network connections from reaching protected systems.

**Easy idea:**

> **Firewall = Controls network traffic using security rules.**

### Practical Task

Create a **firewall rules exercise** in a lab environment.

Example scenario:

> A company wants its web server to accept web traffic but block unnecessary incoming connections.

Create example rules such as:

| Traffic                           | Action | Reason          |
| --------------------------------- | ------ | --------------- |
| HTTP/HTTPS to Web Server          | Allow  | Web service     |
| SSH from authorized admin network | Allow  | Administration  |
| Unnecessary incoming traffic      | Block  | Reduce exposure |

Do not apply rules to systems you do not own or have permission to manage.

### Deliverable

Create a **Firewall Rules Report** containing:

```text
Rule:
Source:
Destination:
Protocol:
Port:
Action:
Reason:
```

**Goal:**

> Understand how firewalls use rules to control network traffic.

---

## d. IDS

### Content

**IDS (Intrusion Detection System)** monitors network or system activity for **suspicious or malicious behavior**.

When an IDS detects something suspicious, it can generate an **alert** for security analysts.

```text
Network Traffic
      ↓
     IDS
      ↓
Analyze Activity
      ↓
Suspicious?
   ↙       ↘
 Yes        No
  ↓          ↓
Alert       Continue
```

An IDS is primarily focused on **detecting and alerting**.

**Easy idea:**

> **IDS = Detects suspicious activity and generates alerts.**

### Practical Task

Set up or use an IDS in an **authorized security lab**.

Observe:

* Normal network traffic
* Security alerts
* Alert details
* Source and destination information
* Detection rules

Then investigate why an alert was generated.

### Deliverable

Create an **IDS Alert Analysis**:

```text
Alert:
Date/Time:
Source:
Destination:
Detected Activity:
Why Was It Detected?
Severity:
Recommended Response:
```

**Goal:**

> Learn how an IDS detects suspicious activity and reports it to security teams.

---

## e. IPS

### Content

**IPS (Intrusion Prevention System)** monitors network traffic and can **automatically take action against detected malicious or suspicious traffic**.

```text
Network Traffic
      ↓
     IPS
      ↓
Analyze Traffic
      ↓
Suspicious?
   ↙       ↘
 Yes        No
  ↓          ↓
Block       Allow
```

Unlike an IDS, an IPS can be placed **inline** so that it can actively block or prevent certain traffic according to its rules.

**Easy idea:**

> **IPS = Detects suspicious activity and can automatically block it.**

### Practical Task

Use an IPS in an **authorized lab environment**.

Create a controlled test scenario where the IPS detects traffic matching a known security rule.

Observe:

* Detection
* Alert
* Action taken
* Whether traffic was blocked
* Logs generated

### Deliverable

Create an **IPS Detection Report**:

```text
Detected Activity:
Source:
Destination:
Detection Rule:
Action Taken:
Blocked / Allowed:
Log Evidence:
Result:
```

**Goal:**

> Understand how an IPS can detect and actively prevent suspicious network activity.

---

# Final Comparison

After studying all five devices, compare their main purposes.

| Device   | Main Purpose                              |
| -------- | ----------------------------------------- |
| Router   | Connects different networks               |
| Switch   | Connects devices within a LAN             |
| Firewall | Controls traffic using security rules     |
| IDS      | Detects suspicious activity and alerts    |
| IPS      | Detects and can block suspicious activity |

### Easy Way to Remember

```text
Router
  ↓
Connects Networks

Switch
  ↓
Connects Devices

Firewall
  ↓
Controls Traffic

IDS
  ↓
Detects + Alerts

IPS
  ↓
Detects + Blocks
```

---

# Final Practical Project

Create a **Network Devices Security Lab** showing how these devices work together.

```text
                    Internet
                       ↓
                    Router
                       ↓
                   Firewall
                       ↓
                    Switch
                 ┌─────┼─────┐
                 ↓     ↓     ↓
                PC    PC   Server
                       ↑
                      IDS
                       ↑
                      IPS
```

### Final Challenge

Create a network diagram containing:

* Router
* Switch
* Firewall
* IDS
* IPS
* At least 2 computers
* A server

Then explain:

1. What each device does
2. Where each device is placed
3. How traffic moves through the network
4. Which device controls traffic
5. Which device detects suspicious activity
6. Which device can block suspicious traffic

### Final Deliverable

Create a GitHub project:

```text
Network-Devices/
│
├── README.md
├── routers.md
├── switches.md
├── firewalls.md
├── ids.md
├── ips.md
├── device-comparison.md
└── diagrams/
    └── network-security-lab.png
```

### Expected Result

After completing this project, you should be able to:

* Explain what routers do
* Explain what switches do
* Understand how firewalls control traffic
* Understand how IDS detects suspicious activity
* Understand how IPS can prevent suspicious activity
* Compare the roles of network and security devices
* Design a basic network security architecture

> **Connect → Forward → Control → Detect → Prevent**
