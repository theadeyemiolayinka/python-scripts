import time

start = time.time()


prime_list = [2]

def add_prime(n: int):

    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            break
    else:
        prime_list.append(n)
        

consecutive_count = 0

i=3
while consecutive_count<4:
    add_prime(i)
    count=0
    for primes in prime_list:        
       if i%primes==0:               
           count+=1
    
    if count==4:
        consecutive_count+=1
    else:
        consecutive_count=0     
    
    i+=1
print(i-4)
print(time.time() -start)
    
