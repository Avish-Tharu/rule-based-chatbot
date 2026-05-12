import json
import random
from datetime import datetime

with open("responses.json", "r") as file:
    responses = json.load(file)

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

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name}."
        else:
            return "I don't know your name yet."

    elif any(word in user_input for word in responses["greeting"]):
        return random.choice(greeting_responses)

    elif any(word in user_input for word in responses["how_are_you"]):
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
            "You can try:\n"
            "- hello\n"
            "- my name is Tharushi\n"
            "- what is my name\n"
            "- tell me a joke\n"
            "- time\n"
            "- thank you\n"
            "- favorite color\n"
            "- bye"
        )

    elif any(word in user_input for word in responses["bye"]):
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


print("Chatbot started! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    response = get_response(user_input)

    print("Bot:", response)

    if response == "Goodbye!":
        break