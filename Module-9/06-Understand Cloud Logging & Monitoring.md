# Understand Cloud Logging & Monitoring

## Contents
1. [Audit Logs](#1-audit-logs)
2. [Activity Monitoring](#2-activity-monitoring)
3. [Security Visibility](#3-security-visibility)
4. [Event Tracking](#4-event-tracking)
5. [Incident Investigation](#5-incident-investigation)

---

## 1. Audit Logs

**Audit logs** are records of activities performed in a cloud environment. They help identify who performed an action, when it happened, and its recorded result.

**Examples:**
- User login attempts.
- Changes to cloud permissions.
- Creation or deletion of resources.

**Why they matter:**
- Provide evidence for investigations.
- Help identify suspicious actions.
- Support security auditing and compliance.

**Cloud services:**
- AWS CloudTrail
- Azure Activity Log
- Google Cloud Audit Logs

## 2. Activity Monitoring

**Activity monitoring** means observing cloud activities to identify unusual behavior and potential security threats.

**Examples:**
- Repeated failed login attempts.
- Unexpected large data downloads.
- Unusual administrator activity.

**How it works:**
1. Collect activity data.
2. Analyze behavior and security rules.
3. Generate alerts for suspicious activity.
4. Investigate the alerts.

**Important:** An alert indicates something that may need investigation; it does not automatically prove an attack.

## 3. Security Visibility

**Security visibility** means being able to see and understand the security status and activities across a cloud environment.

**Why it matters:**
- Helps identify threats and misconfigurations.
- Shows user and resource activity.
- Improves investigation and response.

**How to improve visibility:**
- Enable appropriate logging.
- Monitor network and user activity.
- Use security dashboards and alerts.
- Collect information from relevant cloud services.

**Examples of tools:**
- AWS Security Hub
- Microsoft Defender for Cloud
- Google Cloud Security Command Center

## 4. Event Tracking

**Event tracking** means recording and following events over time to understand the sequence and relationships between actions.

**Examples:**
- A user signs in.
- Storage permissions change.
- A large amount of data is downloaded.

**Why it matters:**
- Connects related events.
- Helps identify suspicious sequences.
- Supports incident investigations.

Audit logs are an important source of event data.

## 5. Incident Investigation

**Incident investigation** is the process of examining a security incident to understand what happened, how it happened, and what was affected.

**Main steps:**
1. **Detect:** Identify a possible security incident.
2. **Collect evidence:** Review logs, alerts, and activity records.
3. **Analyze:** Determine the cause, scope, and affected resources.
4. **Contain and recover:** Limit damage and restore services safely.
5. **Document and improve:** Record findings and strengthen security controls.

**Important:** Preserve relevant evidence and follow incident response procedures.

---

## Key Takeaway

Cloud logging and monitoring help security teams understand activities, detect suspicious behavior, investigate incidents, and improve security. Audit logs, activity monitoring, security visibility, and event tracking work together to support effective incident investigation.
