# Cybersecurity Tools – Task 1 to Task 7

## 1. SAST – Static Application Security Testing

**Already in your notes**

- **Semgrep** – Scans source code to identify insecure coding patterns and vulnerabilities.
- **SonarQube** – Analyzes source code for bugs, code quality issues, and security vulnerabilities.
- **Bandit** – Identifies common security issues in Python code.
- **CodeQL** – Analyzes code using queries to discover security vulnerabilities.
- **Snyk Code** – Performs static application security testing to identify insecure code.

**Additional important tools**

- **Checkmarx** – Performs static code analysis to identify security vulnerabilities.
- **Fortify SAST** – Analyzes source code to detect security weaknesses before execution.

## 2. DAST – Dynamic Application Security Testing

**Already in your notes**

- **Burp Suite** – Intercepts and analyzes web traffic to test web application security.
- **OWASP ZAP** – Scans running web applications to identify security vulnerabilities.
- **Nikto** – Scans web servers for outdated software, dangerous files, and misconfigurations.
- **Nuclei** – Uses customizable templates to scan systems and applications for known vulnerabilities.

**Additional important tools**

- **Acunetix** – Performs automated web application vulnerability scanning.
- **Wapiti** – Scans web applications for vulnerabilities such as SQL injection and XSS.

## 3. Dependency Security / SCA

**Already in your notes**

- **Dependabot** – Detects outdated and vulnerable dependencies and can create update pull requests.
- **Snyk** – Identifies vulnerabilities in open-source dependencies and helps developers fix them.
- **OWASP Dependency-Check** – Identifies known vulnerabilities in project dependencies.
- **Trivy** – Scans dependencies, container images, and other software components for vulnerabilities.
- **GitHub Dependency Review** – Checks dependency changes in pull requests for known security vulnerabilities.
- **npm audit** – Checks Node.js project dependencies for known vulnerabilities.
- **pip-audit** – Checks Python packages for known security vulnerabilities.

**Additional important tools**

- **OSV-Scanner** – Scans project dependencies against the Open Source Vulnerabilities database.
- **Grype** – Scans software packages and container images for known vulnerabilities.
- **Syft** – Generates a Software Bill of Materials (SBOM) listing software components and dependencies.

## 4. Secrets Management and Secret Scanning

**Already in your notes**

- **HashiCorp Vault** – Securely stores and manages sensitive information such as passwords, API keys, and tokens.
- **AWS Secrets Manager** – Stores, manages, and retrieves application secrets in AWS.
- **Azure Key Vault** – Protects secrets, encryption keys, and certificates in Microsoft Azure.
- **Kubernetes Secrets** – A Kubernetes resource used to store sensitive information required by applications.

**Additional important tools**

- **Gitleaks** – Scans Git repositories for accidentally exposed passwords, API keys, and other secrets.
- **TruffleHog** – Searches repositories and other data sources for exposed credentials and secrets.

## 5. Container Security

**Already in your notes**

- **Trivy** – Scans container images for vulnerabilities and misconfigurations.
- **Clair** – Identifies known vulnerabilities in container images.

**Additional important tools**

- **Grype** – Detects known vulnerabilities in container images and software packages.
- **Docker Scout** – Analyzes container images and identifies vulnerable software components.

## 6. CI/CD Pipeline and Automation

**Additional important tools**

- **Jenkins** – Automates software building, testing, and deployment through CI/CD pipelines.
- **GitHub Actions** – Automates workflows such as code testing, security scanning, and deployment.
- **GitLab CI/CD** – Automates application building, testing, and deployment using pipeline configurations.

## 7. Infrastructure-as-Code Security

**Additional important tools**

- **Checkov** – Scans Infrastructure-as-Code files for security misconfigurations.
- **KICS** – Detects security vulnerabilities and misconfigurations in Infrastructure-as-Code.
- **Terrascan** – Checks Infrastructure-as-Code configurations against security policies.

## 8. Software Integrity and Supply Chain Security

**Additional important tools**

- **Cosign** – Signs and verifies software artifacts and container images.
- **in-toto** – Helps verify the integrity of software supply chain steps.
- **SLSA tools and integrations** – Help organizations implement and verify software supply chain security requirements.

## 9. Threat Modeling

**Additional important tools**

- **OWASP Threat Dragon** – Helps create threat models and identify potential security threats in application architecture.
- **Microsoft Threat Modeling Tool** – Helps identify and analyze security threats during application design.

## 10. Security Monitoring

**Already in your notes**

- **Splunk** – Collects and analyzes security logs to identify suspicious activities.
- **Microsoft Sentinel** – A cloud-based SIEM and security analytics platform.
- **Microsoft Defender for Cloud** – Helps identify security risks and monitor cloud resources.

**Additional important tools**

- **Wazuh** – An open-source security monitoring platform for threat detection, log analysis, and endpoint monitoring.
- **Falco** – Monitors runtime system activity to detect suspicious behavior in containers and Linux environments.

---

## Important Note

The following items in your notes are security standards, frameworks, methods, or technologies rather than standalone security tools:

- PCI DSS, GDPR, HIPAA, ISO 27001, SOC 2 – Standards, regulations, or compliance frameworks.
- STRIDE and PASTA – Threat modeling methodologies.
- SAST and DAST – Security testing approaches.
- CI/CD – Software development and delivery practices.
- RBAC – An authorization model.
- Kubernetes Secrets – A built-in Kubernetes resource, not a dedicated secret management tool.
