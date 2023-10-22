import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "computer", "challenge", "learning"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord to guess: " + display_word(word_to_guess, guessed_letters))
        print("Attempts left: " + str(attempts))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print("Congratulations, you've guessed the word: " + word_to_guess)
                break
        else:
            print("Oops, that letter is not in the word.")
            attempts -= 1

    if attempts == 0:
        print("\nSorry, you're out of attempts. The word was: " + word_to_guess)

# Start the game
play_hangman()
