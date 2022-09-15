import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55555
users = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

lock = threading.Lock()


def ping(nickname, sender):
    try:
        sender_client = users[sender]
        receiver_client = users[nickname]
        with lock:
            if nickname == sender:
                sender_client.send("Why?".encode('ascii'))
            else:
                receiver_client.send(f'PING From {sender}'.encode('ascii'))
                sender_client.send(f'PINGED {nickname}'.encode('ascii'))
    except:
        with lock:
            sender_client.send(f'404'.encode('ascii'))


def handle(client):
    while True:
        try:
            sender = {v: k for k, v in users.items()}[client]
            nick = client.recv(16).decode()
            ping(nick, sender)
        except:
            users.pop(sender)
            client.close()
            break


def receive():
    while True:
        client, address = server.accept()
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        users.update({nickname: client})
        client.send('OK'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
