# Cryptography Practical Reference

## Table of Contents

1. [PowerShell — Hashing](#1-powershell--hashing)

   * [1.1 Create a File](#11-create-a-file)
   * [1.2 SHA-256](#12-sha-256)
   * [1.3 SHA-384](#13-sha-384)
   * [1.4 SHA-512](#14-sha-512)
   * [1.5 Verify File Integrity](#15-verify-file-integrity)
2. [Linux — Hashing](#2-linux--hashing)

   * [2.1 Create a File](#21-create-a-file)
   * [2.2 SHA-256](#22-sha-256)
   * [2.3 SHA-384](#23-sha-384)
   * [2.4 SHA-512](#24-sha-512)
   * [2.5 File Integrity Verification](#25-file-integrity-verification)
3. [Linux — OpenSSL Encryption](#3-linux--openssl-encryption)

   * [3.1 Check OpenSSL](#31-check-openssl)
   * [3.2 Create Plaintext](#32-create-plaintext)
   * [3.3 Encrypt a File](#33-encrypt-a-file)
   * [3.4 View Ciphertext](#34-view-ciphertext)
   * [3.5 Decrypt a File](#35-decrypt-a-file)
4. [VS Code + Python — Hashing](#4-vs-code--python--hashing)

   * [4.1 Install PyCryptodome](#41-install-pycryptodome)
   * [4.2 SHA-256 Hash](#42-sha-256-hash)
   * [4.3 SHA-384 and SHA-512](#43-sha-384-and-sha-512)
   * [4.4 Avalanche Effect](#44-avalanche-effect)
5. [VS Code + Python — AES Encryption](#5-vs-code--python--aes-encryption)

   * [5.1 Create the Program](#51-create-the-program)
   * [5.2 AES Encryption and Decryption](#52-aes-encryption-and-decryption)
   * [5.3 Key and IV](#53-key-and-iv)
6. [CyberChef — Hashing](#6-cyberchef--hashing)

   * [6.1 SHA3-256](#61-sha3-256)
   * [6.2 Demonstrate Hash Change](#62-demonstrate-hash-change)
7. [CyberChef — AES Encryption](#7-cyberchef--aes-encryption)

   * [7.1 AES Encrypt](#71-aes-encrypt)
   * [7.2 AES Decrypt](#72-aes-decrypt)
   * [7.3 Key and IV](#73-key-and-iv)
8. [Quick Reference](#8-quick-reference)

---

# 1. PowerShell — Hashing

PowerShell can calculate hashes of files using `Get-FileHash`.

## 1.1 Create a File

Open **PowerShell**.

Create a test file:

```powershell
"Hello, this is my first hash test." | Out-File message.txt -Encoding utf8
```

Check the file:

```powershell
Get-Content message.txt
```

---

## 1.2 SHA-256

```powershell
Get-FileHash .\message.txt -Algorithm SHA256
```

The long hexadecimal value is the **SHA-256 hash**.

---

## 1.3 SHA-384

```powershell
Get-FileHash .\message.txt -Algorithm SHA384
```

---

## 1.4 SHA-512

```powershell
Get-FileHash .\message.txt -Algorithm SHA512
```

---

## 1.5 Verify File Integrity

Hashing can be used to check whether a file has changed.

Calculate the hash before making changes:

```powershell
Get-FileHash .\message.txt -Algorithm SHA256
```

Change the file:

```powershell
"!" | Add-Content .\message.txt
```

Calculate the hash again:

```powershell
Get-FileHash .\message.txt -Algorithm SHA256
```

### Observation

Even a small change in the file produces a very different hash.

**Small input change → different hash**

---

# 2. Linux — Hashing

Linux provides commands such as `sha256sum`, `sha384sum`, and `sha512sum`.

## 2.1 Create a File

Open the **Linux terminal**.

```bash
echo 'This is my secret message.' > message.txt
```

Check the content:

```bash
cat message.txt
```

---

## 2.2 SHA-256

```bash
sha256sum message.txt
```

### Meaning

`sha256sum` means:

> Calculate the SHA-256 checksum/hash of the file.

---

## 2.3 SHA-384

```bash
sha384sum message.txt
```

---

## 2.4 SHA-512

```bash
sha512sum message.txt
```

---

## 2.5 File Integrity Verification

Save the current SHA-256 hash:

```bash
sha256sum message.txt > message.sha256
```

Verify the file:

```bash
sha256sum -c message.sha256
```

Expected result:

```text
message.txt: OK
```

### What does `-c` mean?

`-c` means **check**.

It tells Linux to compare the current file hash with the saved hash.

If the file was changed:

```text
message.txt: FAILED
```

---

# 3. Linux — OpenSSL Encryption

OpenSSL is a command-line tool used for cryptography, including encryption, hashing, certificates, and TLS.

## 3.1 Check OpenSSL

```bash
openssl version
```

Example:

```text
OpenSSL 3.6.2
```

---

## 3.2 Create Plaintext

Create a file:

```bash
echo 'This is my secret message.' > secret.txt
```

Check it:

```bash
cat secret.txt
```

Expected:

```text
This is my secret message.
```

---

## 3.3 Encrypt a File

Use AES-256-CBC:

```bash
openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.txt -out secret.enc
```

OpenSSL will ask for a password.

Example:

```text
MyPassword123
```

### Meaning of the command

```text
openssl       → OpenSSL tool
enc           → encryption command
-aes-256-cbc  → AES-256 using CBC mode
-salt         → uses a random salt
-pbkdf2       → derives an encryption key from the password
-in           → input file
-out          → output file
```

The encrypted file is:

```text
secret.enc
```

---

## 3.4 View Ciphertext

List the files:

```bash
ls -l secret.txt secret.enc
```

Try to view the encrypted file:

```bash
cat secret.enc
```

You may see random-looking or unreadable data.

This is the **ciphertext**.

```text
Plaintext
   ↓
AES Encryption
   ↓
Ciphertext
```

---

## 3.5 Decrypt a File

Decrypt the encrypted file:

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -in secret.enc -out decrypted.txt
```

Enter the **same password** used during encryption.

Check the decrypted file:

```bash
cat decrypted.txt
```

Expected:

```text
This is my secret message.
```

### Encryption vs Decryption

```text
Encryption:
Plaintext → Ciphertext

Decryption:
Ciphertext → Plaintext
```

---

# 4. VS Code + Python — Hashing

Python can perform hashing using its built-in `hashlib` module.

You can use **VS Code** to write and run the Python program.

## 4.1 Install PyCryptodome

For Python AES encryption later, install:

```bash
pip3 install pycryptodome
```

`hashlib` itself does **not** require installation because it is included with Python.

---

## 4.2 SHA-256 Hash

Create a file in VS Code:

```text
hash_test.py
```

Add:

```python
import hashlib

message = b"This is my secret message."

hash_value = hashlib.sha256(message).hexdigest()

print("SHA-256:", hash_value)
```

Run:

```bash
python3 hash_test.py
```

### Important parts

```python
import hashlib
```

Loads Python's hashing library.

```python
hashlib.sha256(message)
```

Calculates SHA-256.

```python
.hexdigest()
```

Converts the result into readable hexadecimal characters.

---

## 4.3 SHA-384 and SHA-512

### SHA-384

```python
hash_value = hashlib.sha384(message).hexdigest()
```

### SHA-512

```python
hash_value = hashlib.sha512(message).hexdigest()
```

The complete example:

```python
import hashlib

message = b"This is my secret message."

print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-384:", hashlib.sha384(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())
```

---

## 4.4 Avalanche Effect

Change:

```python
message = b"This is my secret message."
```

to:

```python
message = b"This is my secret message.!"
```

Run the program again:

```bash
python3 hash_test.py
```

The hash will be significantly different.

### Concept

```text
Original message
       ↓
     Hash A

Changed message
       ↓
     Hash B
```

A very small input change can produce a very different hash.

This is called the **avalanche effect**.

---

# 5. VS Code + Python — AES Encryption

Python can perform AES encryption using **PyCryptodome**.

## 5.1 Create the Program

In VS Code, create:

```text
aes_test.py
```

Make sure PyCryptodome is installed:

```bash
pip3 install pycryptodome
```

---

## 5.2 AES Encryption and Decryption

Use:

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b"1234567890123456"
message = b"This is my secret message."

# Encryption
cipher = AES.new(key, AES.MODE_CBC)

encrypted = cipher.encrypt(
    pad(message, AES.block_size)
)

print("Ciphertext:", encrypted.hex())

# Decryption
decipher = AES.new(
    key,
    AES.MODE_CBC,
    cipher.iv
)

decrypted = unpad(
    decipher.decrypt(encrypted),
    AES.block_size
)

print("Decrypted:", decrypted.decode())
```

Run:

```bash
python3 aes_test.py
```

Expected:

```text
Ciphertext: <random-looking hexadecimal data>
Decrypted: This is my secret message.
```

### What happened?

```text
Plaintext
   ↓
Python + AES-CBC
   ↓
Ciphertext
   ↓
Python + AES-CBC
   ↓
Original plaintext
```

---

## 5.3 Key and IV

### Key

The **key** is the secret value used by the encryption algorithm.

```text
Key = secret used for encryption/decryption
```

Example:

```python
key = b"1234567890123456"
```

### IV

**IV = Initialization Vector**

The IV is a starting value used by encryption modes such as CBC.

In our Python program:

```python
cipher = AES.new(key, AES.MODE_CBC)
```

PyCryptodome generates the IV automatically.

We then use:

```python
cipher.iv
```

during decryption.

### Important

The **key and IV are different things**.

For real applications:

* The key must be protected.
* The IV should be generated appropriately.
* Do not normally reuse the same IV with the same key.
* Do not use simple example keys such as `1234567890123456` for real security.

The example key is only for learning.

---

# 6. CyberChef — Hashing

CyberChef is a browser-based tool useful for learning and experimenting with cryptographic operations.

## 6.1 SHA3-256

Open CyberChef.

Add the operation:

```text
SHA3
```

Enter your message:

```text
This is my secret message.
```

Select the SHA3-256 option if available.

The output is the **SHA3-256 hash**.

---

## 6.2 Demonstrate Hash Change

First calculate the hash for:

```text
This is my secret message.
```

Then change it to:

```text
This is my secret message.!
```

Calculate the hash again.

The output should be significantly different.

### Concept

```text
Input A → Hash A

Input B → Hash B
```

Even a small change in the input produces a different hash.

---

# 7. CyberChef — AES Encryption

## 7.1 AES Encrypt

Open CyberChef.

Enter:

```text
This is my secret message.
```

Add:

```text
AES Encrypt
```

Use these settings for the learning demonstration:

| Setting      | Value              |
| ------------ | ------------------ |
| Key          | `1234567890123456` |
| Key encoding | UTF-8              |
| IV           | `1234567890123456` |
| IV encoding  | UTF-8              |
| Mode         | CBC                |
| Input        | Raw                |
| Output       | Hex                |

The output will be ciphertext.

```text
Plaintext
   ↓
AES Encrypt
   ↓
Ciphertext
```

---

## 7.2 AES Decrypt

To decrypt the ciphertext:

1. Use **AES Decrypt**.
2. Enter the complete ciphertext.
3. Set the ciphertext input encoding to **Hex**.
4. Use the same key.
5. Use the same IV.
6. Use **CBC** mode.
7. Set the output to the appropriate text/UTF-8 format.

The result should be:

```text
This is my secret message.
```

### Decryption workflow

```text
Ciphertext
   ↓
AES Decrypt
   ↓
Plaintext
```

---

## 7.3 Key and IV

### Key

```text
Key = secret value used to encrypt/decrypt
```

Example:

```text
1234567890123456
```

### IV

```text
IV = Initialization Vector
```

It is a starting value used by CBC mode.

### Why did we use the same value?

For our learning demonstration, we used:

```text
Key = 1234567890123456
IV  = 1234567890123456
```

This was only to keep the practical simple.

**Do not use the same key and IV in real-world cryptographic systems.**

---

# 8. Quick Reference

## Hashing Commands

| Environment | SHA-256                               | SHA-384                               | SHA-512                               |
| ----------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| PowerShell  | `Get-FileHash file -Algorithm SHA256` | `Get-FileHash file -Algorithm SHA384` | `Get-FileHash file -Algorithm SHA512` |
| Linux       | `sha256sum file`                      | `sha384sum file`                      | `sha512sum file`                      |
| Python      | `hashlib.sha256()`                    | `hashlib.sha384()`                    | `hashlib.sha512()`                    |

---

## Encryption Tools

| Tool           | Main Practical                 |
| -------------- | ------------------------------ |
| **CyberChef**  | AES encryption/decryption      |
| **OpenSSL**    | AES file encryption/decryption |
| **Python**     | AES encryption/decryption      |
| **PowerShell** | File hashing                   |

---

## Core Concepts

### Hashing

```text
Data
 ↓
Hash Function
 ↓
Hash
```

* Mainly used for integrity.
* One-way.
* Same input → same hash.
* Small input change → very different hash.

### Encryption

```text
Plaintext
 ↓
Encryption + Key
 ↓
Ciphertext
```

### Decryption

```text
Ciphertext
 ↓
Decryption + Key
 ↓
Plaintext
```

### Key

```text
Secret value used for encryption/decryption
```

### IV

```text
Initialization Vector
```

A starting value used by certain encryption modes such as CBC.

---

## Important Security Notes

* Do not use simple keys such as `1234567890123456` for real systems.
* Protect encryption keys carefully.
* Do not treat a hash as something that can be decrypted.
* Use modern cryptographic algorithms and secure configurations.
* For real applications, prefer authenticated encryption modes such as **AES-GCM** where appropriate.
* Never store real passwords directly in source code.
* For password storage, use password-hashing algorithms such as **Argon2id, bcrypt, scrypt, or PBKDF2**, rather than ordinary SHA-256.

---

## Practical Learning Flow

```text
                 CRYPTOGRAPHY PRACTICAL
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Hashing         Encryption       Verification
        │                │                │
   ┌────┴────┐      ┌────┴────┐          │
PowerShell  Linux  OpenSSL  Python    sha256sum -c
                │       │
             CyberChef │
                │       │
                └── AES ┘
```

### Recommended Practice Order

```text
1. PowerShell hashing
2. Linux hashing
3. Linux hash verification
4. OpenSSL AES encryption
5. OpenSSL AES decryption
6. Python hashing
7. Python AES encryption
8. Python AES decryption
9. CyberChef hashing
10. CyberChef AES encryption
11. CyberChef AES decryption
```
