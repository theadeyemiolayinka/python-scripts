import pyjokes

def generate_joke():
    joke = pyjokes.get_joke()
    return joke

def main():
    print("Welcome to the Joke Generator!")
    while True:
        input("Press Enter for a joke...")
        joke = generate_joke()
        print(joke)
        user_input = input("Do you want another joke? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
