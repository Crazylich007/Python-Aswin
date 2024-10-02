import random
a = random.randrange(0,999)
print(a)

while a >= 10:
    b=0
    while a>0:      
        b=b+a%10
        a=a//10
    a=b
print(a)