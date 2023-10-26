def is_disarium(num):
    sum = 0
    temp = num
    n = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
        n -= 1

    return sum == num

result = is_disarium(135)
print("Is 135 a disarium number?", result)
