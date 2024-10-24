

print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("Chatbot: BYE!")
        break
    elif 'hello' in user_input.lower():
        print("Chatbot: Hello there!")
    elif 'how are you' in user_input.lower():
        print("Chatbot:  I'm doing fine! How about you?")
    elif 'name' in user_input.lower():
        print("Chatbot: I have no name.")
    else:
        print("Chatbot: I do not how to respond to that.")

print("Chatbot session is finished.")
