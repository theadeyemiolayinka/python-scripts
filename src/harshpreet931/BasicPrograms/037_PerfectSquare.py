import math

def is_perfect_square(num):
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt == num

result = is_perfect_square(16)
print("Is 16 a perfect square?", result)
