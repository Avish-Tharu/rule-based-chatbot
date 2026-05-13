import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

user_name = ""

greeting_responses = [
    "Hello!",
    "Hi there!",
    "Hey!"
]

how_are_you_responses = [
    "I'm doing great!",
    "I'm fine, thanks!",
    "Doing well!"
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer get cold? Because it forgot to close Windows!",
    "Why was the Python developer calm? Because they handled exceptions well!"
]


def get_response(user_input):
    global user_name

    user_input = user_input.lower()

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name}."
        else:
            return "I don't know your name yet."

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(greeting_responses)

    elif "how are you" in user_input:
        return random.choice(how_are_you_responses)

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"

    elif "favorite color" in user_input:
        return "My favorite color is blue!"

    elif "help" in user_input:
        return (
            "Try:\n"
            "- hello\n"
            "- my name is Tharushi\n"
            "- what is my name\n"
            "- tell me a joke\n"
            "- time\n"
            "- thank you\n"
            "- favorite color\n"
            "- bye"
        )

    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


def send_message():
    user_input = user_entry.get()

    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, f"You: {user_input}\n")

    response = get_response(user_input)

    chat_area.insert(tk.END, f"Bot: {response}\n\n")

    user_entry.delete(0, tk.END)

    chat_area.yview(tk.END)

    if response == "Goodbye!":
        window.after(1000, window.destroy)


window = tk.Tk()
window.title("Rule-Based Chatbot")
window.geometry("500x500")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_entry = tk.Entry(window, font=("Arial", 14))
user_entry.pack(padx=10, pady=10, fill=tk.X)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()