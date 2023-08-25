import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #ip address
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'End'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server Listening')
conn, addr = server.accept()

connection = True
while connection:
    message_length = conn.recv(HEADER)
    if message_length:
        message_length = int(message_length)
        message = conn.recv(message_length).decode(FORMAT)
        if message == DISCONNECT_MESSAGE:
            connection = False
            conn.send('Disconnecting.'.encode(FORMAT))
        else:
            print(message)
            conn.send('Message Received.'.encode(FORMAT))

conn.close()