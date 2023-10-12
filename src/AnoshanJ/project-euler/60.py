import time

start = time.time()

def sieve_of_eratosthenes(n:int):
    primes = [True]*n
    primes[0] = False
    primes[1] = False

    for j in range(3,int(n**0.5)+1, 2):
        index = j*2
        while index<n:
            primes[index] = False
            index+=j

    prime_list = [2]
    
    for i in range(3,n,2):
        if primes[i]:
            prime_list.append(i)
    return prime_list

prime_list = sieve_of_eratosthenes(10000)


def is_prime(n:int):

    if n<=3:
        return n>1
    if n%2==0 or n%3==0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    else:
        return True

def conc_checker( n1, n2):
    number1 = int(str(n1)+ str(n2))
    number2 = int(str(n2)+ str(n1))

    if is_prime(number1) and is_prime(number2):
        return True
    else:
        return False

def prime_pairs():
    for i1 in range(len(prime_list)):
        a = prime_list[i1]
        for i2 in range(i1+1, len(prime_list)):
            b = prime_list[i2]
            if not conc_checker(a,b):
                continue
            for i3 in range(i2+1, len(prime_list)):
                c = prime_list[i3]
                if not conc_checker(a,c):
                    continue
                if not conc_checker(b,c):
                    continue
                for i4 in range(i3+1, len(prime_list)):                
                    d = prime_list[i4]
                    if not conc_checker(a,d):
                        continue
                    if not conc_checker(b,d):
                        continue
                    if not conc_checker(c,d):
                        continue
                    
                    for i5 in range(i4+1, len(prime_list)):
                        e = prime_list[i5]
                        if not conc_checker(a,e):
                            continue
                        if not conc_checker(b,e):
                            continue
                        if not conc_checker(c,e):
                            continue
                        if not conc_checker(d,e):
                            continue
                        return (a+b+c+d+e)

print(prime_pairs())
print(time.time() - start)    
