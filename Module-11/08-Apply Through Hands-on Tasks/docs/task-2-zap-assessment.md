# Task 2 – OWASP ZAP DAST Assessment

## 1. Objective

Dynamic Application Security Testing (DAST) was performed
against the locally running OWASP Juice Shop application
using OWASP ZAP.

## 2. Tool Information

- Tool: OWASP ZAP
- Assessment type: Dynamic Application Security Testing
- Scan type: Baseline (Passive Scan)
- Target: http://127.0.0.1:3000

## 3. Scan Summary

Total alerts: 9

| Risk | Count |
|---|---:|
| Medium | 2 |
| Low | 4 |
| Informational | 3 |
| Total | 9 |

## 4. Important Observations

| Alert | Risk | OWASP relevance |
|---|---|---|
| Content Security Policy Header Not Set | Medium | A02 |
| Cross-Domain Misconfiguration | Medium | A02 |
| COEP Header Missing or Invalid | Low | A02 |
| COOP Header Missing or Invalid | Low | A02 |
| Dangerous JS Functions | Low | A05 - Requires review |
| Deprecated Feature Policy Header | Low | A02 |

Informational observations:
- Modern Web Application
- Storable and Cacheable Content
- Storable but Non-Cacheable Content

## 5. Assessment Limitations

This was a ZAP baseline scan using passive scanning.

The alerts indicate potential security weaknesses and
configuration improvements. They require manual validation
before being classified as confirmed vulnerabilities.

The scan did not perform active attack testing.

## 6. Evidence

- HTML report: reports/zap-report.html
- JSON report: reports/zap-report.json

## 7. Conclusion

OWASP ZAP successfully completed the baseline assessment
and identified 9 alerts.

The results highlight areas for further review, particularly
security headers and cross-domain configuration.
