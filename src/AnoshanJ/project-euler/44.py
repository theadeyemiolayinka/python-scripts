import time

start = time.time()

pentagon_list = []

for i in range(1,10000):
    value = i*(3*i-1)/2
    pentagon_list.append(value)
    
pentagon_list.sort(reverse=True)

for i in pentagon_list:
    for j in range(0,pentagon_list.index(i)):
        val = pentagon_list[j]
        if (i-val) in pentagon_list and (i+val) in pentagon_list:
            break
            

print(time.time() - start)

    
