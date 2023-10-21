import math

def standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

data = [1, 2, 3, 4, 5]
std_dev = standard_deviation(data)
print("Standard Deviation:", std_dev)
