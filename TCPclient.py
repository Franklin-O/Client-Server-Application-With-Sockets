from socket import *

server_name = '192.168.1.242'  # Replace with your server’s LAN IP
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

while True:
    message = input("Enter message (or 'quit' to exit): ")
    client_socket.send(message.encode())

    if message.lower() == 'quit':
        print("Closing connection...")
        break

    modified_message = client_socket.recv(2048)
    print("From server:", modified_message.decode())

client_socket.close()