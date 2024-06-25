import json
import os
from flask import Blueprint, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

chatbot_bp = Blueprint('chatbot', __name__)

# Get the path to the Flask application's root directory
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Construct the full path to the responses.json file
responses_file = os.path.join(project_dir, "static", "responses.json")

# Load the responses JSON file
with open(responses_file, "r", encoding="utf-8") as f:
    responses_data = json.load(f)
responses = responses_data.get("responses", [])  # Get the list of responses, or an empty list if not found

# Initialize the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Preprocess the responses and create a TF-IDF matrix
response_texts = [r.get("question", "") for r in responses]  # Use empty string if "question" key is missing
tfidf_matrix = vectorizer.fit_transform(response_texts)

# Function to find the best response using TF-IDF
def find_best_response(user_input):
    # Convert user input to TF-IDF vector
    user_input_vector = vectorizer.transform([user_input])
    # Calculate cosine similarity between user input and responses
    similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    # Get the index of the most similar response
    best_response_index = similarities.argmax()
    # Return the corresponding response
    return responses[best_response_index]

# Flask route to handle chatbot requests
@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['userInput']
    best_response = find_best_response(user_input)
    return jsonify(best_response)
