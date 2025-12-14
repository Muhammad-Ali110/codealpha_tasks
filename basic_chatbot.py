import random
import datetime

def get_bot_response(user_input):
    """
    This program of mine will Analyze user input and return a predefined response.
    it Includes normalization to handle case-insensitivity.
    """
    normalized_input = user_input.strip().lower()

    
    if "hello" in normalized_input or "hi" in normalized_input:
        return "Hi! How can I help you today?"
    
    elif "how are you" in normalized_input:
        return "I'm fine, thanks! Just a computer program doing my job. How are you?"
    
    elif "your name" in normalized_input or "who are you" in normalized_input:
        return "I am a simple Chatbot created by a CodeAlpha Intern."
    
    elif "time" in normalized_input:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    elif "bye" in normalized_input or "goodbye" in normalized_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that. Try saying 'Hello', 'How are you', or 'Bye'."

def run_chatbot():
    """
    Main loop for the chatbot.
    """
    print("💬 Simple Chatbot (Type 'bye' to exit)")
    print("-" * 40)
    
    while True:
        try:
            user_text = input("You: ")
            
            if not user_text:
                continue
            
            response = get_bot_response(user_text)
            print(f"Bot: {response}")
            
            if "bye" in user_text.lower() or "goodbye" in user_text.lower():
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Exiting... Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()