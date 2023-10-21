def armstrong_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end+1):
        order = len(str(num))
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            armstrong_numbers.append(num)

    return armstrong_numbers

result = armstrong_in_range(1, 1000)
print("Armstrong numbers between 1 and 1000:", result)
