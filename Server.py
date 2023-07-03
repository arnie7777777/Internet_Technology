# import argparse
import socket
import sys 
# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get a local machine name
host = socket.gethostname()

#set the port number
port = int(sys.argv[1])

#bind the socket to a public host and port
server_socket.bind((host, port))

#listen for incoming connections
server_socket.listen(1)

#wait for a connection
print('Server listening on {}:{}'.format(host, port))
client_socket, addr = server_socket.accept()
print('Connected by', addr)

#receive data from the client and modify it
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    modified_data = data.decode().swapcase()
    client_socket.send(modified_data.encode())

# close the connection
client_socket.close()

