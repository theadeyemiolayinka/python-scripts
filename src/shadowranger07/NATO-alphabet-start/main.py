import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
a = {row.letter:row.code for (index, row) in data.iterrows()}
print(a)
list
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def todo():
    try:
        user_input = input("enter a word:").upper()
        result = [a[letter] for letter in user_input]
        print(result)
    except KeyError:
        print("sorry only letters are allowed")
        exception_on = True
        while exception_on:
            todo()


todo()