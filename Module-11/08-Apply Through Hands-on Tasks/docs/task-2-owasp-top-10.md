# Task 2 – OWASP Top 10 Security Assessment

## 1. Objective

The objective is to assess the OWASP Juice Shop application
against the OWASP Top 10:2025 web application security risks.

Testing will be performed only against our locally running
authorized Juice Shop instance.

Target: http://127.0.0.1:3000

## 2. OWASP Top 10:2025 Assessment Checklist

| ID | Security Risk | Assessment Focus | Status |
|---|---|---|---|
| A01 | Broken Access Control | Unauthorized access and privilege restrictions | Not tested |
| A02 | Security Misconfiguration | Application and server security settings | Not tested |
| A03 | Software Supply Chain Failures | Third-party dependencies and software components | Not tested |
| A04 | Cryptographic Failures | Protection of sensitive information | Not tested |
| A05 | Injection | Unsafe handling of user input | Not tested |
| A06 | Insecure Design | Security weaknesses in application design | Not tested |
| A07 | Authentication Failures | Login, authentication and session management | Not tested |
| A08 | Software or Data Integrity Failures | Trust and integrity of software and data | Not tested |
| A09 | Security Logging and Alerting Failures | Security event logging and detection | Not tested |
| A10 | Mishandling of Exceptional Conditions | Error handling and unexpected application behavior | Not tested |

## 3. Assessment Methods

The following methods will be used during this task:

- Manual application security review.
- Source code analysis using Semgrep (SAST).
- Dynamic application testing using OWASP ZAP (DAST).

## 4. Evidence and Findings

Each confirmed finding will include:

- Finding title
- OWASP category
- Affected component or endpoint
- Evidence
- Security impact
- Severity
- Recommended remediation

Potential issues will not be reported as confirmed vulnerabilities
until sufficient evidence has been collected.

## 5. Assessment Status

Initial checklist created.

Detailed security testing is pending.

## 6. Reference

OWASP Top 10:2025:
https://top10.owasp.org/
