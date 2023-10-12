grid=list()                 #create the grid
product=0                   #set the product value to zero

for i in range(0,20):
    grid.append(list(input().split()))      #add items to the list such that there are 20 lists each of input number of items

def multiply(a,b,c,d):                      #multiply function
    """
    This function multiplies the provided input. It converts it to integer and outputs the result as an integer
    
    :param a,b,c,d : all integers
    :return: integer multiplied output
    """

    return (int(a)*int(b)*int(c)*int(d))


for row_no, row_value in enumerate(grid):                           #accessing row numbers and each row one by one
    for cell_no, cell_value in enumerate(row_value):                #accessing each cell item of row
        
        if cell_no+3<len(row_value):                    #check if horizontal multiplication is possible if so multiply
            horizontal_answer = multiply(cell_value, row_value[cell_no+1], row_value[cell_no+2], row_value[cell_no+3])
            if horizontal_answer>product:           #if this mutliplcation is greater set your product to that value
                product=horizontal_answer
            
        if row_no+3<len(grid):  #check if vertical multiplication is possible if so multiply
            vertical_answer = multiply(cell_value, grid[row_no+1][cell_no], grid[row_no+2][cell_no], grid[row_no+3][cell_no])
            if vertical_answer>product:
                product=vertical_answer
            
        if row_no+3<len(grid) and cell_no+3<len(row_value): #check if diagonal right multiplication is possible if so multiply
            diagonal_right_answer = multiply(cell_value, grid[row_no+1][cell_no+1], grid[row_no+2][cell_no+2], grid[row_no+3][cell_no+3])
            if diagonal_right_answer>product:
                product=diagonal_right_answer
                
        if row_no+3<len(grid) and cell_no>3: #check if diagonal left multiplication is possible if so multiply
            diagonal_left_answer = multiply(cell_value, grid[row_no+1][cell_no-1], grid[row_no+2][cell_no-2], grid[row_no+3][cell_no-3])
            if diagonal_left_answer>product:
                product=diagonal_left_answer
print(product)          #print the product
            
            
        
            

