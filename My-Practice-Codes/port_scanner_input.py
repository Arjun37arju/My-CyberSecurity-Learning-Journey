
import socket

def port_scaner(host , start_port , end_port):
    print(f" Scanning {host} from {start_port} to {end_port} \n IP Address: {host} ", socket.gethostbyname(host))

    for port in range(start_port , end_port):
        s = socket.socket( socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host , port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        s.close()

name= input("enter host: ")
a= int(input("enter starting range: "))
b = int(input("enter ending port range: "))

port_scaner(name,a , b)
