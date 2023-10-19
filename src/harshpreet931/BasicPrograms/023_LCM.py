def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return (a * b) // gcd(a, b)

result = lcm(12, 18)
print("LCM of 12 and 18:", result)
