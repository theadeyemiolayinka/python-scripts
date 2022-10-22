# Bubble Sort in Python3

def bubbleSort(vector, n):
    for i in range(n, 0, -1):
        changed = False;
        for j in range(i):
            if vector[j] > vector[j+1]:
                aux = vector[j];
                vector[j]= vector[j+1]
                vector[j+1] = aux;
                changed = True;
        if changed == False:
            return vector

print("Sorting method. bubble method.");
vector = str(input('Enter the sequence of numbers belonging to the vector. Ex "5,7,8,4,3,6,1,9,10,2": '))
vector = vector.split(",")
vector_num = []
for num in vector:
    vector_num.append(int(num))
print(vector_num);
print("vector: ",vector_num);

n = len(vector_num)-1;
print("Ordination: ",bubbleSort(vector_num, n));