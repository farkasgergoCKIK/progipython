#1. Ciklusok
#Feladat
#Írj programot, amely bekér a felhasználótól egy számot, majd kiírja 1-től az adott számig
#vesszővel elválasztva, illetve az adott számtól visszafelé 1-ig! Ügyelj arra, hogy a sorozat végén
#ne legyen vessző, továbbá oldd meg mind a három tanult ciklussal!
#Bemenet
#A bemeneten egy egész szám (0 < x ≤ 100).
#Kimenet
#A kimenet két sorában először a számok növekvő sorrendben, a második sorában a számok
#csökkenő sorrendben szerepeljenek, vesszővel elválasztva.
#Példa
#Be:
#5
#Ki:
#1, 2, 3, 4, 5
#5, 4, 3, 2, 1

x = int(input("Adj meg egy számot: "))

# növekvő
szamok = []
for i in range(1, x + 1):
    szamok.append(str(i))
print(", ".join(szamok))

# csökkenő
vissza = []
for i in range(x, 0, -1):
    vissza.append(str(i))
print(", ".join(vissza))

