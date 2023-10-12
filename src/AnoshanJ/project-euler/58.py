import time

start = time.time()

value=1
prime_count=0

difference= 2
diagonals = 1

def is_prime(n: int) :
    for j in range(3, int(n**0.5)+1, 2):
        if n%j==0:
            return False
    else:
        return True
    
while True:
    for i in range(3):
        value+=difference              
        if is_prime(value):
            prime_count+=1
    diagonals+=4        
    ratio = prime_count / diagonals
    if ratio<0.1:       
        length = difference + 1
        print(length)
        break
    value+=difference
    difference+=2

end = time.time()

print(end - start)
        
