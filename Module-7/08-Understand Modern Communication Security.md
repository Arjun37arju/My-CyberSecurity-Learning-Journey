# — Understand Modern Communication Security

## Content

1. [TLS Handshake](#1-tls-handshake)
2. [Certificate Validation](#2-certificate-validation)
3. [Secure Browsing](#3-secure-browsing)
4. [Encryption in Transit](#4-encryption-in-transit)
5. [Security Weaknesses and Mitigation](#5-security-weaknesses-and-mitigation)

---

## 1. TLS Handshake

**TLS Handshake** = the process used to establish a secure connection between a client and server.

### Main Steps

```text
Client                         Server
  |                              |
  |------ Client Hello --------->|
  |<----- Server Hello ----------|
  |<----- Certificate -----------|
  |------ Key Exchange --------->|
  |<----- Handshake Complete --->|
  |                              |
  |===== Encrypted Data ========>|
```

* **Client Hello** → Client sends supported TLS versions and security options.
* **Server Hello** → Server selects the security options.
* **Certificate** → Server provides its digital certificate.
* **Key Exchange** → Session key material is established.
* **Session Key** → Temporary symmetric key used to protect actual data.
* **After Handshake** → Encrypted communication begins.

**Easy memory:** Hello → Certificate → Key → Secure Data

---

## 2. Certificate Validation

**Certificate Validation** = checking whether a digital certificate is valid and trusted.

### Important Checks

* **Domain** → Certificate matches the website domain.
* **Validity** → Certificate is not expired.
* **Signature** → Certificate was properly signed.
* **Certificate Chain** → Trust path is valid.
* **Revocation** → Certificate has not been revoked.

### Certificate Chain

```text
Root CA
   ↓
Intermediate CA
   ↓
Website Certificate
   ↓
Browser checks the chain
```

### Revocation

* **CRL** → List of revoked certificates.
* **OCSP** → Checks certificate status online.

---

## 3. Secure Browsing

**Secure Browsing** = using the web in a way that protects data and communication from security threats.

### Important Points

* Use **HTTPS** instead of HTTP.
* Do not ignore **certificate/security warnings**.
* **HSTS** helps browsers use HTTPS.
* Keep the browser and operating system updated.
* Avoid entering sensitive information on insecure HTTP websites.

### Important Note

**HTTPS does not guarantee that a website itself is safe or trustworthy.**

It mainly provides protected communication using TLS and certificate-based server authentication.

---

## 4. Encryption in Transit

**Encryption in Transit** = protecting data while it is traveling between systems over a network.

### Examples

* **HTTPS/TLS** → Web communication
* **SSH** → Remote server communication
* **VPN** → Encrypted network tunnel
* **TLS-secured APIs** → Application-to-server communication

### Transit vs At Rest

| Type           | Protection        |
| -------------- | ----------------- |
| **In Transit** | Data while moving |
| **At Rest**    | Data while stored |

### Important Point

TLS establishes the secure connection and session keys, while **symmetric encryption** is mainly used to protect the actual data during communication.

---

## 5. Security Weaknesses and Mitigation

**Security Weakness** = a flaw or poor configuration that can make communication vulnerable.

**Mitigation** = a measure used to reduce or prevent the security risk.

| Weakness              | Mitigation                    |
| --------------------- | ----------------------------- |
| Old SSL/TLS versions  | Use modern TLS                |
| Weak algorithms       | Use strong algorithms         |
| Expired certificate   | Renew certificate             |
| Invalid certificate   | Correct configuration         |
| Ignoring warnings     | Investigate warnings          |
| TLS downgrade attacks | Disable outdated TLS versions |

### Important Points

* Avoid outdated **SSL/TLS versions**.
* Use strong and modern cryptographic algorithms.
* Renew certificates before expiry.
* Properly configure certificate chains.
* Do not blindly ignore certificate warnings.
* Disable outdated TLS versions to reduce downgrade risks.

---

## Practical

Actual hands-on tasks will be performed in **Task 10**:

* Inspect a TLS handshake using Wireshark.
* Investigate a website certificate.
* Check certificate validation.
* Inspect TLS versions and configurations.
* Explore HTTPS encryption and secure communication.

---

## Quick Revision

* **TLS Handshake** → Establishes secure connection and session keys.
* **Certificate Validation** → Checks certificate validity and trust.
* **Secure Browsing** → Use HTTPS and avoid security warnings.
* **Encryption in Transit** → Protects data while moving over a network.
* **Mitigation** → Reduces security risks and vulnerabilities.
