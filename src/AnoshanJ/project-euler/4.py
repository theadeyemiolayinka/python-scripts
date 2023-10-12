highest_palidrome=0
for j in range(100,1000):
    for z in range (100,1000):
        y=''
        multiple=j*z
        x=str(multiple)
        for i in range (1,len(x)+1):
            y+=x[-i]
        y=int(y)
        if y==multiple and y>highest_palidrome:
            highest_palidrome=y
print(highest_palidrome)
        
