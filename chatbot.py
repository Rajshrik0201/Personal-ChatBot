def get_user_input():
    return input("You: ")

def process_question(question):
    question = question.lower()  

    if "year" in question:
        return "This is 2023."
    elif "name" in question:
        return "My name is ChatBot."
    elif "how are you" in question:
        return "I'm just a computer program, but I'm here to help you!"
    elif "who created you" in question:  
        return "I was created by you."
    elif "tell me a joke" in question:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "good morning" in question:
        return "Good morning! How can I assist you today?"
    elif "hello" in question:
        return "Hello! How can I help you?"
    elif "food" in question:
        return "your data is my food."
    else:
        return "I'm sorry, I don't have an answer for that question."

while True:
    user_input = get_user_input()
    response = process_question(user_input.lower())  
    print("ChatBot:", response)
