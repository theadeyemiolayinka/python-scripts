# Binary order search in Python3.

def buscaBin(vector, start, the_end, key):
    if start > the_end:
        return -1
    middle = round((start + the_end)/2);
        
    if key == vector[middle]:
        return middle;

    if key > vector[middle]:
        middle = middle + 1;
        return buscaBin(vector, middle, the_end, key);
    
    else:
        middle = middle - 1;
        return buscaBin(vector, start, middle, key);


vector = str(input('Enter the sequence of numbers belonging to the vector. Ex "1,7,9,20,52,153": '))
num_search = int(input('Number for the search: '))
print(f"Binary search. ordered vector 1~10. Ex: Search for the number {num_search}")

print("vector:  ",vector)
vector = vector.split(",")
vector_num = []
for num in vector:
    vector_num.append(int(num))
n= len(vector_num)-1;

print("Position: ",buscaBin(vector_num, 0, n, num_search) + 1);