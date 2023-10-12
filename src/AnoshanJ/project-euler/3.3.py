n=600851475143
j=1
while j<n:
    j+=1
    if n%j==0:
        n//=j
print("Highest Prime Factor is: {}".format(j))
