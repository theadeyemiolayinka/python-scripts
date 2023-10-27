def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_of_list(numbers):
    def lcm(a, b):
        return (a * b) // (gcd(a, b))

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])

    return result

result = lcm_of_list([12, 18, 24, 30])
print("LCM of numbers:", result)
