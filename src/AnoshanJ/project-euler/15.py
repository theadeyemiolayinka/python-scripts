#Written by Anoshan J.

#importing the time module
import time

#importing factorial from math module
from math import factorial

#initializing the start time
start = time.time()

#Function to output the combinations value
def nCr (n:int, r:int) -> int:
    """This function outputs the combinations value"""

    value = factorial(n)/(factorial(r)*factorial(n-r))

    return value

#initializing answer by inputting 40 and 20 to ncr function as there are 40 possible moves and 20 places to fill them
answer = nCr(40 , 20)

#initializing the end time
end = time.time()

print(answer)
print("*" * 50)
print(end - start)

