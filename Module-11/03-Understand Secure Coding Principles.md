# Understand Secure Coding Principles


---
- [1. Input Validation](#1-input-validation)
- [2. Error Handling](#2-error-handling) 
- [3. Authentication Security](#3-authentication-security) 
- [4. Authorization Security](#4-authorization-security) 
- [5. Secure Development Mindset](#5-secure-development-mindset) 

---

## 1. Input Validation

**Input validation** means checking user-provided data before accepting or processing it.

Applications receive input from users through:

- Login forms
- Registration forms
- Search boxes
- Contact forms
- File uploads

If applications don't validate input properly, attackers may send malicious or unexpected data.

### Example: Age Validation

Imagine an application accepts an age between 1 and 120.

| Input | Result |
|---|---|
| 25 | Accepted |
| -5 | Rejected |
| abc | Rejected |
| 150 | Rejected |

### Security Practices

- Check the expected input format.
- Set maximum and minimum input lengths.
- Validate data types and allowed values.
- Reject unexpected input.
- Use parameterized SQL queries to prevent SQL injection.

**Main Goal:** Prevent invalid or malicious data from entering the application.

---

## 2. Error Handling

**Error handling** means managing unexpected situations or errors without exposing sensitive information or crashing the application.

Applications may experience errors because of:

- Incorrect user input
- Database connection failures
- Missing files
- Server problems
- Programming mistakes

### Example: Login Application

An insecure application might display:

```text
Database authentication failed for user admin
at server 192.168.1.10
```

This message reveals internal technical information.

A secure application should display:

```text
Invalid username or password.
```

### Security Practices

- Avoid displaying internal system details to users.
- Record errors securely in logs.
- Handle unexpected exceptions.
- Avoid exposing passwords, tokens, or sensitive data.
- Use generic error messages where appropriate.

**Main Goal:** Handle errors safely without revealing sensitive system information.

---

## 3. Authentication Security

**Authentication** is the process of verifying the identity of a user.

In simple words, authentication answers:

**"Who are you?"**

### Common Authentication Methods

| Method | Meaning |
|---|---|
| Password | User enters a secret password |
| OTP | One-Time Password used for verification |
| MFA | Uses two or more authentication factors |
| Biometrics | Uses fingerprint or facial recognition |
| Security Key | Uses a physical or cryptographic authentication key |

### Example: Online Banking

1. User enters a username and password.
2. Application verifies the credentials.
3. User completes OTP verification.
4. Application grants access after successful authentication.

### Security Practices

- Store passwords using secure password hashing.
- Enforce strong password policies.
- Implement MFA where appropriate.
- Protect authentication sessions.
- Apply rate limiting to prevent brute-force attacks.

**Main Goal:** Ensure only legitimate users can access their accounts.

---

## 4. Authorization Security

**Authorization** determines what an authenticated user is allowed to access or perform.

In simple words, authorization answers:

**"What are you allowed to do?"**

### Example: Company Application

Imagine a company application has three types of users:

| User | Permission |
|---|---|
| Employee | View personal records |
| Manager | View and manage team records |
| Administrator | Manage users and system settings |

Even after successfully logging in, an employee should not be able to access administrator functions.

### Security Practices

- Apply Role-Based Access Control (RBAC).
- Follow the principle of least privilege.
- Check permissions on the server side.
- Prevent unauthorized access to resources.
- Review user permissions regularly.

**Main Goal:** Ensure users can access only the resources and actions they are permitted to use.

### Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Verifies identity | Checks permissions |
| Who are you? | What can you do? |
| Happens before authorization | Follows successful authentication |
| Example: Password and OTP | Example: Admin or employee access |

---

## 5. Secure Development Mindset

A **secure development mindset** means thinking about security while writing code, designing features, testing applications, and maintaining software.

Developers should not only think about whether their code works. They should also think about how someone could misuse or attack it.

### Important Practices

1. **Think Like an Attacker:** Consider how someone might exploit your application.
2. **Follow Secure Coding Standards:** Use established secure programming practices.
3. **Never Trust User Input:** Validate all untrusted data.
4. **Protect Sensitive Information:** Never expose passwords, API keys, or confidential data.
5. **Review Your Code:** Look for security weaknesses before releasing software.
6. **Keep Learning:** Stay aware of new vulnerabilities and attack techniques.

### Example: File Upload Feature

A developer creates a file upload feature.

Instead of accepting every uploaded file, the developer implements:

- File type validation.
- File size restrictions.
- Safe file storage.
- Access restrictions.

This demonstrates a secure development mindset.

**Main Goal:** Make security a regular part of software development rather than treating it as a separate task.

---

### Important Differences

- **Authentication:** Who are you?
- **Authorization:** What are you allowed to do?
- **Input Validation:** Is the provided data acceptable and safe to process?



**Next Topic:** Understand Secure Software Design and Architecture
