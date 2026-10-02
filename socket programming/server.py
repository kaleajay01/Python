import socket
import threading

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP and port
server.bind(("10.110.36.241", 5000))

# Listen for clients
server.listen(10)

print("Server started...")
print("Waiting for clients...")

# Store connected clients
clients = []


# Function to send message to all clients
def broadcast(message):

    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)


# Function to handle each client
def handle_client(conn, address):

    print("Client connected:", address[0])

    # Add client to list
    clients.append(conn)

    while True:
        try:
            message = conn.recv(1024).decode()

            if not message:
                break

            print(f"Client {address[0]}: {message}")

            # Send client's message to all clients
            broadcast(f"Client {address[0]}: {message}")

        except:
            break

    # Remove disconnected client
    if conn in clients:
        clients.remove(conn)

    conn.close()

    print("Client disconnected:", address[0])


# Accept multiple clients
def accept_clients():

    while True:

        conn, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, address)
        )

        thread.daemon = True
        thread.start()


# Start accepting clients in background
threading.Thread(
    target=accept_clients,
    daemon=True
).start()


# Server sends message to ALL clients
while True:

    message = input("Server: ")

    if message.lower() == "exit":
        break

    broadcast("Server: " + message)


# Close server
server.close()












# import socket
# import threading
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("10.110.36.241", 5000))
# server.listen(5)
# print("Server is waiting for clients...")

# def handle_client(conn, address):
#     print("Client connected:", address[0])
#     # Receive messages from this client
#     def receive_messages():
#         while True:
#             try:
#                 message = conn.recv(1024).decode()
#                 if not message:
#                     print("Client disconnected:", address[0])
#                     break
#                 print(f"\nClient {address[0]}: {message}")
#             except:
#                 break
#         conn.close()

#     # Start receiving in background
#     thread = threading.Thread(target=receive_messages)
#     thread.daemon = True
#     thread.start()

#     # Send messages to this client
#     while True:
#         try:
#             message = input(f"You → {address[0]}: ")
#             if message.lower() == "exit":
#                 break
#             conn.send(message.encode())
#         except:
#             break
#     conn.close()
    
# # Accept multiple clients
# while True:
#     conn, address = server.accept()
#     thread = threading.Thread(
#         target=handle_client,
#         args=(conn, address)
#     )
#     thread.daemon = True
#     thread.start()
#     print("Waiting for another client...")