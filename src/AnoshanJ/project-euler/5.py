value=1
for i in range (1,21):
    multiple=i
    for x in range (2,i):
        for y in range (2,x):
            if x%y==0:
                break
        else:
            while i%x==0:
                multiple//=x
##            print("prime is : {}".format(x))
##    print("Multiple is : {} ".format(multiple))
    value*=multiple
##    print("Value is : {} ".format(value))
print(value)
