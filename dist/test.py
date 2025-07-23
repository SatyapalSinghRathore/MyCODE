import socket
# print(socket.gethostbyname(socket.gethostname()))

server_ip = "192.168.1.45"  # Replace with your wlan0 or eth0 IP
server_port = 12345  # Any open port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server running on {server_ip}:{server_port}")
