def generate_palindromes(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return palindromes

result = generate_palindromes(100, 200)
print("Palindromes between 100 and 200:", result)
