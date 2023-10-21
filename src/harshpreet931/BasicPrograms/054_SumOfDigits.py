def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

result = sum_of_digits(12345)
print("Sum of digits:", result)
