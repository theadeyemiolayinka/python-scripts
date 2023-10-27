def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

result = generate_pascals_triangle(5)
print("Pascal's Triangle:")
for row in result:
    print(row)
