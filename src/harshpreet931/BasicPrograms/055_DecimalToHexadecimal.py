def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

result = decimal_to_hexadecimal(255)
print("Decimal 255 in hexadecimal:", result)
