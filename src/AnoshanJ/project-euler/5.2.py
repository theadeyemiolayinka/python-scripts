num=2520
i=2

while i<21:
    if num%i==0:
        i+=1
    else:
        num+=1
        i=2
print(num)
