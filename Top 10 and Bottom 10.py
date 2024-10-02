
import random
a=[]
for i in range(100):
    b = random.randrange(1,101)
    if b in a:
        print ("duplicate", b)
    elif b%4==0:
        print ("disvisble", b)
    elif b%11==0:
        print ("Same Number", b)
    else:
        a.append(b)


a.sort(reverse=True)
print("The top 10 numbers are", a[:10])
print("The bottom 10 numbers are", a[:-11:-1])



