import time

start = time.time()

number_list = [True]*10001
number_list[0] = False


for i in range(1,len(number_list)):    
        
        forward = str(i)
        reverse = forward[::-1]
        
        for j in range(50):
            
            addition = str(int(forward)+int(reverse))            

            if addition==addition[::-1]:
                number_list[i] = False
                break
            
            forward = addition
            reverse = forward[::-1]
            

print(sum(number_list))        
end = time.time()

print(end - start)
