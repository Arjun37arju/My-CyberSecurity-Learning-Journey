# Understand Security Logging & Monitoring

## Contents

1. [Application Logs](#1-application-logs)
2. [Access Logs](#2-access-logs)
3. [Error Logs](#3-error-logs)
4. [Audit Trails](#4-audit-trails)
5. [Security Visibility](#5-security-visibility)

---

## 1. Application Logs

**Application logs** are records created by an application to show what is happening inside it.

### Examples

```text
User logged in
User created an account
Payment completed
File uploaded
Application started
```

### Example Log

```text
2026-10-07 10:30:15 - User arjun logged in
2026-10-07 10:31:02 - File uploaded
2026-10-07 10:32:10 - User logged out
```

### Why Are Application Logs Important?

They can help identify:

* Normal application activity
* Application errors
* Suspicious behavior
* Possible security incidents
* Problems that need investigation

### Simple Flow

```text
User Action
     ↓
Application
     ↓
Log Created
     ↓
Security / Developer Reviews Log
```

> **Application logs = Records of activities and events happening inside an application.**

---

## 2. Access Logs

**Access logs** are records of requests made to a server or web application.

They can contain information such as:

* IP address
* Time of the request
* Requested resource
* HTTP method
* Response status code

### Example

```text
192.168.1.10 - GET /login - 200
192.168.1.10 - GET /profile - 200
192.168.1.15 - GET /admin - 403
```

Here:

* `GET` → HTTP method
* `/login` → Requested resource
* `200` → Request was successful
* `403` → Access was forbidden

### Why Are Access Logs Important?

Security teams can use them to identify suspicious activity.

```text
Many Requests
      ↓
Same IP Address
      ↓
Different Usernames
      ↓
Possible Brute-Force Activity
```

> **Access logs = Records of requests made to a server or application.**

---

## 3. Error Logs

**Error logs** are records of errors or problems that occur in an application, server, or system.

### Example

```text
2026-10-07 10:35:10 - Database connection failed
2026-10-07 10:36:02 - File not found
2026-10-07 10:37:15 - Authentication service error
```

### Why Are Error Logs Important?

They help developers and security teams:

* Find application problems
* Troubleshoot failures
* Identify unusual behavior
* Investigate possible security incidents

For example, repeated authentication errors could indicate repeated login attempts.

```text
Many Login Errors
       ↓
Repeated Attempts
       ↓
Investigate
       ↓
Possible Suspicious Activity
```

### Security Consideration

Error messages should not expose sensitive information such as:

```text
Database Passwords
API Keys
Session Tokens
Internal System Details
```

> **Error logs = Records of errors and problems that occur in a system or application.**

---

## 4. Audit Trails

An **audit trail** is a record of **who performed an action, what they did, and when they did it**.

It is mainly used for **security, accountability, and investigation**.

### Example

```text
2026-10-07 10:45:20
User: admin
Action: Delete user
Target: user123
Result: Successful
```

### What Can an Audit Trail Record?

* **Who** performed the action
* **What** action was performed
* **When** it happened
* **Which resource** was affected
* Whether the action was **successful or failed**

### Why Is It Important?

If something suspicious happens, security teams can use the audit trail to understand what happened.

```text
Suspicious Activity
       ↓
Check Audit Trail
       ↓
Who did it?
       ↓
What happened?
       ↓
When did it happen?
```

> **Audit trail = A record of important user and system actions used for tracking and investigation.**

---

## 5. Security Visibility

**Security visibility** means having enough information about systems, applications, and networks to **detect and investigate security problems**.

Logs are an important part of security visibility.

### Example

```text
Attacker
   ↓
Server
   ↓
Logs Record Activity
   ↓
Security Team Sees Suspicious Activity
   ↓
Investigation
```

Without proper logging and monitoring, security teams may not know that an attack is happening.

### Sources of Security Visibility

* Application logs
* Access logs
* Error logs
* Audit trails
* Network monitoring
* System monitoring
* Security alerts

### Example

```text
Failed Login
Failed Login
Failed Login
Failed Login
       ↓
Monitoring Detects Unusual Activity
       ↓
Security Team Investigates
```

> **Security visibility = The ability to see, understand, and monitor activities in a system so security problems can be detected and investigated.**

---

## Conclusion

Security logging and monitoring help organizations understand what is happening in their systems and detect suspicious activity.

```text
Application Logs
       ↓
Access Logs
       ↓
Error Logs
       ↓
Audit Trails
       ↓
Security Visibility
       ↓
Detect & Investigate Security Problems
```
