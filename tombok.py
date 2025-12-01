import random

n=int(input())
t=[]
for i in range(n):
    t.append(random.randint(1,6))
print(t)


db=0
for i in range(len(t)):
    if t[i]==6:
        db+=1
print()
print(len(t)-db)

#Egy tömbben megszánolja a T tulajdonságú elemek számát úgy, hogy egy változót beállítunk az elején nullára (darab) Majd a tömbön végighaladunk és ha találunk egy T tulajdonságú elemet, akkor a változót megnöveljük eggyel. A végén kiírjuk a változó értékét.
#Példa BE: t=[1,3,2,6] T=páros Ki: 2
#Algoritmus:


i=0
while i<5 and t[i]!=6:
    i+=1
if i<5:
    print(i)
else:
    print("nincs")


#     be: t,n 
# maxi=-1
# maxé=fiktiv kicsi, -végtelen
# ha t[i]maxé akkor
# maxé=t[i]
# elagazas vege ciklus vege
# ki: maxi
# program vege







