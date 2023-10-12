total=0             #setting initial sum as zero

for i in range(1,1000):
    if i%3==0 or i%5==0:
        total+=i
print(total)
