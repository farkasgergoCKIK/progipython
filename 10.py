szam1=int(input("Adja meg az első számot: "))
szam2=int(input("Adja meg a második számot: "))
if szam1>szam2:
    print(f"{szam1}>{szam2}")
elif szam1<szam2:
    print(f"{szam1}<{szam2}")
else:
    print(f"{szam1}={szam2}")
