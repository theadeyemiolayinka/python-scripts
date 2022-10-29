
m1 = input('Enter Marks of Subject 1: ')
m2= input('Enter Marks of Subject 2: ')
m3 = input('Enter Marks of Subject 3: ')
m4 = input('Enter Marks of Subject 4: ')
m5 = input('Enter Marks of Subject 5: ')
#calculate total and average
total=float(m1)+float(m2)+float(m3)+float(m4)+float(m5)
average=float(total)/5
#display total of the marks
print('The total of marks is ',total)
#display average of the marks
print('The average of marks is ',average)
if average > 90:
   print("You receive grade 0")
elif average > 80:
   print("You receive grade A+")
elif average > 70:
   print("You receive grade A")
elif average > 60:
   print("You receive grade B+")
elif average > 50:
   print("You receive grade B")
elif average >=35:
   print("You receive grade C+")
elif average < 35:
   print("You have failed")
