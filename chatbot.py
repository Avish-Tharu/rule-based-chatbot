import json

with open("responses.json", "r") as file:
    responses = json.load(file)

print("Chatbot started! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if any(word in user_input for word in responses["greeting"]):
        print("Bot: Hello! 👋")

    elif any(word in user_input for word in responses["how_are_you"]):
        print("Bot: I'm doing great! How about you?")

    elif any(word in user_input for word in responses["bye"]):
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")