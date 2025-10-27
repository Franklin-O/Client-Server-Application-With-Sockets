from socket import *

server_name = '192.168.1.242'  # change to your server’s IP
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

message = input("Enter message to be capitalized: ")
client_socket.send(message.encode())

modified_message = client_socket.recv(2048).decode()
print("From server:", modified_message)

client_socket.close()
