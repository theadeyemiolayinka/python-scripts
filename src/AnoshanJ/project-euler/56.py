import time

start = time.time()

highest_length = 0

for a in range(100):
    for b in range(100):
        value = str(a**b)
        total = sum([int(c) for c in value])
        if total>highest_length:
            highest_length = total

print(highest_length)

print(time.time() - start)
