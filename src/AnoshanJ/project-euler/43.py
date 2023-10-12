import time

start = time.time()

divisors = [2,3,5,7,11,13,17]

total = 0

def permutations(input_list: list) -> list:
    if len(input_list)==0:
        return []
    if len(input_list)==1:
        return [input_list]

    perm_list = list()

    for i in range(len(input_list)):
        initial_element = input_list[i]
        remaining_elements = input_list[:i] + input_list[i+1:]
        

        for p in permutations(remaining_elements):
            perm_list.append([initial_element]+p)

    return perm_list


x = list("0123456789")

for p in permutations(x):
    number = "".join(p)    
    for i in range(7):
        sub_string = number[i+1:i+4:]
        if int(sub_string)%divisors[i]!=0:
            break
    else:
        total+=int(number)

print(total)
print(time.time() - start)
            
        
        
    
