highest_value = 0
highest_length = 0

def recurring_cycle_finder(div:int) ->int:
    recurring_values = list()

    if div<=10:
        place_value=10        
    elif div>10 and div<=100:
        place_value=100
    elif div>100 and div<=1000:
        place_value=1000

    val= 1
    
    while True:
        val=((val*place_value)%div)
        if val in recurring_values:
            break
        else:
            recurring_values.append(val)

    return len(recurring_values)

for i in range(2,1000):
    length = recurring_cycle_finder(i)
    if length>highest_length:
        highest_value=i
        highest_length=length

print("Highest value is {} of length {}".format(highest_value,highest_length))
