#  Understand Asymmetric Encryption

## Content

1. [Public Keys](#1-public-keys)
2. [Private Keys](#2-private-keys)
3. [Key Exchange](#3-key-exchange)
4. [Digital Trust](#4-digital-trust)
5. [Practical Applications](#5-practical-applications)

---

## 1. Public Keys

A **public key** is a cryptographic key that can be shared openly.

In encryption:

```text
Public Key → Encrypt
Private Key → Decrypt
```

The public key can be shared with other people, but the private key must remain secret.

---

## 2. Private Keys

A **private key** is a secret cryptographic key that must be protected by its owner.

For encrypted data:

```text
Public Key → Encrypt
Private Key → Decrypt
```

If the private key is compromised, an attacker may be able to decrypt data protected for that key or perform actions that require the private key.

---

## 3. Key Exchange

**Key exchange** is the process of securely establishing a cryptographic key between two parties.

Asymmetric cryptography can help establish a secure connection or session key.

### Hybrid Approach

Modern secure communication often combines asymmetric and symmetric cryptography:

```text
Asymmetric Cryptography
        ↓
Authentication / Key Establishment
        ↓
Symmetric Session Key
        ↓
Encrypt Actual Data
```

Symmetric encryption is commonly used for the actual communication because it is efficient for large amounts of data.

---

## 4. Digital Trust

**Digital trust** means having confidence that a digital identity, such as a website, is authentic and can be trusted.

### Digital Certificate

A certificate can contain:

* Domain / website identity
* Public key
* Certificate Authority (CA) information
* Digital signature
* Validity information

### Certificate Authority (CA)

A **Certificate Authority** is a trusted organization that issues and digitally signs certificates.

A browser can check a certificate to help verify the website's identity and whether the certificate is valid and trusted.

---

## 5. Practical Applications

### HTTPS

Asymmetric cryptography can help with:

* Website authentication
* Secure key establishment

After the secure connection is established, symmetric encryption is commonly used to protect the actual data.

```text
Browser
   ↓
Verify Website
   ↓
Establish Secure Session
   ↓
Symmetric Encryption
   ↓
Secure Communication
```

### Digital Signatures

Digital signatures can be used to verify the sender and detect changes to data.

```text
Sender
   ↓
Private Key
   ↓
Digital Signature
   ↓
Message
   ↓
Receiver
   ↓
Public Key
   ↓
Verify Signature
```

If the message is changed after signing, signature verification will fail.

### SSH

SSH provides secure remote access.

With SSH key-based authentication:

```text
Private Key → Kept securely on user's device
Public Key  → Stored on SSH server
```

The private key is **not sent to the server**. It is used to prove that the user has the corresponding private key.

### Secure Email

Asymmetric cryptography can be used to encrypt email.

```text
Receiver's Public Key
        ↓
Encrypt Email
        ↓
Encrypted Email
        ↓
Receiver's Private Key
        ↓
Decrypt Email
```

The receiver's private key must be kept secret.

---

## Key Points

| Concept           | Main Idea                                                         |
| ----------------- | ----------------------------------------------------------------- |
| Public Key        | Can be shared openly                                              |
| Private Key       | Must be kept secret                                               |
| Key Exchange      | Securely establishes cryptographic keys                           |
| Digital Trust     | Helps verify digital identity                                     |
| Certificate       | Contains identity and public-key information                      |
| CA                | Issues and signs certificates                                     |
| HTTPS             | Uses asymmetric cryptography for authentication/key establishment |
| SSH               | Can use public/private keys for authentication                    |
| Digital Signature | Private key signs, public key verifies                            |

## Quick Revision

```text
Asymmetric Encryption
        ↓
Two Different Keys
        ↓
Public Key + Private Key
        ↓
Public Key → Can be shared
Private Key → Must be protected
```
