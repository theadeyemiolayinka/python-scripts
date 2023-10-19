import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

radius = 5
area = area_of_circle(radius)
print(f"Area of circle with radius {radius}:", area)
