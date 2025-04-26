# Simplified console-based multiplayer chat game
# Requires 'socket' and 'threading' (standard libraries)
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))
    
    username = input("Enter your username: ")
    client.send(username.encode())
    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        message = input()
        if message.lower() == 'quit':
            break
        client.send(f"{username}: {message}".encode())
    
    client.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 55555))
    server.listen()
    
    clients = []
    
    def broadcast(message):
        for client in clients:
            client.send(message)
    
    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                clients.remove(client)
                client.close()
                break
    
    while True:
        client, addr = server.accept()
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    print("Run this script twice: once as server, once as client.")
    mode = input("Type 'server' to start server or 'client' to join: ").lower()
    if mode == 'server':
        start_server()
    elif mode == 'client':
        start_client()