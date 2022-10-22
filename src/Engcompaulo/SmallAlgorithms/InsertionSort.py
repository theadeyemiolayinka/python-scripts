# Sort by insertion sort in Python3.

def insertionSort(vector, n):
    for i in range(1, n):
        j = i;
        while (j > 0) and (vector[j] < vector[j-1]):
            aux = vector[j];
            vector[j] = vector[j-1];
            vector[j-1] = aux;
            j = j-1;
    return vector

print("Insert sort.");
print("Sort by insertion sort")
vector = str(input('Enter the sequence of numbers belonging to the vector. Ex "5,7,8,4,3,6,1,9,10,2": '))
vector = vector.split(",")
vector_num = []
for num in vector:
    vector_num.append(int(num))
print(vector_num);

n = len(vector_num);
print("Ordination: ",insertionSort(vector_num, n));