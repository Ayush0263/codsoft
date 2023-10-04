# WAP to make password generator.
import string
import secrets


def generate_strong_password(length=12):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use secrets module to securely generate a password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))

    if password_length < 8:
        print("Password length should be at least 8 characters for security.")
    else:
        password = generate_strong_password(password_length)
        print("Generated Strong Password:", password)
