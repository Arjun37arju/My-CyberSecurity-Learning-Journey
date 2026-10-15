# Web Fundamentals

## 📌 Table of Contents

- [Introduction](#introduction)
1. [How Websites Work](#1-how-websites-work)
   - [What Is a Website?](#what-is-a-website)
   - [How a Website Works](#how-a-website-works)
   - [DNS and IP Address](#dns-and-ip-address)
   - [Request and Response](#request-and-response)
   - [HTML, CSS and JavaScript](#html-css-and-javascript)
   - [Cybersecurity Connection](#cybersecurity-connection)
2. [Client-Server Architecture](#2-client-server-architecture)
   - [Client](#client)
   - [Server](#server)
   - [Client-Server Communication](#client-server-communication)
   - [Login Example](#login-example)
3. [Frontend and Backend Concepts](#3-frontend-and-backend-concepts)
   - [Frontend](#frontend)
   - [Backend](#backend)
   - [Frontend vs Backend](#frontend-vs-backend)
4. [Web Application Workflows](#4-web-application-workflows)
   - [Registration Workflow](#registration-workflow)
   - [Login Workflow](#login-workflow)
   - [Database Workflow](#database-workflow)
   - [HTTP and HTTPS](#http-and-https)
5. [Modern Web Architecture](#5-modern-web-architecture)
   - [3-Tier Architecture](#3-tier-architecture)
   - [Monolithic Architecture](#monolithic-architecture)
   - [API-Based Architecture](#api-based-architecture)
   - [Microservices Architecture](#microservices-architecture)
   - [Serverless Architecture](#serverless-architecture)
   - [Cloud-Based Architecture](#cloud-based-architecture)
   - [Content Delivery Network (CDN)](#content-delivery-network-cdn)
   - [Load Balancer](#load-balancer)
   - [API Gateway](#api-gateway)
   - [Caching](#caching)
   - [Architecture and Cybersecurity](#architecture-and-cybersecurity)

---

# Introduction

Web fundamentals are the basic concepts needed to understand how websites and web applications work.

Before learning web security, it is important to understand:

- How websites work
- How browsers communicate with servers
- Frontend and backend
- How web applications process requests
- How modern web applications are structured

These concepts help us understand vulnerabilities such as:

- Cross-Site Scripting (XSS)
- SQL Injection
- Authentication vulnerabilities
- Authorization problems
- Session attacks
- API security issues
- Server-side vulnerabilities

---

# 1. How Websites Work

## What Is a Website?

A website is a collection of related web pages and resources that users can access through a web browser.

Examples:

```text
google.com
youtube.com
github.com
```

A website can contain:

- Text and images
- Videos
- HTML and CSS
- JavaScript
- Forms
- APIs
- Databases and other web services

## How a Website Works

When you enter a website address in a browser, the browser communicates with the server to retrieve the required resources.

Example:

```text
User
  ↓
Browser
  ↓
DNS Lookup
  ↓
IP Address
  ↓
Server Connection
  ↓
HTTP Request
  ↓
Server Processing
  ↓
HTTP Response
  ↓
Browser Displays Website
```

### Step 1: User enters the website

The user enters a URL into the browser.

```text
https://example.com
```

The browser needs to locate the server associated with the domain name.

### Step 2: DNS finds the IP address

DNS stands for **Domain Name System**.

It helps translate a domain name into an IP address.

```text
example.com
     ↓
    DNS
     ↓
  IP Address
```

DNS works like a directory that helps the browser find the server's IP address.

### Step 3: Browser connects to the server

After obtaining the IP address, the browser establishes a connection with the server.

For HTTPS websites, the browser also establishes a secure TLS connection.

### Step 4: Browser sends a request

The browser sends an HTTP request to ask for a resource.

Example:

```http
GET / HTTP/1.1
Host: example.com
```

In simple words:

> Please send me the homepage.

### Step 5: Server processes the request

The server receives the request and determines what to return.

Depending on the application, it may:

- Return an HTML page
- Retrieve information from a database
- Execute backend logic
- Check authentication and permissions
- Communicate with another service
- Return an API response

### Step 6: Server sends a response

The server sends an HTTP response to the browser.

The response may contain:

- HTML
- CSS
- JavaScript
- Images
- JSON data
- An HTTP status code

### Step 7: Browser displays the website

The browser processes the received resources and displays the webpage.

```text
HTML       → Structure
CSS        → Appearance
JavaScript → Behaviour
```

The user can then interact with the website.

---

## DNS and IP Address

A domain name is easy for humans to remember.

Example:

```text
example.com
```

Computers use IP addresses to identify network interfaces and communicate across networks.

DNS helps resolve domain names to IP addresses.

```text
Domain Name
     ↓
    DNS
     ↓
  IP Address
     ↓
  Web Server
```

**Simple analogy:**

- Domain name = A person's name
- IP address = An address used to locate them
- DNS = A directory that helps find the address

---

## Request and Response

Web communication commonly follows a request-response model.

```text
Client
  │
  │ Request
  ↓
Server
  │
  │ Response
  ↓
Client
```

### Request

A request is a message sent by a client to ask for a resource or action.

Example:

```http
GET /about HTTP/1.1
Host: example.com
```

### Response

A response is the server's reply to the request.

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

The response can include the requested content.

---

## HTML, CSS and JavaScript

Webpages commonly use three important technologies.

### HTML

HTML stands for **HyperText Markup Language**.

It provides the structure of a webpage.

Example:

```html
<h1>Welcome</h1>
<p>This is my website.</p>
```

HTML creates elements such as headings, paragraphs, forms, buttons and links.

### CSS

CSS stands for **Cascading Style Sheets**.

It controls the appearance and layout of a webpage.

It can control:

- Colours
- Fonts
- Size
- Spacing
- Layout
- Responsiveness

### JavaScript

JavaScript adds behaviour and interaction to a webpage.

Examples:

- Button actions
- Form interaction
- Dynamic content
- Client-side validation
- Updating page content

Easy way to remember:

```text
HTML       → Structure
CSS        → Style
JavaScript → Behaviour
```

---

## Cybersecurity Connection

Understanding how websites work helps us identify where security problems can occur.

```text
Browser
   ↓
HTTP/HTTPS
   ↓
Web Server
   ↓
Backend Application
   ↓
Database
```

Examples of security concerns:

```text
Browser Input      → XSS
HTTP Requests      → Request Manipulation
Backend            → Authentication Issues
Database Queries   → SQL Injection
Server              → Security Misconfiguration
```

Understanding normal website behaviour is important before learning how attackers may abuse it.

---

# 2. Client-Server Architecture

Client-server architecture describes how a client and a server communicate to provide services or resources.

The basic idea is:

> Client requests something → Server processes it → Server responds.

## Client

A client is a device or application that requests a service or resource.

For web applications, the browser commonly acts as the client.

Examples:

```text
Chrome
Firefox
Edge
Safari
```

Example:

```text
Chrome → Request → Web Server
```

## Server

A server is a system that receives requests and provides or processes resources and services.

A web server or backend system can:

- Receive requests
- Process requests
- Return web resources
- Communicate with databases
- Apply application logic
- Communicate with other services

## Client-Server Communication

```text
Client
  ↓
Request
  ↓
Server
  ↓
Processing
  ↓
Response
  ↓
Client
```

### Example

When opening YouTube:

```text
Browser
   ↓
Sends a request
   ↓
YouTube infrastructure
   ↓
Processes the request
   ↓
Returns a response
   ↓
Browser displays content
```

## Login Example

When logging into a website:

```text
Browser
   ↓
Username and Password
   ↓
Backend Server
   ↓
Authentication Check
   ↓
Success or Failure Response
```

If the credentials are valid, the application may create a session and allow access to the dashboard.

If they are invalid, the application returns an error message.

**Important:** Authentication and permission checks must be enforced on the server, not only in the browser.

## Cybersecurity Connection

Security testing often involves examining communication between the client and server.

A security tester may investigate:

- HTTP requests and responses
- Headers
- Cookies
- Authentication
- Authorization
- Input validation
- Session management
- HTTPS/TLS
- Access control

The basic model remains:

```text
CLIENT ↔ SERVER
```

---

# 3. Frontend and Backend Concepts

A web application commonly has a user-facing side and a server-side component.

```text
Web Application
       │
   ┌───┴───┐
   ↓       ↓
Frontend  Backend
               ↓
            Database
```

## Frontend

The frontend is the part of the application that the user sees and interacts with.

Examples:

- Buttons
- Forms
- Menus
- Text and images
- Page layouts
- Login pages
- Navigation bars

Common frontend technologies:

```text
HTML
CSS
JavaScript
```

## Backend

The backend works behind the scenes and handles application logic.

It can:

- Process requests
- Authenticate users
- Check permissions
- Validate input
- Communicate with databases
- Execute business logic
- Return responses

Common backend technologies include Python, Java, JavaScript with Node.js, PHP and C#.

Example:

```text
Frontend
   ↓
Login Request
   ↓
Backend
   ↓
Database
   ↓
Backend Response
   ↓
Frontend
```

## Frontend vs Backend

| Frontend | Backend |
|---|---|
| User-facing part | Server-side part |
| Displays content | Processes requests |
| Handles user interaction | Handles application logic |
| HTML, CSS, JavaScript | Python, Java, PHP, etc. |
| Runs mainly in the browser | Runs on the server |
| Client-side validation | Server-side validation |

**Important:** Frontend validation improves usability, but backend validation is essential for security because client-side checks can be bypassed.

---

# 4. Web Application Workflows

A workflow describes the steps an application follows to complete an action.

## Registration Workflow

When a user creates an account:

```text
User
  ↓
Registration Form
  ↓
Frontend Validation
  ↓
Backend Receives Data
  ↓
Server-Side Validation
  ↓
Password Hashing
  ↓
Database Stores Account
  ↓
Success Response
```

Important security practices:

- Validate input on the server.
- Use secure password-hashing algorithms.
- Use parameterized queries.
- Protect sensitive data in transit using HTTPS.
- Avoid storing plaintext passwords.

## Login Workflow

When a user logs in:

```text
User
  ↓
Enters Credentials
  ↓
HTTPS Request
  ↓
Backend Receives Credentials
  ↓
Checks Stored Password Hash
  ↓
Authentication Result
  ↓
Creates Secure Session
  ↓
Dashboard
```

If authentication fails, the application should reject the login.

**Authentication** verifies who the user is.

**Authorization** determines what the authenticated user is allowed to access.

## Database Workflow

A database stores and manages application data.

Example:

```text
User Input
    ↓
Backend Application
    ↓
Parameterized SQL Query
    ↓
Database
    ↓
Query Result
    ↓
Backend
    ↓
Response to User
```

Examples of database systems:

- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server

Security practices:

- Use parameterized queries to prevent SQL injection.
- Apply access controls.
- Give database accounts only the permissions they need.
- Protect sensitive information.
- Avoid exposing database credentials.

## HTTP and HTTPS

### HTTP

HTTP stands for **HyperText Transfer Protocol**.

It is used for communication between clients and web servers.

### HTTPS

HTTPS stands for **HyperText Transfer Protocol Secure**.

It uses TLS to protect communication between the client and server.

| HTTP | HTTPS |
|---|---|
| Communication is not encrypted by HTTP itself | Communication is protected using TLS |
| Data may be exposed to network observers | Data is encrypted in transit |
| Does not provide TLS server authentication | TLS certificates help authenticate the server |
| Generally unsuitable for sensitive information | Essential for protecting sensitive web traffic |

**Remember:**

- Encryption in transit → Protects data while it travels.
- Encryption at rest → Protects data while it is stored.

---

# 5. Modern Web Architecture

Web architecture describes how the components of a web application are organised and communicate with each other.

Different architectures are selected depending on the application's size, complexity, performance and security requirements.

## 3-Tier Architecture

3-tier architecture separates an application into three layers.

```text
Presentation Layer
       ↓
Application Layer
       ↓
Data Layer
```

### 1. Presentation Layer

The user interface through which users interact with the application.

Example: HTML, CSS and JavaScript in a browser.

### 2. Application Layer

Processes requests and implements application logic.

Example: A Python Flask backend.

### 3. Data Layer

Stores and manages information.

Example: A MySQL or PostgreSQL database.

**Benefits:**

- Separates responsibilities.
- Makes maintenance easier.
- Helps organise security controls.
- Allows layers to be managed independently.

**Cybersecurity connection:** The database should not be directly exposed to the public internet without appropriate protection.

---

## Monolithic Architecture

A monolithic application is built and deployed as a single application unit.

Its components may include:

- User authentication
- Business logic
- Product management
- Database access

```text
Web Application
       │
  ┌────┼────┐
  ↓    ↓    ↓
Login Products Orders
       │
    Database
```

**Benefits:**

- Simple to develop for small applications.
- Easier to deploy initially.
- Components can share code directly.

**Limitations:**

- Large applications can become difficult to maintain.
- A change may require redeploying the entire application.
- A serious vulnerability may affect multiple features.

**Cybersecurity connection:** A vulnerability in one part of a monolith can sometimes expose other parts if access controls are weak.

---

## API-Based Architecture

API-based architecture allows different applications or components to communicate through APIs.

API stands for **Application Programming Interface**.

Example:

```text
Web Browser
     ↓
    API
     ↓
Backend Application
     ↓
  Database
```

An API defines how one software component can request services or data from another.

Example HTTP request:

```http
GET /api/users HTTP/1.1
Host: example.com
```

An API might return JSON:

```json
{
  "username": "arjun",
  "role": "user"
}
```

**Benefits:**

- Allows applications to communicate.
- Supports web and mobile applications.
- Helps separate frontend and backend.
- Enables integration with external services.

**Cybersecurity connection:**

- Authenticate users where required.
- Enforce authorization on every protected operation.
- Validate incoming data.
- Apply rate limiting where appropriate.
- Avoid exposing sensitive information.

---

## Microservices Architecture

Microservices architecture divides an application into smaller, independently deployable services.

Each service handles a specific responsibility.

Example:

```text
             API Gateway
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
   User Service Order Service Payment Service
       ↓          ↓          ↓
   User Data   Order Data  Payment Data
```

Examples of services:

- User service
- Payment service
- Notification service
- Order service

**Benefits:**

- Services can be developed independently.
- Individual services can be scaled separately.
- Teams can maintain different services.

**Limitations:**

- Communication between services adds complexity.
- Monitoring and troubleshooting become harder.
- More network endpoints need protection.

**Cybersecurity connection:** Each service needs appropriate authentication, authorization, secure communication and access controls.

---

## Serverless Architecture

Serverless architecture allows developers to run application code without directly managing the underlying servers.

The cloud provider manages much of the infrastructure.

Example:

```text
User Request
     ↓
API Gateway
     ↓
Cloud Function
     ↓
Database or Other Service
```

Examples of serverless platforms include AWS Lambda, Azure Functions and Google Cloud Functions.

**Benefits:**

- Reduces server management.
- Can scale automatically.
- Often charges based on usage.

**Cybersecurity connection:**

- Protect function permissions.
- Store secrets securely.
- Validate incoming events and requests.
- Monitor execution logs.
- Restrict access to cloud resources.

**Important:** Serverless does not mean there are no servers; the provider manages the servers.

---

## Cloud-Based Architecture

Cloud-based architecture uses cloud computing services to host applications, databases, storage and other resources.

Examples of cloud providers:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud

Example:

```text
Users
  ↓
Cloud Web Application
  ↓
Backend Service
  ↓
Cloud Database
  ↓
Cloud Storage
```

**Benefits:**

- Flexible resource scaling.
- Access to managed services.
- Global availability options.
- Easier infrastructure expansion.

**Cybersecurity connection:**

- Configure permissions correctly.
- Prevent public exposure of private storage.
- Protect cloud credentials.
- Enable logging and monitoring.
- Encrypt sensitive data.
- Apply security updates.

---

## Content Delivery Network (CDN)

A CDN is a network of distributed servers that delivers content to users from locations closer to them.

It is commonly used for images, videos, stylesheets and other static resources.

Example:

```text
User in India
      ↓
Nearby CDN Server
      ↓
Website Content
```

Without a CDN, content may need to travel from a distant origin server.

**Benefits:**

- Reduces content delivery latency.
- Improves loading speed.
- Reduces traffic to the origin server.
- Can help absorb some traffic spikes and attacks.

**Cybersecurity connection:**

A CDN may provide DDoS protection and web application firewall features, depending on the service and configuration.

---

## Load Balancer

A load balancer distributes incoming requests across multiple servers.

Example:

```text
          Incoming Requests
                  ↓
             Load Balancer
             /     |     \
            ↓      ↓      ↓
        Server 1 Server 2 Server 3
```

**Benefits:**

- Distributes traffic.
- Helps prevent one server from becoming overloaded.
- Improves availability.
- Supports scaling across multiple servers.

**Cybersecurity connection:**

- Configure secure communication.
- Restrict direct access to backend servers where appropriate.
- Monitor unusual traffic.
- Configure health checks securely.
- Avoid trusting client-supplied forwarding headers without validation.

---

## API Gateway

An API gateway acts as an entry point for API requests and routes them to the appropriate backend services.

Example:

```text
Web App       Mobile App
    \           /
     \         /
      API Gateway
           ↓
     ┌─────┼─────┐
     ↓     ↓     ↓
   Users Orders Payments
```

Depending on its configuration, an API gateway can provide:

- Request routing
- Authentication integration
- Rate limiting
- Logging
- Request and response handling

**Cybersecurity connection:**

An API gateway can help enforce security controls, but backend services must still enforce their own required authorization checks.

---

## Caching

Caching stores a copy of data temporarily so it can be retrieved more quickly later.

Example:

```text
User Request
     ↓
Cache Check
   /     \
Hit      Miss
 ↓         ↓
Return   Fetch from
Cached   Origin Server
Data        ↓
         Store in Cache
```

A **cache hit** occurs when the requested content is available in the cache.

A **cache miss** occurs when the content must be retrieved from another source.

Examples:

- Browser cache
- CDN cache
- Application cache
- Database query cache

**Benefits:**

- Improves response speed.
- Reduces repeated processing.
- Reduces load on backend systems.

**Cybersecurity connection:**

Incorrect caching rules can expose sensitive information. Private or personalised responses must not be cached in a way that allows other users to access them.

---

## Architecture and Cybersecurity

Different architectural components introduce different security considerations.

| Component | Important security concern |
|---|---|
| Frontend | Cross-Site Scripting (XSS) |
| Backend | Authentication and authorization |
| Database | SQL injection and access control |
| API | Broken access control and excessive data exposure |
| Microservices | Service-to-service security |
| Cloud | Misconfiguration and exposed resources |
| CDN | Cache configuration and traffic attacks |
| Load balancer | Traffic handling and trusted headers |
| API gateway | Authentication and rate limiting |
| Cache | Accidental exposure of sensitive data |
| Serverless | Excessive permissions and exposed functions |

### Basic Secure Web Architecture

```text
User
  ↓
CDN / Web Protection
  ↓
Load Balancer
  ↓
Web Application / API Gateway
  ↓
Backend Services
  ↓
Database
```

Security controls can include:

- HTTPS/TLS for data in transit.
- Input validation and output encoding.
- Parameterized database queries.
- Secure authentication and session management.
- Server-side authorization.
- Least-privilege access.
- Secure configuration and patching.
- Logging and monitoring.
- Encryption of sensitive stored data.
- Regular security testing.

**Final takeaway:** Understanding web architecture helps cybersecurity learners identify where data travels, where it is processed, where it is stored and where security controls should be applied.
