import os
import mysql.connector
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


## importing project's package
from app.Backend.customer.service import get_allcustomer

def main():
    customers = get_allcustomer()

    print("Customer List")
    print("-" * 80)

    for customer in customers:
        print(
            f"ID: {customer['customer_id']}, "
            f"Name: {customer['customer_name']}, "
            f"Phone: {customer['phone']}, "
            f"Email: {customer['email']}"
        )


if __name__ == "__main__":
    main()