import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data.get("content")
        author = quote_data.get("author")
        return f'"{quote}" - {author}'
    return None

def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        input("Press Enter for a random quote...")
        quote = get_random_quote()
        if quote:
            print(quote)
        else:
            print("Failed to fetch a quote. Please try again later.")
        user_input = input("Do you want another quote? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
