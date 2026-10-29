# Understand Backend Fundamentals

## 📑 Content

1. [APIs](#1-apis)
2. [Databases](#2-databases)
3. [Authentication Concepts](#3-authentication-concepts)
4. [Session Management](#4-session-management)
5. [Web Application Workflows](#5-web-application-workflows)


---

## 1. APIs

### What is an API?

API stands for **Application Programming Interface**.

An API allows different software applications to communicate with each other.

For example:

```text
Website / Mobile App
        ↓
       API
        ↓
     Server
        ↓
     Database
        ↓
     Response
        ↓
Website / Mobile App
```

### API Endpoint

An **API endpoint** is a specific URL or path used to access a resource.

Example:

```text
/api/users
```

### Common HTTP Methods Used with APIs

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Read data             |
| POST   | Create or send data   |
| PUT    | Replace/update data   |
| PATCH  | Partially update data |
| DELETE | Delete data           |

Example:

```http
GET /api/users
```

This can be used to request user data.

---

## 2. Databases

### What is a Database?

A **database** is a system used to store, organize, and manage data.

Web applications commonly store:

* User accounts
* Products
* Orders
* Messages
* Account information

Basic flow:

```text
User
 ↓
Website / App
 ↓
Backend
 ↓
Database
```

### Tables

A database can contain tables.

Example:

| id | name  | email                                         |
| -: | ----- | --------------------------------------------- |
|  1 | Arjun | [arjun@example.com](mailto:arjun@example.com) |
|  2 | Rahul | [rahul@example.com](mailto:rahul@example.com) |
|  3 | Vivek | [vivek@example.com](mailto:vivek@example.com) |

### Important Terms

* **Table** → Collection of related data
* **Column** → Type/category of data
* **Row** → One complete record
* **ID** → Identifies a particular record

### CRUD

CRUD represents four basic database operations:

| Operation | Meaning              |
| --------- | -------------------- |
| Create    | Add new data         |
| Read      | Get data             |
| Update    | Change existing data |
| Delete    | Remove data          |

CRUD can be related to HTTP methods:

```text
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

> Passwords should not normally be stored as plain text. They should be stored using secure password hashing.

---

## 3. Authentication Concepts

### What is Authentication?

**Authentication** is the process of verifying who a user is.

Simple question:

> **Who are you?**

For example, a user enters:

```text
Username: Arjun
Password: ********
```

The browser commonly sends a login request:

```http
POST /login
```

The backend receives the login information and checks the user's account information in the database.

### Authentication Flow

```text
User enters username + password
          ↓
Browser sends request
          ↓
Backend receives request
          ↓
Backend checks database
          ↓
Credentials are verified
          ↓
Authentication successful
```

### Authentication vs Authorization

**Authentication:**

> Who are you?

**Authorization:**

> What are you allowed to do?

Example:

```text
Login
 ↓
Authentication
 ↓
User identified
 ↓
Authorization
 ↓
Check what the user can access
```

---

## 4. Session Management

### What is Session Management?

**Session management** is the process of keeping track of a user's session after they log in.

HTTP is generally **stateless**, so the server needs a mechanism to recognize the same logged-in user across multiple requests.

Example:

```text
User logs in
     ↓
Server verifies credentials
     ↓
Session is created
     ↓
User moves to another page
     ↓
Browser sends session information
     ↓
Server identifies the session
```

### Session ID

A **session ID** is a unique identifier for a user's session.

Example:

```text
session_id = abc123
```

The server can associate the session ID with a user:

```text
Session ID → User ID
abc123     → User 25
```

### Cookies

A **cookie** is a small piece of data that the browser stores and sends back to the website.

A session ID can be stored inside a cookie.

The server may send:

```http
Set-Cookie: session_id=abc123
```

The browser stores the cookie.

Later, the browser sends:

```http
Cookie: session_id=abc123
```

The server can then use the session ID to identify the user's session.

### Cookie vs Session ID

They are **different**, but they work together.

```text
Cookie
  ↓
Stores / carries
  ↓
Session ID
```

* **Cookie** → storage/transport mechanism in the browser
* **Session ID** → identifier of the user's session

### Logout

When a user logs out:

```text
User clicks Logout
       ↓
Browser sends request
       ↓
Server ends/invalidates session
       ↓
User is no longer logged in
```

---

## 5. Web Application Workflows

### What is a Web Application Workflow?

A **web application workflow** is the sequence of steps that happens when a user performs an action on a website.

For example, when a user logs in:

```text
User
 ↓
Enters username + password
 ↓
Browser sends HTTP request
 ↓
Backend receives request
 ↓
Backend checks database
 ↓
Credentials are correct
 ↓
Session is created/maintained
 ↓
Server sends response
 ↓
Browser shows result
```

### Browser to Server

When the user clicks a button such as **Login**, the browser usually sends a request to the server.

```text
Browser
   ↓
HTTP Request
   ↓
Server
```

### Server Processing

The server processes the request and may communicate with the database.

```text
HTTP Request
     ↓
   Server
     ↓
  Database
     ↓
Processing
```

### Server Response

After processing the request, the server sends an HTTP response back to the browser.

```text
Server
   ↓
HTTP Response
   ↓
Browser
```

### Complete Workflow

```text
User Action
    ↓
Browser
    ↓
HTTP Request
    ↓
Server
    ↓
Database / Processing
    ↓
Session
    ↓
HTTP Response
    ↓
Browser
```

---

# Summary

Backend fundamentals help us understand what happens behind a website.

```text
API
 ↓
Communication between applications

Database
 ↓
Stores and manages data

Authentication
 ↓
Verifies who the user is

Session Management
 ↓
Keeps track of the user's login session

Web Application Workflow
 ↓
Shows how requests, backend processing,
database operations, sessions, and responses
work together
```

### Key Points

* **API** → Allows applications to communicate.
* **Database** → Stores and manages data.
* **Authentication** → Verifies the user's identity.
* **Authorization** → Determines what the user is allowed to do.
* **Session Management** → Maintains the user's login state.
* **Cookie** → Stores/carries information in the browser.
* **Session ID** → Identifies a user's session.
* **Web Application Workflow** → Describes the complete flow between the user, browser, server, and database.
