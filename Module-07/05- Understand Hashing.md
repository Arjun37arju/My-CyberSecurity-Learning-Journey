# Task 5 — Understand Hashing

## Content

1. [Hash Functions](#1-hash-functions)
2. [Password Hashing](#2-password-hashing)
3. [Data Integrity](#3-data-integrity)
4. [Hash Verification](#4-hash-verification)
5. [Collision Awareness](#5-collision-awareness)

---

## 1. Hash Functions

### 1.1 What is a Hash Function?

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

### 1.2 SHA-256

**SHA-256** is a cryptographic hash function from the **SHA-2 family**.

* Output size: **256 bits**
* Hexadecimal representation: **64 characters**
* One-way
* Commonly used for integrity verification

```text
Data → SHA-256 → 256-bit Hash
```

### 1.3 SHA-384

**SHA-384** is a cryptographic hash function from the **SHA-2 family**.

* Output size: **384 bits**
* Hexadecimal representation: **96 characters**
* One-way
* Longer output than SHA-256

### 1.4 SHA-512

**SHA-512** is a cryptographic hash function from the **SHA-2 family**.

* Output size: **512 bits**
* Hexadecimal representation: **128 characters**
* One-way
* Longer output than SHA-256 and SHA-384

### 1.5 SHA-3

**SHA-3** is a separate cryptographic hash family from SHA-2.

Common variants:

* SHA3-224
* SHA3-256
* SHA3-384
* SHA3-512

```text
SHA-2
 ├── SHA-256
 ├── SHA-384
 └── SHA-512

SHA-3
 ├── SHA3-224
 ├── SHA3-256
 ├── SHA3-384
 └── SHA3-512
```

---

## 2. Password Hashing

### 2.1 What is Password Hashing?

Passwords should **not** normally be stored as plaintext.

Bad approach:

```text
Password
   ↓
Database
```

Password hashing:

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

A password hash is designed to be **one-way**. The application should not need to decrypt the stored password hash.

### 2.2 Why Not Use SHA-256 Alone?

SHA-256 is designed to be fast.

This is useful for many integrity applications, but it is not ideal for password storage because attackers can try many password guesses quickly.

```text
Password Guess
      ↓
SHA-256
      ↓
Hash
```

An attacker can repeat this process very quickly.

Password-specific algorithms are designed to make password guessing more expensive.

### 2.3 Password Salting

A **salt** is a random value added to a password before hashing.

```text
Password + Salt
       ↓
Hash Function
       ↓
Password Hash
```

The salt does not normally need to be secret and is stored with the password hash.

Without salt:

```text
User A: password123 → Hash X
User B: password123 → Hash X
```

With different salts:

```text
User A:
password123 + Salt A → Hash A

User B:
password123 + Salt B → Hash B
```

Therefore:

> **Same password + different salt → different hashes**

Salting helps protect against precomputed hash tables and rainbow-table attacks.

### 2.4 Argon2

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

### 2.5 bcrypt

**bcrypt** is a password-hashing algorithm designed to make password guessing slower and more expensive.

It uses an adjustable **cost/work factor**.

```text
Password + Salt
       ↓
    bcrypt
       ↓
Password Hash
```

### 2.6 scrypt

**scrypt** is a password-hashing/key-derivation algorithm designed to require significant memory and computation.

```text
Password + Salt
       ↓
    scrypt
       ↓
Password Hash
```

Its memory requirement makes large-scale password guessing more expensive.

### 2.7 PBKDF2

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

### 2.8 Password Hashing Comparison

| Algorithm  | Main characteristic            |
| ---------- | ------------------------------ |
| **Argon2** | Memory + computation intensive |
| **bcrypt** | Adjustable computational cost  |
| **scrypt** | Memory + computation intensive |
| **PBKDF2** | Repeated iterations            |

These algorithms are designed specifically for password hashing or key derivation rather than fast general-purpose hashing.

---

## 3. Data Integrity

### 3.1 What is Data Integrity?

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

### 3.2 Detecting Changes

If the hashes are different:

```text
Hash 1 ≠ Hash 2
     ↓
Data changed
```

If they match, the data passes the hash check, assuming the trusted hash itself has not been compromised.

### 3.3 Example

```text
Original File
     ↓
SHA-256
     ↓
Hash A

Received File
     ↓
SHA-256
     ↓
Hash B
```

If:

```text
Hash A = Hash B
```

The file passes the integrity check.

If:

```text
Hash A ≠ Hash B
```

The file has changed or the data being checked is different.

---

## 4. Hash Verification

### 4.1 What is Hash Verification?

**Hash verification** means calculating a hash and comparing it with a known/trusted hash.

```text
File
 ↓
Calculate Hash
 ↓
Compare with Known Hash
```

### 4.2 Verification Process

Same hash:

```text
Hash A = Hash B
       ↓
Verification Passed
```

Different hash:

```text
Hash A ≠ Hash B
       ↓
Verification Failed
```

### 4.3 Practical Example

A software developer publishes:

```text
Expected SHA-256:
ABC123...
```

You download the file and calculate its SHA-256 hash.

```text
Downloaded File
      ↓
SHA-256
      ↓
ABC123...
```

If both values match, the file passes the hash verification check.

---

## 5. Collision Awareness

### 5.1 What is a Hash Collision?

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

### 5.2 Hash Collision Attack

A **hash collision attack** attempts to deliberately find two different inputs that produce the same hash.

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

### 5.3 Collision Resistance

**Collision resistance** means it should be computationally difficult to find two different inputs with the same hash.

It does **not** mean collisions are mathematically impossible.

```text
Collision exists theoretically
          ↓
Finding a useful collision
          ↓
Should be computationally difficult
```

### 5.4 MD5

**MD5** is an older hash algorithm.

Practical collision attacks have been demonstrated against MD5.

Therefore, MD5 should **not** be relied upon for security applications where collision resistance is important.

It may still appear in some legacy or non-security contexts.

### 5.5 SHA-1

**SHA-1** is also an older hash algorithm.

Practical collision attacks have been demonstrated against SHA-1.

Therefore, SHA-1 should not be used for new security applications where collision resistance is required.

### 5.6 Modern Hash Alternatives

Modern cryptographic hash functions include:

* SHA-256
* SHA-384
* SHA-512
* SHA-3

These are designed to provide stronger collision resistance than MD5 and SHA-1.

---

## 6. Practical Work

The practical work for Task 5 can be performed later in **Task 10**.

### 6.1 CyberChef

CyberChef can be used to:

* Generate hashes
* Compare different hash algorithms
* Observe how a small input change changes the hash
* Explore cryptographic operations
* Identify and process different types of encoded or hashed data

### 6.2 md5sum

Linux can calculate an MD5 hash:

```bash
md5sum file.txt
```

### 6.3 OpenSSL

OpenSSL can be used to explore cryptographic operations and hashing.

### 6.4 Password Security Tools

Authorized lab environments can be used to understand password-hash security with tools such as:

* CrackStation
* John the Ripper
* Hashcat

These tools should only be used on passwords/hashes you are authorized to test.

### 6.5 Practical Objective

The practical work demonstrates:

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

## 7. Conclusion

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
