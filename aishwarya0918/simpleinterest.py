#code to calculate simple interest
#accept required data from user
Princi= input("Enter Principal amount:")
R= input("Enter Rate of Interest in percent per annum:")
r=0
r=float(R)/100
Time = input("Enter time in number in years:")
#calculate simple interest
si = float(Princi)*r*float(Time)
#display simple interest
print("The simple interest : ",si)
