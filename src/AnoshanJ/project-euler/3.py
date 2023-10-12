n=600851475143               #Setting our number
for j in range(2,n):        #Considering from number 2 to one less than our calucation number
    if n%j==0:              #considering only factors
        for i in range(2,j):    #Test to check if that number is prime 
            if j%i==0:          #Considering from 2 to one less than that number,
                break           #if it is divisible by any of these numbers it won't be a prime number
        else:                   #if is has not been divisible by any of these digits so far it has to be a prime number
            highest_factor=j   #Now we know this factor is a prime number too, at the end of the cycle it will be assinged the highest value of the factors
print(highest_factor)
