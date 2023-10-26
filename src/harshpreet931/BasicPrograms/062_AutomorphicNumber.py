def is_automorphic(num):
    square = num ** 2
    return str(square).endswith(str(num))

result = is_automorphic(25)
print("Is 25 an automorphic number?", result)
