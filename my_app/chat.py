from flask import Flask, jsonify, request
from fuzzywuzzy import fuzz  # Install using: pip install fuzzywuzzy

app = Flask(__name__)

# Load responses from JSON file
import json
with open('responses.json', 'r') as file:
    responses = json.load(file)['responses']

# Function to calculate similarity between two strings
def calculate_similarity(str1, str2):
    return fuzz.ratio(str1.lower(), str2.lower())  # Using simple ratio comparison

# Route to handle user queries
@app.route('/get_answer', methods=['POST'])
def get_answer():
    user_question = request.json['question']
    
    # Find the most similar question in the responses JSON
    max_similarity = -1
    best_answer = None
    for response in responses:
        similarity = calculate_similarity(user_question, response['question'])
        if similarity > max_similarity:
            max_similarity = similarity
            best_answer = response['answer']
    
    # Return the best answer
    return jsonify({'answer': best_answer})

if __name__ == '__main__':
    app.run(debug=True)
