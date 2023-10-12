import time

start = time.time()

alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())
count=0

triangular_list = []

def solution_finder(x):
    n=0
    while True:
        n+=1
        if n*(n+1)-2*x==0:
            triangular_list.append(x)
            return True            
        if n*(n+1)-2*x>0:
            return False
           

with open("42_words.txt","r") as word_file:
    word_list = word_file.read().split(",")

    for index in range(len(word_list)):
        word_list[index] = word_list[index].strip('"')
        total=0
        for char in word_list[index]:
            total+=alphabet.index(char)+1
        if total in triangular_list:
            count+=1
        else:
            if solution_finder(total):
                count+=1
                continue

print(count)
print(time.time() -start)
    
