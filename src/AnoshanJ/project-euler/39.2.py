import time

start = time.time()


highest_count = 0
highest_value = 0

#It is a collection where elements are stored
##as dictionary keys and their counts are stored
##as dictionary values
from collections import Counter

perimeters_list = []

#since a+b+sqrt(a^2+b^2)<=1000 when a is set to 0 b can be maximum 500 and vice versa
for a in range(1,500):    
    for b in range(a, 500):
        c=((a**2+b**2)**0.5)
        #checking if the c was an integer and the total is less than 1000
        if int(c)==c  and (a+b+c)<=1000:
            #if so append to the list
            perimeters_list.append(a+b+c)
    
#counter creates a dictionary with the element as a key and counts stored as values        
counter_dict = Counter(perimeters_list)
#Using the most_common the mode (1) has to be used
##to find the most common which returns a list containing
##a tuple like this[(840.0, 8)]
print(counter_dict.most_common(1)[0][0])
print(counter_dict.most_common(1)[0][1])

print(time.time() - start)
