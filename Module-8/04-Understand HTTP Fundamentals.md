# Understand HTTP Fundamentals

## 📑 Content

1. [HTTP Requests](#1-http-requests)
2. [HTTP Responses](#2-http-responses)
3. [HTTP Methods](#3-http-methods)
4. [HTTP Status Codes](#4-http-status-codes)
5. [HTTP Headers](#5-http-headers)

---

## 1. HTTP Requests

### What is an HTTP Request?

An **HTTP request** is a message sent by the client to the server asking for a resource or action.

```text
Client → HTTP Request → Server
```

For example, when you open a website, your browser sends an HTTP request to the web server.

### Example

```http
GET /index.html HTTP/1.1
Host: example.com
```

* `GET` → Method
* `/index.html` → Requested resource
* `HTTP/1.1` → HTTP version
* `Host` → Website/domain

### Request Structure

An HTTP request can contain:

* Request Line
* Headers
* Blank Line
* Body

Example:

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{"username":"arjun","password":"1234"}
```

---

## 2. HTTP Responses

### What is an HTTP Response?

An **HTTP response** is the message sent by the server back to the client after receiving an HTTP request.

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

### Example

```http
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello</h1>
```

* `HTTP/1.1` → HTTP version
* `200` → Status code
* `OK` → Meaning of the status code
* `Content-Type` → Type of content
* `<h1>Hello</h1>` → Response body

### Remember

> **Request = Client asks**
> **Response = Server answers**

---

## 3. HTTP Methods

HTTP methods tell the server **what action the client wants to perform**.

### GET

Used to **get or read data**.

```http
GET /users HTTP/1.1
Host: example.com
```

> **GET = Get data**

### POST

Used to **send or create data**.

```http
POST /users HTTP/1.1
Host: example.com
```

> **POST = Send/Create data**

### PUT

Used to **replace or update existing data**.

```http
PUT /users/10
```

> **PUT = Replace/Update data**

### PATCH

Used to **partially update existing data**.

```http
PATCH /users/10
```

For example, changing only a user's email address.

> **PATCH = Partial update**

### DELETE

Used to **delete data**.

```http
DELETE /users/10
```

> **DELETE = Delete data**

### Quick Reference

```text
GET     → Get data
POST    → Send/Create data
PUT     → Replace/Update data
PATCH   → Partially update data
DELETE  → Delete data
```

---

## 4. HTTP Status Codes

An **HTTP status code** is a number sent by the server to tell the client what happened to the request.

### Status Code Categories

| Range | Meaning       |
| ----- | ------------- |
| `1xx` | Informational |
| `2xx` | Success       |
| `3xx` | Redirection   |
| `4xx` | Client Error  |
| `5xx` | Server Error  |

### Common Status Codes

#### 200 OK

The request was successful.

```text
200 OK
```

#### 201 Created

A new resource was created successfully.

```text
201 Created
```

#### 301 Moved Permanently

The requested resource has permanently moved to another location.

```text
301 Moved Permanently
```

#### 400 Bad Request

The request sent by the client is invalid or incorrect.

```text
400 Bad Request
```

#### 401 Unauthorized

Authentication is required.

```text
401 Unauthorized
```

#### 403 Forbidden

The client does not have permission to access the resource.

```text
403 Forbidden
```

#### 404 Not Found

The requested resource could not be found.

```text
404 Not Found
```

#### 500 Internal Server Error

Something went wrong on the server.

```text
500 Internal Server Error
```

### Quick Reference

```text
200 → Success
201 → Created
301 → Moved Permanently
400 → Bad Request
401 → Authentication Required
403 → Forbidden
404 → Not Found
500 → Server Error
```

---

## 5. HTTP Headers

### What is an HTTP Header?

An **HTTP header** contains additional information about an HTTP request or response.

General format:

```text
Header-Name: Value
```

### Example

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Chrome
Accept: text/html
```

Here:

* `Host` → Header
* `User-Agent` → Header
* `Accept` → Header

### Common HTTP Headers

#### Host

Tells the server which website/domain the client wants.

```http
Host: example.com
```

#### Content-Type

Tells what type of data is being sent.

```http
Content-Type: application/json
```

Examples:

```text
application/json → JSON data
text/html        → HTML data
```

#### Authorization

Used to send authentication information to the server.

```http
Authorization: Bearer abc123
```

#### User-Agent

Provides information about the client/software making the request.

```http
User-Agent: Chrome
```

#### Content-Length

Tells the size of the data being sent.

```http
Content-Length: 120
```

### Quick Reference

```text
Host          → Website/domain
Content-Type  → Type of data
Authorization → Authentication information
User-Agent    → Client information
Content-Length → Data size
```

---

## Summary

HTTP is used for communication between a **client and a server**.

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

Important concepts:

```text
HTTP Request  → Client asks the server
HTTP Response → Server answers the client

GET     → Get data
POST    → Send/Create data
PUT     → Replace/Update data
PATCH   → Partially update data
DELETE  → Delete data

200 → Success
201 → Created
301 → Moved
400 → Bad Request
401 → Authentication Required
403 → Forbidden
404 → Not Found
500 → Server Error

Host          → Website/domain
Content-Type  → Type of data
Authorization → Authentication information
User-Agent    → Client information
```
