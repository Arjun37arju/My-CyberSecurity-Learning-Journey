# Understand Symmetric Encryption

## Content

* [1. Shared-Key Encryption](#1-shared-key-encryption)
* [2. Encryption Workflow](#2-encryption-workflow)
* [3. Key Protection](#3-key-protection)
* [4. Practical Use Cases](#4-practical-use-cases)
* [5. Security Considerations](#5-security-considerations)

---

## 1. Shared-Key Encryption

Symmetric encryption is a method of encryption that uses the **same secret key** for both encryption and decryption.

### Basic idea

```text
Plaintext
   ↓
Encryption + Shared Key
   ↓
Ciphertext
   ↓
Decryption + Same Key
   ↓
Plaintext
```

The key must be kept **secret**. If an attacker gets the key, they may be able to decrypt the protected data.

### Examples

* AES
* ChaCha20

---

## 2. Encryption Workflow

The basic symmetric encryption workflow is:

```text
Sender
  ↓
Plaintext
  ↓
Encryption Algorithm + Shared Key
  ↓
Ciphertext
  ↓
Network / Storage
  ↓
Decryption Algorithm + Same Key
  ↓
Plaintext
  ↓
Receiver
```

The ciphertext can travel through an untrusted network, but the **shared key must remain protected**.

---

## 3. Key Protection

Key protection means securing the cryptographic key from:

* Theft
* Unauthorized access
* Exposure
* Compromise

### Key protection methods

* Secure storage
* Access control
* Secure key distribution
* Key rotation
* Key revocation
* Secure destruction

Because symmetric encryption uses the same key for encryption and decryption, protecting the key is very important.

---

## 4. Practical Use Cases

Symmetric encryption is commonly used for protecting large amounts of data because it is generally **fast and efficient**.

### Common use cases

* File encryption
* Disk encryption
* Database encryption
* Backup encryption
* Secure communication

### Common algorithms

```text
AES
ChaCha20
```

---

## 5. Security Considerations

When using symmetric encryption, consider the following:

### 1. Protect the Key

The shared key must be protected from unauthorized access.

### 2. Use Strong Encryption Algorithms

Use modern and well-established algorithms such as:

```text
AES
ChaCha20
```

Avoid weak or obsolete algorithms.

### 3. Secure Key Distribution

The shared key must be securely provided to the authorized parties.

### 4. Key Rotation

Replace keys periodically according to the security requirements of the system.

### 5. Key Revocation

If a key is compromised, it should be **revoked and replaced**.

---

## Summary

Symmetric encryption uses **one shared secret key** for both encryption and decryption.

The main security concern is protecting the shared key.

```text
Strong Algorithm
        +
Strong Key Protection
        +
Secure Key Management
        =
Better Symmetric Encryption Security
```
