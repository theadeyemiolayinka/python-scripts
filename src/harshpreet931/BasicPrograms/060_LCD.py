def gcd_of_list(numbers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])

    return result

numbers = [24, 36, 48, 60]
result = gcd_of_list(numbers)
print("GCD of numbers:", result)
