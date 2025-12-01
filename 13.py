szam=int(input("Kérek egy számot: "))
a=0
b=1
osszeg=0
db=2
while (a+b<szam):
    # print(a+b,end="")
    b=osszeg
    a=b
    db+=1
    print(db+1)

