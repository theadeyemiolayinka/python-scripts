i=12370
prime_number=[2]

def make_prime(lower, upper):
    for k in range(lower, upper):
        for j in range (2,int(k**0.5)+1):
            if k%j==0:
                break
        else:
            prime_number.append(k)

def factor_counter(triangular_number):
    
    factor_list=[]
    factor_count=1
    
    for numbers in prime_number:
        dividend=triangular_number
        indice_count=0
        while dividend%numbers==0:
            dividend//=numbers
            indice_count+=1
        factor_list.append(indice_count)

    for item in factor_list:
        factor_count*=(item+1)

    return factor_count

def factor_counter_v1(triangular_number):
    factor_count=0
    for i in range(1,triangular_number):
        if triangular_number%i==0:
            factor_count+=1
    return factor_count

while True:
    i+=1
    
    triangular_number=int(i*(i+1)/2)

    
##    make_prime(prime_number[-1]+1, triangular_number+1)

    factor_count=factor_counter_v1(triangular_number)    
    
    if factor_count>500:
        print(triangular_number)
        break



