def decimal_to_octal(n):
    return oct(n).replace("0o", "")

result = decimal_to_octal(10)
print("Decimal 10 in octal:", result)
