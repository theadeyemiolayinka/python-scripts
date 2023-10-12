import time

start = time.time()

highest_count = 0
value = 0
length = 0

def sieve_of_eratosthenes(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    

    for i in range (3, int(n**0.5)+1,2):
        j=2
        index = i*2

        while index<n:
            is_prime[index] = False
            index+=i

    primes_list = [2]
    for i in range(3,n,2):
        if is_prime[i]:
            primes_list.append(i)

    return primes_list
        
prime_list = sieve_of_eratosthenes(1000000)

upper_limit = len(prime_list)

for i in range(len(prime_list)):
    for j in range(i+length, upper_limit):
        total = sum(prime_list[i:j])
        if total<1000000:
            if total in prime_list:
                length = j - i                
                highest_count = length
                value = total
        else:
            upper_limit = j+1
            break



print(value)

end = time.time()

print(end - start)
