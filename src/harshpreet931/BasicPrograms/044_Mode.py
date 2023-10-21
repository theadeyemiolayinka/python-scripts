from collections import Counter

def mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    mode_values = [k for k, v in count.items() if v == max_count]
    return mode_values

data = [1, 2, 2, 3, 4, 4, 5]
mode_result = mode(data)
print("Mode:", mode_result)
