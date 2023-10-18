import random
min= 1
max= 6
i="yes"
while i=="yes" or i== "y":
  print("Rolling Dices.....")
  print("The values are....")
  v1= random.randint(min,max)
  v2= random.randint(min,max)
  print(v1,v2)
  i=input("Press 'y' or 'yes' to re roll dices.")
print("Have a good day.")