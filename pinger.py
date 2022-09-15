#!/usr/bin/python3
import socket
import sys
import threading


# '132.145.109.138' 8002
host = '127.0.0.1'
port = 55555

if len(sys.argv) == 1:
    print("use: ")

nickname = sys.argv[1]

if len(sys.argv) == 3:
    nick_for_ping = sys.argv[2]


def connecting():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    message = client.recv(16).decode('ascii')
    if message == 'NICK':
        client.send(nickname.encode('ascii'))

    message = client.recv(16).decode('ascii')
    if message == "OK":
        print("ok")
        write_thread.start()
    return client


def pinger():
    while True:
        try:
            message = client.recv(16).decode('ascii')
            if message[:4] == "PING":
                print(message)
                print("nick for ping:")
            elif message == "Why?":
                print(message)
                print("nick for ping:")
            elif message == "404":
                print(message)
                print("nick for ping:")
            else:
                print("unknown message: ", message)
                client.close()
                print("connection close")
                sys.exit(1)
        except:
            print("An error occured!")
            client.close()
            sys.exit(1)


def send_msg(message):
    client.send(message.encode('ascii'))


def write():
    while True:
        print("nick for ping:")
        message = input()
        send_msg(message)


write_thread = threading.Thread(target=write)
receive_thread = threading.Thread(target=pinger)
client = connecting()
receive_thread.start()
