name_list = []
alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())

net_total = 0

with open("22_names.txt", "r") as text_file:
    text = text_file.readline()
    name_list = text.split(",")

name_list.sort()

for index, name in enumerate(name_list):
    
    name_list[index] = name.strip('"')

    multiplier = index + 1
    
    total= 0
    
    for char in name_list[index]:        
        value = alphabet.index(char) + 1
        total +=value
    total = total * multiplier
    net_total+=total
    

print(net_total)



    
