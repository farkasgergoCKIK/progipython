jegy=-1
osszeg=0
db=0    
while jegy!=0:
    jegy=int(input("Adja meg a jegyet (0 a kilepeshez): "))
    osszeg+=jegy
    darab+=1

    print(round(osszeg/(db-1),2))