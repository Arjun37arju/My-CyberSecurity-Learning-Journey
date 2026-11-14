# Task 1 – Application Threat Model

## 1. Introduction

Threat modeling is the process of identifying application assets,
potential attackers, entry points, trust boundaries and security threats.

This assessment uses the STRIDE threat-modeling framework.

The application under review is OWASP Juice Shop.

## 2. Application Assets

Important assets identified in the application include:

- User accounts and authentication information
- Customer addresses
- Shopping basket information
- Product and order information
- Payment-related information
- Uploaded files
- Application configuration
- Database records

## 3. Application Actors

The existing Juice Shop threat model identifies:

- B2C Customer (Browser)
- B2B Customer (Browser)
- Admin (Browser)
- Accounting (Browser)
- Google (External Actor)

## 4. Application Components

- Angular Frontend
- Node.js and Express Application Server
- B2B API
- SQLite Database
- Local File System

The existing threat model also represents a MarsDB NoSQL database.
Its active usage in the current application instance has not been
established by this architecture review.

## 5. Application Entry Points

Potential security investigation areas include:

- Login and registration
- Password reset
- User profile
- Product search
- Shopping basket
- Payment operations
- Address management
- File uploads
- Order operations
- REST API endpoints
- Real-time communication

## 6. Trust Boundaries

### Browser to Backend

Requests from the browser enter the backend application.
Input validation and authentication are important here.

### Backend to Database

The application server communicates with the database.
Database access and authorization must be controlled.

### Application to Local File System

The application interacts with files and uploaded content.
File handling and access permissions must be reviewed.

### External Services to Application

Communication with external services introduces additional
trust and data-validation requirements.

## 7. STRIDE Threat Analysis

| STRIDE Category | Potential Threat | Security Concern |
|---|---|---|
| Spoofing | Account impersonation | Unauthorized account access |
| Tampering | Modification of order or basket data | Unauthorized data changes |
| Repudiation | Insufficient activity records | Actions may be difficult to trace |
| Information Disclosure | Exposure of user or application data | Privacy and confidentiality risks |
| Denial of Service | Excessive requests or resource usage | Application availability |
| Elevation of Privilege | Access-control weaknesses | Unauthorized administrative access |

These are potential threats requiring further investigation.
They are not confirmed vulnerabilities.

## 8. Existing Threat Model Review

The source repository includes a threat-model.json file.

The file contains a high-level data-flow diagram using the STRIDE
threat-modeling approach.

The diagram represents application actors, processes, data stores,
data flows and trust boundaries.

During inspection, no explicit threat records or mitigation
descriptions were found in the examined JSON structure.

Therefore, this project includes an additional preliminary
STRIDE analysis based on the identified application architecture.

## 9. Security Controls to Investigate

The source code includes security-related mechanisms such as:

- Authentication
- Access-control checks
- Helmet
- CORS
- Rate limiting
- File-upload validation

Their configuration and effectiveness must be verified during
the later security assessment.

## 10. Conclusion

The threat-model review identified important application assets,
actors, entry points, trust boundaries and potential security threats.

The STRIDE framework provides a foundation for investigating
application security weaknesses in the next assessment phase.
