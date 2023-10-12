import time

start =time.time()

#list to store prime values
prime_list = []

#function to check if a number is a prime
def is_prime(n :int)->bool:
    for j in range(2,int(n**0.5)+1):    #checking numbers only upto to the square root of the number
        if n%j==0:
            return False
            break
    else:  
        
        return True
print(is_prime(1))
#since the quadratic gives only prime numbers for b values which are prime, and the count of prime numbers given is high when a is also prime. we can only consider first 1000 values for a and b    
for i in range(2,1001):             
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        prime_list.append(i)

#since the prime_list will be updated over time make a copy of just the 1000 prime numbers
primes1000 = prime_list.copy()

#set the largest count to zero to initialize
largest = 0
product = 0


for b in primes1000:
    for a in primes1000:
        if (a**2-4*b)>0:    #skip functions that produce negative values since they cannot be prime numbers
            continue

        #code to check for positive a and positive b values
        i=0
        while True:
            #calcuate value of the function
            quadratic = i**2 +a*i+b
            #if that value isn't already in the prime_list check if it is
            if quadratic not in prime_list:
                #if it is prime, add that to the prime_list and proceed
                if (is_prime(quadratic)):
                    prime_list.append(quadratic)
                #if the number is not prime, set the new largest count to one less as the previous number will be highest
                else:
                    #only update if it exceeds the current largest values
                    if i-1>largest:
                        largest = i-1
                        product = a*b
                    break
            i+=1

        i=0
        #repeat for a negative values and b positive (note that b cannot be negative as it gives negative output for even zero independant variable value
        while True:
            quadratic = i**2 -a*i+b
            if quadratic not in prime_list:
                if (is_prime(quadratic)):
                    prime_list.append(quadratic)
                else:
                    if i-1>largest:
                        largest = i-1
                        product =  (-1)*a*b    
                    break
            i+=1

print(product)
print(time.time() - start)

        
