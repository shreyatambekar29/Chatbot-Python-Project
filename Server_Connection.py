import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
clients = []

print("Server started on port 5555")
while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    print(f"Connection from {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
