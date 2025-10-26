from socket import *

server_name = '192.168.1.242'  # Replace with the server’s LAN IP
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("Enter message (or 'quit' to exit): ")
    if message.lower() == 'quit':
        break
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, _ = client_socket.recvfrom(2048)
    print("From server:", modified_message.decode())

client_socket.close()
