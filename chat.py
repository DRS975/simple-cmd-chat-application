import threading
import socket
import sys

# function to receive messages from the other user
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            break

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the local IP address and choose a port number
host = socket.gethostbyname(socket.gethostname())
port = 5000

# connect to the other user
sock.connect(('localhost', port))
print('Connected to the chat server')

# start a new thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(sock,))
receive_thread.start()

# send messages to the other user
while True:
    message = input()
    if message == 'quit':
        sock.close()
        sys.exit()
    sock.send(message.encode())
