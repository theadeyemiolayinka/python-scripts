#Coded by Anoshan J.

#importing time module
import time

#Time at the start of execution
start = time.time() 

#highest chain length 
highest_count = 0

#number of the highest chain length
highest_chain_number = 0

#collatz function
def collatz(n: int) -> int:
    """This function returns the collatz length of the input number"""

    counter = 1
    while n!=1:
        if n%2 == 0:
            n = n/2
            counter +=1
        else:
            n = 3*n +1
            counter +=1
    else:
        return counter
            

for i in range(1, 1000000):

    n = collatz(i)

    if n>highest_count:
        highest_count = n
        highest_chain_number = i
    
print(str(highest_chain_number)+" is the number with the highest chain length of "+str(highest_count))
print("*"*40)
end = time.time()
print (end - start)
