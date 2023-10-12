import time

start = time.time()

distinct_term_list = []

for a in range(2,101):
    for b in range(2,101):
        value = a**b
        if value not in distinct_term_list:
            distinct_term_list.append(value)

print(len(distinct_term_list))
print(time.time() - start)

        
