import requests
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Database connection parameters
db_params = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

# API endpoint
api_url = os.getenv("API_URL")

def fetch_api_data():
    """Fetch market trend data from the API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None

def connect_to_db():
    """Establish PostgreSQL connection."""
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def insert_data(connection, data):
    """Insert API data into PostgreSQL."""
    try:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO market_trends (trend_id, category, value, timestamp)
            VALUES (%s, %s, %s, %s)
        """
        for item in data:
            cursor.execute(insert_query, (
                item.get("trend_id"),
                item.get("category"),
                item.get("value"),
                datetime.now()
            ))
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
    finally:
        cursor.close()

def main():
    # Fetch data from API
    data = fetch_api_data()
    if not data:
        return

    # Connect to database
    connection = connect_to_db()
    if not connection:
        return

    # Insert data
    insert_data(connection, data)

    # Clean up
    connection.close()

if __name__ == "__main__":
    main()
