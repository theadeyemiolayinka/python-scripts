import time

start = time.time()

total=0
x=''
for i in range (1,1001):
    total+=i**i
for i in range (1,11):
    x+=(str(total)[-i])
print(x[::-1])

print(time.time() -start)
