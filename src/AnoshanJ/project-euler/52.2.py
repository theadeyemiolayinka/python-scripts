import time

start = time.time()


i=1

while True:
    if set(str(i)) == set(str(i*6)):
        if set(str(i)) == set(str(i*5)):
            if set(str(i)) == set(str(i*4)):
                if set(str(i)) == set(str(i*3)):
                    if set(str(i)) == set(str(i*1)):
                        print(i)
                        break
    i+=1

end = time.time()

print(end - start)
