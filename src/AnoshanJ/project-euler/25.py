
a=1
b=1
index=2

while True:
    a=a+b
    b=b+a
    index +=2
    if len(str(a))==1000:
        print(index-1)
        break
    if len(str(b))==1000:
        print(index)
        break
        
