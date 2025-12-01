#2. Ki nevet a végén
#Feladat
#A Ki nevet végén társasjátékban egy játékos csak akkor léphet ki, ha hatost dob. Készíts
#programot, ami megszámolja, hogy a dobásokból hány alkalommal jöhetett ki a játékos! A
#kockadobást véletlenszámokkal szimuláljuk, a generált számokat megjelenítjük.
#Bemenet
#A bemeneten egy egész szám, ami a kockadobások számát adja meg (0 < x ≤ 100).
#Kimenet
#A kimenet két sorában először jelenítsük meg a véletlen számokat szóközzel elválasztva,
#majd alatta, hogy hány alkalommal sikerült 6-ost dobni.
#Példa
#Be:
#6
#Ki:
#6 1 2 3 5 6
#2

import random
x = int(input("Hány dobást szeretnél szimulálni? "))
dobasok = []
for i in range(x):
    dobas = random.randint(1, 6)
    dobasok.append(str(dobas))

print(" ".join(dobasok))
hatosok_szama = dobasok.count("6")
print(hatosok_szama)
