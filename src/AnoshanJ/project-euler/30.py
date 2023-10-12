##In base ten, the highest digit is 9 and 9**5 = 59049 
## which has five digits. This implies that the highest possible
##number, which equals the sum of the fifth power of its digits is 5(length of 59049) times 9**5
##times 
## The lowest possible number is 2 times 2**5=64 which is 128
##All numbers with this property thus must range between these two values.

#5*59049 = 295245


import time

start = time.time()

fifth_power_number_total = 0

for i in range(128,295245):
    text = str(i)
    total = 0

    for char in text:
        total+=int(char)**5
    if i==total:
        fifth_power_number_total+=i

print(fifth_power_number_total)
print(time.time() - start)


    
