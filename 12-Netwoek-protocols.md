# 3. Understand Network Protocols

Network protocols are **rules that allow computers and devices to communicate with each other**.

---

## a. HTTP

**HTTP (HyperText Transfer Protocol)** is used to **transfer web pages between a browser and a web server**.

```text
Browser
   ↓
 HTTP
   ↓
Web Server
```

Example:

> You open a website → HTTP helps your browser communicate with the server.

**Port:** `80`

**Easy idea:**

> **HTTP = Used for web communication.**

---

## b. HTTPS

**HTTPS (HyperText Transfer Protocol Secure)** is the **secure version of HTTP**.

It encrypts the communication between your browser and the server.

```text
Browser
   ↓
 HTTPS
   ↓
Encrypted Communication
   ↓
Web Server
```

Example:

> You open your bank's website → HTTPS helps protect the communication.

**Port:** `443`

**Easy idea:**

> **HTTPS = Secure web communication.**

---

## c. DNS

**DNS (Domain Name System)** converts a **domain name into an IP address**.

Example:

```text
google.com
    ↓
   DNS
    ↓
142.250.x.x
```

You remember the website name, but the network uses an **IP address** to communicate.

**Port:** `53`

**Easy idea:**

> **DNS = Name → IP address.**

---

## d. DHCP

**DHCP (Dynamic Host Configuration Protocol)** automatically gives network settings to a device.

When your laptop joins Wi-Fi:

```text
Laptop
   ↓
 DHCP
   ↓
IP Address
Subnet Mask
Gateway
DNS
```

Example:

> You connect your laptop to Wi-Fi → DHCP automatically provides the network configuration.

**Ports:** `67 / 68`

**Easy idea:**

> **DHCP = Automatically gives your device network configuration.**

---

## e. FTP

**FTP (File Transfer Protocol)** is used to **transfer files between computers**.

```text
Computer
    ↓
   FTP
    ↓
Server
```

Example:

> Uploading or downloading files from an FTP server.

**Ports:** `20 / 21`

**Easy idea:**

> **FTP = File transfer.**

---

## f. SMTP

**SMTP (Simple Mail Transfer Protocol)** is used to **send email**.

```text
Your Email
    ↓
  SMTP
    ↓
Mail Server
    ↓
Receiver's Mail Server
```

Example:

> You send an email → SMTP helps deliver the email to the mail server.

**Common ports:** `25 / 465 / 587`

**Easy idea:**

> **SMTP = Sends email.**

---

## g. SSH

**SSH (Secure Shell)** allows you to **securely connect to and control another computer remotely**.

```text
Your PC
   ↓
  SSH
   ↓
Remote Server
```

Example:

> You connect to a Linux server and use its terminal remotely.

**Port:** `22`

**Easy idea:**

> **SSH = Secure remote access.**

---

# Quick Revision

```text
HTTP  → Web communication
HTTPS → Secure web communication
DNS   → Name → IP address
DHCP  → Gives network configuration
FTP   → File transfer
SMTP  → Sends email
SSH   → Secure remote access
```

## Ports to Remember

```text
HTTP  → 80
HTTPS → 443
DNS   → 53
DHCP  → 67 / 68
FTP   → 20 / 21
SMTP  → 25 / 465 / 587
SSH   → 22
```
