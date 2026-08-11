#  Understand Network Security

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

Security technologies such as **encryption** help prevent unauthorized users from reading or modifying the communication.

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

### Practical Task

Research how secure communication works using **HTTPS and SSH**.

Compare:

* Normal communication
* Encrypted communication
* Encryption
* Authentication
* Data protection

### Deliverable

Create a comparison:

| Feature         | Normal Communication | Secure Communication |
| --------------- | -------------------- | -------------------- |
| Encryption      |                      |                      |
| Data Protection |                      |                      |
| Authentication  |                      |                      |
| Example         |                      |                      |

**Goal:**

> Understand how encryption and secure protocols protect network communication.

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

### Practical Task

Design a small company network with three segments:

```text
Users
Servers
Guest Network
```

Decide:

* Which devices belong in each segment
* Which segments should communicate
* Which communication should be restricted

### Deliverable

Create a network segmentation diagram:

```text
Internet
    ↓
Firewall
    ↓
 ┌──┼──────────┐
 ↓  ↓          ↓
Users Servers Guests
```

Then explain why the network was divided.

**Goal:**

> Understand how segmentation can separate systems and reduce security risk.

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

### Practical Task

Create an access-control plan for a small organization.

Example roles:

* Administrator
* Developer
* Employee
* Guest

Assign appropriate access to:

* Company files
* Servers
* Applications
* Network resources

### Deliverable

Create an access-control matrix:

| Resource          | Administrator | Developer | Employee | Guest |
| ----------------- | ------------- | --------- | -------- | ----- |
| Company Files     |               |           |          |       |
| Server            |               |           |          |       |
| Applications      |               |           |          |       |
| Network Resources |               |           |          |       |

Use:

```text
Full Access
Read
Limited
No Access
```

**Goal:**

> Understand how permissions and authorization control access to network resources.

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

### Practical Task

Research how a VPN works.

Understand:

* VPN client
* VPN server
* VPN tunnel
* Encryption
* Authentication
* VPN use cases

Then create a simple VPN lab using an authorized environment if available.

### Deliverable

Create a VPN diagram:

```text
Your Computer
      ↓
Encrypted VPN Tunnel
      ↓
VPN Server
      ↓
Private Network
```

Explain what happens when the VPN connection is established.

**Goal:**

> Understand the basic concept of VPNs and how they provide protected network connections.

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

### Practical Task

Set up basic security monitoring in an **authorized lab environment**.

Collect and analyze examples of:

* Login events
* Failed login attempts
* Network connections
* System events
* Security alerts

### Deliverable

Create a **Security Monitoring Report**:

```text
Event:
Date/Time:
Source:
Activity:
Why It Is Important:
Severity:
Investigation:
Recommended Action:
```

Analyze at least **5 security events**.

**Goal:**

> Understand how security monitoring helps identify and investigate suspicious activity.

---

# Final Practical Project

Create a **Network Security Lab** combining all five concepts.

```text
                    Internet
                       ↓
                    Firewall
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
           VPN Server        Network
                                ↓
                    ┌───────────┼───────────┐
                    ↓           ↓           ↓
                  Users       Servers     Guests
                    ↓           ↓           ↓
                 Access      Access      Restricted
                 Control     Control       Access
                    │
                    ↓
             Security Monitoring
```

### Final Challenge

Design a secure network for a small organization.

Your design should include:

* Secure communication
* Network segmentation
* Access control
* VPN
* Security monitoring

Then document:

1. How communication is protected
2. How the network is segmented
3. Who can access each resource
4. Where the VPN is used
5. What security events are monitored

### Final Deliverable

Create a GitHub project:

```text
Network-Security/
│
├── README.md
├── secure-communication.md
├── network-segmentation.md
├── access-control.md
├── vpn-concepts.md
├── security-monitoring.md
└── diagrams/
    └── network-security-lab.png
```

### Expected Result

After completing this module, you should be able to:

* Explain secure network communication
* Understand network segmentation
* Understand access control
* Explain basic VPN concepts
* Understand security monitoring
* Design a basic network security architecture

> **Protect → Separate → Control → Secure → Monitor**
