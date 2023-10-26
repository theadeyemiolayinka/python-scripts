def is_harshad(num):
    sum_digits = sum(int(digit) for digit in str(num))
    return num % sum_digits == 0

result = is_harshad(18)
print("Is 18 a Harshad number?", result)
