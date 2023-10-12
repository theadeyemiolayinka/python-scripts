#initialzing the start date, month and year
day = 1
month = 1
year = 1900
#initialzing a counter to keep track of name of day    
day_counter = 1
#counting the required sundays
sunday_count = 0
#list having the no of days in a month
days_in_months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Continue loop till it breaks
while True:
   

    #if december 31st move to january 1st
    if (month==12 and day==31): 
        if (year!=2000):        
            month=1
            year+=1
            day=1
        else:
           break #Stop if this date is reached
      #move to next month 
    if (day==days_in_months[month-1]):
        day=1
        month+=1
    
    #Leap year adjustment    
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                days_in_months[1] = 29
            else:
                days_in_months[1] = 28
        else:
            days_in_months[1] = 29
    else:
        days_in_months[1] = 28    
    #adding sundays which occur on the first of the months (note that this will miss checking the last day of every month, but is not an issue since only first days are required)
    if (year > 1900 and day== 1 and day_counter%7==0):
        sunday_count +=1   
    #Incrementing days and the day counter    
    day+=1
    day_counter+=1

    
   

    
    
    

       
    
    
    
    
print(sunday_count)    

    
