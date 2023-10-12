import time

start = time.time()

checked = []
count = 2
duplicates = ["2","4","6","8","5","0"]

def is_prime(n: int) ->bool:
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
            break
    else:
        return True
    
    
def cyclic_permutations(number)->list:
    permutations = list()
    
    
    for i in range(len(number)):
        initial = (number[0])
        for index in range(len(number)-1):
            number[index] = (number[index+1])
        number[-1]=initial
        permutations.append("".join(number))
        
    return permutations     



    
for i in range(2,1000000):
    number=list(str(i))
    
    for char in number:
        if char in duplicates:
            break
    else:    
        if i not in checked:
            
            if is_prime(i):           
                
                cyclic_numbers = cyclic_permutations(number)
                
                for index in range(len(cyclic_numbers)-1,-1,-1):
                    cyclic_numbers[index] = int(cyclic_numbers[index])
                    if len(str(cyclic_numbers[index]))!=len(str(i)):
                        del cyclic_numbers[index]
                    if not is_prime(cyclic_numbers[index]):
                        checked.append(cyclic_numbers[index])                                              
                        break                
                else:                 
                    cyclic_numbers = list(dict.fromkeys(cyclic_numbers))                
                    count+=len(cyclic_numbers)                    
                    checked.extend(cyclic_numbers)     

  
print(count)
print(time.time() - start)
                
    
        


        
