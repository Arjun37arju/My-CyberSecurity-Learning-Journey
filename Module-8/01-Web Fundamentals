# Web Fundamentals

## 📌 Table of Contents

[Introduction](#introduction)
1. [How Websites Work](#1-how-websites-work)
2. [Client-Server Architecture](#2-client-server-architecture)
3. [Frontend and Backend Concepts](#3-frontend-and-backend-concepts)
4. [Web Application Workflows](#4-web-application-workflows)
5. [Modern Web Architecture](#5-modern-web-architecture)
   * [3-Tier Architecture](#3-tier-architecture)
   * [Monolithic Architecture](#monolithic-architecture)
   * [API-Based Architecture](#api-based-architecture)
   * [Microservices Architecture](#microservices-architecture)
   * [Serverless Architecture](#serverless-architecture)
   * [Cloud-Based Architecture](#cloud-based-architecture)
   * [CDN](#cdn)
   * [Load Balancer](#load-balancer)
   * [API Gateway](#api-gateway)
   * [Caching](#caching)
   * [Architecture and Cybersecurity](#architecture-and-cybersecurity)


---

# Introduction

Web fundamentals are the basic concepts needed to understand how websites and web applications work.

Before learning **web security**, it is important to understand:

* How websites work
* How browsers communicate with servers
* Frontend and backend
* How web applications process requests
* How modern web applications are structured

These concepts form the foundation for understanding vulnerabilities such as:

* Cross-Site Scripting (XSS)
* SQL Injection
* Authentication vulnerabilities
* Authorization problems
* Session attacks
* API security issues
* Server-side vulnerabilities

---

# 1. How Websites Work

## What is a Website?

A website is a collection of web resources that can be accessed through the internet using a web browser.

Examples:

```text
google.com
youtube.com
github.com
```

A website can contain:

* Text
* Images
* Videos
* HTML
* CSS
* JavaScript
* Forms
* APIs
* Databases
* Other web services

---

## How a Website Works

When you type a website address into a browser, several things happen.

For example:

```text
youtube.com
```

The basic process is:

```text
User
 ↓
Browser
 ↓
DNS
 ↓
IP Address
 ↓
Web Server
 ↓
Request
 ↓
Server Processing
 ↓
Response
 ↓
Browser
 ↓
Web Page
```

### Step 1: User enters the website

The user enters:

```text
https://youtube.com
```

The browser needs to find the server associated with this website.

---

### Step 2: DNS finds the IP address

The browser uses DNS to find the IP address associated with the domain name.

```text
youtube.com
      ↓
     DNS
      ↓
IP Address
```

DNS works like a directory that helps translate a domain name into an IP address.

The browser needs the IP address so it can locate and communicate with the appropriate server.

---

### Step 3: Browser connects to the server

After obtaining the IP address, the browser can establish communication with the server.

```text
Browser
   ↓
IP Address
   ↓
Web Server
```

---

### Step 4: Browser sends a request

The browser sends a request asking the server for a resource.

For example:

```http
GET / HTTP/1.1
Host: example.com
```

In simple words:

> "Please give me the webpage."

---

### Step 5: Server processes the request

The server receives the request and determines what needs to be returned.

Depending on the application, the server may:

* Return HTML
* Retrieve information
* Communicate with a database
* Execute backend logic
* Call another service
* Return an API response

---

### Step 6: Server sends a response

The server sends a response back to the browser.

The response may contain:

* HTML
* CSS
* JavaScript
* Images
* JSON data
* Other resources

---

### Step 7: Browser displays the website

The browser processes the received resources and builds the webpage.

```text
HTML       → Structure
CSS        → Appearance
JavaScript → Behavior
```

The user can then see and interact with the website.

---

## DNS and IP Address

A domain name is easier for humans to remember:

```text
example.com
```

Computers communicate using IP addresses.

DNS helps connect the two:

```text
Domain Name
     ↓
    DNS
     ↓
IP Address
     ↓
Server
```

### Simple analogy

Think of a domain name as a person's name and the IP address as their address.

You know:

```text
Person's Name
```

You need:

```text
Their Address
```

DNS helps you find the address.

---

## Request and Response

Web communication mainly follows a request-response model.

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

The client asks the server for something.

Example:

```text
"Give me the homepage."
```

### Response

The server sends something back.

Example:

```text
"Here is the homepage."
```

---

## HTML, CSS and JavaScript

Webpages commonly use three important technologies.

### HTML

HTML provides the **structure** of the webpage.

Example:

```html
<h1>Welcome</h1>
<p>This is my website.</p>
```

HTML creates elements such as:

* Headings
* Paragraphs
* Forms
* Buttons
* Links

---

### CSS

CSS controls the **appearance and style**.

It can control:

* Colors
* Fonts
* Size
* Spacing
* Layout

---

### JavaScript

JavaScript provides **behavior and interaction**.

For example:

* Button actions
* Form interaction
* Dynamic content
* User interface behavior

Easy way to remember:

```text
HTML       → Structure
CSS        → Style
JavaScript → Behavior
```

---

## Cybersecurity Connection

Understanding how websites work helps identify where security problems can occur.

```text
Browser
   ↓
HTTP/HTTPS
   ↓
Server
   ↓
Backend
   ↓
Database
```

Different parts can have different security problems.

Examples:

```text
Browser       → XSS
HTTP Request  → Request manipulation
Backend       → Authentication issues
Database      → SQL Injection
Server        → Misconfiguration
```

Understanding the normal workflow is important before learning how attackers try to abuse it.

---

# 2. Client-Server Architecture

Client-server architecture describes how a client and server communicate.

The basic idea is:

> **Client requests something → Server processes it → Server responds.**

---

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

For example:

```text
Chrome → Request → Web Server
```

---

## Server

A server is a system that receives requests and provides or processes resources and services.

A web server can:

* Receive requests
* Process requests
* Return web resources
* Communicate with backend applications
* Communicate with databases

---

## Client-Server Communication

The basic model is:

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
Chrome
   ↓
"Give me the YouTube webpage."
   ↓
YouTube Server
   ↓
Processes request
   ↓
Response
   ↓
Chrome
```

---

## Login Example

When logging into a website:

```text
Browser
   ↓
Username + Password
   ↓
Server
   ↓
Authentication
   ↓
Response
   ↓
Browser
```

If the credentials are valid:

```text
Server
   ↓
Login successful
   ↓
Browser
   ↓
Dashboard
```

If they are invalid:

```text
Server
   ↓
Invalid credentials
   ↓
Browser
```

---

## Cybersecurity Connection

Understanding client-server communication is important because security testing often involves examining the communication between the client and server.

A security tester may investigate:

* HTTP requests
* HTTP responses
* Headers
* Cookies
* Authentication
* Authorization
* Input validation
* Session management
* HTTPS/TLS

The basic model remains:

```text
CLIENT ↔ SERVER
```

---

# 3. Frontend and Backend Concepts

A web application generally has a user-facing side and a server-side side.

```text
Web Application
       │
   ┌───┴───┐
   ↓       ↓
Frontend Backend
```

---

## Frontend

The frontend is the part of the application that the user sees and interacts with.

Examples:

* Buttons
* Forms
* Menus
* Text
* Images
* Page layouts
* Login pages

Common frontend technologies include:

```text
HTML
CSS
JavaScript
```

---

## Backend

The backend works behind the scenes.

It can:

* Process requests
* Apply business logic
* Authenticate users
* Check permissions
* Communicate with databases
* Communicate with other services
* Return responses

Example:

```text
Frontend
   ↓
Login Request
   ↓
Backend
   ↓
Database
```

---

## Frontend vs Backend

| Frontend         | Backend            |
| ---------------- | ------------------ |
| User-facing      | Behind the scenes  |
| User interaction | Request processing |
| HTML             | Server-si          |
