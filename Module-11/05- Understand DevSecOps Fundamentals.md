# Understand DevSecOps Fundamentals

---

- [Introduction](#introduction)
- [1. What is DevSecOps?](#what-is-devsecops)
- [2. Shift-Left Security](#shift-left-security)
- [3. Security Automation](#security-automation)
- [4. Security Integration](#security-integration)
- [5. Continuous Security](#continuous-security)
- [DevSecOps Workflow](#devsecops-workflow)


---

## Introduction

DevSecOps is an approach that integrates security into the software development and operations process.

Instead of checking security only at the end of development, DevSecOps encourages teams to consider security throughout the software development lifecycle.

## What is DevSecOps?

DevSecOps stands for:

- **Dev** – Development
- **Sec** – Security
- **Ops** – Operations

It brings developers, security professionals, and operations teams together to build and maintain secure applications.

**Example:**

When developers write application code, security checks are performed to identify vulnerabilities before the application is released.

## Shift-Left Security

Shift-Left Security means performing security checks as early as possible in the software development lifecycle.

The goal is to identify and fix security issues before they become bigger problems.

**Example:**

A developer checks application code for security vulnerabilities while writing the code instead of waiting until the application is completed.

**Benefits:**
- Finds security issues early.
- Reduces the cost of fixing vulnerabilities.
- Improves application security.

## Security Automation

Security automation means using tools and scripts to perform security tasks automatically.

It reduces manual work and helps teams identify security issues faster.

**Examples of automated security tasks:**
- Source code scanning.
- Dependency vulnerability scanning.
- Secret detection.
- Configuration checks.
- Automated security testing.

**Common tools:**
- SonarQube
- Trivy
- Snyk
- GitHub Actions

## Security Integration

Security integration means including security tools and checks in the software development workflow.

Security tools can be integrated into the **CI/CD pipeline**.

CI/CD stands for:
- **CI:** Continuous Integration
- **CD:** Continuous Delivery or Continuous Deployment

**Example:**

When a developer pushes code to a repository, the CI/CD pipeline can automatically:
1. Build the application.
2. Perform source code security scanning.
3. Check dependencies for vulnerabilities.
4. Detect exposed secrets.
5. Run tests.
6. Continue toward deployment if required checks pass.

If a serious security issue is detected, the pipeline can stop the release until the issue is fixed.

## Continuous Security

Continuous Security means maintaining security throughout the application lifecycle, including after deployment.

Security does not end when an application is released.

**Examples:**
- Continuously monitoring application logs.
- Performing regular vulnerability scans.
- Applying security patches.
- Monitoring suspicious activities.
- Responding to security incidents.

**Why is it important?**

New vulnerabilities and threats can appear even after an application is deployed.

## DevSecOps Workflow

A simple DevSecOps workflow:

```text
Developer writes code
        |
        v
Code is pushed to repository
        |
        v
CI/CD pipeline starts
        |
        v
Automated security checks
        |
        v
Application testing
        |
        v
Deployment
        |
        v
Continuous monitoring
```

Security checks are included throughout this workflow.

