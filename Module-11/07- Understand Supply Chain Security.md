# Understand Supply Chain Security

## Navigation

- [ Introduction](#introduction)
- [1. Third-Party Software Risks](#1-third-party-software-risks)
- [2. Dependency Management](#2-dependency-management)
- [3. Software Integrity](#3-software-integrity)
- [4. Security Monitoring](#4-security-monitoring)
- [5. Risk Mitigation](#5-risk-mitigation)
- [Supply Chain Security Workflow](#supply-chain-security-workflow)
- [Additional Resources](#Additional-Resources)


---

## Introduction

**Software Supply Chain Security** focuses on protecting all components, tools, services, and processes involved in developing and delivering software.

A software application may depend on external libraries, open-source packages, third-party tools, and build systems.

If any component in the supply chain is compromised, attackers may use it to introduce malicious code or vulnerabilities into the application.

**Main objective:**
- Protect software components.
- Identify third-party risks.
- Verify software integrity.
- Monitor security threats.
- Reduce supply chain vulnerabilities.

## 1. Third-Party Software Risks

Third-party software risks are security threats that come from external software, libraries, packages, or services used in an application.

Developers often use third-party components to save development time. However, these components may contain security weaknesses.

**Common risks:**
- Vulnerable third-party libraries.
- Malicious open-source packages.
- Compromised software updates.
- Untrusted software vendors.
- Outdated external components.

**Example:**

A developer downloads an external library containing malicious code. When the library is included in an application, the malicious code may affect the application and its users.

**Security practices:**
- Use trusted software sources.
- Check the reputation of external packages.
- Scan third-party components.
- Avoid unnecessary dependencies.

## 2. Dependency Management

Dependency management is the process of identifying, installing, updating, and maintaining external libraries and packages used by an application.

Poor dependency management can introduce vulnerable or outdated components.

**Important practices:**
- Maintain a list of application dependencies.
- Update outdated libraries regularly.
- Remove unused dependencies.
- Check dependencies for known vulnerabilities.
- Use trusted package repositories.
- Review dependency updates before installation.

**Common tools:**
- Dependabot
- Snyk
- OWASP Dependency-Check

**Example:**

An application uses an outdated JavaScript package with a known vulnerability. Dependabot can identify an available update and create a pull request to update the package.

## 3. Software Integrity

Software integrity means ensuring that software has not been modified, replaced, or tampered with by unauthorized parties.

It helps verify that the software received is the same as the software originally created and approved.

**Important practices:**
- Verify software checksums.
- Use digital signatures.
- Verify downloaded packages.
- Protect source code repositories.
- Secure build artifacts.
- Use trusted software distribution sources.

**Important concepts:**

**Checksum:**
A value calculated from a file to help detect unexpected changes.

**Digital Signature:**
A cryptographic mechanism used to verify the authenticity and integrity of software.

**Example:**

Before installing a downloaded software package, its SHA-256 checksum can be compared with the checksum provided by the trusted publisher. If the values do not match, the file may have been modified or corrupted.

## 4. Security Monitoring

Security monitoring means continuously observing software components, dependencies, repositories, and development systems to identify suspicious activities and security issues.

It helps detect threats that may affect the software supply chain.

**Important monitoring activities:**
- Monitor dependency vulnerabilities.
- Track suspicious repository changes.
- Review software update activities.
- Monitor access to development systems.
- Check security alerts.
- Analyze build and deployment logs.

**Common tools:**
- GitHub Security Advisories
- Dependabot
- Snyk
- SIEM tools

**Example:**

If a third-party package is reported as malicious, security monitoring helps identify applications using that package so the affected dependency can be investigated and removed.

## 5. Risk Mitigation

Risk mitigation means taking security measures to reduce the likelihood and impact of software supply chain attacks.

It focuses on preventing security issues and reducing damage when a component is compromised.

**Important practices:**
- Use trusted third-party components.
- Apply security updates regularly.
- Remove vulnerable dependencies.
- Verify software signatures and checksums.
- Restrict access to repositories and build systems.
- Maintain backup and recovery procedures.
- Prepare incident response plans.

**Example:**

If a dependency is found to contain a critical vulnerability, developers can update or replace it with a secure version and verify that the application is no longer affected.

##  Supply Chain Security Workflow

```text
Identify Software Components
          |
          v
Review Third-Party Risks
          |
          v
Manage Dependencies
          |
          v
Verify Software Integrity
          |
          v
Monitor Security Issues
          |
          v
Apply Risk Mitigation
          |
          v
Maintain Secure Software
```

---

### Additional Resources

For more information about Secure SDLC, DevSecOps, and related security tools, refer to:

[Secure Software Development Lifecycle & DevSecOps Tools](../resources/Secure%20Software%20Development%20Lifecycle%20%26%20DevSec%20Ops%20Tools.md)
