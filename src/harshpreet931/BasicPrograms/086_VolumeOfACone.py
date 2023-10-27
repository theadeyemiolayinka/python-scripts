import math
def volume_of_cone(radius, height):
    return (1/3) * math.pi * (radius**2) * height

result = volume_of_cone(4, 7)
print("Volume of cone:", result)
