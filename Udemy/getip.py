
import socket

hostname = socket.gethostname()
ip_add = socket.gethostbyname(hostname)

print(ip_add)
