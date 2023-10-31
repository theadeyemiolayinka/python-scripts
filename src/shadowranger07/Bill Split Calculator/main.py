#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage tip do you want to give? ")
ppl = input("How many people to split the bill? ")

multiplier = int(tip)
totalbill = float(bill)*(1+((float(tip))/100))
split = totalbill/int(ppl)

new_split = "{:.2f}".format(split)
print(f"Each person should pay: ${new_split}")

