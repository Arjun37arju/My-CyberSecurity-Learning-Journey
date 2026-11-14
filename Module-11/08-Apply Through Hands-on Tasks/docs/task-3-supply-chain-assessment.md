# Task 3 – Software Supply Chain Security Assessment

## 1. Objective

Assess third-party dependencies, software components,
known vulnerabilities, configuration risks and potential
secret exposure in OWASP Juice Shop.

## 2. Tools Used

| Tool | Purpose |
|---|---|
| npm audit | Dependency vulnerability assessment |
| Syft | Software Bill of Materials generation |
| Trivy | Vulnerability, misconfiguration and secret scanning |
| Gitleaks | Potential exposed secret detection |

## 3. Results

### npm audit

Total dependency vulnerabilities: 40

| Severity | Count |
|---|---:|
| Critical | 6 |
| High | 13 |
| Moderate | 19 |
| Low | 2 |

### Syft – SBOM

- Components identified: 67
- Output: sbom/juice-shop-sbom.json
- Format: CycloneDX JSON

### Trivy

| Scan result | Count |
|---|---:|
| Vulnerabilities | 0 |
| Misconfigurations | 89 |
| Secret findings | 5 |

### Gitleaks

- Potential findings: 75
- Assessment requires validation of detected matches.
- Raw output is excluded from Git because it may contain sensitive values.

## 4. Important Observations

- npm audit identified known vulnerabilities in the dependency tree.
- Trivy identified configuration issues requiring review.
- Trivy reported no vulnerabilities in this filesystem scan.
- Gitleaks identified potential secret exposures.
- Juice Shop contains intentional security challenges, examples and test data.

The findings from different tools have different coverage.
A zero-vulnerability result from Trivy does not invalidate
the npm audit findings.

## 5. Evidence

- SBOM: sbom/juice-shop-sbom.json
- npm audit: reports/npm-audit.json
- Trivy raw report: retained locally, excluded from Git
- Gitleaks raw report: retained locally, excluded from Git

## 6. Limitations

Scanner findings require manual validation.
Potential secrets may include intentional training data.
No dependency upgrades or source-code remediation were
performed during this assessment.

OpenSSF Scorecard review remains pending.

## 7. Conclusion

Dependency auditing, SBOM generation, Trivy scanning and
Gitleaks scanning were completed.

The assessment identified dependency risks, configuration
issues and potential secret exposures for further review.
