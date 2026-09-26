# Apply Through Hands-on Tasks

## Table of Contents

1. [Analyze HTTPS Traffic](#1-analyze-https-traffic)
2. [Investigate Certificates](#2-investigate-certificates)
3. [Explore Hashing Workflows](#3-explore-hashing-workflows)
4. [Demonstrate Encryption Concepts](#4-demonstrate-encryption-concepts)
5. [Create Secure Communication Reports](#5-create-secure-communication-reports)
6. [Complete Hands-on Workflow](#complete-hands-on-workflow)

---

## 1. Analyze HTTPS Traffic

### What is HTTPS Traffic Analysis?

**HTTPS traffic analysis** means examining encrypted web communication to understand the connection, protocol, certificates, and network information.

Tools such as **Wireshark** can help observe:

* Source and destination IP addresses
* Source and destination ports
* TLS protocol information
* TLS handshake packets
* Certificate information
* TCP communication
* Connection timing

> HTTPS encrypts application data, so normal packet capture does not expose the website's plaintext content.

### Practical Task

1. Open Wireshark.
2. Start capturing network traffic.
3. Visit an HTTPS website.
4. Stop the capture.
5. Filter for TLS traffic.

Example filter:

```text
tls
```

Then observe:

```text
Client
   ↓
TCP Connection
   ↓
TLS Handshake
   ↓
Certificate
   ↓
Encrypted Communication
```

### Practical Goal

Analyze HTTPS traffic and identify the major components of a secure web connection.

---

## 2. Investigate Certificates

### What is a Digital Certificate?

A **digital certificate** binds an identity, such as a domain name, to a public key and is used to support trust in secure communications.

A certificate can contain:

* Domain name
* Public key
* Issuer
* Validity period
* Certificate fingerprint
* Signature information

### Practical Task

Open an HTTPS website and inspect its certificate using the browser.

Check:

```text
Domain
Issuer
Valid From
Valid To
Public Key Information
Certificate Fingerprint
```

You can also inspect certificate details using OpenSSL:

```bash
openssl s_client -connect example.com:443
```

### Verification

Check:

```text
Is the certificate valid?
Is the domain name correct?
Who issued the certificate?
Is the certificate expired?
```

### Practical Goal

Learn how to inspect and understand the important fields of an HTTPS certificate.

---

## 3. Explore Hashing Workflows

### What is a Hashing Workflow?

A **hashing workflow** converts input data into a fixed-length hash value and can be used to verify data integrity.

```text
Input Data
    ↓
Hash Algorithm
    ↓
Hash Value
    ↓
Compare With Expected Hash
    ↓
Match / Mismatch
```

### Example

Using SHA-256:

```bash
echo -n "Hello" | sha256sum
```

You can change the input and generate the hash again.

```bash
echo -n "Hello!" | sha256sum
```

Even a small change in the input produces a different hash.

### Practical Task

1. Create a text file.
2. Generate its SHA-256 hash.
3. Modify the file.
4. Generate the hash again.
5. Compare both hashes.

### Example

```bash
sha256sum sample.txt
```

### Practical Goal

Understand how hashing can be used to verify whether data has changed.

---

## 4. Demonstrate Encryption Concepts

### What is Encryption?

**Encryption** converts readable plaintext into ciphertext using an encryption algorithm and key.

```text
Plaintext
    ↓
Encryption + Key
    ↓
Ciphertext
    ↓
Decryption + Key
    ↓
Plaintext
```

### Practical Task

Demonstrate the basic difference between plaintext and ciphertext using a simple encryption tool or Python program.

Example concept:

```text
Plaintext:
Hello World

        ↓ Encryption

Ciphertext:
Encrypted Data

        ↓ Decryption

Plaintext:
Hello World
```

For learning, you can explore encryption using tools such as **CyberChef**.

### Compare

| Concept    | Meaning                                   |
| ---------- | ----------------------------------------- |
| Plaintext  | Original readable data                    |
| Ciphertext | Encrypted unreadable data                 |
| Encryption | Plaintext → Ciphertext                    |
| Decryption | Ciphertext → Plaintext                    |
| Key        | Used by the encryption/decryption process |

### Practical Goal

Understand the basic encryption and decryption workflow and the role of keys.

---

## 5. Create Secure Communication Reports

### What is a Secure Communication Report?

A **secure communication report** summarizes the security properties observed during an HTTPS/TLS investigation.

A report can include:

* Website / domain
* Protocol used
* TLS information
* Certificate details
* Certificate validity
* Encryption information
* Observed network details
* Security observations

### Example Report

```text
========== SECURE COMMUNICATION REPORT ==========

Website       : example.com
Protocol      : HTTPS
Security      : TLS
Certificate   : Valid
Issuer        : Certificate Authority
Status        : Not Expired

Observations:
- HTTPS connection detected
- TLS communication observed
- Certificate inspected
- Application data is encrypted

==================================================
```

### Practical Goal

Create a clear report that summarizes the security information collected during HTTPS and certificate analysis.

---

# Complete Hands-on Workflow

The five tasks can be combined into one secure communication analysis project:

```text
              HTTPS Website
                    ↓
             Capture Traffic
                    ↓
             Analyze TLS Data
                    ↓
          Investigate Certificate
                    ↓
             Explore Hashing
                    ↓
          Demonstrate Encryption
                    ↓
        Analyze Security Properties
                    ↓
        Create Security Report
```

---

# Example Mini Project

## HTTPS Security Analysis and Reporting Tool

### Features

```text
1. Analyze HTTPS traffic
2. Identify TLS communication
3. Investigate the website certificate
4. Check certificate validity
5. Explore SHA-256 hashing
6. Demonstrate encryption concepts
7. Generate a secure communication report
```

### Basic Investigation Structure

```text
Website
   ↓
HTTPS Connection
   ↓
TLS Handshake
   ↓
Certificate Verification
   ↓
Encrypted Communication
   ↓
Security Analysis
   ↓
Final Report
```

### Practical Deliverable

```text
Project Name:

Target Website:

HTTPS Status:

TLS Information:

Certificate Details:

Certificate Validity:

Hashing Test:

Encryption Demonstration:

Security Observations:

Final Report:
```

---

# Quick Revision

| Task                                | Purpose                              |
| ----------------------------------- | ------------------------------------ |
| Analyze HTTPS Traffic               | Understand secure web communication  |
| Investigate Certificates            | Verify certificate information       |
| Explore Hashing Workflows           | Understand integrity verification    |
| Demonstrate Encryption Concepts     | Understand encryption and decryption |
| Create Secure Communication Reports | Document security findings           |

---

# Key Learning

```text
HTTPS Analysis
      ↓
Certificate Investigation
      ↓
Hashing
      ↓
Encryption
      ↓
Secure Communication
      ↓
Security Report
```

> **Hands-on practice helps connect cryptography and communication-security concepts with real security tools and workflows.**
