import math
def area_of_regular_polygon(n, side_length):
    return (n * (side_length ** 2)) / (4 * math.tan(math.pi / n))

result = area_of_regular_polygon(6, 4)
print("Area of regular hexagon:", result)
