#!/usr/bin/python3
import sys
import threading
from pinger import connecting, send_msg, notif
from tkinter import Tk, Label, Text, Button, END, mainloop


connected = 0
root = Tk()
root.geometry("200x145")
root.title(" Pinger ")

client = None


def pinger():
    while True:
        try:
            message = client.recv(16).decode('ascii')
            if message[:5] == "PING ":
                Output.config(text=message)
                notif(message)
            elif message[:6] == "PINGED":
                Output.config(text=message)
            elif message == "Why?":
                Output.config(text=message)
            elif message == "404":
                Output.config(text=message)
            else:
                print("unknown message: ", message)
                client.close()
                print("connection close")
                sys.exit(1)
        except:
            print("An error occured!")
            client.close()
            sys.exit(1)


def Take_input():
    global client, connected
    INPUT = inputtxt.get("1.0", "end-1c").strip()
    if INPUT == '':
        return 0
    if not connected:
        client = connecting(INPUT)
        Output.config(text=f"Connect with {INPUT}")
        l.config(text="Nick for Ping:")
        Display.config(text="Ping!")
        connected = 1
        receive_thread.start()
    else:
        send_msg(INPUT)
    inputtxt.delete('1.0', END)


l = Label(text="Your nickname?", font=('Times New Roman', 15, 'bold'))

inputtxt = Text(root, height=1,
                width=15,
                font=('Times New Roman', 16))

Display = Button(root, height=1,
                 width=13,
                 text="start",
                 command=lambda: Take_input(),
                 font=('Times New Roman', 17))

Output = Label(text="")
inputtxt.bind('<Return>', lambda _: Take_input())
l.pack(padx=4, pady=4)
inputtxt.pack(padx=4, pady=4)
Display.pack(padx=4, pady=4)
Output.pack(padx=4, pady=4)

receive_thread = threading.Thread(target=pinger)

mainloop()
