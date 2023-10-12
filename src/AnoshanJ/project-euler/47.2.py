import time

start = time.time()

def no_of_pr_factors(n:int):
    i=2
    a = set()
    """
    function which will return the number of prime factors
    """
    while n!=1 and i<n**0.5: #check upto the square root, there will be only one afterwards which can be added later
        if n%i==0:
            n//=i
            a.add(i)
            i-=1
        i+=1

    return(len(a)+1)


j=2*3*5*7
while True:
    if no_of_pr_factors(j)==4:
        j+=1
        if no_of_pr_factors(j)==4:
            j+=1
            if no_of_pr_factors(j)==4:
                j+=1
                if no_of_pr_factors(j)==4:
                    print(j-3)
                    break
    j+=1

print(time.time() - start)


