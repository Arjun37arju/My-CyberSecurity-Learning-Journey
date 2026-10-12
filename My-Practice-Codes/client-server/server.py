import socket

server = socket.socket()
server.bind(("localhost",5000))
server.listen(1)

conn, addr = server.accept()
data = conn.recv(1024)
print(data)
conn.send(b"thankyou for sending...! ")

conn.close()
server.close()
