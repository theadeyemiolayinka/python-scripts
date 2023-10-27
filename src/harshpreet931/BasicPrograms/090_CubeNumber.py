def is_cube(num):
    return round(num**(1/3))**3 == num

result = is_cube(27)
print("Is 27 a cube number?", result)
