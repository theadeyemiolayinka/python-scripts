def median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 0:
        return (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    else:
        return sorted_numbers[length // 2]

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
med = median(my_numbers)
print("Median:", med)
