import time
start = time.time()
total=0
values_list = []
for multiplicand in range(100):
    for multiplier in range(100,10000):
        value = multiplicand  * multiplier
        text = str(value)+str(multiplicand)+str(multiplier)
        if len(text)==9:
            for i in range(1,10):
                if str(i) not in text:
                    break
            else:                
                if value not in values_list:
                   values_list.append(value)
        
print(sum(values_list))
print(time.time() - start)
