import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.86", 5000))
server.listen(5)
print("Server is waiting for clients...")

def handle_client(conn, address):
    print("Client connected:", address[0])
    # Receive messages from this client
    def receive_messages():
        while True:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    print("Client disconnected:", address[0])
                    break
                print(f"\nClient {address[0]}: {message}")
            except:
                break
        conn.close()

    # Start receiving in background
    thread = threading.Thread(target=receive_messages)
    thread.daemon = True
    thread.start()

    # Send messages to this client
    while True:
        try:
            message = input(f"You → {address[0]}: ")
            if message.lower() == "exit":
                break
            conn.send(message.encode())
        except:
            break
    conn.close()
    
# Accept multiple clients
while True:
    conn, address = server.accept()
    thread = threading.Thread(
        target=handle_client,
        args=(conn, address)
    )
    thread.daemon = True
    thread.start()
    print("Waiting for another client...")