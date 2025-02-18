import secrets
import string

def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ""
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    return password

new_password = generate_password(8)
print(new_password)