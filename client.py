import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #ip address
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'End'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(message):
    try:
        message = message.encode(FORMAT)
        message_length = len(message)
        send_length = str(message_length).encode(FORMAT)
        send_length += b'' * (HEADER - len(send_length))

        client.send(send_length)
        client.send(message)

        print(client.recv(2048).decode(FORMAT))
    except Exception as e:
        print("An error occurred:", e)
