import nltk
from nltk.chat.util import Chat, reflections

from .utils import get_chatbot_data

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
    data = get_chatbot_data('responses.json')
    short_text = next((q for q in data["questions"] if q["short_text"] == user_input), None)
    if short_text:
        return short_text["response"]
    else:
        return chatbot.respond(user_input)
