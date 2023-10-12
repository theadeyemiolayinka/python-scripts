import time

start=time.time()

count=0
factorial_list=[1]

for n in range(1,10):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    factorial_list.append(factorial)


#digital factorial of 99999999 is 2903040, that means the maximum that could be roughly represented is digital factorial of 9999999 is 2540160 because this is the highest number that a 7 digit digital factorial can produce matching that same length
for i in range(10,2540160): #established upper limit roughly
    
    text = str(i)
    total = 0
    for char in text:
        total+=factorial_list[int(char)]
    if total==i:
        count+=i
print(count)
end = time.time()
print(end-start)
