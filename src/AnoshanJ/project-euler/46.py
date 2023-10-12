import time

start = time.time()

prime_list = [2]

def is_not_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    else:
        prime_list.append(n)
        return False

i=3
while True:
    if is_not_prime(i):
        for j in prime_list:
            x = ((i-j)//2)**0.5
            if x==int(x):                   
                break        
            
        else:
            print("Not true for {}.".format(i))
            break
    i+=2    
print(time.time() - start)
