import os
from dotenv import load_dotenv
import mysql.connector

# Load variables from .env
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        return connection

    except mysql.connector.Error as error:
        print(f"Database connection error: {error}")
        return None