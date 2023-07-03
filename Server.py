import socket
import sys 
#creating the socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#getting the local machine name
host = socket.gethostname()

#setting the port number
port = int(sys.argv[1])

#binding the socket to the public host and port
server_socket.bind((host, port))

#listening for incoming connections
server_socket.listen(1)

#waiting for the connection
print('Server listening on {}:{}'.format(host, port))
client_socket, addr = server_socket.accept()
print('Connected by', addr)

#receiving the data from the client and modifying it
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    modified_data = data.decode().swapcase()
    client_socket.send(modified_data.encode())

client_socket.close()

