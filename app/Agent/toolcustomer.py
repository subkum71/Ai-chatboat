## Convert all our functions in tool
from langchain.tools import tool

from app.Backend.customer.service import get_customer


@tool
def get_customer_by_phone(phone: str) -> list:
    """
    Fetch customer information using the customer's phone number.

    The phone number may have been provided in an earlier
    conversation turn. If the user refers to 'him', 'her',
    'this customer', etc., use the phone number of the
    previously identified customer.

    Args:
        phone_number: Customer's phone number.

    Returns:
        Customer records matching the phone number.
    """
    return get_customer(phone)