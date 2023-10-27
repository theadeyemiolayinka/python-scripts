def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd_product(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

result = gcd_product([8, 12, 16, 24])
print("Greatest common product:", result)
