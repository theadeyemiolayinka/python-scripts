import time
from itertools import permutations

start = time.time()

lexi_permutations = (permutations([0,1,2,3]))

print("".join(lexi_permutations[999999]))

print(time.time() - start)
