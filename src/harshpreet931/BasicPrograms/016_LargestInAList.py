def find_largest(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [4, 7, 2, 11, 8, 15]
largest = find_largest(numbers)
print("Largest number:", largest)
