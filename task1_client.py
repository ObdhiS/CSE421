import socket

SERVER_PORT = 5050
BUFFER_SIZE = 16
ENCODING = 'utf-8'
DISCONNECT_SIGNAL = "False"

client_hostname = socket.gethostname()
client_ip = socket.gethostbyname(client_hostname)

print(f"Server Hostname: {client_hostname}")
print(f"Server IP Address: {client_ip}")


SERVER_IP = client_ip
server_address = (SERVER_IP,SERVER_PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

def send_message(message):
    encoded_message = message.encode(ENCODING)

    message_length= str(len(encoded_message)).encode(ENCODING)
    padded_length = message_length + b' ' * (BUFFER_SIZE - len(message_length))


    client_socket.send(padded_length)
    client_socket.send(encoded_message)

    response = client_socket.recv(2048).decode(ENCODING)
    print(f"Server response: {response}")


intro_message = f"client IP: {client_ip}, Client Name: {client_hostname}"
send_message(intro_message)


send_message(DISCONNECT_SIGNAL)
client_socket.close()
print("Disconneted from server")