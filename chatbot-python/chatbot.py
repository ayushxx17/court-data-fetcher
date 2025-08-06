print("🤖 Hello! I'm AyushBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == 'hello':
        print("Bot: Hello! How can I help you?")
    elif user_input == 'how are you':
        print("Bot: I'm just a bot, but I'm doing great! 😄")
    elif user_input == 'your name':
        print("Bot: I'm AyushBot, your friendly assistant.")
    elif user_input == 'help':
        print("Bot: You can ask me things like 'hello', 'how are you', or 'bye'.")
    elif user_input == 'bye':
        print("Bot: Goodbye! Have a great day 👋")
        break
    else:
        print("Bot: Sorry, I didn't understand that. Try something else.")
