import time

start=time.time()


def is_prime(n:int) -> bool:
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
            break
    else:
        return True

for i in range(999999999,1,-1):
    if is_prime(i):
        for j in range (1,len(str(i))+1):
            if str(j) not in str(i):
                break
        else:
            print(i)
            break
            
            

print(time.time()-start)
    
        
    
