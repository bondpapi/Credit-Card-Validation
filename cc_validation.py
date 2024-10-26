import re


def is_valid_credit_card(card):
    """Check if the card matches the pattern: starts with 4, 5, or 6; exactly 16 digits or groups of 4 separated by '-'"""
    if not re.match(r"^[456]\d{3}(-?\d{4}){3}$", card):
        return "Invalid"

    # Remove hyphens if present
    card_number = card.replace("-", "")

    # Check for consecutive repeated digits (four or more)
    if re.search(r"(\d)\1{3,}", card_number):
        return "Invalid"

    return "Valid"


# Input handling
N = int(input("Enter the number of credit card numbers to validate: "))
for _ in range(N):
    card = input("Enter credit card number: ").strip()
    print(is_valid_credit_card(card))
