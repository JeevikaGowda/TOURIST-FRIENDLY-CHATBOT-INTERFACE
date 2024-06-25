# Tourist-Friendly Chatbot Interface

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Code Breakdown](#code-breakdown)
8. [Database Management](#database-management)
9. [Note on Images](#note-on-images)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [License](#license)

## Project Overview

This project implements a tourist-friendly chatbot interface with a frontend website and a backend for handling bookings. The chatbot provides information about destinations and assists users in planning their trips.

## Features

- Home page
- Destination page with interactive chatbot
- Package page
- Gallery page
- Booking form with database storage

## Prerequisites

- Python 3.7+
- Flask
- SQLite3
- scikit-learn

## Installation

1. Clone the repository:
2. Install the required packages:
## Usage

1. Run the main application: python main.py
2. Open a web browser and navigate to `http://localhost:5000` to access the website.

3. To view or manage bookings, run: python bookings.py
## Project Structure

- `main.py`: Main Flask application file
- `flask_app/`: Directory containing Flask application files
- `templates/`: HTML templates for web pages
- `static/`: Static files (CSS, JavaScript, images)
- `bookings.db`: SQLite database for storing bookings
- `chatbot.py`: Chatbot implementation using TF-IDF and cosine similarity
- `bookings.py`: Script to view and manage bookings in the database

## Code Breakdown

### main.py

This is the main Flask application file. It sets up the routes for different pages, handles form submissions for bookings, and initializes the database.

Key components:
- Flask application setup
- Database initialization
- Route handlers for home, destination, package, gallery, and booking pages
- Integration with the chatbot blueprint

### chatbot.py

This file implements the chatbot functionality using TF-IDF vectorization and cosine similarity for finding the best response to user queries.

Key components:
- Loading responses from a JSON file
- TF-IDF vectorization of responses
- Function to find the best response based on user input
- Flask blueprint for handling chatbot requests

### bookings.py

This script allows viewing and managing bookings stored in the SQLite database.

Key components:
- Database connection
- Functions to view all bookings and delete specific bookings

## Database Management

The project uses SQLite for storing booking information. The database file is located at `flask_app/bookings.db`.

To view or manage bookings:
1. Run `python bookings.py`
2. Follow the prompts to view all bookings or delete specific bookings

## Note on Images

Not all images referenced in the source code have been uploaded to the repository. Make sure to add your own images to the appropriate directories or update the image paths in the HTML files.

## Troubleshooting

If you encounter any issues:
1. Ensure all prerequisites are installed correctly
2. Check that the database file exists and has the correct permissions
3. Verify that all file paths are correct for your system

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

