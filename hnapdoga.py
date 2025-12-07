import random

n=int(input())
tomb=[]
for i in range(n):
    tomb[i].append(random.randint(-100000, 1000000))

print(tomb)


db=0
for i in range(len(tomb)):
    if tomb[i]>0:
        db=db+1
if (db/len(tomb))>=0.95:
    print ("igazolva")
else:
    print("nem igazolva")


#Mennyi az átlagos bevétel?

# osszeg=
# ciklus i=0-tól i<n-ig egyesével
#     osszeg+=t[i]

# db=0
# ciklus i=0-tól i<n-ig egyesével
#     ha (T(t[i])) akkor
#     db+=1
# ki: db

osszeg=0
for i in range(len(tomb)):
    if tomb[i]>0:
        osszeg+=tomb[i]
db=0
for i in range(len(tomb)):
    if tomb[i]>0:
        db+=1
        print(osszeg/db)

#ha egy napon 12 konyvelesi adat tortenik, akkor hanyadik napon volt a ledtobbet ero biznisz?

osszeg=0
maxnap=-1
maxertek=-1
for i in range(len(tomb)):
    osszeg+=tomb[i]
    if ((i+1)%12==0) or (i==(len(tomb)-1)):
        if osszeg>maxertek:
             maxertek=osszeg
             maxnap=(i+1)//12
    osszeg=0
print(maxnap,maxertek) 

#dönts el, hogy melyikbol vantöbb az atlagnal nagyobb vagy az atlagnal kisebb kiadasokbol 

osszeg=0
for i in range(len(tomb)):
    osszeg+=tomb[i]
    db+=1
atlag=osszeg/db
print(atlag)
dbk=0
dbn=0
for i in range(len(tomb)):
    if tomb[i]>atlag:
        dbk+=1
    elif tomb[i]>atlag:
        dbn+=1
if dbn>dbk:
    print("atlagnal nagyobbakbol volt tobb")
elif dbn<dbk:
    print("atlagnal kisebbekbol volt tobb")
else:
    print("egyenlo szamu volt")



#gyakorlas

#1.-es feladat, A;
t = [3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]  
osszegpozitiv=0
osszegnegativ=0
for i in range (t[i]):
    if t[i]>0:
        osszegpozitiv+=t[i]
    else:
        osszegnegativ+=t[i]
kulonbseg=osszegpozitiv-abs(osszegnegativ)
print("A pozitív és negatív számok összegének különbsége:", kulonbseg)


#2.-es feladat, gyakorlas

t = [3, 1, -4, -4, 3, 0, 2, 3, -1, -1, -3, -2, 4, 1, -2, -1, 2, -3, 3, 4]
db=0
for i in range(len(t)):
    if t[i]>0 and t[i]%2==0:
        db+=1   
        print("A pozitív páros számok darabszáma: ", db)
        






