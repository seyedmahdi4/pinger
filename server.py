import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55556

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

lock = threading.Lock()

users= {}

def ping(nickname,yaro):
    try:
        client = users[nickname]
        with lock:
            client.send(f'PING {yaro}'.encode('ascii'))
    except:
        pass
        #with lock:
        #client.send(f'KEZB NICK'.encode('ascii'))
        #print("kezb")

def handle(client):
    while True:
        try:
            nick = client.recv(16)
            yaro ,nick = nick.decode().split(": ")
            ping(nick,yaro)
        except:
            # remove nick az dic
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        users.update({nickname:client})
        client.send('OK'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()