# Active Directory – Security Architecture, Protocols & Advanced Concepts

## Navigation

- [1. Important Active Directory Protocols](#1-important-active-directory-protocols)
- [2. Important Active Directory Components](#2-important-active-directory-components)
- [3. Active Directory Database – NTDS.dit](#3-active-directory-database--ntdsdit)
- [4. SYSVOL and NETLOGON](#4-sysvol-and-netlogon)
- [5. Global Catalog](#5-global-catalog)
- [6. Active Directory Replication](#6-active-directory-replication)
- [7. Authentication Mechanisms](#7-authentication-mechanisms)
- [8. Windows Security Event IDs](#8-windows-security-event-ids)
- [9. Log Monitoring and Tampering Indicators](#9-log-monitoring-and-tampering-indicators)
- [10. Advanced Privileged Access Security](#10-advanced-privileged-access-security)
- [11. Active Directory Security Best Practices](#11-active-directory-security-best-practices)
- [12. Quick Revision](#12-quick-revision)

---

## 1. Important Active Directory Protocols

Protocols allow computers, servers, and applications to communicate across a network.

### 1.1 LDAP – Lightweight Directory Access Protocol

LDAP is used to communicate with directory services such as Active Directory.

**Main purposes:**
- Search for users and groups.
- Retrieve account information.
- Access directory objects.
- Make permitted directory changes.

**Common ports:**
- 389 – LDAP
- 636 – LDAP over TLS (LDAPS)

**Security:**
- Use encrypted LDAP connections where appropriate.
- Enable LDAP signing according to security requirements.
- Restrict access to sensitive directory information.

### 1.2 Kerberos

Kerberos is an authentication protocol commonly used by Active Directory to verify user and computer identities.

**How it works:**
1. A user provides their authentication credentials.
2. The Key Distribution Center (KDC) helps authenticate the user.
3. The user receives a Ticket Granting Ticket (TGT).
4. The TGT can be used to request service tickets.
5. The service ticket allows access to an authorized network service.

**Important terms:**
- TGT – Ticket Granting Ticket.
- TGS – Ticket Granting Service.
- KDC – Key Distribution Center.

**Common port:**
- 88 – Kerberos.

**Security:** Protect privileged accounts, monitor unusual ticket activity, and maintain accurate time synchronization.

### 1.3 DNS – Domain Name System

DNS translates domain names and computer names into IP addresses.

Active Directory depends on DNS to locate Domain Controllers and other domain services.

**Example:**

A domain computer uses DNS to find a Domain Controller before performing certain domain operations.

**Common port:**
- 53 – DNS (UDP and TCP).

**Important DNS records:**
- A – Maps a hostname to an IPv4 address.
- AAAA – Maps a hostname to an IPv6 address.
- SRV – Helps locate services such as Domain Controllers.
- CNAME – Provides an alias for another hostname.

### 1.4 SMB – Server Message Block

SMB is a network protocol used to share files, folders, printers, and other resources.

**Example:**
- Computer A shares a folder.
- Computer B accesses the shared folder.
- SMB handles the network communication.

**Common port:**
- 445 – SMB over TCP.

**Security:**
- Disable SMBv1.
- Use SMB signing where required.
- Enable SMB encryption where appropriate.
- Restrict access to shared folders.

### 1.5 RPC – Remote Procedure Call

RPC allows a computer or application to request an operation from another computer over a network.

Active Directory uses RPC for several administrative and replication-related operations.

**Common ports:**
- 135 – RPC Endpoint Mapper.
- Dynamic RPC ports – Used for additional RPC communication.

**Security:** Restrict RPC access to trusted systems and required network paths.

### 1.6 NTLM – New Technology LAN Manager

NTLM is a Microsoft authentication protocol that can be used in Windows environments.

It is an older authentication mechanism that may still be present for compatibility.

**Security concerns:**
- NTLM can be exposed to credential-relay attacks in poorly configured environments.
- NTLM authentication should be reduced where possible.
- Monitor NTLM usage and investigate unexpected authentication.

### 1.7 NTP – Network Time Protocol

NTP synchronizes time between computers and network devices.

Accurate time is important for Kerberos authentication and security log correlation.

**Common port:**
- 123 – NTP (UDP).

### Important Protocol Port Summary

| Protocol | Port | Purpose |
|---|---:|---|
| DNS | 53 | Name resolution |
| Kerberos | 88 | Authentication |
| LDAP | 389 | Directory communication |
| LDAPS | 636 | Encrypted LDAP communication |
| SMB | 445 | File sharing |
| RPC Endpoint Mapper | 135 | RPC service discovery |
| Global Catalog | 3268 | Global Catalog queries |
| Secure Global Catalog | 3269 | Encrypted Global Catalog queries |
| NTP | 123 | Time synchronization |
| Kerberos password change | 464 | Password change operations |

---

## 2. Important Active Directory Components

Active Directory contains several important components that support authentication, directory management, and domain operations.

### 2.1 Domain Controller (DC)

A Domain Controller is a Windows Server that runs Active Directory Domain Services (AD DS).

**Responsibilities:**
- Authenticate users and computers.
- Store and manage directory information.
- Apply domain security policies.
- Handle directory replication.

### 2.2 NTDS.dit

NTDS.dit is the main Active Directory database file.

It stores:
- User account information.
- Computer account information.
- Group information.
- Directory objects.
- Sensitive credential-related data, including password hashes.

**Security:** Protecting this database is critical because unauthorized access may expose sensitive domain information.

### 2.3 SYSVOL

SYSVOL (System Volume) is a replicated shared folder on Domain Controllers.

It contains:
- Group Policy files.
- Logon and logoff scripts.
- Other domain-wide files.

**Security:** Unauthorized changes to SYSVOL files or scripts can affect domain computers and users.

### 2.4 NETLOGON

NETLOGON is a shared folder on Domain Controllers commonly used for domain logon-related files and scripts.

**Purpose:**
- Provides access to logon scripts.
- Supports certain domain logon operations.
- Can contain scripts used during user logon.

**Security:** Protect scripts and restrict write permissions to authorized administrators.

---

## 3. Active Directory Database – NTDS.dit

### What is NTDS.dit?

NTDS.dit is the primary database file used by Active Directory Domain Services.

It normally resides at:

`C:\Windows\NTDS\ntds.dit`

### Why is it important?

The database contains important information about the domain, including sensitive credential-related information.

If an attacker obtains unauthorized access to this database, they may attempt to extract password hashes and other sensitive information.

### Security practices

- Restrict physical and administrative access to Domain Controllers.
- Use BitLocker or suitable storage protection.
- Protect backups containing Active Directory data.
- Apply security updates.
- Monitor access to sensitive files.
- Use least privilege.
- Secure Domain Controller recovery and backup procedures.

**Important:** NTDS.dit does not simply store every user's password in readable plaintext. Password-related information is stored in protected credential formats.

---

## 4. SYSVOL and NETLOGON

Both are important shared folders on Domain Controllers, but they serve different purposes.

### SYSVOL

- Stores Group Policy files.
- Stores logon and logoff scripts.
- Replicates domain-wide policy-related files between Domain Controllers.

### NETLOGON

- Provides access to domain logon-related files.
- Commonly contains logon scripts.
- Supports domain logon processes.

### Difference

| SYSVOL | NETLOGON |
|---|---|
| Stores Group Policy files and scripts | Commonly provides logon-related files and scripts |
| Used for domain-wide policy distribution | Used for domain logon-related operations |
| Replicated between Domain Controllers | Commonly points to the domain's SYSVOL NETLOGON folder |

**Security:** Protect both shares against unauthorized file modification.

---

## 5. Global Catalog

### What is Global Catalog?

The Global Catalog (GC) is a searchable representation of selected attributes from objects across an Active Directory forest.

It helps users and applications find directory information across multiple domains.

### Main purposes

- Search for users across the forest.
- Find objects in different domains.
- Support certain logon processes.
- Provide selected attributes from other domains.

### Common ports

- 3268 – Global Catalog.
- 3269 – Global Catalog over SSL/TLS.

**Example:**

An organization has multiple domains. A user can be searched for across the forest using the Global Catalog without searching each domain separately.

---

## 6. Active Directory Replication

### What is replication?

Replication is the process of synchronizing directory information between Domain Controllers.

When directory information changes on one Domain Controller, the change is replicated to other relevant Domain Controllers.

### Example

1. An administrator creates a new user on DC1.
2. Active Directory replication distributes the change.
3. Other Domain Controllers receive the updated directory information.

### Why is replication important?

- Keeps directory information synchronized.
- Helps maintain consistent user and group information.
- Supports domain availability.
- Helps ensure changes are available across the domain.

### Security considerations

- Monitor unexpected directory changes.
- Protect Domain Controllers.
- Investigate replication failures.
- Restrict administrative permissions.
- Monitor unusual replication activity.

---

## 7. Authentication Mechanisms

Authentication verifies the identity of a user, computer, or service.

### 7.1 Password-based authentication

Users authenticate using a username and password.

**Security concerns:**
- Weak passwords.
- Password reuse.
- Phishing.
- Brute-force attempts.
- Password spraying.

### 7.2 Multi-Factor Authentication (MFA)

MFA requires two or more different types of verification.

Examples:
- Something you know – Password.
- Something you have – Security key.
- Something you are – Fingerprint.

MFA adds another layer of protection if a password is compromised.

### 7.3 Passwordless Authentication

Passwordless authentication allows users to authenticate without entering a traditional password.

Common methods include:
- Passkeys.
- Cryptographic security keys.
- Supported biometric authenticators.
- Other supported device-based authenticators.

**Benefits:**
- Reduces password-related attacks.
- Helps protect against phishing when phishing-resistant methods are used.
- Reduces dependence on traditional passwords.

---

## 8. Windows Security Event IDs

Windows Event Viewer records security-related activities.

Event IDs help administrators identify what happened on a Windows system or Domain Controller.

### 8.1 Logon and Authentication Events

| Event ID | Meaning |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Account logged off |
| 4648 | Logon attempted using explicit credentials |
| 4672 | Special privileges assigned to a new logon |
| 4740 | User account locked out |

### 8.2 Account Management Events

| Event ID | Meaning |
|---|---|
| 4720 | User account created |
| 4722 | User account enabled |
| 4723 | Attempt to change an account password |
| 4724 | Attempt to reset an account password |
| 4725 | User account disabled |
| 4726 | User account deleted |
| 4728 | Member added to a security-enabled global group |
| 4732 | Member added to a security-enabled local group |
| 4739 | Domain policy changed |
| 4756 | Member added to a security-enabled universal group |

### 8.3 Kerberos and Authentication Events

| Event ID | Meaning |
|---|---|
| 4768 | Kerberos Ticket Granting Ticket requested |
| 4769 | Kerberos service ticket requested |
| 4771 | Kerberos pre-authentication failed |
| 4776 | NTLM credential validation |

### 8.4 Directory and Security Policy Events

| Event ID | Meaning |
|---|---|
| 4719 | System audit policy changed |
| 4662 | An operation was performed on an Active Directory object (when appropriate auditing is enabled) |
| 5136 | Directory service object modified |

**Important:** Some events require specific audit policies and configuration. The events available depend on the system, audit settings, and activity being monitored.

---

## 9. Log Monitoring and Tampering Indicators

### What is security log monitoring?

Security log monitoring means reviewing system and authentication events to identify suspicious activities.

### Important log-clearing and monitoring events

| Event ID | Meaning |
|---|---|
| 1102 | Security audit log cleared |
| 104 | An event log was cleared (System log provider) |
| 4719 | System audit policy changed |
| 1100 | Event logging service shut down |
| 1104 | Security log is full |
| 4616 | System time changed |

### Why are these events important?

Attackers may attempt to hide suspicious activity by interfering with logging or changing audit settings.

These events do not automatically prove an attack, but unexpected occurrences should be investigated.

### Common warning signs

- Security logs unexpectedly cleared.
- Auditing settings changed without approval.
- Event logging service unexpectedly stopped.
- Unusual administrator activity.
- Unexpected changes to Domain Controller configuration.
- Gaps in expected security logs.

### Monitoring tools

- Windows Event Viewer.
- PowerShell.
- Windows Event Forwarding.
- SIEM platforms.

### Security practices

- Enable appropriate audit policies.
- Forward important logs to a centralized system.
- Restrict access to log management.
- Monitor log-clearing events.
- Protect log storage from unauthorized modification.
- Investigate missing or unusual events.

**Important:** Event IDs are investigation clues, not proof by themselves. Always examine the event details, account, computer, timestamp, and surrounding activity.

---

## 10. Advanced Privileged Access Security

These concepts help organizations reduce the risks associated with administrative permissions.

### 10.1 Just-in-Time (JIT) Access

JIT access provides elevated permissions only for a limited period when they are needed.

**Example:**

An administrator needs Domain-level privileges for a maintenance task. JIT access can provide the required permission temporarily and remove it after the approved period.

**Benefits:**
- Reduces permanent administrative access.
- Limits the time privileged permissions are available.
- Reduces the risk of misuse.

### 10.2 Just-Enough Administration (JEA)

JEA restricts administrative users to a specific set of permitted management operations.

It is particularly useful in supported PowerShell management environments.

**Example:**

An IT support employee may be allowed to restart a particular service but not create Domain Admin accounts.

**Benefits:**
- Limits administrative capabilities.
- Reduces unnecessary permissions.
- Supports least privilege.

### 10.3 Privileged Access Management (PAM)

PAM refers to technologies and processes used to control, protect, and monitor privileged accounts and sessions.

**Common capabilities:**
- Privileged account management.
- Approval-based access.
- Credential protection.
- Session monitoring.
- Temporary privilege assignment.

**Benefits:**
- Protects high-impact accounts.
- Improves administrative accountability.
- Reduces privileged access risks.

### Difference between JIT, JEA and PAM

| Concept | Main purpose |
|---|---|
| JIT | Provides privileges temporarily |
| JEA | Limits what administrative actions a user can perform |
| PAM | Protects and manages privileged accounts and sessions |

---

## 11. Active Directory Security Best Practices

### Account Security
- Use strong and unique passwords.
- Enable MFA where supported.
- Disable unused accounts.
- Review privileged accounts regularly.

### Domain Controller Security
- Restrict physical and remote access.
- Apply security updates.
- Protect NTDS.dit and backups.
- Use secure administrative practices.

### Network Security
- Restrict unnecessary ports and services.
- Disable outdated protocols such as SMBv1.
- Use secure LDAP configurations.
- Monitor authentication traffic.

### Monitoring and Auditing
- Enable suitable audit policies.
- Monitor login activities.
- Monitor privileged group changes.
- Investigate unexpected log-clearing events.
- Centralize security logs.

### Privileged Access
- Apply least privilege.
- Use JIT access where supported.
- Apply JEA for restricted administrative operations.
- Use PAM to protect high-impact accounts.

---

## 12. Quick Revision

| Term | Important meaning |
|---|---|
| LDAP | Communicates with directory services |
| Kerberos | Authenticates users and services |
| DNS | Resolves names and locates domain services |
| SMB | Shares files and resources over a network |
| RPC | Supports remote operations between systems |
| NTLM | Older Windows authentication mechanism |
| NTP | Synchronizes system time |
| NTDS.dit | Main Active Directory database |
| SYSVOL | Stores Group Policy files and scripts |
| NETLOGON | Provides domain logon-related files |
| Global Catalog | Supports forest-wide directory searches |
| Replication | Synchronizes directory data between Domain Controllers |
| Passwordless | Authenticates without a traditional password |
| JIT | Temporary privileged access |
| JEA | Restricted administrative operations |
| PAM | Protects and manages privileged access |

### Important Event IDs to Remember

- **4624** – Successful logon.
- **4625** – Failed logon.
- **4720** – User account created.
- **4728** – Member added to global security group.
- **4740** – Account locked out.
- **4768** – Kerberos TGT requested.
- **4769** – Kerberos service ticket requested.
- **4719** – Audit policy changed.
- **5136** – Directory object modified.
- **1102** – Security audit log cleared.

