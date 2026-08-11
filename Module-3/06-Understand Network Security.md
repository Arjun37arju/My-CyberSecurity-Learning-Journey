# Understand Network Security

**Network security** focuses on protecting networks, devices, and data from unauthorized access, misuse, and security threats.

## Table of Contents

* [a. Secure Communication](#a-secure-communication)
* [b. Network Segmentation](#b-network-segmentation)
* [c. Access Control](#c-access-control)
* [d. VPN Concepts](#d-vpn-concepts)
* [e. Security Monitoring](#e-security-monitoring)

---

## a. Secure Communication

### Content

**Secure communication** protects data while it is being transmitted between devices.

Security technologies such as **encryption** help prevent unauthorized users from reading or modifying communication.

```text
Device A
   ↓
Encrypted Communication
   ↓
Network
   ↓
Device B
```

Examples include:

* HTTPS
* SSH
* TLS
* VPN encryption

**Easy idea:**

> **Secure Communication = Protecting data while it travels across a network.**

---

## b. Network Segmentation

### Content

**Network segmentation** is the process of dividing a network into **separate sections**.

Segmentation can help limit access between different parts of a network and reduce the impact of security incidents.

```text
                Network
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      Users      Servers    Guests
      Network    Network    Network
```

For example, a company may separate:

* Employee devices
* Servers
* Guest devices

**Easy idea:**

> **Network Segmentation = Dividing a network into separate sections.**

---

## c. Access Control

### Content

**Access control** determines **who or what is allowed to access a resource**.

A simple access-control process is:

```text
User
 ↓
Authentication
 ↓
Authorization
 ↓
Resource
```

For example:

> A user logs into a system and is allowed to access only the files they have permission to use.

Access control can involve:

* Users
* Roles
* Permissions
* Authentication
* Authorization

**Easy idea:**

> **Access Control = Decide who can access what.**

---

## d. VPN Concepts

### Content

A **VPN (Virtual Private Network)** creates a protected connection between a device and a network or between networks.

```text
Your Device
     ↓
  VPN Tunnel
     ↓
   Internet
     ↓
VPN Server / Network
```

A VPN can use encryption to protect traffic while it travels across an untrusted network.

Common VPN concepts include:

* VPN client
* VPN server
* VPN tunnel
* Encryption
* Authentication

**Easy idea:**

> **VPN = Creates a protected connection over a network.**

---

## e. Security Monitoring

### Content

**Security monitoring** is the process of observing network and system activity to identify **suspicious or potentially malicious behavior**.

```text
Network Activity
       ↓
Monitoring
       ↓
Logs / Events
       ↓
Analysis
       ↓
Alert
```

Security monitoring can involve:

* Network traffic
* System logs
* Authentication events
* Security alerts
* Suspicious activity

**Easy idea:**

> **Security Monitoring = Observe activity → detect suspicious behavior → investigate.**
