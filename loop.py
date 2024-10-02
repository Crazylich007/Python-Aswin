a = 7987987987

while a >= 10:
    b = str(a)  
    c = 0 
    
    for i in b:
        c = c + int(i)  

    a = c

print(a)
