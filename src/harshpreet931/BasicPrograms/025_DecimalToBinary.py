def decimal_to_binary(n):
    return bin(n).replace("0b", "")

result = decimal_to_binary(10)
print("Binary representation of 10:", result)
