import os
import mysql.connector
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()

## importing project's package
from app.Database.db import get_db_connection


def get_allcustomer():
    print(f"Getting customer")

    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        if connection is None:
            return None
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                customer_id,
                customer_name,
                phone,
                email
            FROM customer
        """

        cursor.execute(query)

        customers = cursor.fetchall()

        return customers

    except Exception as error:
        print(f"Error fetching customer: {error}")
        return None

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

def get_allcustomers():
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
