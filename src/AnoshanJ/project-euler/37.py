import time

start=time.time()

primes = []

total=0
count=0

def is_prime(n:int) ->bool:
    if n==1:
        return False
    else:
        if n in primes:
            return True
        else:
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False                
                    break
            else:
                primes.append(n)
                return True

def truncater(text:str) ->list:
    truncations = []
    truncations.append(int(text))
    for i in range(len(text)-1):
        truncations.append(int(text[i+1:]))
        truncations.append(int(text[:(-1)*(i+1)]))
    return(truncations)

       
        
i=10 
while count<11:
    text = str(i)
    if (text[0] not in "2357") or (text[-1] not in "37"):
        i+=1
        continue
    else:   
        if is_prime(i):
            possibilites = truncater(text)
            for number in possibilites:
                if not is_prime(number):
                    break
            else:
                total+=i
                count+=1
                
    i+=1


print(total)
print(time.time() - start)
