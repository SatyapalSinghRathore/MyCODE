import socket

addr = ('192.168.1.45', 5020)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(addr)