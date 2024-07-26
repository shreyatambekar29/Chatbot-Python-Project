import socket
import threading
from tkinter import *
from tkinter import scrolledtext


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            chat_area.config(state=NORMAL)
            chat_area.insert(END, message + "\n")
            chat_area.config(state=DISABLED)
            chat_area.yview(END)
        except:
            break


def send():
    message = entry.get()
    chat_area.config(state=NORMAL)
    chat_area.insert(END, "You: " + message + "\n")
    chat_area.config(state=DISABLED)
    chat_area.yview(END)
    client_socket.send(message.encode("utf-8"))
    entry.delete(0, END)
    # Simulate a bot reply
    simulate_bot_reply(message)


def simulate_bot_reply(user_message):
    # Simple bot response logic
    user_message = user_message.lower()
    if "hello" in user_message or "hi" in user_message:
        bot_message = "Bot: Hi there! How can I assist you today?"
    elif "how are you" in user_message:
        bot_message = "Bot: I'm just a bot, but I'm doing great! Thanks for asking."
    elif "bye" in user_message:
        bot_message = "Bot: Goodbye! Have a great day!"
    elif "help" in user_message:
        bot_message = "Bot: Sure, I'm here to help! What do you need assistance with?"
    elif "time" in user_message:
        from datetime import datetime

        now = datetime.now()
        bot_message = f"Bot: The current time is {now.strftime('%H:%M:%S')}."
    else:
        bot_message = "Bot: Sorry, I didn't understand that."

    chat_area.config(state=NORMAL)
    chat_area.insert(END, bot_message + "\n")
    chat_area.config(state=DISABLED)
    chat_area.yview(END)


# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5555))

# Set up the GUI
root = Tk()
root.title("Chat Application")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

chat_area = scrolledtext.ScrolledText(root, wrap=WORD, bg="#e6e6e6", fg="#333333", font=("Arial", 10))
chat_area.pack(pady=10, padx=10)
chat_area.config(state=DISABLED)

entry_frame = Frame(root, bg="#f0f0f0")
entry_frame.pack(pady=5)

entry = Entry(entry_frame, width=30, font=("Arial", 12))
entry.pack(side=LEFT, padx=5)

send_button = Button(entry_frame, text="Send", command=send, bg="#4CAF50", fg="white", font=("Arial", 10))
send_button.pack(side=LEFT)

# Start the receive thread
threading.Thread(target=receive).start()

root.mainloop()
