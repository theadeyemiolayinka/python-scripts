def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

result = is_palindrome_number(121)
print("Is 121 a palindrome number?", result)
