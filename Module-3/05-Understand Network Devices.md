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

For example, your home router connects your **local network** to the Internet.

```text id="i9t0ae"
Your Devices
     ↓
  Router
     ↓
  Internet
```

A router uses **IP addresses** to determine where network traffic should go.

Routers can also provide functions such as:

* Routing
* NAT
* DHCP
* Default gateway
* Basic network filtering

**Easy idea:**

> **Router = Connects different networks and forwards traffic between them.**

---

## b. Switches

### Content

A **switch** connects multiple devices within a **local network (LAN)**.

```text id="v4f5l4"
       Switch
      /  |  \
     ↓   ↓   ↓
    PC  PC  Printer
```

A switch uses **MAC addresses** to forward Ethernet frames to the appropriate device on the local network.

A switch maintains a **MAC address table** to learn which devices are connected to which switch ports.

**Easy idea:**

> **Switch = Connects devices within a local network.**

---

## c. Firewalls

### Content

A **firewall** is a security system that **monitors and controls network traffic based on defined security rules**.

```text id="r1m2n9"
Internet
    ↓
 Firewall
    ↓
Internal Network
```

A firewall can evaluate traffic based on:

* Source IP
* Destination IP
* Port
* Protocol
* Connection state

Example:

```text id="g4up7c"
Internet
   ↓
Firewall
   ↓
Allowed Traffic → Internal Network
Blocked Traffic → ❌
```

Firewalls help prevent unauthorized connections and control which network traffic is allowed or blocked.

**Easy idea:**

> **Firewall = Controls network traffic using security rules.**

---

## d. IDS

### Content

**IDS (Intrusion Detection System)** monitors network or system activity for **suspicious or potentially malicious behavior**.

```text id="u9g5dy"
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

When an IDS detects suspicious activity, it generates an **alert** for security analysts.

An IDS is mainly focused on **detection and alerting** rather than automatically blocking the traffic.

**Easy idea:**

> **IDS = Detects suspicious activity and generates alerts.**

---

## e. IPS

### Content

**IPS (Intrusion Prevention System)** monitors network traffic and can **automatically take action against detected malicious or suspicious traffic**.

```text id="s8xq7k"
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

An IPS is commonly placed **inline** in the network so it can inspect traffic and take action when a security rule is triggered.

Unlike an IDS, an IPS can **actively block or prevent** certain traffic.

**Easy idea:**

> **IPS = Detects suspicious activity and can block it.**

---

## Quick Comparison

| Device       | Main Purpose                              |
| ------------ | ----------------------------------------- |
| **Router**   | Connects different networks               |
| **Switch**   | Connects devices within a LAN             |
| **Firewall** | Controls network traffic                  |
| **IDS**      | Detects suspicious activity and alerts    |
| **IPS**      | Detects and can block suspicious activity |

### Easy Way to Remember

```text id="gqz6jv"
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
