import time
sum_of_amicable =0
pair_list = []

start = time.time()

def sum_of_divisors(number: int) ->int:
    """This function outputs the sum of divisors of a number"""
    divisor_list = []
    divisor_total=1
    i=1
    while (i<(int(number**0.5))):
        i+=1
        if number%i==0:
            divisor_list.append(i)
            divisor_list.append(number//i)
        

    for number in divisor_list:
        divisor_total+=number

    return divisor_total

for i in range(10000):

    if i not in pair_list:
        number1_total = sum_of_divisors(i)
        number2_total = sum_of_divisors(number1_total)

        if (number2_total == i and number1_total!=i):
            pair_list.append(i)
            pair_list.append(number1_total)
            sum_of_amicable+=(i+number1_total)
            

print(sum_of_amicable)           
print(time.time() - start)
        
