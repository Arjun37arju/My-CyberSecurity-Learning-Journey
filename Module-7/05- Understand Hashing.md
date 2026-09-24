# Understand Hashing

## Content

1. [Hash Functions](#1-hash-functions)
2. [SHA-256](#2-sha-256)
3. [SHA-384](#3-sha-384)
4. [SHA-512](#4-sha-512)
5. [SHA-3](#5-sha-3)
6. [Data Integrity](#6-data-integrity)
7. [Hash Verification](#7-hash-verification)
8. [Hash Collision](#8-hash-collision)
9. [Hash Collision Attack](#9-hash-collision-attack)
10. [MD5 and SHA-1](#10-md5-and-sha-1)
11. [Password Hashing](#11-password-hashing)
12. [Password Salting](#12-password-salting)
13. [Argon2](#13-argon2)
14. [bcrypt](#14-bcrypt)
15. [scrypt](#15-scrypt)
16. [PBKDF2](#16-pbkdf2)
17. [Password Hashing Comparison](#17-password-hashing-comparison)
18. [Practical Work](#18-practical-work)
19. [Conclusion](#19-conclusion)

---

## 1. Hash Functions

A **hash function** converts input data into a fixed-length hash value.

```text
Input Data
    ↓
Hash Function
    ↓
Hash Value
```

Example:

```text
"Hello"
   ↓ SHA-256
Hash Value
```

Important properties:

* Same input → same hash
* Small input change → very different hash
* Fixed-length output
* One-way process
* Designed to resist collisions

Hashing is **not encryption** because there is normally no decryption process.

---

## 2. SHA-256

**SHA-256** is a cryptographic hash function from the **SHA-2 family**.

* Output size: **256 bits**
* Hexadecimal representation: **64 characters**
* One-way
* Commonly used for integrity verification

```text
Data → SHA-256 → 256-bit Hash
```

---

## 3. SHA-384

**SHA-384** is another member of the SHA-2 family.

* Output size: **384 bits**
* Hexadecimal representation: **96 characters**
* One-way
* Provides a longer hash than SHA-256

---

## 4. SHA-512

**SHA-512** is a SHA-2 cryptographic hash function.

* Output size: **512 bits**
* Hexadecimal representation: **128 characters**
* One-way
* Longer output than SHA-256 and SHA-384

---

## 5. SHA-3

**SHA-3** is a separate cryptographic hash family from SHA-2.

Common variants:

* SHA3-224
* SHA3-256
* SHA3-384
* SHA3-512

Important:

```text
SHA-2 → SHA-256, SHA-384, SHA-512
SHA-3 → SHA3-224, SHA3-256, SHA3-384, SHA3-512
```

---

## 6. Data Integrity

**Data integrity** means ensuring that data has not been changed or tampered with.

Hashing can be used to detect changes.

```text
Original File
     ↓
Calculate Hash
     ↓
Known Hash
```

Later:

```text
Received File
     ↓
Calculate Hash
     ↓
Compare Hashes
```

If the hashes are different:

```text
Hash 1 ≠ Hash 2
     ↓
Data changed
```

If they match, the data passes the hash check, assuming the trusted hash itself has not been compromised.

---

## 7. Hash Verification

**Hash verification** means calculating a hash and comparing it with a known/trusted hash.

```text
File
 ↓
Calculate Hash
 ↓
Compare with Known Hash
```

### Same hash

```text
Hash A = Hash B
→ Verification passes
```

### Different hash

```text
Hash A ≠ Hash B
→ Verification fails
```

Hash verification is commonly used for checking file integrity.

---

## 8. Hash Collision

A **hash collision** occurs when two different inputs produce the same hash.

```text
Input A ≠ Input B

Hash(Input A) = Hash(Input B)
```

Example:

```text
File A → Hash X
File B → Hash X
```

Although the files are different, their hash values are the same.

Because hash outputs have a fixed size, collisions must theoretically exist. Good cryptographic hash functions make finding useful collisions computationally difficult.

---

## 9. Hash Collision Attack

A **hash collision attack** attempts to deliberately find two different inputs that produce the same hash.

### Goal

```text
Input A ≠ Input B
       ↓
Same Hash
```

If successful, an attacker may be able to bypass systems that incorrectly rely only on the hash value.

Possible security impacts include:

* File integrity verification
* Digital signatures
* Certificate security
* Software verification

Strong modern hash functions are designed to make practical collision attacks extremely difficult.

---

## 10. MD5 and SHA-1

**MD5** and **SHA-1** are older hash algorithms.

Practical collision attacks have been demonstrated against both.

Therefore, they should **not be relied upon for security applications where collision resistance is important**.

Modern alternatives include:

* SHA-256
* SHA-384
* SHA-512
* SHA-3

MD5 and SHA-1 can still appear in legacy or non-security contexts, but they should not be chosen for new collision-resistant security applications.

---

## 11. Password Hashing

Passwords should **not** normally be stored as plaintext.

### Bad approach

```text
Password
   ↓
Database
```

Anyone who obtains the database could directly see the passwords.

### Password hashing

```text
Password
   ↓
Password Hashing Function
   ↓
Hash
   ↓
Database
```

During login:

```text
Entered Password
       ↓
Hashing Process
       ↓
New Hash
       ↓
Compare with Stored Hash
```

If the values match, authentication can succeed.

A password hash is designed to be one-way. The application should not need to decrypt the stored password hash.

---

## 12. Password Salting

A **salt** is a random value added to a password before hashing.

```text
Password + Salt
       ↓
Hash Function
       ↓
Password Hash
```

The salt does not normally need to be secret and is stored with the password hash.

### Without salt

```text
User A: password123 → Hash X
User B: password123 → Hash X
```

### With different salts

```text
User A:
password123 + Salt A → Hash A

User B:
password123 + Salt B → Hash B
```

Therefore:

> **Same password + different salt → different hashes**

Salting helps defend against precomputed hash tables and rainbow-table attacks.

---

## 13. Argon2

**Argon2** is a modern password-hashing algorithm.

It can be configured to require significant:

* Memory
* CPU time
* Computation

This makes large-scale password guessing more expensive.

```text
Password + Salt
       ↓
     Argon2
       ↓
Password Hash
```

---

## 14. bcrypt

**bcrypt** is a password-hashing algorithm designed to make password guessing slower and more expensive.

It uses an adjustable **cost/work factor**.

```text
Password + Salt
       ↓
    bcrypt
       ↓
Password Hash
```

The cost can be increased as computing power improves.

---

## 15. scrypt

**scrypt** is a password-hashing/key-derivation algorithm designed to require significant memory and computation.

```text
Password + Salt
       ↓
    scrypt
       ↓
Password Hash
```

Its memory requirement makes large-scale password guessing more expensive.

---

## 16. PBKDF2

**PBKDF2** stands for:

> **Password-Based Key Derivation Function 2**

It uses:

* Password
* Salt
* Repeated iterations

```text
Password + Salt
       ↓
 Repeated Processing
       ↓
Derived Key
```

The repeated work makes password guessing slower.

PBKDF2 is commonly used for password-based key derivation and password storage systems.

---

## 17. Password Hashing Comparison

| Algorithm  | Main characteristic            |
| ---------- | ------------------------------ |
| **Argon2** | Memory + computation intensive |
| **bcrypt** | Adjustable computational cost  |
| **scrypt** | Memory + computation intensive |
| **PBKDF2** | Repeated iterations            |

These are designed specifically for password hashing/key derivation rather than fast general-purpose hashing.

### Why not SHA-256 alone?

SHA-256 is designed to be fast.

That is useful for many integrity applications, but it also means an attacker can test a very large number of password guesses quickly.

Therefore:

```text
SHA-256 alone
     ↓
Too fast for password storage
```

Password-specific algorithms are designed to make guessing more expensive.

---

## 18. Practical Work

The practical work for this task can be performed later in **Task 10**.

Tools and activities include:

### CyberChef

Use CyberChef to:

* Generate hashes
* Compare hashing algorithms
* Observe changes when input changes
* Explore encoding and cryptographic operations

### md5sum

Linux can calculate an MD5 hash:

```bash
md5sum file.txt
```

### OpenSSL

OpenSSL can be used to explore cryptographic operations and hashing.

### Password Security Tools

Tools such as:

* CrackStation
* John the Ripper
* Hashcat

can be used in authorized lab environments to understand password-hash security and password-guessing concepts.

### Practical objective

The goal is to understand:

```text
Input
 ↓
Hash
 ↓
Verification
 ↓
Password Security
 ↓
Collision Awareness
```

---

## 19. Conclusion

Hashing is a **one-way process** that converts data into a fixed-length value.

It is useful for:

* Data integrity
* File verification
* Password storage
* Digital signatures
* Security systems

Important concepts:

```text
Hashing
   ↓
Integrity + Verification

Password Hashing
   ↓
Argon2 / bcrypt / scrypt / PBKDF2

Salt
   ↓
Different hash for the same password

Collision
   ↓
Different inputs → Same hash
```

For modern security applications, strong cryptographic hash functions such as **SHA-256, SHA-384, SHA-512, and SHA-3** are preferred over older algorithms such as MD5 and SHA-1 when collision resistance is required.
