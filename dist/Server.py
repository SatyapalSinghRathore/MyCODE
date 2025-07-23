import socket
import threading

Server_IP = "192.168.1.45"
Port = 5050

Addr = (Server_IP, Port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Addr)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] : The Device which IP address {addr} is connected to this Server.")

    connection = True
    while connection:
        msg_length = conn.recv(64).decode('utf-8')   #HEADER = 64, FORMAT = 'utf-8'
        if msg_length:
            msg_length = int(msg_length)
            message = conn.recv(msg_length).decode('utf-8')
            if message == "-clear":
                connection = False
            print(f"\t\t\t[MESSAGE From {addr}] :   {message}")
    conn.close()
    print(f"[ACTIVE CONNECTION] : {threading.activeCount() - 1} Device is connected to this Server.")


def start():
    server.listen()
    print(f"[LISTINING] Server is listining on {Server_IP} IP address.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] : {threading.activeCount() - 1} Device is connected to this Server.")


print(f"[STARTING] Server is starting....")
start()