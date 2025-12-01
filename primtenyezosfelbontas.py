# 11. Prímtényezős felbontás
# Feladat 
# Írj programot, ami bekér egy egész számot, majd elkészíti a prímtényezős felbontását.
# Bemenet
# A bemeneten egyetlen egy sora egy egész számot (0 < x ≤ 106
# ) tartalmaz.
# Kimenet
# Kimenet a prímtényezős felbontás szerepeljen szorzásjellel (*) elválasztva, ügyelve 
# arra, hogy az utolsó prímszám után ne legyen szorzásjel.
# Példa
# Be:
# 100
# Ki:
# 2*2*5*5

import math

szam=int(input("add meg a szamot:"))

oszto=2

while (szam>1):
    if (szam%oszto==0):
        print(f'{oszto}*', end="")
        szam/=oszto
    else:
        oszto+=1









