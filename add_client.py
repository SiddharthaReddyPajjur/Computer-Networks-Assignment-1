import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

print("🟢 Connected to server on port 9999.")

while True:
    msg = input("Client (enter number or 'exit'): ")
    client_socket.send(msg.encode())
    if msg.lower() == 'exit':
        break

    reply = client_socket.recv(1024).decode()
    print(f"Server: {reply}")

    # Try to compute sum if both are integers
    try:
        client_num = int(msg)
        server_num = int(reply)
        total = client_num + server_num
        print(f"🔢 Sum: {client_num} + {server_num} = {total}")
    except ValueError:
        print("⚠️ One of the values is not an integer. Skipping sum.")

client_socket.close()
print("❌ Disconnected from server.")
