import time

start = time.time()

abundant_numbers = []
sum_of_n_abundant= 0
all_numbers = []


def abundant_number(n: int) ->None:
    """
    adds the input number to the abundant_number list if it is
    """
    divisor_total = [1] 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divisor_total.append(i)
            if (n//i) not in divisor_total:
                divisor_total.append(n//i)
     
    divisor_total = sum(divisor_total)
    if divisor_total > n:
        abundant_numbers.append(n)
       
for i in range(1, 28124):
    abundant_number(i)
    
all_numbers = [0]*28124


for i in range(len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        
        total = abundant_numbers[i]+abundant_numbers[j]
        if total <28124:
            if(all_numbers[total]==0):            
                all_numbers[total]=total
         
        


for number in range(1,len(all_numbers)):
    if all_numbers[number]==0:
        sum_of_n_abundant+=number
        
print(sum_of_n_abundant)
print(time.time() - start) 
        
