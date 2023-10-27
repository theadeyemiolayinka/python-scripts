import math
def is_pronic(num):
    for i in range(int(math.sqrt(num)) + 1):
        if i * (i + 1) == num:
            return True
    return False

result = is_pronic(20)
print("Is 20 a pronic number?", result)
