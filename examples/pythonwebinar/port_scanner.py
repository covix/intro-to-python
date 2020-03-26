import socket

name = str(input("Enter the hostname to be scanned: "))  # Target Host, www.example.com
ip = socket.gethostbyname(name)  # Resolve host to IPv4 address

print(ip)  # Print the IP address

while True:
    port = int(input("Enter the port: "))  # Enter the port to be scanned

    try:
        sock = socket.socket()
        sock.settimeout(5)
        res = sock.connect((ip, port))
        print(f"Port {port}: Open")
        sock.close()
    except socket.timeout:
        print(f"Port {port}: Closed")

print("Port Scanning complete")
