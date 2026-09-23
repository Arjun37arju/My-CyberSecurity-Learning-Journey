# 🔐Understand Encryption Fundamentals

## 📑 Content

* [1. Plaintext](#1-plaintext)
* [2. Ciphertext](#2-ciphertext)
* [3. Encryption Process](#3-encryption-process)
* [4. Decryption Process](#4-decryption-process)
* [5. Key Management Concepts](#5-key-management-concepts)

---

## 1. Plaintext

**Plaintext** is the original readable data before encryption.

### Example

```text
Hello Arjun
```

This is plaintext because it is readable and has not been encrypted.

---

## 2. Ciphertext

**Ciphertext** is the encrypted form of plaintext. It is normally unreadable without the appropriate decryption method or key.

### Example

```text
Plaintext  →  Hello
Encryption →  X7@kP2
Ciphertext →  X7@kP2
```

---

## 3. Encryption Process

**Encryption** is the process of converting plaintext into ciphertext using a cryptographic algorithm and a key.

### Basic flow

```text
Plaintext
    ↓
Encryption Algorithm + Key
    ↓
Ciphertext
```

### Purpose

Encryption protects data from unauthorized access.

### Example

```text
Plaintext:  Hello
     ↓
Encryption + Key
     ↓
Ciphertext: X7@kP2
```

---

## 4. Decryption Process

**Decryption** is the process of converting ciphertext back into the original plaintext using the appropriate key and decryption algorithm.

### Basic flow

```text
Ciphertext
    ↓
Decryption Algorithm + Key
    ↓
Plaintext
```

### Example

```text
Ciphertext: X7@kP2
     ↓
Decryption + Key
     ↓
Plaintext:  Hello
```

### Encryption vs Decryption

| Process    | Conversion             |
| ---------- | ---------------------- |
| Encryption | Plaintext → Ciphertext |
| Decryption | Ciphertext → Plaintext |

---

## 5. Key Management Concepts

**Key management** is the secure management of cryptographic keys throughout their lifecycle.

### Main key management activities

#### Key Generation

Creating a cryptographic key using a secure method.

```text
Generate → Key
```

#### Key Storage

Keeping keys in a secure location to prevent unauthorized access.

#### Key Protection

Protecting keys from being exposed, stolen, or misused.

#### Key Distribution

Securely providing a key to an authorized person or system.

#### Key Rotation

Replacing an old key with a new key.

```text
Old Key → New Key
```

#### Key Revocation

Invalidating a key because it is no longer trusted or should no longer be used.

```text
Key → Revoked
```

#### Key Destruction

Securely deleting a cryptographic key when it is no longer needed.

```text
Key → Destroyed
```

### Key Management Lifecycle

```text
Generate
   ↓
Store
   ↓
Protect
   ↓
Distribute
   ↓
Rotate
   ↓
Revoke
   ↓
Destroy
```

### 🧠 Quick Revision

| Concept             | Meaning                                           |
| ------------------- | ------------------------------------------------- |
| **Plaintext**       | Original readable data                            |
| **Ciphertext**      | Encrypted data                                    |
| **Encryption**      | Plaintext → Ciphertext                            |
| **Decryption**      | Ciphertext → Plaintext                            |
| **Key Management**  | Securely managing keys throughout their lifecycle |
| **Key Rotation**    | Replacing an old key with a new key               |
| **Key Revocation**  | Stopping trust/use of a key                       |
| **Key Destruction** | Securely deleting a key                           |
