# Task 2 – Consolidated Security Assessment Report

## 1. Objective

The objective was to assess the OWASP Juice Shop application
using the OWASP Top 10:2025 as the security assessment framework.

Target: http://127.0.0.1:3000

All dynamic testing was performed against the locally running
authorized application.

## 2. Assessment Tools

| Tool | Assessment Type | Purpose |
|---|---|---|
| Manual review | Source review | Understand potential security weaknesses |
| Semgrep | SAST | Identify insecure coding patterns |
| OWASP ZAP | DAST | Identify potential runtime security issues |

## 3. Semgrep Results

- Tool version: 1.185.0
- Total findings: 71

| Semgrep Severity | Count |
|---|---:|
| ERROR | 20 |
| WARNING | 46 |
| MEDIUM | 2 |
| INFO | 3 |
| Total | 71 |

Important areas identified for review:

- SQL injection patterns
- Hardcoded HMAC and JWT secrets
- Dynamic eval() usage
- Possible path traversal
- Open redirect patterns
- Potential cross-site scripting
- GitHub Actions workflow security
- Directory listing configuration

These are preliminary scanner findings and are not all
confirmed vulnerabilities.

## 4. OWASP ZAP Results

- Scan type: Baseline / Passive Scan
- Total alerts: 9

| Risk | Count |
|---|---:|
| Medium | 2 |
| Low | 4 |
| Informational | 3 |
| Total | 9 |

Important alerts:

- Content Security Policy Header Not Set
- Cross-Domain Misconfiguration
- Cross-Origin-Embedder-Policy Header Missing or Invalid
- Cross-Origin-Opener-Policy Header Missing or Invalid
- Dangerous JS Functions
- Deprecated Feature Policy Header Set

Informational observations:

- Modern Web Application
- Storable and Cacheable Content
- Storable but Non-Cacheable Content

These alerts require validation before being treated as
confirmed vulnerabilities.

## 5. OWASP Top 10:2025 Mapping

| Category | Assessment observations | Status |
|---|---|---|
| A01 Broken Access Control | Possible path traversal and open redirect patterns | Preliminary |
| A02 Security Misconfiguration | Missing security headers and directory listing observation | Preliminary |
| A03 Software Supply Chain Failures | Dependency and package configuration require further review | Partial |
| A04 Cryptographic Failures | Hardcoded cryptographic secret patterns | Preliminary |
| A05 Injection | SQL injection, eval(), and XSS patterns | Preliminary |
| A06 Insecure Design | Requires deeper manual design review | Not fully assessed |
| A07 Authentication Failures | JWT and authentication-related code requires validation | Preliminary |
| A08 Software or Data Integrity Failures | GitHub Actions workflow integrity concerns | Preliminary |
| A09 Security Logging and Alerting Failures | Requires dedicated logging and alerting review | Not assessed |
| A10 Mishandling of Exceptional Conditions | Requires dedicated error-handling review | Not assessed |

## 6. Important Limitations

OWASP Juice Shop is intentionally vulnerable and includes
security challenge examples, test files, and demonstration code.

Semgrep findings and ZAP alerts are scanner results, not
automatically confirmed vulnerabilities.

The ZAP assessment used a passive baseline scan. It did not
perform active attack testing.

Semgrep severity labels are not CVSS scores.

No vulnerability fixes or changes to the upstream Juice Shop
application were performed as part of this assessment.

## 7. Evidence Files

- OWASP checklist: docs/task-2-owasp-top-10.md
- Semgrep assessment: docs/task-2-semgrep-assessment.md
- ZAP assessment: docs/task-2-zap-assessment.md
- Semgrep JSON: reports/semgrep-results.json
- ZAP HTML: reports/zap-report.html
- ZAP JSON: reports/zap-report.json

## 8. Conclusion

Static and dynamic security assessment tools were successfully
executed against the local OWASP Juice Shop application.

Semgrep reported 71 preliminary findings, while OWASP ZAP
reported 9 alerts.

The results identified areas requiring further security review,
including injection patterns, authentication-related code,
security headers, and workflow integrity.

Task 2 provides an initial security assessment baseline.
Some OWASP categories require additional dedicated testing
before the assessment can be considered comprehensive.
