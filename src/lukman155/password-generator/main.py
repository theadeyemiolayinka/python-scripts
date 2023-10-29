import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets based on user preferences
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "Password cannot be generated with no character set selected."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the password length: "))
        use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Use digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a positive integer for the password length.")
