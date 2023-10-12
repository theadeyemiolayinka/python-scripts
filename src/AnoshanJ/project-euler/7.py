prime_counter=1 #counter to identify the prime number sequence
j=2             #assigning the first prime number
while prime_counter<10001:        #continue till the prime counter reaches the 10001st number
    j+=1                          #check all numbers by icrementing one by one
    for i in range(2,j):
        if j%i==0:      #prime number test, if it is divisible by anthing other than 1 or itself it should not be prime
            break       #if so stop checking this number
    else:
        prime_counter+=1  #if it didn't break the for loop then it should be a prime number, therefore icrement the prime counter
print("The {}st prime number is:{}".format(prime_counter,j))
    
