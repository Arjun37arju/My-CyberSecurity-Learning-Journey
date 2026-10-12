
import socket


def port_scaner(host, start_port, end_port):
    print(f"Scanning {host} from {start_port} to {end_port}\n")

    ip = socket.gethostbyname(host)
    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port} is CLOSED")

        s.close()

    print("\n========== SUMMARY ==========")
    print(f"IP Address : {ip}")
    print("-----------------------------")

    for port in open_ports:
        service = service_ide(host, port)

        print(f"Port       : {port}")
        print(f"Service    : {service}")
        print("-----------------------------")


def service_ide(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))

        try:
            data = s.recv(1024)
            service = data.decode(errors="ignore").strip()
        except:
            service = "Unknown"

        s.close()

        return service

    except Exception as e:
        print(f"Can't grab {host}:{port} - {e}")
        return "Unknown"


port_scaner("example.com", 1, 100)
