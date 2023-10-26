import math

def area_of_sector(radius, angle):
    return (angle / 360) * math.pi * (radius ** 2)

result = area_of_sector(7, 45)
print("Area of sector:", result)
