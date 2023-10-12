import time

start = time.time()

#maximum time you can make 2 pounds with 2 pounds coin is once, so adding that to the counter already
count=1

#a is 100pence, maximum times is twice
for a in range(3):
    #maximum times for 50 pence coin is (200-100*a)/50
    for b in range(1+(200-100*a)//50):
        #maximum times for 20 pence coin is (200-100*a - 50*b)/20
        for c in range(1+(200-100*a-50*b)//20):
            #maximum times for 10 pence coin is 200-100*a-50*b - 20*c)/10)
            for d in range(1+(200-100*a-50*b - 20*c)//10):
                #maximum times for 5 pence coin is (200-100*a-50*b-20*c-10*d)/5
                for e in range(1+(200-100*a-50*b-20*c-10*d)//5):
                #maximum times for 2 pence coin is (200-100*a-50*b-20*c-10*d-5*e)/2
                    for f in range(1+(200-100*a-50*b-20*c-10*d-5*e)//2): #the remainder doesn't have to be calucated bcz these are all instances in which 2 pence coin is used so the remianing is automatically 1 pence
                        count+=1    #if all the rest coins are taken what is left is one pence coin(example if all are set to zero only then you make a 200pence using 200 1 pence which will add to count
                                       
            
print(count)
print(time.time() - start)
