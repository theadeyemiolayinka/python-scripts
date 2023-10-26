def is_neon(num):
    square = num ** 2
    sum_digits = sum(int(digit) for digit in str(square))
    return sum_digits == num

result = is_neon(9)
print("Is 9 a neon number?", result)
