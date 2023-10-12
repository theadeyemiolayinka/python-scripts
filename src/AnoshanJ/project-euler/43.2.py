import time

start =time.time()
#list of divisors
divisors = [13,11,7,5,3,2]
#list of digits
digits = list("0123456789")
#list of multiples of 17
multiples = list()
i=1
num=""

#list of final qualified values
values_list = []

#adding the multiples of 17 with 3 digits
while len(num)<4:
    num=str(i*17)
    if len(num)==4:
        break
    if len(num)==2:
        num = "0"+num
    multiples.append(num)
    i+=1

#this recursive function goes from reverse creating qualifying numbers
def finder(full_number, div):   
    
    for digit in digits:
        num=full_number        
        if digit not in full_number:            
            index=(-1)*(divisors.index(div)+1)            
            
            num=str(digit)+num[:index]
            
            if int(num)%div!=0:
                continue                       
                    
            elif div==2:
                
                for numbers in digits:
                    if numbers not in (str(digit)+full_number):
                        final_number = str(numbers)+(str(digit)+full_number)
                        break
                for numbers in digits:
                    if numbers not in final_number:
                        break           
                        
                else:                          
                    values_list.append(int(final_number))
                    continue               
                    
            else:               
                finder((str(digit)+full_number),divisors[divisors.index(div)+1])
                
                
for multiple in multiples:
    finder(multiple,13)

print(sum(values_list))
print(time.time() -start)
