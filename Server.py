# import argparse
import socket
import sys 
# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = int(sys.argv[1])

# bind the socket to a public host and port
server_socket.bind((host, port))

# listen for incoming connections
server_socket.listen(1)

# wait for a connection
print('Server listening on {}:{}'.format(host, port))
client_socket, addr = server_socket.accept()
print('Connected by', addr)

# receive data from the client and modify it
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    modified_data = data.decode().swapcase()
    client_socket.send(modified_data.encode())

# close the connection
client_socket.close()

# parser = argparse.ArgumentParser(description="""This is a very basic client program""")
# parser.add_argument('-f', type=str, help='This is the source file for the strings to reverse', default='source_strings.txt', action='store', dest='in_file')
# parser.add_argument('-o', type=str, help='This is the destination file for the reversed strings', default='results.txt', action='store', dest='out_file')
# parser.add_argument('server_location', type=str, help='This is the domain name or ip address of the server', action='store')
# parser.add_argument('port', type=int, help='This is the port to connect to the server on', action='store')
# args = parser.parse_args()

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = (args.server_location, args.port)
# server_socket.bind(server_address)
# server_socket.listen(1)

# # Accept incoming connections
# client_socket, client_address = server_socket.accept()

# # Receive data from the client and send back the modified string
# with open(args.out_file, 'wb') as write_file:
#     for line in open(args.in_file, 'rb'):
#         data = line.strip()
#         modified_data = data.decode().swapcase()
#         client_socket.sendall(modified_data.encode())
#         answer = client_socket.recv(512)
#         write_file.write(answer)

# # Close the connection
# client_socket.close()
# server_socket.close()