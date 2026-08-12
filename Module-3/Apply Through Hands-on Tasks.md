#  Apply Through Hands-on Tasks

Hands-on tasks help you **apply networking concepts in practical environments**. Instead of only learning theory, you perform actual network analysis, calculations, configuration, and investigation.

## a. Analyze Packet Captures

### Content

Packet capture analysis involves examining network packets to understand how devices communicate.

You can use tools such as **Wireshark** to analyze:

* Source and destination IP addresses
* Source and destination ports
* Protocols
* Packet size
* TCP flags
* Packet flow
* DNS requests
* HTTP/HTTPS communication

### Practical Task

Capture or open a packet capture file in Wireshark.

Identify:

1. Source IP address
2. Destination IP address
3. Protocol
4. Source and destination ports
5. Important packet information

### Deliverable

| Packet | Source IP | Destination IP | Protocol | Port | Observation |
| ------ | --------- | -------------- | -------- | ---- | ----------- |
| 1      |           |                |          |      |             |
| 2      |           |                |          |      |             |
| 3      |           |                |          |      |             |

**Goal:**

> Develop practical skills in understanding network communication by analyzing real packet data.

---

## b. Perform Subnet Calculations

### Content

Subnet calculations are used to determine how an IP network can be divided into smaller networks.

You should practice identifying:

* Network address
* Broadcast address
* Subnet mask
* Number of subnets
* Number of usable hosts
* Host range
* CIDR notation

### Practical Task

Take an IP address and subnet, for example:

```text
IP Address: 192.168.10.25
Subnet Mask: 255.255.255.0
```

Determine:

```text
Network Address:
Broadcast Address:
First Usable Host:
Last Usable Host:
Number of Usable Hosts:
CIDR:
```

Repeat the calculation using different subnet masks.

### Deliverable

| IP Address | Subnet Mask | Network | Broadcast | Usable Hosts |
| ---------- | ----------- | ------- | --------- | ------------ |
|            |             |         |           |              |
|            |             |         |           |              |
|            |             |         |           |              |

**Goal:**

> Build confidence in calculating network ranges and determining how IP addresses are organized into subnets.

---

## c. Identify Network Protocols

### Content

Network protocols define how devices communicate across a network.

You should be able to identify common protocols such as:

* TCP
* UDP
* HTTP
* HTTPS
* DNS
* DHCP
* ARP
* ICMP
* FTP
* SSH

### Practical Task

Use Wireshark or another network-analysis tool to observe network traffic.

Identify the protocols being used and determine their purpose.

### Deliverable

| Protocol | Port | Purpose | Example Usage |
| -------- | ---- | ------- | ------------- |
| TCP      |      |         |               |
| UDP      |      |         |               |
| DNS      |      |         |               |
| HTTP     |      |         |               |
| HTTPS    |      |         |               |

**Goal:**

> Develop the ability to recognize network protocols and understand their role in network communication.

---

## d. Build Network Diagrams

### Content

Network diagrams provide a visual representation of network devices and their connections.

A basic network diagram may contain:

```text
PC
 │
 │
Switch
 │
 │
Router
 │
 │
Internet
```

You can create network diagrams using **Cisco Packet Tracer**.

Include devices such as:

* PCs
* Switches
* Routers
* Servers
* Wireless devices
* Connections
* IP addresses

### Practical Task

Build a small network in Cisco Packet Tracer.

For example:

```text
PC1 ──┐
      │
PC2 ──┤
      │
     Switch ─── Router ─── Server
      │
PC3 ──┘
```

Configure IP addresses and verify connectivity using `ping`.

### Deliverable

Create a network diagram showing:

* Network devices
* Device connections
* IP addresses
* Network/subnet information
* Communication paths

**Goal:**

> Gain practical experience designing and understanding network topologies using a network simulation environment.

---

## e. Investigate Network Incidents

### Content

Network incident investigation involves examining network activity to determine whether suspicious or abnormal behavior has occurred.

You can investigate indicators such as:

* Repeated connection attempts
* Unusual ports
* Suspicious IP addresses
* Port scanning
* Abnormal traffic
* Failed connections
* Unexpected communication
* Large amounts of data transfer

### Practical Task

Use a sample packet capture, logs, or a simulated network incident.

Investigate:

1. What happened?
2. Which systems were involved?
3. What protocols were used?
4. Was the traffic normal or suspicious?
5. What evidence supports your conclusion?
6. What security action could be taken?

### Deliverable

Create a **Network Incident Investigation Report**:

```text
Incident:
Date / Time:

Source System:
Destination System:

Protocols Observed:

Suspicious Activity:

Evidence:

Analysis:

Impact:

Recommended Action:

Final Conclusion:
```

**Goal:**

> Develop practical skills in identifying, analyzing, and documenting suspicious network activity.
