# Understand IP Addressing

**IP addressing** is used to identify devices and networks so that data can be delivered to the correct destination.

## Table of Contents

* [a. IPv4](#a-ipv4)
* [b. IPv6](#b-ipv6)
* [c. Public IPs](#c-public-ips)
* [d. Private IPs](#d-private-ips)
* [e. Subnetting Fundamentals](#e-subnetting-fundamentals)

---

## a. IPv4

### Content

**IPv4 (Internet Protocol version 4)** is a commonly used addressing system for identifying devices on a network.

An IPv4 address contains **32 bits**, divided into **4 octets**.

Example:

```text
192.168.1.10
```

Each octet contains **8 bits** and can have a value from **0 to 255**.

```text
192    .    168    .    1    .    10
 ↓          ↓          ↓         ↓
8 bits     8 bits     8 bits    8 bits

              = 32 bits
```

### IPv4 Notation

IPv4 can be represented using:

**Dotted Decimal Notation**

```text
192.168.1.10
```

**Binary Notation**

```text
11000000.10101000.00000001.00001010
```

**CIDR Notation**

```text
192.168.1.10/24
```

The `/24` indicates that **24 bits are used for the network portion**.

### IPv4 Address Structure

```text
Network Portion | Host Portion
       ↓               ↓
192.168.1       |      10
```

The exact network and host portions depend on the **subnet mask or CIDR prefix**.

**Easy idea:**

> **IPv4 = 32-bit address written as four decimal numbers.**

---

## b. IPv6

### Content

**IPv6 (Internet Protocol version 6)** was developed to provide a much larger address space than IPv4.

IPv6 uses **128 bits**.

Example:

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

An IPv6 address contains **8 groups**, called hextets.

Each hextet contains **16 bits** and is written using hexadecimal characters.

```text
2001 : 0db8 : 85a3 : 0000 : 0000 : 8a2e : 0370 : 7334
  ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓
16     16     16     16     16     16     16     16 bits

                    = 128 bits
```

### IPv6 Notation

IPv6 addresses can be shortened using **zero compression**.

For example:

```text
2001:0db8:0000:0000:0000:0000:0000:0001
```

Can be written as:

```text
2001:db8::1
```

The `::` represents consecutive groups of zeros.

### IPv6 CIDR Notation

Example:

```text
2001:db8::/64
```

The `/64` indicates that the first **64 bits** represent the network prefix.

**Easy idea:**

> **IPv6 = 128-bit address written using hexadecimal and colons.**

---

## c. Public IPs

### Content

A **public IP address** is an IP address used for communication over the **public Internet**.

```text
Your Network
     ↓
Public IP
     ↓
Internet
     ↓
Internet Server
```

A public IP is normally assigned to your Internet connection by your **Internet Service Provider (ISP)**.

Example:

```text
203.0.113.10
```

Public IP addresses must be globally unique within their routing context so that Internet traffic can reach the correct destination.

### Public IPv4

Public IPv4 addresses are generally addresses that are **not reserved for private or special purposes**.

For example:

```text
8.8.8.8
```

is a public IPv4 address.

**Easy idea:**

> **Public IP = Address used to communicate across the public Internet.**

---

## d. Private IPs

### Content

A **private IP address** is used inside a **local/private network**.

Private IPv4 addresses are not directly routable across the public Internet.

### Private IPv4 Ranges

| Range                           | CIDR  | Common Use             |
| ------------------------------- | ----- | ---------------------- |
| `10.0.0.0 – 10.255.255.255`     | `/8`  | Large private networks |
| `172.16.0.0 – 172.31.255.255`   | `/12` | Private networks       |
| `192.168.0.0 – 192.168.255.255` | `/16` | Home/small networks    |

Example:

```text
Laptop      → 192.168.1.10
Phone       → 192.168.1.11
Printer     → 192.168.1.12
```

These devices can communicate within the local network.

```text
Laptop
   ↓
Private Network
   ↓
Router
   ↓
Public Internet
```

A router commonly uses **NAT (Network Address Translation)** to allow private devices to communicate with the Internet using a public IP.

**Easy idea:**

> **Private IP = Address used inside a local or private network.**

---

## e. Subnetting Fundamentals

### Content

**Subnetting** is the process of dividing one network into **smaller logical networks called subnets**.

```text
Large Network
      ↓
 ┌────┼────┬────┐
 ↓    ↓    ↓    ↓
Subnet Subnet Subnet Subnet
```

Subnetting helps with:

* Organizing networks
* Managing IP addresses
* Separating network sections
* Controlling network traffic
* Efficiently using IP addresses

### Subnet Mask

A **subnet mask** determines which part of an IPv4 address represents the **network** and which part represents the **host**.

Example:

```text
IP Address:
192.168.1.10

Subnet Mask:
255.255.255.0
```

This is commonly represented as:

```text
192.168.1.10/24
```

### CIDR Notation

**CIDR (Classless Inter-Domain Routing)** uses `/number` notation to represent the network prefix.

Examples:

```text
192.168.1.0/24
192.168.1.0/25
192.168.1.0/26
192.168.1.0/27
192.168.1.0/28
```

The number after `/` represents the number of **network bits**.

For IPv4:

```text
/8   → 8 network bits
/16  → 16 network bits
/24  → 24 network bits
/32  → 32 network bits
```

### Common IPv4 CIDR Notations

| CIDR  | Subnet Mask       | Total Addresses |
| ----- | ----------------- | --------------: |
| `/8`  | `255.0.0.0`       |      16,777,216 |
| `/16` | `255.255.0.0`     |          65,536 |
| `/24` | `255.255.255.0`   |             256 |
| `/25` | `255.255.255.128` |             128 |
| `/26` | `255.255.255.192` |              64 |
| `/27` | `255.255.255.224` |              32 |
| `/28` | `255.255.255.240` |              16 |
| `/29` | `255.255.255.248` |               8 |
| `/30` | `255.255.255.252` |               4 |
| `/32` | `255.255.255.255` |               1 |

For a typical IPv4 subnet, some addresses have special purposes:

```text
Network Address
      ↓
192.168.1.0

Usable Host Addresses
      ↓
192.168.1.1 – 192.168.1.254

Broadcast Address
      ↓
192.168.1.255
```

So a `/24` network has:

```text
256 total addresses
      ↓
1 Network Address
254 Usable Host Addresses
1 Broadcast Address
```

**Easy idea:**

> **Subnetting = Dividing a larger network into smaller networks using subnet masks and CIDR notation.**
