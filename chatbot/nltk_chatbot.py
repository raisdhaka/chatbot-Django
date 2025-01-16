import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for pattern-response
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm fine, thank you. How can I help you?"]),
    (r"what is your name?", ["I'm a chatbot created with NLTK."]),
    (r"quit", ["Bye! Take care."]),
    (r"(.*)", ["Sorry, I don't understand that."])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)
