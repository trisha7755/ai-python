# Simple Text-Based AI Chatbot

def chatbot_response(user_input):
    # Dictionary of predefined responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm an AI chatbot, so I don't have feelings, but thank you for asking!",
        "what is your name": "I'm a simple AI chatbot. What's your name?",
        "bye": "Goodbye! Have a great day!",
    }
    
    # Convert user input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Check if the user input is in the predefined responses
    if user_input in responses:
        return responses[user_input]
    else:
        # Default response for unrecognized input
        return "I'm not sure I understand. Can you please rephrase?"

# Main loop to interact with the chatbot
def main():
    print("Welcome to the Simple AI Chatbot! Type 'bye' to exit.")
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    main()
