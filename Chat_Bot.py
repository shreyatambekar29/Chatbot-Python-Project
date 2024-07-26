import socket
import threading
from tkinter import *

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            messages.insert(END, message)
        except:
            break

def send():
    message = entry.get()
    client_socket.send(message.encode('utf-8'))
    entry.delete(0, END)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

root = Tk()
root.title("Chat Application")

messages = Listbox(root)
messages.pack()

entry = Entry(root)
entry.pack()

send_button = Button(root, text="Send", command=send)
send_button.pack()

threading.Thread(target=receive).start()
root.mainloop()
