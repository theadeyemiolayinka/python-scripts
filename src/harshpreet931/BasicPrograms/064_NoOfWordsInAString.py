def count_words(input_string):
    words = input_string.split()
    return len(words)

result = count_words("Hello, how are you?")
print("Number of words:", result)
