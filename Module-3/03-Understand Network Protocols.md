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

### Practical Task

Open a website and research:

* What HTTP is
* HTTP request
* HTTP response
* Common HTTP methods
* HTTP status codes

### Deliverable

Create an HTTP communication diagram and explain:

```text
Browser → Request → Server
Browser ← Response ← Server
```

**Goal:**

> Understand how browsers communicate with web servers using HTTP.

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

### Practical Task

Compare HTTP and HTTPS.

Research:

* HTTP
* HTTPS
* TLS
* Encryption
* Certificates
* Why HTTPS is important

### Deliverable

Create a comparison:

| Feature    | HTTP | HTTPS |
| ---------- | ---- | ----- |
| Security   |      |       |
| Encryption |      |       |
| TLS        |      |       |
| Common Use |      |       |

**Goal:**

> Understand why HTTPS is used to secure web communication.

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

### Practical Task

Research how DNS works when you open a website.

Understand:

* Domain name
* DNS resolver
* DNS server
* IP address
* DNS response

### Deliverable

Create a DNS flow diagram:

```text
Your Computer
      ↓
DNS Resolver
      ↓
DNS Server
      ↓
IP Address
      ↓
Your Computer
```

Then explain the process in your own words.

**Goal:**

> Understand how DNS helps devices find websites and network services.

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

Example:

```text
Laptop
   ↓
DHCP Request
   ↓
DHCP Server
   ↓
IP Configuration
   ↓
Laptop
```

**Easy idea:**

> **DHCP = Automatically gives devices network configuration.**

### Practical Task

Research the DHCP DORA process.

Explain:

1. DHCP Discover
2. DHCP Offer
3. DHCP Request
4. DHCP Acknowledgment

### Deliverable

Create a DHCP flow diagram and explain what happens at each step.

**Goal:**

> Understand how devices automatically receive network configuration.

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

FTP can be used for activities such as:

* Uploading files
* Downloading files
* Managing files on a server

FTP itself does **not provide encryption for the transferred data**.

**Easy idea:**

> **FTP = File transfer between systems.**

### Practical Task

Research:

* FTP client
* FTP server
* Upload
* Download
* FTP security limitations
* Secure alternatives such as SFTP

### Deliverable

Create a simple FTP communication diagram and explain how file transfer works.

**Goal:**

> Understand the purpose of FTP and why secure file-transfer methods are important.

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

SMTP is mainly associated with **sending** email.

Other protocols, such as IMAP and POP3, are commonly used for retrieving email.

**Easy idea:**

> **SMTP = Sends email.**

### Practical Task

Research how an email travels from one user to another.

Understand:

* Email client
* SMTP server
* Sender's mail server
* Receiver's mail server
* Email delivery

### Deliverable

Create an email flow diagram:

```text
Sender
  ↓
SMTP Server
  ↓
Internet
  ↓
Receiver Mail Server
  ↓
Receiver
```

Then explain the process.

**Goal:**

> Understand how SMTP is used to send and deliver email.

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

SSH provides an encrypted connection for remote administration.

Example:

> A security professional connects to a Linux server remotely and manages it through a terminal.

**Easy idea:**

> **SSH = Secure remote access.**

### Practical Task

Set up an SSH connection in an **authorized lab environment**.

Practice:

* Connecting to a Linux VM
* Authenticating
* Running basic commands
* Closing the SSH session

### Deliverable

Document:

```text
SSH Client:
SSH Server:
Connection:
Authentication:
Commands Tested:
Result:
```

Include a simple diagram:

```text
Your PC
   ↓
Encrypted SSH Connection
   ↓
Linux Server
```

**Goal:**

> Understand how SSH provides secure remote access to systems.

---

# Final Practical Project

Create a **Network Protocols Research & Practice Project** covering all seven protocols.

```text
HTTP
 ↓
HTTPS
 ↓
DNS
 ↓
DHCP
 ↓
FTP
 ↓
SMTP
 ↓
SSH
```

### Final Challenge

Create a scenario where a user:

> **Connects their laptop to Wi-Fi → gets an IP address → opens a website → communicates securely with the web server.**

Explain which protocols are involved.

```text
Laptop
  ↓
DHCP
  ↓
Gets Network Configuration
  ↓
DNS
  ↓
Finds Website IP
  ↓
HTTPS
  ↓
Web Server
```

Then research where the other protocols fit:

* HTTP → Web communication
* FTP → File transfer
* SMTP → Email sending
* SSH → Secure remote administration

### Final Deliverable

Create a GitHub project:

```text
Network-Protocols/
│
├── README.md
├── http.md
├── https.md
├── dns.md
├── dhcp.md
├── ftp.md
├── smtp.md
├── ssh.md
└── diagrams/
    ├── http-flow.png
    ├── dns-flow.png
    ├── dhcp-flow.png
    └── email-flow.png
```

### Expected Result

After completing this project, you should be able to:

* Explain HTTP and HTTPS
* Understand DNS name resolution
* Explain DHCP configuration
* Understand FTP file transfer
* Explain SMTP email delivery
* Understand SSH remote access
* Identify where different protocols are used
* Trace basic network communication

> **Protocol → Purpose → Communication Flow → Practice → Document**
