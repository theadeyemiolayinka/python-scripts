def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

result = sum_of_squares(5)
print("Sum of squares:", result)
