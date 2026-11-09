#  Understand Application Security Testing


- [1. Security Reviews](#1-security-reviews) 
- [2. Static Analysis Awareness (SAST)](#2-static-analysis-awareness-sast) 
- [3. Dynamic Analysis Awareness (DAST)](#3-dynamic-analysis-awareness-dast) 
- [4. Vulnerability Discovery Concepts](#4-vulnerability-discovery-concepts) 
- [5. Security Validation](#5-security-validation) 
- [6. SAST vs DAST](#6-sast-vs-dast) 


---

## 1. Security Reviews

**Security review** means examining an application's code, design, configuration, and security practices to identify possible security problems.

Security reviews help identify mistakes before the application is released.

### What Do Security Teams Review?

- Source code.
- Authentication mechanisms.
- Authorization rules.
- Data protection.
- Input validation.
- Application configurations.

### Example

Imagine a developer creates a login system.

During a security review, the security team discovers that passwords are stored as plain text in the database.

This is a serious security weakness because anyone who gains access to the database could read the passwords.

The developer should implement secure password hashing.

**Main Goal:** Identify security weaknesses by reviewing the application's implementation and design.

---

## 2. Static Analysis Awareness (SAST)

**SAST (Static Application Security Testing)** means analyzing an application's source code without executing the application.

It helps developers identify security weaknesses directly in the code.

### How Does It Work?

1. Developers write application code.
2. A static analysis tool examines the source code.
3. The tool identifies potentially insecure coding patterns.
4. Developers review and fix the reported issues.

### Example

Consider this SQL query:

```sql
query = "SELECT * FROM users WHERE name = '" + username + "'";
```

If user input is directly added to a SQL query, it may create an SQL injection vulnerability.

A static analysis tool may identify this unsafe coding pattern.

### Common SAST Tools

- SonarQube
- Semgrep
- Checkmarx

**Main Goal:** Find potential security vulnerabilities in source code without running the application.

---

## 3. Dynamic Analysis Awareness (DAST)

**DAST (Dynamic Application Security Testing)** means testing an application while it is running to identify security vulnerabilities.

Unlike SAST, DAST does not need to analyze the application's source code.

It examines how the application behaves when it receives different requests and inputs.

### How Does It Work?

1. The application is deployed in a testing environment.
2. A security testing tool sends different requests.
3. The tool observes the application's responses.
4. It identifies possible security weaknesses.
5. Developers investigate and fix the findings.

### Example

Imagine a web application has a login page.

A DAST tool sends unexpected input to the login form and checks how the application responds.

It may discover that the application is vulnerable to SQL injection.

### Common DAST Tools

- OWASP ZAP
- Burp Suite
- Invicti

**Main Goal:** Identify security vulnerabilities by testing a running application.

---

## 4. Vulnerability Discovery Concepts

**Vulnerability discovery** means finding weaknesses in an application that attackers could potentially exploit.

Security professionals use different methods to discover vulnerabilities.

### Common Vulnerability Discovery Methods

| Method | Meaning |
|---|---|
| Code Review | Manually examine source code for security mistakes |
| Vulnerability Scanning | Use tools to automatically identify known weaknesses |
| Penetration Testing | Simulate attacks to identify exploitable vulnerabilities |
| Configuration Review | Check whether application settings are secure |
| Dependency Scanning | Identify vulnerable third-party libraries and packages |

### Example

Imagine a web application uses an outdated software library.

A security researcher discovers that the library has a known vulnerability.

The security team identifies the affected component and updates it to a secure version.

### Common Vulnerability Examples

- SQL Injection
- Cross-Site Scripting (XSS)
- Broken Authentication
- Broken Access Control
- Security Misconfiguration
- Vulnerable Components

**Main Goal:** Discover weaknesses before attackers find and exploit them.

---

## 5. Security Validation

**Security validation** means verifying that security controls are working correctly and that identified vulnerabilities have been properly fixed.

Finding and fixing a vulnerability is not enough. Security teams must also confirm that the solution works.

### How Does It Work?

1. Identify a security vulnerability.
2. Fix the vulnerability.
3. Test the application again.
4. Confirm that the vulnerability is no longer present.
5. Check that the fix has not introduced new security problems.

### Example

Imagine a security tester discovers SQL injection in a login page.

The developer fixes the issue using parameterized SQL queries.

The security tester tests the login page again to confirm that the SQL injection vulnerability has been addressed.

**Main Goal:** Confirm that security measures work correctly and vulnerabilities have been resolved.

---

## 6. SAST vs DAST

| SAST | DAST |
|---|---|
| Analyzes source code | Tests a running application |
| Does not execute the application | Requires the application to be running |
| Finds potentially insecure coding patterns | Finds vulnerabilities observable through application behavior |
| Usually used during development | Often used during testing and before release |
| Example: Semgrep | Example: OWASP ZAP |

### Easy Way to Remember

- **SAST:** Checks the code itself.
- **DAST:** Checks the running application.

---

| Concept | Description |
|---|---|
| Security Reviews | Examine code, design, and configurations |
| Static Analysis (SAST) | Analyze source code without executing it |
| Dynamic Analysis (DAST) | Test a running application |
| Vulnerability Discovery | Find security weaknesses |
| Security Validation | Verify security controls and fixes |

