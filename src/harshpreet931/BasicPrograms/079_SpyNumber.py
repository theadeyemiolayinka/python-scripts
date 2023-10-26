def is_spy(num):
    digits = [int(digit) for digit in str(num)]
    product = 1
    sum_digits = sum(digits)

    for digit in digits:
        product *= digit

    return product == sum_digits

result = is_spy(1124)
print("Is 1124 a spy number?", result)
