import time

start=time.time()

alphabet = list("abcdefghijklmnopqrstuvwxzy")
flag = True

if flag:
    for char1 in alphabet:
        if flag:
            for char2 in alphabet:
                if flag:
                    for char3 in alphabet:            
                        with open("59_cipher.txt", "r") as en_file:
                            
                            codes = [int(x) for x in en_file.read().split(",")]
                            
                            decrypted = []
                            
                            for i in range(0,len(codes)-2,3):
                                
                                decrypted.append(chr(codes[i] ^ ord(char1) ))                  
                                decrypted.append(chr(codes[i+1] ^ ord(char2) )) 
                                decrypted.append(chr(codes[i+2] ^ ord(char3) )) 
                                
                            decrypted = "".join(decrypted)
                            
##                            if "the " in decrypted and "of " in decrypted: 
##                                print(decrypted)
##                                print(char1, char2, char3)
##                                print("="*100)
##                                print(sum([ord(x) for x in decrypted]))
##                                flag = False
##                                break
                            if "the " in decrypted: 
                                print(decrypted)
                                print(char1, char2, char3)
                                print("="*100)
                                print(sum([ord(x) for x in decrypted]))
                                
                                

print(time.time() - start)
