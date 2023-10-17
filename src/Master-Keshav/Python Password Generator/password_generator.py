import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        print("Generated Password: ", password)
        user_input = input("Do you want another password? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
