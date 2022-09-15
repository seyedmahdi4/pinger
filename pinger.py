#!/usr/bin/python3
import socket
import sys
import threading
from notifypy import Notify

host = '132.145.109.138'
port = 8002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def notif(msg):
    notification = Notify()
    notification.title = "pinger"
    notification.message = msg
    notification.audio = "notif.wav"
    notification.icon = "bell.png"
    notification.send()


def connect(nickname):
    client.connect((host, port))

    message = client.recv(16).decode('ascii')
    if message == 'NICK':
        client.send(nickname.encode('ascii'))

    message = client.recv(16).decode('ascii')
    if message == "OK":
        if __name__ == "__main__":
            write_thread.start()
    return client


def pinger():
    # A function for receive data from server

    while True:
        try:
            message = client.recv(16).decode('ascii')

            # When you pinged
            if message[:5] == "PING ":
                print(message)
                notif(message)
                print("nick for ping:")

            # When ping your frined
            elif message[:6] == "PINGED":
                print(message)

            # When ping yourself !!
            elif message == "Why?":
                print(message)
                print("nick for ping:")

            # When nickname notfound !
            elif message == "404":
                print(message)
                print("nick for ping:")
            
            # for debug :)
            else:
                print("unknown message: ", message)
                client.close()
                print("connection close")
                sys.exit(1)

        except Exception as e:
            print("An error occured!")
            print(e)
            client.close()
            sys.exit(1)


def send_nick(nick):
    # A function for send nickname for sevrer
    client.send(nick.encode('ascii'))


def write():
    # A function for get input
    while True:
        print("nick for ping:")
        nick = input()
        send_nick(nick)


if __name__ == "__main__":
    # Check args
    if len(sys.argv) == 1:
        print("use: ./pinger YOUR_NICKNAME")
        sys.exit(1)
    nickname = sys.argv[1]

    # Thread definition
    write_thread = threading.Thread(target=write)
    receive_thread = threading.Thread(target=pinger)

    # Connect to server
    client = connect(nickname)

    # Start ping receiver
    receive_thread.start()