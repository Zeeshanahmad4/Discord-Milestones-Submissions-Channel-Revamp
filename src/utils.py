import random
import string

def generate_random_string(length=10):
    """
    Generates a random string of alphanumeric characters.
    :param length: Length of the generated string (default is 10).
    :return: The randomly generated string.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def format_currency(amount):
    """
    Formats a currency amount with appropriate symbols and formatting.
    :param amount: The amount of currency to format.
    :return: The formatted currency string.
    """
    return f"${amount:.2f}"
