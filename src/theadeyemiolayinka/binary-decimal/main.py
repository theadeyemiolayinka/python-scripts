
def binary_to_decimal(binary):
    binary = str(binary)
    """
    Converts a binary number into a decimal number.
    """
    return int(binary, 2)

def decimal_to_binary(decimal):
    decimal = int(decimal)
    """
    Converts a decimal number into a binary number.
    """
    return bin(decimal).replace("0b", "")

def get_choice(text):
    val = int(input(text))
    if val == 1 or val == 2:
        return val
    else:
        return get_choice('Invalid choice, try again: ')

if __name__ == '__main__':
    print ("""
1. Binary to Decimal
2. Decimal to Binary
    """)

    choice = int(get_choice('> '))

    if choice == 1:
        binary = int(input("Binary to convert: "))
        print ("The binary number %d in decimal is %d" % \
              (binary, binary_to_decimal(binary)))
    elif choice == 2:
        decimal = int(input("Decimal to convert: "))
        print ("The decimal number %d in binary is %s" % \
              (decimal, decimal_to_binary(decimal)))
    else:
        print ("Invalid choice")