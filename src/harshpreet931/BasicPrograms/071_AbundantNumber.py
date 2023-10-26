def is_abundant(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) > num

result = is_abundant(12)
print("Is 12 an abundant number?", result)
