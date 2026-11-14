# Task 5 – Final DevSecOps Security Assessment Report

## 1. Project Overview

This project demonstrates an integrated DevSecOps security assessment of OWASP Juice Shop. It combines application security testing, dependency analysis, software supply-chain assessment, and automated security scanning through GitHub Actions.

**Application:** OWASP Juice Shop  
**Repository:** My-CyberSecurity-Learning-Journey  
**Environment:** Kali Linux, Docker, GitHub Actions

## 2. Application Architecture and Threat Model

The application uses:
- Frontend: Angular
- Backend: Node.js, Express, and TypeScript
- Database: SQLite with Sequelize ORM
- Real-time communication: Socket.IO
- API: REST and B2B API endpoints

The assessment identified important entry points such as authentication, password reset, payment, file uploads, user profiles, and application APIs.

A threat model was prepared to document application components, data flows, actors, and trust boundaries.

## 3. OWASP Top 10 Assessment

The application was reviewed against the OWASP Top 10:2025 categories:

1. Broken Access Control
2. Security Misconfiguration
3. Software Supply Chain Failures
4. Cryptographic Failures
5. Injection
6. Insecure Design
7. Authentication Failures
8. Software or Data Integrity Failures
9. Security Logging and Alerting Failures
10. Mishandling of Exceptional Conditions

The review identified potential security weaknesses requiring further validation. The application is intentionally vulnerable and is used for security learning and testing.

## 4. Static Application Security Testing – Semgrep

Semgrep was used to identify potentially insecure coding patterns.

**Results:**
- Total findings: 71
- ERROR: 20
- WARNING: 46
- MEDIUM: 2
- INFO: 3

Potential issues included SQL injection patterns, hardcoded secrets, dynamic code execution, path traversal, open redirects, and potential cross-site scripting.

These results require manual validation because some findings may originate from intentional challenges, test files, and example code.

## 5. Dynamic Application Security Testing – OWASP ZAP

OWASP ZAP Baseline Scan was performed against the locally hosted Juice Shop application.

**Results:**
- Total alerts: 9
- Medium: 2
- Low: 4
- Informational: 3

Important alerts included:
- Content Security Policy header not set.
- Cross-domain misconfiguration.
- Missing or invalid COEP and COOP headers.
- Dangerous JavaScript functions.

The baseline scan was passive and did not perform an active attack assessment.

## 6. Dependency and Supply Chain Security

### npm audit

The CI pipeline reported 42 dependency findings:

- Critical: 6
- High: 13
- Moderate: 21
- Low: 2

These findings indicate dependency risks requiring review and prioritization.

### Trivy

The CI pipeline reported 94 items:

- Critical: 20
- High: 25
- Medium: 9
- Low: 40

The report combines different scanner finding types, including vulnerabilities, misconfigurations, and secrets. These severity counts must not be interpreted as vulnerability counts alone.

### Gitleaks

Gitleaks reported 75 potential findings:

- generic-api-key: 60
- jwt: 12
- private-key: 3

These are potential secret exposures. They require manual verification to determine whether they are genuine active credentials or intentional test data.

### Software Bill of Materials

Syft generated a CycloneDX SBOM.

- Format: CycloneDX
- Version: 1.7
- Components: 67

The SBOM provides an inventory of application components and supports dependency transparency.

## 7. Secure CI/CD Pipeline

An integrated GitHub Actions workflow was implemented in:

`.github/workflows/security.yml`

The pipeline integrates:

- npm audit – dependency vulnerability assessment
- Semgrep – static application security testing
- Trivy – vulnerability, misconfiguration, and secret scanning
- Gitleaks – secret detection
- Syft – SBOM generation
- OpenSSF Scorecard – repository security practices assessment

The workflow runs on relevant pushes, pull requests, and manual execution.

**Execution result:** The updated pipeline completed successfully.

Security reports were uploaded as GitHub Actions artifacts for later review.

## 8. OpenSSF Scorecard Assessment

OpenSSF Scorecard identified several repository security improvements:

- Branch protection is not enabled on the main branch.
- GitHub Actions and container dependencies are not fully pinned by immutable hashes.
- A license file was not detected.
- A security policy file was not detected.
- No dependency update automation was detected.
- No fuzzing integration was detected.
- No OpenSSF Best Practices badge effort was detected.

These findings identify opportunities to improve repository security and software development practices.

The supplied SARIF summary does not establish an overall Scorecard score.

## 9. Recommendations

1. Enable branch protection and require code review.
2. Pin GitHub Actions and container images to immutable versions or digests.
3. Review and update vulnerable dependencies.
4. Manually validate Semgrep, Trivy, and Gitleaks findings.
5. Add a security policy and license file where appropriate.
6. Introduce automated dependency update management.
7. Consider fuzz testing for important application components.
8. Review security headers and configuration.
9. Continue running automated security scans during development.
10. Keep SBOMs and security reports updated.

## 10. Conclusion

This project demonstrated how security practices can be integrated throughout the software development lifecycle using DevSecOps tools and automation.

The assessment combined architecture review, threat modeling, OWASP Top 10 analysis, SAST, DAST, dependency auditing, secret detection, SBOM generation, and repository security assessment.

The integrated GitHub Actions pipeline successfully executed the configured security checks and generated reports.

The findings provide a foundation for understanding application security weaknesses, improving software supply-chain security, and strengthening CI/CD workflows.

**Project Outcome:** Successfully implemented an integrated DevSecOps security assessment and automated CI/CD pipeline for OWASP Juice Shop.
