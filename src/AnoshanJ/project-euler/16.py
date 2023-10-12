number = int(input("Please input the number: "))
final_number = 2**(number)
string_number = str(final_number)
total=0
for digit in string_number:
    total+=int(digit)
print(total)
