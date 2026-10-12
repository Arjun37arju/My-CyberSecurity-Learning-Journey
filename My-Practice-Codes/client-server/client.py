import socket

s = socket.socket()
s.connect(("example.com",22))
s.send(b"hello")
data = s.recv(1024)
print(data)

s.close()
