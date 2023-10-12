import time

start= time.time()

all_numbers = ["1","2","3","4","5","6","7","8","9"]
not_found = True

for i in range(9999,10,-1): #going in reverse, since the first digits of the concatanated product will product the highest value
    string = str(i)
    j=2
    while not_found:    #by going this way from the highest the first answer that is found will definitely be the answer     
        string+= str(i*j)   #creating a string concatanating with the multiples
        j+=1
        if len(string)==9:  #if the length becomes equal to 9 check
            for digits in all_numbers:  #check if all the 9 digits are present in this, if so it is the answer
                if digits not in string:    #skip this number if it a certain digit is missing
                    break
            else:
                not_found = False   #since the answer is found we can exit out of the for loop  
                print(i, string)    #print the answer along with the concatanated product
                break
        if len(string)>9:   #suppose you create a string longer than 9 you can skip checking this value
            break
    if not not_found:  #since the answer is found we can exit out of the for loop  
        break
print(time.time() - start)
        
    
