# Apply Through Hands-on Tasks

## Contents

* [Introduction](#introduction)
* [Project Goal](#project-goal)
* [1. Analyze Authentication Logs](#1-analyze-authentication-logs)
* [2. Review Access Control Scenarios](#2-review-access-control-scenarios)
* [3. Investigate Suspicious Login Activities](#3-investigate-suspicious-login-activities)
* [4. Assess Identity Risks](#4-assess-identity-risks)
* [5. Create IAM Security Reports](#5-create-iam-security-reports)
* [Conclusion](#conclusion)
* [References](#references)

---

## Introduction

In this hands-on task, you will perform practical Identity and Access Management (IAM) security activities using Windows security logs, Active Directory and Splunk.

The goal is to understand how authentication events are monitored, how user permissions are managed, and how suspicious identity-related activities are investigated.

The main objective is to **analyze authentication, review access permissions, investigate suspicious activities, identify identity risks, and document security findings through practical tasks.**

---

## Project Goal

You will perform basic IAM security activities to understand how user identities are authenticated, authorized, monitored, and protected.

You will practice:

* Analyzing authentication logs.
* Reviewing access control scenarios.
* Investigating suspicious login activities.
* Assessing identity-related security risks.
* Creating IAM security reports.

### Technologies and Tools

* Windows Server
* Active Directory (AD)
* Windows Event Viewer
* Splunk Enterprise
* Group Policy Management
* Windows Security Logs
* AI tools for security analysis, when useful

Use an authorized Windows environment or cybersecurity training lab such as TryHackMe.

---

# 1. Analyze Authentication Logs

Authentication logs help security analysts understand user login activities and identify possible authentication-related security issues.

For this task, use Windows Security Logs and Splunk to investigate authentication events.

### Step 1: Understand Authentication Events

Review important Windows Security Event IDs:

| Event ID | Description |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Account logged off |
| 4648 | Logon attempted using explicit credentials |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM authentication attempt |

### Step 2: Analyze Kerberos Authentication

Investigate the Kerberos authentication process using the following events:

* Event ID 4768 – A user requests a Ticket-Granting Ticket (TGT).
* Event ID 4769 – A user requests a service ticket.
* Event ID 4624 – A successful logon is recorded.

Understand how these events help analysts monitor authentication activities in an Active Directory environment.

### Practical Evidence

**Kerberos Authentication Sequence**

![Kerberos Authentication Sequence](images/iam-hands-on/kerberos-authentication.png)

The screenshot demonstrates:

1. TGT requested (4768).
2. Service ticket requested (4769).
3. Successful logon (4624).

### Step 3: Investigate Failed Logons

Use Event ID 4625 to identify failed authentication attempts.

Look for:

* Repeated failed login attempts.
* Account names involved.
* Source IP addresses.
* Login timestamps.
* Authentication failure codes.

### Practical Evidence

**Failed Login Attempts – Event ID 4625**

![Failed Login Analysis](images/iam-hands-on/failed-login-analysis.png)

### Step 4: Analyze Authentication Activity Using Splunk

Use Splunk to search and organize authentication events.

Example searches:

**Kerberos service ticket requests**

```spl
index=win EventCode=4769
| stats count by Service_Name
| sort -count
```

**TGT requests**

```spl
index=* EventCode=4768
| table _time, Account_Name, Client_Address, Ticket_Encryption_Type
```

**Failed logon attempts**

```spl
index=win EventCode=4625
| stats count by Account_Name, Client_Address
| sort -count
```

### Record Your Observations

Document the authentication events you investigated, the accounts involved, and any unusual login patterns.

---

# 2. Review Access Control Scenarios

Access control determines what resources users can access and what actions they are allowed to perform.

For this task, review user accounts, group memberships, and permissions in Active Directory.

### Step 1: Review User Accounts

Open Active Directory Users and Computers.

Explore available user accounts and understand how they are organized.

Check:

* User account names.
* Account status.
* Account properties.
* Organizational Unit (OU) membership.

### Step 2: Review Group Memberships

Investigate the groups assigned to different users.

Understand the difference between:

* Security groups.
* Distribution groups.
* Domain Users.
* Domain Admins.
* Other administrative groups.

Check whether users have appropriate group memberships according to their job responsibilities.

### Step 3: Review User Permissions

Examine the permissions assigned to users and groups.

Look for:

* Excessive permissions.
* Unnecessary administrator access.
* Unauthorized group memberships.
* Permissions that exceed job requirements.

### Step 4: Analyze Access Control Scenarios

Consider the following examples:

**Scenario 1: Excessive Privileges**

A normal employee account is added to the Domain Admins group.

This could provide unnecessary administrative access.

**Scenario 2: Unauthorized Access**

A user receives permission to access a sensitive shared folder without an approved business requirement.

**Scenario 3: Least Privilege**

A user receives only the permissions required to perform their job.

This is an example of the Principle of Least Privilege.

### Record Your Observations

Document the accounts and permissions reviewed, identify potential access control weaknesses, and suggest appropriate improvements.

---

# 3. Investigate Suspicious Login Activities

Suspicious login activities may indicate unauthorized access attempts, compromised credentials, or other identity-related threats.

For this task, use Windows Security Logs and Splunk to investigate unusual authentication patterns.

### Step 1: Identify Common Suspicious Activities

Examples include:

* Repeated failed login attempts.
* Login attempts from unusual IP addresses.
* Login activity outside normal working hours.
* Successful login after multiple failed attempts.
* Unexpected login activity involving administrator accounts.

### Step 2: Investigate Failed Login Attempts

Use Event ID 4625 to identify repeated authentication failures.

Examine:

* Account name.
* Source IP address.
* Timestamp.
* Logon type.
* Failure status and code.

### Step 3: Investigate Login Patterns Using Splunk

Use the following search to identify accounts with repeated failed login attempts.

```spl
index=win EventCode=4625
| stats count by Account_Name, Client_Address
| sort -count
```

To investigate successful logins:

```spl
index=win EventCode=4624
| table _time, Account_Name, Client_Address, Logon_Type
| sort -_time
```

### Step 4: Correlate Authentication Events

Compare failed and successful login events.

For example:

* Multiple failed attempts followed by a successful login may require investigation.
* Repeated failures against an administrative account may indicate password guessing.
* An unexpected source IP may require additional verification.

Do not assume suspicious activity is malicious without sufficient evidence.

### Practical Evidence

**Suspicious Authentication Activity – Splunk**

![Suspicious Login Investigation](images/iam-hands-on/suspicious-login-investigation.png)

### Record Your Findings

Document the suspicious activity, affected accounts, source IP addresses, possible causes, and recommended investigation steps.

---

# 4. Assess Identity Risks

Identity risk assessment helps identify weaknesses in user accounts, permissions, authentication methods, and security configurations.

### Step 1: Review Privileged Accounts

Identify accounts with administrative privileges.

Check:

* Domain Admin accounts.
* Local Administrator accounts.
* Unnecessary privileged access.
* Accounts with excessive permissions.

### Step 2: Review Authentication Security

Examine the authentication security controls.

Look for:

* Multi-Factor Authentication (MFA) availability and configuration.
* Weak authentication practices.
* Repeated authentication failures.
* Insecure or outdated authentication methods.

### Step 3: Review Account Management

Investigate account-related security events.

Important Windows Event IDs include:

| Event ID | Description |
|---|---|
| 4720 | User account created |
| 4722 | User account enabled |
| 4725 | User account disabled |
| 4726 | User account deleted |
| 4728 | Member added to a global security group |
| 4732 | Member added to a local security group |
| 4756 | Member added to a universal security group |

Review whether account creation and permission changes are authorized.

### Practical Evidence

**Account Creation Investigation – Event ID 4720**

![Account Creation Event](images/iam-hands-on/account-creation-4720.png)

The example shows an account creation event involving `nathan.brooks`, with `adm-luke.sullivan` recorded as the subject account.

Verify the activity against the approved account-creation process.

### Step 4: Review Audit Policy Configuration

Open Group Policy Management Editor.

Navigate to:

```text
Computer Configuration
    |
Windows Settings
    |
Security Settings
    |
Advanced Audit Policy Configuration
    |
Audit Policies
```

Review the available categories:

* Account Logon.
* Account Management.
* Detailed Tracking.
* DS Access.
* Logon/Logoff.
* Object Access.
* Policy Change.
* Privilege Use.
* System.

Check whether the required auditing policies are configured.

### Practical Evidence

**Advanced Audit Policy Configuration**

![Advanced Audit Policy](images/iam-hands-on/advanced-audit-policy.png)

### Step 5: Identify Identity Risks

Examples of identity-related risks:

```text
1. Excessive administrative privileges.
2. Missing or insufficient MFA protection.
3. Unauthorized account creation.
4. Weak authentication controls.
5. Insufficient security auditing.
6. Unnecessary user group memberships.
```

These are potential risks to investigate, not automatically confirmed findings.

### Record Your Observations

Document the identity weaknesses identified, their potential impact, and the security improvements required.

---

# 5. Create IAM Security Reports

Finally, prepare an IAM security report based on the practical activities performed.

The report should explain the environment, investigations, evidence, identified risks, and recommended improvements.

### Step 1: Environment Overview

Mention:

* Operating system and environment.
* Active Directory domain.
* Security monitoring tools.
* Log analysis platform.
* Authentication mechanisms investigated.

### Step 2: Security Activities

Describe the activities performed:

* Authentication log analysis.
* Access control review.
* Suspicious login investigation.
* Identity risk assessment.
* Audit policy review.

### Step 3: Document Security Findings

For each finding, include:

* Finding description.
* Affected account or resource.
* Supporting evidence.
* Potential security impact.
* Risk level.

Example:

| Finding | Risk Level |
|---|---|
| Unauthorized account creation | Medium–High |
| Excessive administrative permissions | Medium–High |
| Insufficient audit configuration | Medium |
| Repeated failed login attempts | Depends on investigation |

Risk levels should be assigned based on the actual evidence and business impact.

### Step 4: Provide Recommendations

Suggest appropriate security improvements.

```text
- Apply the Principle of Least Privilege.
- Review privileged group memberships regularly.
- Enable MFA for privileged accounts.
- Investigate repeated failed login attempts.
- Monitor account creation and permission changes.
- Configure appropriate Windows audit policies.
- Review authentication logs regularly.
```

### Step 5: Prepare the Final Report

Organize your findings into a professional report containing:

1. Introduction.
2. Environment overview.
3. Security activities performed.
4. Evidence and observations.
5. Risk assessment.
6. Recommendations.
7. Conclusion.

Keep the report clear, concise, and based on the evidence collected.

---

## Conclusion

By completing this hands-on task, you practiced five important IAM security activities:

```text
1. Analyze authentication logs.
2. Review access control scenarios.
3. Investigate suspicious login activities.
4. Assess identity risks.
5. Create IAM security reports.
```

These activities help develop practical knowledge of identity security, authentication monitoring, access management, and security investigation.

**The goal is to understand how identities are authenticated, how access is controlled, how suspicious activities are detected, and how identity-related security risks are reported.**

---
* [View IAM Authentication Log Analysis Report](resources/hands-on-report/IAM_Authentication_Log_Analysis_Report.pdf)
## IAM Authentication Log Analysis Report

📄 [Open IAM Authentication Log Analysis Report](../resources/hands-on-report/IAM_Authentication_Log_Analysis_Report_Updated.pdf)
