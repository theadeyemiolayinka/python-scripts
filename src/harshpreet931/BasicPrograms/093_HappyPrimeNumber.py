def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_happy(num):
    def sum_of_squares(n):
        return sum(int(digit)**2 for digit in str(n))

    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    return num == 1

def is_happy_prime(num):
    def sum_of_squares(n):
        return sum(int(digit)**2 for digit in str(n))

    return is_prime(num) and is_happy(num)

result = is_happy_prime(19)
print("Is 19 a happy prime number?", result)
