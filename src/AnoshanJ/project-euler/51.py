import time

start = time.time()


def is_prime(n:int) ->bool :
    """
    This functions returns the result if the given integer is prime or not
    """

    if n%2!=0:
        #Skipping division by even numbers
        for j in range(3,int(n**0.5)+1,2):
            if n%j==0:
                return False           
        else:
            return True
    else:
        return False


def combination_prime_counter(n:int) ->int :
    """This function returns the highest the number of highest possible prime number arrangements
    """
    #converting the number to string
    text = str(n)
    highest_count = 1    

    #going through each digit
    for char in "0123456789":

        #skip the process if the digit is not found        
        if char in text:
            #start the count for that possible variation
            count=1           
            #replace with possible digits
            for j in "0123456789":                
                #skip if same digit replacement
                if char==j:
                    continue                
                #replace the same characters with the other digits
                text = text.replace(char, j)
                
                val = int(text)
                #checking if the length is same to avoid error due to leading zeroes
                if len(str(val)) == len(text):
                    #if it is prime add to the count
                    if is_prime(val):
                        count+=1
                #reset the text
                text= str(n)
            #record the highest possible value
            if count>highest_count:
                highest_count= count                
        else:
            #skip the process if the digit is not found 
            continue
    #return the count
    return (highest_count)

#start with this value since we know this was the last place where 7 possibilities were encountered
i = 56003
while True:
    #go through the check only if the number is prime
    if is_prime(i):
        val = combination_prime_counter(i)
        #if encounter 8 stop the process and print the value
        if val==8:
            print(i)
            break
    #skip even numbers as they cannot be prime
    i+=2
    
end = time.time()
print(end - start)
            
