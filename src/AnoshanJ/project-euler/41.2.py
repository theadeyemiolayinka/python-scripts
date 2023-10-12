import time
from itertools import permutations

start=time.time()


def is_prime(n:int) -> bool:
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
            break
    else:
        return True

for i in range(9,1,-1):
    num=""
    for j in range (1,i+1):
            num+=str(j)
    
    permutations_list = list(permutations(num))
    
    for index in range(len(permutations_list)-1,-1,-1):
        permutations_list[index] = int("".join(permutations_list[index]))
        if not is_prime(permutations_list[index]):
            del permutations_list[index]   
    
    if permutations_list:        
        print(max(permutations_list))
        break           

print(time.time()-start)
    
