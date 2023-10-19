def count_occurrences(input_string, char):
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count

result = count_occurrences("Hello, World!", "l")
print("Occurrences of 'l':", result)
