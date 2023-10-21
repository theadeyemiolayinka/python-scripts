def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(letter in sentence.lower() for letter in alphabet)

result = is_pangram("The quick brown fox jumps over the lazy dog")
print("Is it a pangram?", result)
