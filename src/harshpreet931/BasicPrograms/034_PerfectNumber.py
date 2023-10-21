def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

result = is_perfect_number(28)
print("Is 28 a perfect number?", result)
