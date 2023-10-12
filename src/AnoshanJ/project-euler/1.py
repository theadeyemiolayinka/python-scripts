total=0             #setting initial sum as zero

for i in range(3,1000,3):
    if (i%5)!=0:    #eliminating common multiples of 3 and 5 to avoid double counting
        total+=i    #adding such multiples of 3 till 1000

for j in range(5,1000,5):
    total+=j        #adding multiples of 5 till 1000 including common multiples of 3 and 5
print("Sum of all the multiples of 3 or 5 below 1000 is : {}".format(total))
