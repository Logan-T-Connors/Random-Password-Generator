import random
import string


def generate_password(length=12, include_digits=True, include_special_chars=True):
# Define character sets
    letters = string.ascii_letters
    digits = string.digits if include_digits else ""
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" if include_special_chars else ""

# Combine character sets based on user preferences
    characters = f"{letters}{digits}{special_chars}"

# Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# User input for password customization
password_length = int(input("Enter password length: "))
include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes' or 'y' or 'Yes' or 'YES' or 'Y'
include_special_characters = input("Include special characters? (yes/no): ").lower() == 'yes' or 'y' or 'Yes' or 'YES' or 'Y'

# Generate password
generated_password = generate_password(
    password_length,
    include_numbers,
    include_special_characters
)

print(f"Generated Password: {generated_password}")
