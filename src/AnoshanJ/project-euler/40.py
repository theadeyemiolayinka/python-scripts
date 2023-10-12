import time

start = time.time()
index=0
number=1
product=1
check_no =1
while index<1000000:
    for char in str(number):
        index+=1
        if index==check_no:
            product*=int(char)
            check_no*=10
    number+=1

print(product)
print(time.time() - start)
