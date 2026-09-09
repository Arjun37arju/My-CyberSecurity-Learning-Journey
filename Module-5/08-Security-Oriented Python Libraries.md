# 🔐 Security-Oriented Python Libraries

## 📑 Contents

* [1. Requests](#1-requests)
* [2. JSON](#2-json)
* [3. OS](#3-os)
* [4. Socket](#4-socket)
* [5. Subprocess](#5-subprocess)

---

## 1. Requests

### What is Requests?

`requests` is a Python library used to send **HTTP/HTTPS requests** to web servers and APIs.

### Security Uses

* Web application testing
* API communication
* Checking HTTP status codes
* Inspecting HTTP headers

### Example

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
print(response.headers)
```

---

## 2. JSON

### What is JSON?

`json` is a Python built-in module used to work with **JSON (JavaScript Object Notation)** data.

### Important Functions

```text
json.dumps() → Python object → JSON string
json.loads() → JSON string → Python object
```

### Example

```python
import json

data = {
    "name": "Arjun",
    "role": "student"
}

text = json.dumps(data)

print(text)
```

---

## 3. OS

### What is OS?

`os` is a Python built-in module that allows Python programs to interact with the **operating system**.

### Security Uses

* Checking files and directories
* Reading environment variables
* Working with file paths
* Getting system information

### Example

```python
import os

print(os.getcwd())
print(os.path.isfile("main.py"))
print(os.getenv("API_KEY"))
```

---

## 4. Socket

### What is Socket?

`socket` is a Python built-in module used for **network communication**.

It can work with:

* IP addresses
* Ports
* TCP
* UDP
* Network connections

### Security Uses

* Testing network connectivity
* Understanding ports
* Network programming
* Security experiments

### Example

```python
import socket

s = socket.socket()
s.settimeout(2)

result = s.connect_ex(("localhost", 80))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

s.close()
```

---

## 5. Subprocess

### What is Subprocess?

`subprocess` is a Python built-in module used to **execute external programs and operating-system commands** from Python.

### Security Uses

* Security automation
* System administration
* Collecting system information
* Automating security tasks

### Example

```python
import subprocess

result = subprocess.run(
    ["whoami"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

### Security Note

Avoid passing untrusted user input directly into shell commands. Prefer passing commands and arguments as a list.

---

## 📌 Quick Summary

| Library      | Main Purpose                 |
| ------------ | ---------------------------- |
| `requests`   | HTTP/HTTPS communication     |
| `json`       | JSON data handling           |
| `os`         | Operating system interaction |
| `socket`     | Network communication        |
| `subprocess` | Execute external commands    |
