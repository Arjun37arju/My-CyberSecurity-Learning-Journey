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

**IPv4 (Internet Protocol version 4)** is a widely used addressing system for identifying devices on a network.

An IPv4 address contains **32 bits** and is written as four numbers separated by dots.

Example:

```text
192.168.1.10
```

Each part is called an **octet** and can contain a value from **0 to 255**.

```text
192 . 168 . 1 . 10
 ↑     ↑     ↑    ↑
Octet Octet Octet Octet
```

**Easy idea:**

> **IPv4 = 32-bit IP address written as four numbers.**

---

## b. IPv6

### Content

**IPv6 (Internet Protocol version 6)** is the newer version of the Internet Protocol and provides a much larger address space than IPv4.

IPv6 uses **128-bit addresses** and is written using hexadecimal numbers separated by colons.

Example:

```text
2001:db8:abcd:0012::1
```

IPv6 provides a much larger number of possible addresses than IPv4.

**Easy idea:**

> **IPv6 = 128-bit IP addressing with a much larger address space.**

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
```

A public IP is typically assigned to your Internet connection by your **Internet Service Provider (ISP)**.

**Easy idea:**

> **Public IP = Address used for communication on the Internet.**

---

## d. Private IPs

### Content

A **private IP address** is used inside a **local or private network**.

Common private IPv4 ranges are:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Example:

```text
Laptop     → 192.168.1.10
Phone      → 192.168.1.11
Printer    → 192.168.1.12
```

Private IP addresses are commonly used in homes, offices, and other internal networks.

**Easy idea:**

> **Private IP = Address used inside a private/local network.**

---

## e. Subnetting Fundamentals

### Content

**Subnetting** is the process of dividing a network into **smaller logical networks called subnets**.

```text
Large Network
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
Subnet Subnet Subnet
```

Subnetting helps with:

* Organizing networks
* Managing IP addresses
* Separating network sections
* Improving network design

Subnetting commonly uses **CIDR notation**.

Example:

```text
192.168.1.0/24
```

The `/24` represents the number of bits used for the network portion of the address.

A `/24` IPv4 network contains **256 total addresses**.

**Easy idea:**

> **Subnetting = Dividing one network into smaller networks.**
