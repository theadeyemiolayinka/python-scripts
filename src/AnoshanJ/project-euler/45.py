import time

start = time.time()

def is_pentagon(n:int) ->bool:
    if ((24*n+1)**0.5+1)%6==0:
        return True
    else:
        return False

def is_triangular(n:int) ->bool:
    if ((8*n+1)**0.5-1)%2==0:
        return True
    else:
        return False

i=1


while True:
    
    hexagon = i*(2*i-1)
    if hexagon>40755:
        if is_pentagon(hexagon) & is_triangular(hexagon):
            break    
        
    i+=1
    
print(hexagon)
print(time.time() - start)

    
    


