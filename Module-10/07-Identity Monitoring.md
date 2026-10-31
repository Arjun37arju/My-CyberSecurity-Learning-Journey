# Identity Monitoring

Identity Monitoring is the process of tracking, analyzing, and reviewing identity-related activities to detect unauthorized access, compromised accounts, and suspicious behavior within an organization.

---

## 📑 Contents

- [Login Events](#login-events)
- [Authentication Logs](#authentication-logs)
- [Access Monitoring](#access-monitoring)
- [Suspicious Activities](#suspicious-activities)
- [SOC Investigation Workflows](#soc-investigation-workflows)
- [Summary](#summary)

---

# Login Events

## What Are Login Events?

Login events are records generated whenever a user attempts to access a system, application, or network resource.

These events help security teams track authentication activities and user access patterns.

### Types of Login Events

#### Successful Login

Occurs when valid credentials are provided and access is granted.

#### Failed Login

Occurs when authentication fails because of incorrect credentials or other issues.

#### Logoff Event

Recorded when a user signs out of a system.

#### Remote Login

Occurs when users access resources from external networks or remote devices.

### Information Typically Recorded

- Username
- Date and time
- Source IP address
- Device name
- Login status
- Authentication method

### Importance of Login Events

- Detect unauthorized access attempts
- Identify brute-force attacks
- Monitor account activity
- Support incident investigations

---

# Authentication Logs

## What Are Authentication Logs?

Authentication logs are records that capture how users verify their identity when accessing systems and services.

They provide detailed information about authentication attempts and outcomes.

### Information Found in Authentication Logs

- User identity
- Authentication success or failure
- Authentication method used
- Location information
- Timestamp
- Device information

### Common Authentication Methods Logged

- Password authentication
- Multi-Factor Authentication (MFA)
- Smart card authentication
- Biometric authentication
- Single Sign-On (SSO)

### Benefits of Authentication Logs

- Verify user activities
- Detect suspicious authentication attempts
- Investigate potential security incidents
- Identify compromised accounts

---

# Access Monitoring

## What Is Access Monitoring?

Access monitoring is the process of tracking how users interact with systems, applications, and data after authentication.

The objective is to ensure that users only access resources they are authorized to use.

### Activities That Can Be Monitored

- File access
- Database access
- Application usage
- Administrative actions
- Permission changes
- Group membership changes

### Benefits

#### Detect Unauthorized Access

Identifies attempts to access restricted resources.

#### Enforce Access Controls

Helps ensure security policies are being followed.

#### Improve Visibility

Provides insight into how resources are accessed and used.

### Example

A user from the finance department accessing engineering documentation may indicate unusual behavior that requires review.

---

# Suspicious Activities

## What Are Suspicious Activities?

Suspicious activities are actions that differ from expected user behavior and may indicate malicious activity or account compromise.

### Common Indicators

#### Multiple Failed Login Attempts

May indicate a brute-force attack or password-spraying attempt.

#### Login From Unusual Locations

Authentication attempts from unexpected countries or regions.

#### Impossible Travel

A user appears to log in from distant geographic locations within an unrealistic timeframe.

#### Excessive Privilege Requests

Repeated attempts to gain elevated permissions.

#### Unusual Resource Access

Accessing systems or data unrelated to a user’s normal responsibilities.

#### Activity Outside Normal Working Hours

Access patterns that significantly differ from a user's typical behavior.

### Why Detection Matters

- Enables faster threat response
- Reduces potential damage
- Protects sensitive information
- Prevents unauthorized access

---

# SOC Investigation Workflows

## What Is a SOC?

A Security Operations Center (SOC) is a team responsible for monitoring, detecting, investigating, and responding to security incidents.

## Typical SOC Investigation Workflow

### 1. Alert Generation

Security tools generate alerts based on suspicious activities or policy violations.

Examples:

- Failed whether the alert represents a genuine threat or a false positive.

### 3. Evidence Collection

Relevant information is gathered from multiple sources, including:

- Login logs
- Authentication logs
- Access logs
- Endpoint data
- Network data

### 4. Investigation

Analysts analyze the collected evidence to determine:

- What happened
- How it happened
- Which systems were affected
- Whether unauthorized access occurred

### 5. Containment

Actions are taken to limit the impact of the incident.

Examples:

- Disabling compromised accounts
- Blocking malicious IP addresses
- Restricting access permissions

### 6. Eradication and Recovery

The root cause is removed and systems are restored to secure operation.

### 7. Documentation and Lessons Learned

The incident is documented to improve future detection and response processes.

---

---

### 📚 Additional Resources

For deeper understanding and advanced concepts, refer to the following resource:

- [Active Directory – Security Architecture, Protocols & Advanced Concepts](../resources/Active%20Directory%20%E2%80%93%20Security%20Architecture%2C%20Protocols%20%26%20Advanced%20Concepts.md)
