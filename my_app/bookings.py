import sqlite3
import os

# Get the path to the Flask app directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the bookings.db file
DATABASE = os.path.join(project_dir, 'flask_app', 'bookings.db')

# Connect to the SQLite database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

def view_bookings():
    try:
        # Fetch data from the bookings table
        cursor.execute('SELECT * FROM bookings')
        rows = cursor.fetchall()

        # Check if the table is empty
        if not rows:
            print("The 'bookings' table is empty.")
        else:
            # Print the data
            for row in rows:
                print(row)

    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")

def delete_booking(id):
    try:
        # Delete a row from the bookings table based on the provided id
        cursor.execute('DELETE FROM bookings WHERE id = ?', (id,))
        conn.commit()
        print(f"Booking with id {id} has been deleted.")

    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")

# View all bookings
view_bookings()

# Uncomment the following lines to enable the deletion functionality
# booking_id = input("Enter the id of the booking to delete (or 'q' to quit): ")
#
# while booking_id.lower() != 'q':
#     try:
#         delete_booking(int(booking_id))
#     except ValueError:
#         print("Invalid input. Please enter a valid integer or 'q' to quit.")
#
#     booking_id = input("Enter the id of the booking to delete (or 'q' to quit): ")

# Close the database connection
conn.close()