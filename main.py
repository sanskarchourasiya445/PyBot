# PYBOT – RULE BASED PYTHON CHATBOT

import datetime

# Greet user based on time
def greet_user():
    user_name = input("Swagat hai! Enter your name: ")
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        print(f"Good Morning, {user_name}")
    elif 12 <= current_hour < 17:
        print(f"Good Afternoon, {user_name}")
    elif 17 <= current_hour < 21:
        print(f"Good Evening, {user_name}")
    else:
        print(f"Good Night, {user_name}")

    print("\n🤖 Namaste! Welcome to PyBot")
    print("PyBot is ready to help you. Type 'bye' to exit.\n")

# PyBot knowledge base
pybot_responses = {
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hi there 😊",
    "hey": "Hey! What’s up?",
    
    # Small talk
    "how are you": "I am doing great. Thanks for asking!",
    "what's up": "Just waiting to help you 😄",
    "how is life": "Life is all about learning and growing!",
    
    # Identity
    "who are you": "I am a simple rule-based AI chatbot 🤖",
    "what is your name": "You can call me PythonBot",
    "are you human": "No, I am a program written in Python 🐍",
    
    # Motivation
    "motivate me": "Keep going! Every small step matters 💪",
    "i am tired": "Rest a little, then come back stronger!",
    "i feel sad": "Hard times make strong people. You got this ❤️",
    
    # Programming related
    "what is python": "Python is a powerful and beginner-friendly programming language.",
    "why learn python": "Python is easy, versatile, and used in AI, web, data science.",
    "what is function": "A function is a reusable block of code that performs a task.",
    "what is list": "A list stores multiple values in a single variable.",
    "what is dictionary": "A dictionary stores data in key-value pairs.",
    "functions kya hote hai": "Functions reusable code blocks hote hain. Chapter 7 padho 📘",
    
    # Mood
    "happy": "Nice! Keep smiling 😊",
    "bored": "Try learning something new or take a short break!",
    
    # Thanks
    "thank you": "You're welcome!",
    "thanks": "Anytime 😊",
    
    # Exit
    "bye": "Goodbye! See you again 👋"
}


# Get PyBot response
def get_pybot_response(user_message):
    user_message = user_message.lower()

    for key in pybot_responses:
        if key in user_message:
            return pybot_responses[key]

    return "PyBot is still learning this. I will improve soon 🙂"

# Start chat
def start_pybot():
    while True:
        user_input = input("You: ")

        response = get_pybot_response(user_input)
        print("PyBot:", response)

        if "bye" in user_input.lower():
            break

# Program start
greet_user()
start_pybot()
