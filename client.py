import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55556))



def receive():
    while True:
        try:
            message = client.recv(16).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message[:4] == "PING":
                yaro = message.split(" ")[1]
                print(f"server: PING From {yaro}\n")
            elif message == "OK":
                print("ok")
                write_thread.start()
            else:
                print("chert omad : ", message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input('nick for ping:\n'))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)

