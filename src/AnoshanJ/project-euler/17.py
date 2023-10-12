ones = ["","one" , "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
tens = ["","ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ten_to_twenty = ["ten", "eleven", "twelve", "thirteen", "fourteen" , "fifteen", "sixteen" , "seventeen", "eighteen", "nineteen" ]
total = 0
#lists contains words to be made and the initial total set to zero


def number_of_letters (input_number : int) -> int:
    """This function returns the number of letters exclusive
    of spaces and hyphens that the number has"""
    number = str(input_number)  #converts the number to a string so that operations can be performed
    read_out = None #sets the number to word conversion to be null at start
    if len(number)==1: #conversion for length 1 numbers
        read_out = ones[int(number)]
    elif len(number)==2: # conversion for length 2 numbers
        if(number[0])=="1":
            read_out = ten_to_twenty[int(number[1])]
        else:
            read_out = tens[int(number[0])]
            read_out += ones[int(number[1])]
        
    elif len(number)==3:    #conversion for length 3 numbers
        read_out = ones[int(number[0])]
        read_out += "hundred"
        if not(number[1]=="0" and number[2]=="0"):
            read_out += "and"
            if(number[1])=="1":
                read_out+=ten_to_twenty[int(number[2])]
            else:
                read_out += tens[int(number[1])]
                read_out += ones[int(number[2])]       
        
    elif int(number)==1000: #coversion for one thousand which is a special case
        read_out = "onethousand"
    else:
        raise ValueError("This is not in the range")    #Raise an error if a value out of the programmed index is input
    return (len(read_out))

for i in range(1,1001):         #parses numbers from 1 to 1000 to the functions and adds all of them
    total+=number_of_letters(i)

print("The total is {}.".format(total)) #Outputting the total
##print(number_of_letters(245))
##print(number_of_letters(299))
##print(number_of_letters(201))
##print(number_of_letters(214))
##print(number_of_letters(210))

        
        
    
    
