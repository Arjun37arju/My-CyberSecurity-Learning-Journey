# Understand Authentication Mechanisms

## 📑 Table of Contents
- [1. Password-Based Authentication](#1-password-based-authentication)
- [2. Multi-Factor Authentication (MFA)](#2-multi-factor-authentication-mfa)
- [3. Single Sign-On (SSO) Concepts](#3-single-sign-on-sso-concepts)
- [4. Identity Federation Awareness](#4-identity-federation-awareness)
- [5. Modern Authentication Practices](#5-modern-authentication-practices)
- [Quick Comparison](#quick-comparison)
- [Key Takeaways](#key-takeaways)

---

## 1. Password-Based Authentication

Password-based authentication is the most common authentication method. Users verify their identity by providing a username and password.

### How It Works
1. User enters a username and password.
2. The system validates the credentials against stored records.
3. Access is granted if the credentials match.

### Advantages
- Easy to implement
- Widely supported
- Familiar to users

### Disadvantages
- Vulnerable to brute-force attacks
- Password reuse increases risk
- Weak passwords can be easily compromised

### Best Practices
- Use strong passwords (12+ characters)
- Avoid password reuse
- Enable password complexity requirements
- Store passwords as salted hashes

---

## 2. Multi-Factor Authentication (MFA)

Multi-Factor Authentication (MFA) requires users to provide two or more verification factors before gaining access.

### Authentication Factors

#### Something You Know
- Password
- PIN

#### Something You Have
- Mobile phone
- Security key
- Smart card

#### Something You Are
- Fingerprint
- Face recognition
- Iris scan

### Example
1. User enters a password.
2. A verification code is sent to their phone.
3. User enters the code.
4. Access is granted.

### Benefits
- Increases account security
- Reduces risk from stolen passwords
- Helps prevent unauthorized access

---

## 3. Single Sign-On (SSO) Concepts

Single Sign-On (SSO) allows users to authenticate once and access multiple applications without logging in again.

### Example
A user signs in once and gains access to:
- Outlook
- Teams
- OneDrive
- SharePoint

### Benefits
- Improved user experience
- Fewer passwords to remember
- Centralized authentication management

### Challenges
- A compromised SSO account can impact multiple services
- Requires proper identity management

---

## 4. Identity Federation Awareness

Identity Federation enables organizations to share identity information and trust authentication performed by another organization.

### Key Components

#### Identity Provider (IdP)
Authenticates users and provides identity information.

#### Service Provider (SP)
Offers services and relies on the Identity Provider for authentication.

#### Trust Relationship
A mutual agreement allowing authentication information to be shared securely.

### Common Federation Protocols
- SAML (Security Assertion Markup Language)
- OAuth 2.0
- OpenID Connect (OIDC)

### Benefits
- Simplified user access
- Reduced account management overhead
- Improved collaboration across organizations

### Example
A student uses their university credentials to access library systems and external educational platforms without creating separate accounts.

---

## 5. Modern Authentication Practices

Modern authentication enhances security by reducing dependence on traditional passwords.

### Passwordless Authentication
Authentication without passwords using:
- Biometrics
- Security keys
- Authenticator applications
- Passkeys

### Risk-Based Authentication
The system evaluates:
- Device information
- User location
- Login behavior

Additional verification is requested when suspicious activity is detected.

### Adaptive Authentication
Authentication requirements change dynamically based on the level of risk.

### Zero Trust Security Model
Principles:
- Never trust, always 
