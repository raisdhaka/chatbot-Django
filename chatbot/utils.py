# chatbot/utils.py
import json

def get_chatbot_data(json_file=None):    
    with open(json_file, 'r') as f:
        return json.load(f)
    
