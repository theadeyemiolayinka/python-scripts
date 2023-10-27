def is_magic(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num == 1

result = is_magic(19)
print("Is 19 a magic number?", result)
