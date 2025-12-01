#4. Prím
#Feladat
#Írj programot, amely a bekért számról eldönti, hogy prím-e!
#Bemenet
#A bemeneten egyetlen egy sora egy egész szám (0 < x ≤ 106
#).
#Kimenet
#A kimenet egyetlen sorába írjuk, hogy a bekért szám prím-e. Amennyiben nem prím, írjuk
#ki, hogy összetett szám.
#Példa 1
#Be:
#23244
#Ki:
#Összetett szám
#Példa 2
#Be:
#1907
#Ki:
#Prim


import math

x = int(input("Írj be egy számot: "))

if x <= 1:
    print("Összetett szám")
elif x <= 3:
    print("Prim")
elif x % 2 == 0:
    print("Összetett szám")
else:
    oszto_talalt = False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            oszto_talalt = True
            break
    if oszto_talalt:
        print("Összetett szám")
    else:
        print("Prim")
