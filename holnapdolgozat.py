#1. feladat

t=[3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]

teljesut=0
for lepes in t:
    if lepes <0:
        teljesut += -lepes
    else:
        teljesut += lepes

csakelore=0
for lepes in t:
        if lepes>0:
            csakelore += lepes


kulonbseg=((teljesut)-(csakelore) /csakelore)*100   #százalék

print (kulonbseg)


#1.-es feladat, B;

t = [3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]

aktualishossz=0
maxhossz=0

for lepes in t:
    if lepes>0:
     aktualishossz +=1
    if aktualishossz < maxhossz:
          maxhossz=aktualishossz

    else: aktualishossz=0

print("Leghosszabb előre haladó sorozat hossza:", maxhossz)

#1.-es feladat, C;

t = [3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]

maxlepes=0
for lepes in t:
    for lepes in t:
        if abs(lepes)==maxlepes:
            db+=1
    print (f"{db} és {maxlepes} láb volt")



#for i in range-el


t = [3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]

max_lepes=0

for i in range(len(t)):
    if abs(t[i]) > max_lepes:
        max_lepes= abs(t[i])

db=0
for i in range (len(t)):
    if abs(t[i])==max_lepes:
        db+=1

print(f'{db} darab, és {max_lepes} lab!')


#1.-es feladat, D;

t=[3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]

voltnulla=False
for i in range (len(t)):
    if t[i]==0:
        voltnulla=True
        break

    if voltnulla:
        print("igen.")

else:
    print("nem.")



#2. feladat

t = [160, 185, 159, 185, 167, 174, 172, 185]

for i in range(1, len(t)-1):
    if t[i]>t[i-1] and t[i]>t[i+1]:
        print(f"A(z) {i + 1}. diák csak a mellette levőket látja.")






    




