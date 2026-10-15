import socket

SERVER_PORT = 5050
BUFFER_SIZE = 16
ENCODING = 'utf-8'
DISCONNECT_SIGNAL = "False"

server_hostname = socket.gethostname()
server_ip = socket.gethostbyname(server_hostname)

print(f"Server Hostname: {server_hostname}")
print(f"Server IP Address: {server_ip}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, SERVER_PORT))
server_socket.listen()

print(f"Server is running and listening on {server_ip}:{SERVER_PORT}")

connection, client_address = server_socket.accept()
print(f"Conection established with client: {client_address}")

connected = True
while connected:

    raw_msg_length = connection.recv(BUFFER_SIZE).decode(ENCODING)

    if raw_msg_length:
       msg_length = int(raw_msg_length.strip())

       message = connection.recv(msg_length).decode(ENCODING)

       if message == DISCONNECT_SIGNAL:
          connection.send("Goodbye!".encode(ENCODING))
          print("Client requeste disconnect. Closing connection.")
          connected = False

       else:
          print(f"Client info received -> {message}")
          connection.send("Server received your info".encode(ENCODING))

    else:
        connected = False

connection.close()
server_socket.close()
print("Closed connection with client.")