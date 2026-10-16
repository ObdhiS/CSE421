import socket
import threading

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

def count_vowels(text):
   vowels='aeiouAEIOU'
   return sum(ch in vowels for ch in text)

def handle_client(connection, client_address):
    """Runs in its own thread: talks to ONE client until it disconnects."""
    print(f"connection established with client: {client_address}")

    connected = True
    while connected:
    
           raw_msg_length = connection.recv(BUFFER_SIZE).decode(ENCODING)
    
           if raw_msg_length:
              msg_length = int(raw_msg_length.strip())
              message = connection.recv(msg_length).decode(ENCODING)
    
              if message == DISCONNECT_SIGNAL:
                  connection.send("Goodbye!".encode(ENCODING))
                  print(f"{client_address}Client requested disconnect.")
                  connected = False
    
              else:
                   print(f"[{client_address}]Received message: {message}")
    
                   vowel_count=count_vowels(message)
                   print(f"[{client_address}] Vowels counted: {vowel_count}")
    
                   if vowel_count == 0:
                       reply = "Not enough vowels"
                   elif vowel_count<=2:
                       reply = "Enough vowels I guess"
                   else:
                       reply = "Too many vowels"
    
    
    
                   connection.send(reply.encode(ENCODING))
    
           else:
                
                 connected = False

    connection.close()
    print("Closed connection with client. \n")

    


while True: 
    connection, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()
    print(f"Active connections: {threading.active_count() - 1}")

    

    