import random
from datetime import datetime

# Define responses for different types of user inputs
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Nice to meet you!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!", "Take care!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!", "Don't mention it!"],
    "question": [
        "I'm not sure, but I can try to find out.",
        "That's a good question.",
        "Let me think about that.",
        "I'll need more information to answer that.",
        "That's an interesting question. Let's explore it together.",
        "Hmm, I'm not certain. Would you like me to look it up for you?",
        "I'm not an expert, but I'll do my best to help you.",
        "I'm glad you asked! Let's see if we can figure it out."
    ],
    "positive": ["That's great!", "Awesome!", "Fantastic!", "Wonderful!", "Excellent!"],
    "negative": ["I'm sorry to hear that.", "That must be tough.", "Hang in there.", "Things will get better.", "I'm here to listen."],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean.", "Can you provide more details?"]
}

# Define rules for different types of user inputs
rules = {
    "greeting": ["hello", "hi", "hey", "howdy"],
    "farewell": ["goodbye", "bye", "see you"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "question": ["what", "how", "why", "when", "where", "who"],
    "positive": ["good", "great", "awesome", "fantastic", "wonderful"],
    "negative": ["bad", "terrible", "awful", "horrible", "not good"],
}

def get_response(user_input):
    user_input = user_input.lower()
    response = None
    
    # Check for specific patterns in user input
    for intent, keywords in rules.items():
        for keyword in keywords:
            if keyword in user_input:
                response = generate_response(intent)
                break
    
    # If no specific pattern matches, return a default response
    if response is None:
        response = random.choice(responses["default"])
    
    return response

def generate_response(intent):
    if intent == "question":
        return random.choice(responses[intent])
    else:
        return random.choice(responses[intent])

# Main function to handle user interaction
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
