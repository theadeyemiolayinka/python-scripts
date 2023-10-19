def is_palindrome(word):
    return word == word[::-1]

result = is_palindrome("racecar")
print("Is 'racecar' a palindrome?", result)
