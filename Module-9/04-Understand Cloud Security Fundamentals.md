# Understand Cloud Security Fundamentals

## Contents
- [Shared Responsibility Model](#1-shared-responsibility-model)
- [Identity Management](#2-identity-management)
- [Access Control](#3-access-control)
- [Security Monitoring](#4-security-monitoring)
- [Security Best Practices](#5-security-best-practices)

---

## 1. Shared Responsibility Model

The **Shared Responsibility Model** divides cloud security responsibilities between the cloud provider and the customer.

- **Cloud provider:** Secures the physical data centers, hardware, and underlying cloud infrastructure.
- **Customer:** Secures their data, user accounts, permissions, applications, and configurations, depending on the service.

### Responsibilities by Service Model

| Service | Customer's Main Responsibilities |
|---|---|
| IaaS | Guest OS, applications, accounts, and data |
| PaaS | Application code, data, and access settings |
| SaaS | User access, data, and available security settings |

**Example:** Making a cloud database publicly accessible by mistake is a customer configuration risk.

## 2. Identity Management

**Identity Management** manages the identities of people, applications, and machines that access cloud resources.

- **Authentication:** Verifies who you are.
- **Authorization:** Determines what you are allowed to do.
- **IAM (Identity and Access Management):** Manages identities, roles, and permissions.
- **MFA:** Requires an additional verification step during login.

**Best practices:**
- Use individual accounts.
- Enable MFA.
- Remove access when users leave.
- Use temporary credentials when appropriate.
- Review inactive accounts regularly.

## 3. Access Control

**Access Control** determines who can access a resource and which actions they can perform.

- **Least Privilege:** Give only the permissions required.
- **RBAC (Role-Based Access Control):** Assign permissions based on roles.
- **ABAC (Attribute-Based Access Control):** Make access decisions using attributes such as department or resource type.
- **Separation of Duties:** Divide sensitive tasks between different people or roles.

**Example:** A report viewer can read reports but cannot delete them.

## 4. Security Monitoring

**Security Monitoring** means observing cloud systems and activities to detect suspicious behavior.

### Important Concepts

- **Logs:** Records of events, such as logins and API activity.
- **Monitoring:** Analyzes activity and looks for unusual behavior.
- **Alerts:** Notify security teams about activity that may need attention.
- **Investigation:** Helps determine what happened and whether it was a threat.

### Common Cloud Monitoring Services

- **AWS:** CloudTrail and CloudWatch
- **Microsoft Azure:** Azure Monitor
- **Google Cloud:** Cloud Audit Logs and Cloud Monitoring

**Basic workflow:**

Collect logs → Analyze activity → Generate alerts → Investigate → Respond

## 5. Security Best Practices

- **Strong passwords and MFA:** Help protect accounts from unauthorized access.
- **Least privilege:** Limit unnecessary permissions.
- **Encryption:** Protect data at rest and in transit.
- **Patching:** Apply security updates to fix known vulnerabilities.
- **Backups:** Keep backups and test data restoration.
- **Monitoring:** Review logs and investigate suspicious activity.
- **Network security:** Restrict unnecessary public access to cloud resources.
- **Configuration reviews:** Check for publicly exposed storage, overly permissive rules, and other misconfigurations.

### Quick Revision

| Concept | Main Purpose |
|---|---|
| Shared Responsibility | Divides security duties |
| Identity Management | Manages identities |
| Authentication | Verifies identity |
| Authorization | Determines allowed actions |
| Access Control | Restricts resource access |
| Security Monitoring | Detects suspicious activity |
| Encryption | Protects data confidentiality |
| Patching | Fixes known vulnerabilities |
| Backups | Supports recovery |

