n=600851475143           #Setting our number
for j in range(2,n):    #Considering from number 2 to one less than our calucation number
    if n%j==0:          #if it is divisible by that number divide it         
        n=n//j           #keep on dividing the already divided number by higher multiples
        highest=j      #the last number will be divisible by its highest prime factor and sometimes from a smaller multiple from already it was divided, but since we now dividing by a higher number it will be the highest prime fact, so this final number it is divided by will be the highest common factor
    if j>n:
        print("Highest is {}".format(highest))
        break
