# Understand Network Traffic Analysis

Network Traffic Analysis (NTA) is the process of **monitoring, examining, and analyzing network communication** to understand normal activity and identify suspicious or malicious behavior.

It helps security teams detect threats such as unauthorized access, malware communication, data theft, scanning, and unusual network activity.

---

## a. Packets

A **packet** is a small unit of data transmitted across a network.

When a device sends information, the data is divided into smaller pieces called packets. Each packet contains information that helps it reach the correct destination.

### Main parts of a packet

* **Source IP** – IP address of the device sending the packet.
* **Destination IP** – IP address of the receiving device.
* **Protocol** – Defines how the communication works, such as TCP, UDP, ICMP, or HTTP.
* **Source port** – Port used by the sender.
* **Destination port** – Port used by the receiving service.
* **Payload** – The actual data being transmitted.
* **Flags** – Control information used by protocols such as TCP.

### Example

A user opens a website:

```text
Client
  |
  | TCP packet
  | Source: 192.168.1.10:52000
  | Destination: 93.184.216.34:443
  ↓
Web Server
```

Security analysts can inspect packets using tools such as **Wireshark** to understand what is happening on the network.

### Security importance

Packet analysis can help identify:

* Port scanning
* Suspicious connections
* Malware communication
* Unusual protocols
* Data exfiltration
* Unauthorized connections

---

## b. Traffic Flows

A **traffic flow** represents communication between two network endpoints over a period of time.

Instead of examining every individual packet, analysts can study information about the overall communication.

A flow commonly contains:

```text
Source IP
Destination IP
Source Port
Destination Port
Protocol
Start Time
End Time
Number of Packets
Amount of Data
```

### Example

```text
192.168.1.10:51520
        ↓
    TCP/443
        ↓
142.250.195.14:443
```

This tells us that a device communicated with another system using TCP port 443.

### Why traffic flows are useful

Flow analysis can reveal:

* Which devices are communicating
* How much data is being transferred
* Which destinations are contacted
* Unusual communication patterns
* Potential command-and-control traffic

For example, if a workstation suddenly sends **large amounts of data to an unknown external IP**, the flow could be investigated for possible data exfiltration.

---

## c. Network Visibility

**Network visibility** means having enough information about network activity to understand what is happening inside the network.

Without visibility, security teams may not notice suspicious communication.

### Sources of network visibility

```text
Network Devices
      ↓
Firewalls
      ↓
IDS / IPS
      ↓
Packet Capture
      ↓
Flow Data
      ↓
Logs
      ↓
Security Monitoring
```

Network visibility can provide information about:

* Devices
* IP addresses
* Ports
* Protocols
* Connections
* DNS requests
* Network traffic
* Authentication activity

### Example

If an employee's computer suddenly communicates with an unfamiliar external server, good network visibility allows the security team to investigate that connection.

---

## d. Log Generation

A **log** is a record of an event that occurred on a system, application, or network device.

Network devices and security tools continuously generate logs about activities.

### Examples

**Firewall log:**

```text
2026-08-11 22:10:15
Source: 192.168.1.25
Destination: 10.10.10.5
Port: 22
Protocol: TCP
Action: BLOCK
```

**DNS log:**

```text
Client: 192.168.1.25
Query: suspicious-example.com
Response: 203.0.113.50
```

### Common sources of logs

* Firewalls
* Routers
* Switches
* Servers
* DNS servers
* Web servers
* IDS/IPS
* Endpoint security tools
* Authentication systems

Security teams can collect these logs in a **SIEM (Security Information and Event Management)** system to correlate events and detect suspicious behavior.

---

## e. Threat Indicators

**Threat indicators** are pieces of information that may indicate malicious or suspicious activity.

They are often called **Indicators of Compromise (IoCs)** when they provide evidence that a system may have been compromised.

### Common threat indicators

| Indicator              | Example                                         |
| ---------------------- | ----------------------------------------------- |
| Suspicious IP          | `203.0.113.50`                                  |
| Malicious domain       | `malicious-example.com`                         |
| Unusual port           | Unexpected connection to `4444`                 |
| Suspicious DNS request | Random-looking domain                           |
| Large data transfer    | Unusually high outbound traffic                 |
| Repeated connections   | Constant communication with one external server |
| Port scanning          | One device contacting many ports                |
| Unknown protocol       | Unexpected protocol usage                       |

### Example

Suppose a computer repeatedly connects to an unfamiliar external server:

```text
PC
 ↓
Internet
 ↓
Unknown IP
 ↓
Repeated connections
 ↓
Large outbound data
```

These combined indicators could suggest **malware communication or possible data exfiltration** and should be investigated.

---

## Simple Traffic Analysis Process

```text
Network Traffic
      ↓
   Packets
      ↓
 Traffic Flows
      ↓
 Network Visibility
      ↓
      Logs
      ↓
Analyze Activity
      ↓
Identify Threat Indicators
      ↓
Investigate / Respond
```

### Key idea

> **Network Traffic Analysis is about observing network communication, understanding what is normal, and identifying activity that may indicate a security threat.**
