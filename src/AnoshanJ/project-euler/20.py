

def factorial(n: int) ->int:
    """This function outputs the factorial value of the number"""
    value =1
    for i in range(1,n+1):
        value*=i
    return value

def digitalroot(n: int) ->int:
    total = 0
    string_number = str(n)
    for digit in string_number:
        total += int(digit)

    return total

answer= digitalroot(factorial(100))
print(answer)

    
        
