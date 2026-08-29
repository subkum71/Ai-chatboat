import os
import mysql.connector
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


## importing project's package
from app.Database.db import get_db_connection

def get_customers():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
            SELECT customer_id, phone, customer_name
            FROM customer
            LIMIT 10;
        """

        cursor.execute(query)

        customers = cursor.fetchall()

        for customer in customers:
            print(customer)

        return customers

    except Exception as e:
        print(f"Database error: {e}")
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    get_customers()