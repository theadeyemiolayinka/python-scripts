import time
start = time.time()

length = 1001
half_length = (length -1)//2

total=1
incrementing_factor = 2

value = 1

for i in range(half_length):
    for j in range(4):
        value=value+incrementing_factor
        total+=value
    incrementing_factor+=2

print(total)

print(time.time() - start)
    
