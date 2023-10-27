def is_duck(num):
    return '0' in str(num) and str(num)[0] != '0'

result = is_duck(1023)
print("Is 1023 a duck number?", result)
