def is_happy(num):
    def sum_of_squares(n):
        return sum(int(digit)**2 for digit in str(n))

    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    return num == 1

result = is_happy(19)
print("Is 19 a happy number?", result)
