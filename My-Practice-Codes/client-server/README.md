# Client–Server Socket Communication

## Description
A simple Python socket example demonstrating how a client sends data and a server receives it and sends a response.

## Files
- `client.py` — Connects to a remote host and sends data.
- `server.py` — Listens for a local connection, receives data, and sends a response.

## Requirements
Python 3.

## Usage

**1. Start the server** in one terminal:

```bash
python server.py
```

**2. Run the client** in another terminal:

```bash
python client.py
```

The server listens on `localhost` port `5000`, while the client connects to `example.com` on port `22`. These are different endpoints, so this client will not communicate with the local server as written.

To test the client and server together, the client must connect to `localhost` on port `5000`.

## Learning Goals
- Understand TCP sockets.
- Learn how a server listens for connections.
- Learn how a client sends data.
- Understand receiving and sending messages.
