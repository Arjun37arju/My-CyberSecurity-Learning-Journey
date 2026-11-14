# Task 2 – Semgrep SAST Assessment

## 1. Objective

Static Application Security Testing (SAST) was performed
on the OWASP Juice Shop source code using Semgrep.

## 2. Tool Information

- Tool: Semgrep
- Version: 1.185.0
- Assessment type: Static Application Security Testing
- Target: app/juice-shop
- Report: reports/semgrep-results.json

## 3. Scan Summary

Total findings: 71

| Semgrep Severity | Count |
|---|---:|
| ERROR | 20 |
| WARNING | 46 |
| MEDIUM | 2 |
| INFO | 3 |
| Total | 71 |

## 4. Important Observations

| Potential issue | Affected file or area | OWASP relevance |
|---|---|---|
| SQL injection patterns | routes/login.ts, routes/search.ts | A05 |
| Hardcoded HMAC/JWT secrets | lib/insecurity.ts | A04, A07 |
| Dynamic eval() usage | routes/userProfile.ts | A05 |
| Possible path traversal | routes/fileServer.ts | A01 |
| Open redirect | routes/redirect.ts | A01 |
| Potential XSS | views/promotionVideo.pug | A05 |
| Mutable GitHub Actions references | .github/workflows/ | A03, A08 |
| Directory listing | server.ts | A02 |

These are preliminary observations and require validation.

## 5. Assessment Limitations

Juice Shop is intentionally vulnerable training software.

The scan also included:
- Security challenge examples.
- Test and specification files.
- Upstream GitHub workflows.
- Terraform infrastructure examples.

Therefore, all scanner findings must be reviewed before being
classified as confirmed vulnerabilities.

Semgrep severity labels are rule classifications and are not
equivalent to CVSS ratings.

## 6. Evidence

The complete machine-readable scan output is stored at:

reports/semgrep-results.json

## 7. Conclusion

Semgrep successfully completed static analysis and reported
71 potential security findings.

The results provide a starting point for identifying insecure
coding patterns and mapping potential weaknesses to OWASP Top 10.

Further validation and dynamic application testing are required.
