#  Understand Digital Signatures

## Content

1. Identity Verification
2. Non-repudiation
3. Signature Workflow
4. Verification Process
5. Trust Models

---

## 1. Identity Verification

**Digital Signature** = a cryptographic method used to verify the sender's identity and message integrity.

### 1.1 Private Key

**Private Key** = secret key used by the sender to create a digital signature.

### 1.2 Public Key

**Public Key** = key used by the receiver to verify the sender's digital signature.

### 1.3 Identity Verification

**Identity Verification** = verifying that a signature was created using the expected private key.

```text
Private Key → Sign
Public Key  → Verify
```

---

## 2. Non-repudiation

**Non-repudiation** = providing evidence that the sender signed the data, making it difficult to falsely deny the signature later.

### 2.1 Purpose

**Purpose** = helps provide evidence of who signed the data.

### 2.2 Important

**Private-key protection** = important because anyone who obtains the private key may be able to create signatures.

---

## 3. Signature Workflow

**Signature Workflow** = sender signs data with a private key and receiver verifies it with the public key.

### 3.1 Signing

```text
Message
   ↓
Hash
   ↓
Private Key
   ↓
Digital Signature
```

### 3.2 Sending

**Sender** = sends the original message together with the digital signature.

### 3.3 Verification

```text
Message + Signature
        ↓
   Public Key
        ↓
     Verify
```

### 3.4 Important

**Private Key → Create Signature**

**Public Key → Verify Signature**

---

## 4. Verification Process

**Signature Verification** = checking whether a digital signature is valid for the received data.

### 4.1 Valid Signature

**Valid Signature** = signature matches the data and the corresponding public key.

### 4.2 Invalid Signature

**Invalid Signature** = verification fails because the data may have changed, the signature may be invalid, or the key may not be trusted.

### 4.3 Data Modification

**Modified Message** = changing the signed message normally causes signature verification to fail.

---

## 5. Trust Models

**Trust Model** = a system used to establish whether a public key and its owner can be trusted.

### 5.1 CA

**CA (Certificate Authority)** = trusted organization that issues and digitally signs certificates.

### 5.2 PKI

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

### 5.3 Web of Trust

**Web of Trust** = trust model where users verify and trust each other's public keys instead of relying on a central CA.

### 5.4 Digital Certificate

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
