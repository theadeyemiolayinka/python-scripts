import time

start = time.time()

def is_permutation(original: int, multiple:int):

    text = str(original)
    text2 = str(multiple)

    if len(text) == len(text2):
        for char in text:
            if char not in text2:
                return False
        else:
            return True
    else:
        return False

i=1
while True:
    if is_permutation(i*6, i):
        if is_permutation(i*5, i):
            if is_permutation(i*4, i):
                if is_permutation(i*3, i):
                    if is_permutation(i*2, i):
                        print(i)
                        break
    i+=1

end = time.time()

print(end - start)

    
