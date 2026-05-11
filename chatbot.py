import json
import random

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


def get_response(user_input):
    global user_name

    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}!"

    elif any(word in user_input for word in responses["greeting"]):
        return random.choice(greeting_responses)

    elif any(word in user_input for word in responses["how_are_you"]):
        return random.choice(how_are_you_responses)

    elif any(word in user_input for word in responses["bye"]):
        return "Goodbye!"

    elif "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name}."
        else:
            return "I don't know your name yet."

    else:
        return "Sorry, I don't understand that."


print("Chatbot started! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    response = get_response(user_input)

    print("Bot:", response)

    if response == "Goodbye!":
        break