import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.90", 5000))

server.listen(5)

print("Server is waiting for client...")

conn, address = server.accept()

print("Client connected!")
print("Client IP:", address[0])

# Function to receive messages
def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode()

            if not message:
                print("Client disconnected.")
                break

            print("\nClient:", message)

        except:
            break

# Start receiving messages in background
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

# Server sends messages
while True:
    message = input("You: ")
    if message.lower() == "exit":
        conn.send("exit".encode())
        break
    conn.send(message.encode())

conn.close()
server.close()