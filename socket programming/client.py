
import socket
import threading

# Function to receive messages
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message or message.lower() == "exit":
                print("\nServer disconnected.")
                break

            print("\nServer:", message)
        except OSError:
            break

    client.close()


# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("Connected to server!")

# Start receiving in a separate thread
threading.Thread(
    target=receive_messages,
    args=(client,),
    daemon=True
).start()

# Send messages continuously
while True:
    message = input("You: ")

    if message.lower() == "exit":
        client.sendall("exit".encode())
        break

    try:
        client.sendall(message.encode())
    except OSError:
        print("Connection closed.")
        break

client.close()