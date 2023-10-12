low_limit=1
upper_limit=101
z=0
y=0
for i in range(low_limit, upper_limit):
    z+=i
    y+=(i**2)
print((z**2)-y)
