# Understand Cloud Threats

## Contents
1. [Misconfigurations](#1-misconfigurations)
2. [Credential Theft](#2-credential-theft)
3. [Excessive Permissions](#3-excessive-permissions)
4. [Data Exposure](#4-data-exposure)
5. [Insider Threats](#5-insider-threats)

---

## 1. Misconfigurations

**Misconfiguration** means setting up a cloud service incorrectly or insecurely.

**Examples:**
- Making a private storage bucket public.
- Allowing unnecessary network traffic through a firewall.
- Leaving a database accessible from the internet.

**Prevention:**
- Review cloud settings regularly.
- Restrict public access.
- Configure firewalls securely.
- Use security tools to detect incorrect settings.

## 2. Credential Theft

**Credential theft** occurs when attackers steal passwords, API keys, access tokens, or other login information.

**Common causes:**
- Phishing attacks.
- Weak or reused passwords.
- Exposed API keys in source code.
- Leaked credentials.

**Prevention:**
- Enable Multi-Factor Authentication (MFA).
- Use strong, unique passwords.
- Store secrets securely.
- Revoke exposed credentials immediately.
- Monitor suspicious login activity.

## 3. Excessive Permissions

**Excessive permissions** means giving a user or application more access than necessary.

**Risks:**
- Unauthorized data access.
- Accidental or malicious data deletion.
- Changes to important cloud settings.

**Prevention:**
- Follow the **Principle of Least Privilege**.
- Use Role-Based Access Control (RBAC).
- Review permissions regularly.
- Remove unnecessary access.
- Monitor permission changes.

## 4. Data Exposure

**Data exposure** occurs when sensitive information becomes accessible to unauthorized people.

**Examples:**
- Publicly accessible customer records.
- Unprotected databases.
- Exposed passwords or API keys.
- Sensitive data without adequate encryption.

**Prevention:**
- Restrict access to sensitive data.
- Encrypt data at rest and in transit.
- Avoid storing secrets in public repositories.
- Monitor access logs.
- Investigate suspected exposure promptly.

**Important:** Data exposure does not automatically mean attackers have accessed or stolen the data.

## 5. Insider Threats

An **insider threat** is a security risk involving someone with authorized access who misuses that access or unintentionally creates a risk.

**Types:**
- **Malicious insider:** Intentionally steals data or damages systems.
- **Negligent insider:** Accidentally exposes data or ignores security procedures.
- **Compromised insider account:** An attacker uses a legitimate user's stolen credentials.

**Prevention:**
- Apply least privilege.
- Monitor user activity.
- Review access regularly.
- Separate sensitive responsibilities.
- Provide security awareness training.
- Remove access promptly when employees leave.

**Important:** Unusual activity should be investigated; it is not proof that an employee is malicious.

---

## Key Takeaway

Cloud threats can arise from incorrect settings, stolen credentials, excessive permissions, exposed data, or insider activity. Strong access controls, secure configurations, encryption, monitoring, and regular reviews help reduce these risks.
