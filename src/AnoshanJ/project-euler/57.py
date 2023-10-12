import time

start = time.time()

num , den = 3, 2
count = 0


for i in range(1000):
    num, den = (num+2*den) , (num+den)

    if len(str(num))>len(str(den)):
        count+=1

print(count)
print(time.time() - start)
