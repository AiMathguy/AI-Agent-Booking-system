import mysql.connector
from mysql.connector import Error
from datetime import datetime

# 📦 Function to create a booking
def create_booking(name, email, date_time,service,price):
    try:
        # Connect to MySQL
        # You would need to replace these with the actual data but for security purposes lets rather not and keep it as dummy info
        conn = mysql.connector.connect(
            host="localhost",
            user="secrets",
            password="topsecret", 
            database="booking_db" 
        )
        cursor = conn.cursor()

        # Insert booking into DB
        insert_query = """
            INSERT INTO Bookings (customer_name, email, booking_time,service)
            VALUES (%s, %s, %s,%s)
        """
        cursor.execute(insert_query, (name, email, date_time,service,price))
        conn.commit()

        booking_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return booking_id

    except Error as e:
        print(f"MySQL error: {e}")
        return None
def track_booking():
    pass
def cancel_booking():
    pass
