import time

from fractions import Fraction

start = time.time()
product = 1
for n in range(10,100):
    for d in range(n+1, 100):
        common = list(set(str(n))&set(str(d)))
        if len(common)!=0:
            if common[0]!="0": #removing trivial fractions
                
                num = list(str(n))
                den = list(str(d))
                num.remove(common[0])
                den.remove(common[0])

                if num[0]!="0" and den[0]!="0":
                    if Fraction(int(num[0]), int(den[0])) == Fraction(n, d):
                        product*=Fraction(n,d)

print(product.denominator)
print(time.time() - start)
