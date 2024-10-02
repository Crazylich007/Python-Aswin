# guess game

a = input ("Enter your guess (either o or e): ")

import random
b = random.randrange(1,100)
print (b)

if (a=="e" and b%2==0) or (a=="o" and b%2!=0):
    print ("win")
else:
    print ("lose")