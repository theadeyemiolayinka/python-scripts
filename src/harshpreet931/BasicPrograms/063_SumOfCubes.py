def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n+1))

result = sum_of_cubes(3)
print("Sum of cubes:", result)
