def is_triangular(num):
    n = 1
    while (n * (n + 1)) < 2 * num:
        n += 1
    return (n * (n + 1)) / 2 == num

result = is_triangular(21)
print("Is 21 a triangular number?", result)
