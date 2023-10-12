import time

start = time.time()


highest_count = 0
highest_value = 0


for i in range(1000):
    count=0
    for a in range(1,int(i/3)+1):
        for b in range(a, int(i/2)+1):
            c=float((a**2+b**2)**0.5)
            if c==float(i-a-b):
                count+=1
    if count>highest_count:
        highest_count=count
        highest_value=i

print(highest_value)
print(highest_count)

print(time.time() - start)
