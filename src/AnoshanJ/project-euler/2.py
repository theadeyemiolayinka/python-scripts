total=0
x=1
y=2
while total<4000000:
    if x%2==0:
        total+=x
    z=x+y
    x=y
    y=z
print(total)
