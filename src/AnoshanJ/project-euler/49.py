import time

start = time.time()


def is_prime(n: int):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True     

    
def permutations(input_list : list) ->list:

    if len(input_list)==0:
        return []
    if len(input_list)==1:
        return [input_list]

    perm_list = list()

    for i in range(len(input_list)):
        initial_element = input_list[i]
        remaining_list = input_list[:i] + input_list[i+1:]
        for p in permutations(remaining_list):
            perm_list.append([initial_element]+p)
    return perm_list


def permutation_checker(num: int):
    if is_prime(num):
        perms = permutations(list(str(num)))        
        for i in range(len(perms)-1,-1,-1):
            perms[i]= "".join(perms[i])
            perms[i] = int(perms[i])
            if perms[i]<num:
                del perms[i]
            elif not is_prime(perms[i]):
                del perms[i]
        perms = list(set(perms))
        perms.sort()
                
        for i in range(1,len(perms)-1):
            value = (2*perms[i] - perms[0])
            
            if value in perms:
                super_string=str(perms[0])+str(perms[i])+str(perms[perms.index(value)])                
                print(super_string)
                return True     
        
    return False



for i in range(1488,10000):
    if permutation_checker(i):
        break
    
print(time.time() - start)    
        

    
