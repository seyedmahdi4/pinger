import socket
import threading

# Connection Data
host = '0.0.0.0'
port = 8002
users = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()


def ping(nickname, sender):
    try:
        sender_client = users[sender]
        receiver_client = users[nickname]
        if nickname == sender:
            sender_client.send("Why?".encode('utf8'))
        else:
            receiver_client.send(f'PING From {sender}'.encode('utf8'))
            sender_client.send(f'PINGED {nickname}'.encode('utf8'))
    except:
        sender_client.send(f'404'.encode('utf8'))


def handle(client):
    while True:
        try:
            nick = client.recv(16).decode('utf8')
            if nick == "PING!":
                client.send('PONG!'.encode('utf8'))
                continue
            sender = {v: k for k, v in users.items()}[client]
            ping(nick[:17], sender)
        except:
            try:
                users.pop(sender)
            except:
                pass
            client.close()
            break


def receive():
    while True:
        try:
            client, address = server.accept()
            client.send('NICK'.encode('utf8'))
            nickname = client.recv(512).decode('utf8')
            users.update({nickname: client})
            client.send('OK'.encode('utf8'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except:
            try:
                client.send('500'.encode('utf8'))
                client.close()
            except:
                client.close()


receive()
