from flask import Flask, render_template, request, jsonify
import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load medical knowledge base
with open('medical_kb.json', 'r') as f:
    medical_kb = json.load(f)

def process_user_input(user_input):
    # Tokenize and clean user input
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Simple keyword matching
    response = "I'm sorry, I don't understand. Could you please rephrase that?"
    
    for item in medical_kb['responses']:
        if any(keyword in tokens for keyword in item['keywords']):
            response = item['response']
            break
            
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = process_user_input(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True) 