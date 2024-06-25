from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import sqlite3
import json
from flask_app.chatbot.chatbot import chatbot_bp

app = Flask(__name__, static_folder='static', template_folder='flask_app/templates')

# Get the path to the Flask application's root directory
project_dir = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(project_dir, 'flask_app', 'bookings.db')

# Construct the full path to the responses.json file
responses_file = os.path.join(project_dir, "static", "responses.json")


with open(responses_file, "r", encoding="utf-8") as f:
    responses_data = json.load(f)
responses = responses_data["responses"]

def to_json(obj):
    return json.dumps(obj)


app.jinja_env.filters['tojson'] = to_json

# Create the bookings table if it doesn't exist
def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT, age INTEGER, mobile TEXT, email TEXT,
                   guests INTEGER, availability DATE, package TEXT, price REAL)''')
    conn.commit()
    conn.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def handle_booking():
    if request.method == 'POST':
        # Handle POST request (form submission)
        name = request.form['name']
        age = request.form['age']
        mobile = request.form.get('mobile', '')
        email = request.form.get('email', '')
        guests = request.form['guests']
        availability = request.form.get('availability', '')
        package = request.form['package']
        price = request.form['price']

        # Connect to the database and insert the booking data
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, age, mobile, email, guests, availability, package, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (name, age, mobile, email, guests, availability, package, price))
        conn.commit()
        conn.close()

        # Pass the success message to the template
        success_message = "Booking successful!"
        return render_template('booking.html', success_message=success_message)
    else:
        # Handle GET request (display the form)
        return render_template('booking.html')

@app.route('/gallery')
def render_gallery():
    return render_template('gallery.html')

@app.route('/package')
def render_package():
    return render_template('package.html')

@app.route('/destination')
def render_destination():
    booking_url = url_for('handle_booking', _external=True)
    print(f"booking_url: {booking_url}")
    return render_template('destination.html', responses=responses, booking_url=booking_url)

app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', debug=True)
