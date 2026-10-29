
# Understand Network Automation

## Table of Contents

1. [Socket Programming Fundamentals](#1-socket-programming-fundamentals)
2. [Network Communication](#2-network-communication)
3. [Service Interaction](#3-service-interaction)
4. [Automated Checks](#4-automated-checks)
5. [Basic Scanning Concepts](#5-basic-scanning-concepts)

---

## 1. Socket Programming Fundamentals

A **socket** is an endpoint used by programs to communicate over a network.

A socket uses an **IP address and port** to establish communication.

### Client and Server

```text
Client → Server
   ↓
Connect
   ↓
Send / Receive Data
```

### Python Socket

```python
import socket

s = socket.socket()
s.connect(("localhost", 5000))

print("Connected")

s.close()
```

### Important Functions

* `socket.socket()` → Creates a socket.
* `connect()` → Connects to a server.
* `send()` → Sends data.
* `recv()` → Receives data.
* `close()` → Closes the connection.
* `connect_ex()` → Attempts a connection and returns `0` if successful.

### TCP and UDP

* **TCP** → Reliable and connection-oriented.
* **UDP** → Faster and connectionless.

---

## 2. Network Communication

**Network communication** is the process of exchanging data between two or more devices or programs through a network.

### Important Concepts

* **IP address** → Identifies a device.
* **Port** → Identifies a service or communication endpoint.
* **Send** → Sends data.
* **Receive** → Receives data.

### Server Functions

```python
server.bind(("localhost", 5000))
server.listen(1)
conn, addr = server.accept()
```

* `bind()` → Assigns an address and port to the server.
* `listen()` → Waits for incoming connections.
* `accept()` → Accepts a client connection.
* `conn` → Connection object used to communicate with the client.
* `addr` → Client's address.

### `recv(1024)`

```python
data = conn.recv(1024)
```

This receives **up to 1024 bytes** in one call.

### Bytes

Sockets normally communicate using bytes.

```python
s.send(b"Hello")
```

`b"Hello"` represents bytes.

---

## 3. Service Interaction

A **network service** is a program that provides a function over a network.

Examples:

```text
HTTP  → Port 80
HTTPS → Port 443
SSH   → Port 22
DNS   → Port 53
```

**Service interaction** means communicating with a network service by connecting, sending a request, receiving a response, and checking the result.

### HTTP and HTTPS

* **HTTP** → HyperText Transfer Protocol.
* **HTTPS** → HTTP protected using TLS.
* **TLS** → Transport Layer Security.

TLS provides:

* Encryption
* Authentication
* Integrity

### Python `requests`

The `requests` library is mainly used for **HTTP and HTTPS** communication.

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
print(response.text)
```

* `status_code` → Shows the HTTP result.
* `text` → Contains the response content.

### `raise_for_status()`

```python
response.raise_for_status()
```

It checks the HTTP status and **raises an error if the request failed**.

It can be used with `try` and `except`:

```python
try:
    response.raise_for_status()
except requests.RequestException:
    print("Request failed")
```

---

## 4. Automated Checks

**Automated checks** use a program to automatically check hosts, ports, or services instead of checking them manually.

### Common Checks

1. **Host check** → Is the host reachable?
2. **Port check** → Is the port accepting connections?
3. **Service check** → Is the service responding?
4. **HTTP check** → Is the website responding?

### Port Check Example

```python
import socket

s = socket.socket()

result = s.connect_ex(("localhost", 5000))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

s.close()
```

`connect_ex()` returns:

```text
0       → Connection successful
Non-zero → Connection failed
```

### Automated HTTP Check

```python
import requests

try:
    response = requests.get("https://example.com", timeout=5)

    if response.status_code == 200:
        print("Website is working")
    else:
        print("Website responded with:", response.status_code)

except requests.RequestException:
    print("Website is not reachable")
```

`timeout=5` prevents the program from waiting indefinitely.

### Security Use

Automated checks can:

* Save time
* Reduce repetitive manual work
* Detect problems quickly
* Check services repeatedly
* Report results automatically

---

## 5. Basic Scanning Concepts

**Scanning** means automatically checking a system or network to discover information.

### Host Discovery

Host discovery finds which devices are **reachable** on a network.

```text
Network
   ↓
Find reachable hosts
   ↓
192.168.1.1 → Reachable
192.168.1.2 → Not reachable
192.168.1.3 → Reachable
```

### Port Scanning

Port scanning checks which ports on a host are **open or closed**.

```text
Host: 192.168.1.10

Port 22  → OPEN   → SSH
Port 80  → OPEN   → HTTP
Port 443 → OPEN   → HTTPS
Port 25  → CLOSED
```

Example:

```python
result = s.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")
```

### Service Identification

After finding an open port, we can try to identify the service running on it.

```text
Open Port
    ↓
Service Check
    ↓
Identify Service
```

### Basic Scanning Flow

```text
Host Discovery
      ↓
Port Scanning
      ↓
Service Identification
      ↓
Report Results
```

> **Basic scanning = discovering reachable hosts, open ports, and available services.**

---

## Conclusion

Network automation allows security professionals to use programs and scripts to communicate with network services, perform automated checks, scan authorized systems, and reduce repetitive manual work.

### Key Points

```text
Socket
  ↓
Network Communication
  ↓
Service Interaction
  ↓
Automated Checks
  ↓
Basic Scanning
```

**Note:** Scanning should only be performed on systems and networks that you own or have permission to test.
