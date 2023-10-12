import time

start = time.time()

count=0

def factorial(n:int):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        value = 1
        for i in range(2,n+1):
            value*=i
        return value

for n in range(1,101):
    for r in range(1,n+1):
        value = factorial(n)/(factorial(r)*factorial(n-r))
        if value>1000000:
            count+=1

print(count)

end = time.time()

print(end - start)


