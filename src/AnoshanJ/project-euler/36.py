import time

start = time.time()

total = 0

for i in range(1,1000000):
    number = str(i)[::-1]
    if int(number)==i:
        b = str(bin(i))[2:]               
        if (b[::-1])==b:
            total+=i
            
print(total)
print(time.time() - start)
    
                  
