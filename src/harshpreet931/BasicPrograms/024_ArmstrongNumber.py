def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    return num == sum

result = is_armstrong(153)
print("Is 153 an Armstrong number?", result)
