# Task 6 — Understand Digital Signatures

## Content

1. [Identity Verification](#1-identity-verification)
2. [Non-repudiation](#2-non-repudiation)
3. [Signature Workflow](#3-signature-workflow)
4. [Verification Process](#4-verification-process)
5. [Trust Models](#5-trust-models)

---

## 1. Identity Verification

**Digital Signature** = a cryptographic method used to verify the sender's identity and message integrity.

### Private Key

**Private Key** = secret key used by the sender to create a digital signature.

### Public Key

**Public Key** = key used by the receiver to verify the sender's digital signature.

```text
Private Key → Sign
Public Key  → Verify
```

---

## 2. Non-repudiation

**Non-repudiation** = providing evidence that the sender signed the data, making it difficult to falsely deny the signature later.

**Private-key protection** = important because anyone who obtains the private key may be able to create signatures.

---

## 3. Signature Workflow

**Signature Workflow** = sender signs data with a private key and receiver verifies it with the public key.

### Signing

```text
Message
   ↓
Hash
   ↓
Private Key
   ↓
Digital Signature
```

### Sending

**Sender** = sends the original message together with the digital signature.

### Verification

```text
Message + Signature
        ↓
   Public Key
        ↓
     Verify
```

**Private Key → Create Signature**

**Public Key → Verify Signature**

---

## 4. Verification Process

**Signature Verification** = checking whether a digital signature is valid for the received data.

### Valid Signature

**Valid Signature** = signature matches the data and the corresponding public key.

### Invalid Signature

**Invalid Signature** = verification fails because the data may have changed, the signature may be invalid, or the key may not be trusted.

### Data Modification

**Modified Message** = changing the signed message normally causes signature verification to fail.

---

## 5. Trust Models

**Trust Model** = a system used to establish whether a public key and its owner can be trusted.

### CA

**CA (Certificate Authority)** = trusted organization that issues and digitally signs certificates.

### PKI

**PKI (Public Key Infrastructure)** = complete system used to manage public keys, digital certificates, CAs, and digital trust.

```text
PKI
│
├── CA
├── Digital Certificates
├── Public & Private Keys
├── Certificate Verification
└── Trust Management
```

**CA is a component of PKI.**

### Web of Trust

**Web of Trust** = trust model where users verify and trust each other's public keys instead of relying on a central CA.

### Digital Certificate

**Digital Certificate** = electronic document that connects an identity/domain with a public key and is digitally signed by a trusted CA.

Important certificate information:

1. Domain/identity
2. Public key
3. CA information
4. Validity period
5. Digital signature

---

## Practical

**OpenSSL** = can be used to create and verify digital signatures.

**Certificate Inspection** = can be used to examine CA, public key, validity, and certificate details.

**CyberChef** = can be used to explore hashing and cryptographic operations.

**Task 10** = actual hands-on practicals will be performed here.

---

## Quick Revision

```text
Private Key → Sign
Public Key  → Verify
```

```text
Digital Signature
→ Identity Verification
→ Integrity
→ Non-repudiation
```

```text
CA = Certificate Authority

PKI = Public Key Infrastructure

CA → Part of PKI
```
