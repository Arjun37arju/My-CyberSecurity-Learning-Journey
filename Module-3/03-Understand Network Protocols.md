# Understand Network Protocols

Network protocols are **rules that allow devices and systems to communicate over a network**.

## Table of Contents

* [a. HTTP](#a-http)
* [b. HTTPS](#b-https)
* [c. DNS](#c-dns)
* [d. DHCP](#d-dhcp)
* [e. FTP](#e-ftp)
* [f. SMTP](#f-smtp)
* [g. SSH](#g-ssh)

---

## a. HTTP

### Content

**HTTP (Hypertext Transfer Protocol)** is used to **transfer web resources between a browser and a web server**.

```text
Browser
   ↓
HTTP Request
   ↓
Web Server
   ↓
HTTP Response
   ↓
Browser
```

Example:

> You open a website → your browser sends a request to the web server → the server sends the requested content back.

**Easy idea:**

> **HTTP = Web communication.**

---

## b. HTTPS

### Content

**HTTPS (Hypertext Transfer Protocol Secure)** is the **secure version of HTTP**.

HTTPS uses **TLS (Transport Layer Security)** to protect communication between the client and server.

```text
Browser
   ↓
HTTPS
   ↓
Encrypted Communication
   ↓
Web Server
```

HTTPS helps protect data from being easily read or modified while it travels between the client and server.

**Easy idea:**

> **HTTPS = Secure web communication.**

---

## c. DNS

### Content

**DNS (Domain Name System)** converts **domain names into IP addresses** so devices can locate network services.

Example:

```text
google.com
     ↓
    DNS
     ↓
IP Address
```

Instead of remembering an IP address, users can use an easy-to-remember domain name.

**Easy idea:**

> **DNS = Domain name → IP address.**

---

## d. DHCP

### Content

**DHCP (Dynamic Host Configuration Protocol)** automatically provides network configuration to devices.

When a device joins a network, DHCP can provide:

* IP address
* Subnet mask
* Default gateway
* DNS server

A common DHCP process is called **DORA**:

```text
Discover
   ↓
Offer
   ↓
Request
   ↓
Acknowledge
```

**Easy idea:**

> **DHCP = Automatically gives devices network configuration.**

---

## e. FTP

### Content

**FTP (File Transfer Protocol)** is used to **transfer files between a client and a server**.

```text
Client
   ↓
FTP
   ↓
FTP Server
```

FTP can be used for:

* Uploading files
* Downloading files
* Managing files on a server

FTP itself does **not provide encryption for the transferred data**.

**Easy idea:**

> **FTP = File transfer between systems.**

---

## f. SMTP

### Content

**SMTP (Simple Mail Transfer Protocol)** is used mainly for **sending email between mail systems and from email clients to mail servers**.

```text
Sender
   ↓
SMTP
   ↓
Mail Server
   ↓
Receiver's Mail Server
   ↓
Receiver
```

SMTP is mainly associated with **sending email**.

Other protocols, such as IMAP and POP3, are commonly used for retrieving email.

**Easy idea:**

> **SMTP = Sends email.**

---

## g. SSH

### Content

**SSH (Secure Shell)** is a protocol used to **securely connect to and manage a remote computer or server**.

```text
Your Computer
      ↓
     SSH
      ↓
Remote Server
```

SSH provides an **encrypted connection** for remote administration.

Example:

> A security professional connects to a Linux server remotely and manages it through a terminal.

**Easy idea:**

> **SSH = Secure remote access.**
