# Selection sort in Python3

def selectionSort(vector, n):
    n = n - 1;
    for i in range(n, 1, -1):
        im = 0;
        for j in range(n+1):
           if vector[j] > vector[im]:
               im = j;
           if im < i:
               aux = vector[i];
               vector[i] = vector[im];
               vector[im] = aux;
    return vector

print("Ordination by selection.");
vector = str(input('Enter the sequence of numbers belonging to the vector. Ex "5,7,8,4,3,6,1,9,10,2": '))
vector = vector.split(",")
vector_num = []
for num in vector:
    vector_num.append(int(num))
print(vector_num);
print("vector: ",vector_num);

n = len(vector_num);
print("Ordination: ",selectionSort(vector_num, n));