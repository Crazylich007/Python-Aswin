import random
a = random.randrange(0,9999999999999)
print(a)

while a>=10:
    b=str(a)
    c=0
    for i in b:
        c=c+int(i)
    a=c
print(c)
