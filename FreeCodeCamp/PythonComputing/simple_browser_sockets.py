import socket

# AF_INET means make a socket that goes across the internet
# SOCK_STREAM means that its a stream socket: which means,
# it's a series of chars that come one after another,
# rather than blocks of text
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect parameter is a tuple, which is the host, followed by the port
my_socket.connect(('data.pr4e.org', 80))

# get request, the protocol, two returns, and encode() prepares the data by turning the string into utf-8 bytes
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# send the command
my_socket.send(command)

while True:
    # receive the data 512 characters at a time in bytes
    data = my_socket.recv(512)

    # when there is no more characters to receive we will break the loop and then close socket
    if len(data) < 1:
        break
    # decode the bytes into utf-8 string
    print(data.decode(), end='')
my_socket.close()
