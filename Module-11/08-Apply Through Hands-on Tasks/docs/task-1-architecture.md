# Task 1 – Review Application Architecture

## 1. Project Overview

OWASP Juice Shop is an intentionally vulnerable web application used for application security training and testing.

## 2. Application Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Frontend | Angular 22 | User interface |
| Backend | Node.js, Express 4 | Server-side logic |
| Language | TypeScript | Application development |
| API | REST API | Frontend-backend communication |
| Database | SQLite | Data storage |
| ORM | Sequelize | Database interaction |
| Real-time | Socket.IO | Real-time communication |

## 3. Main Application Components

### Frontend
Location: `app/juice-shop/frontend/`

Angular provides the user interface and communicates with the backend.

### Backend
Files:
- `app/juice-shop/app.ts`
- `app/juice-shop/server.ts`

Node.js and Express handle application logic, middleware and requests.

### API Routes
Location: `app/juice-shop/routes/`

Examples:
- `login.ts`
- `payment.ts`
- `address.ts`
- `basketItems.ts`
- `resetPassword.ts`

### Database
Location: `app/juice-shop/models/`

Sequelize ORM connects the application to SQLite.

Default database: `data/juiceshop.sqlite`

### Real-time Communication

File: `app/juice-shop/lib/startup/registerWebsocketEvents.ts`

The application uses Socket.IO.

## 4. Application Architecture

```mermaid
flowchart TD
    A[Browser / User] --> B[Angular Frontend]
    B -->|HTTP Requests| C[Express Backend]
    C --> D[REST API Routes]
    D --> E[Application Logic]
    E --> F[Sequelize ORM]
    F --> G[SQLite Database]
    C <-->|Socket.IO| A
## 9. API Documentation Review

The application source includes a Swagger/OpenAPI specification:

File: `app/juice-shop/swagger.yml`

Observed details:

- OpenAPI version: 3.0.0
- API title: NextGen B2B API
- API version: 2.0.0
- Documented endpoint: `/orders`
- HTTP method: POST
- Authentication scheme: Bearer JWT

This specification describes the B2B order API and does not
represent every API route in the application.

## 10. Application Route Overview

The `routes/` directory contains route modules for different
application functionalities.

Examples include:

- login.ts – Login functionality
- resetPassword.ts – Password recovery
- basket.ts – Shopping basket
- payment.ts – Payment operations
- address.ts – Address management
- fileUpload.ts – File uploads
- userProfile.ts – User profile operations
- search.ts – Search functionality
- order.ts – Order operations
- passkey.ts – Passkey authentication
- 2fa.ts – Two-factor authentication

These routes represent potential areas for security investigation.

## 11. Existing Threat Model Reference

The source repository contains `app/juice-shop/threat-model.json`.

The existing model represents:

- B2C and B2B customers
- Admin and Accounting users
- Angular frontend
- Application server
- B2B API
- SQLite database
- MarsDB NoSQL database
- Local file system
- Data flows and trust boundaries

Our inspection found no explicit threat records or mitigation
descriptions in the examined JSON structure.

A separate preliminary STRIDE analysis is documented in
`task-1-threat-model.md`.
