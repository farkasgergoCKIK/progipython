#3. Mekegő nyelv
#Feladat
#Kiss Dénes A magyar nyelvről1
#szóló írásában olvashatjuk, hogy a magyar nyelv egy
#mekegő nyelv, azaz magyarok sok „e” betűt használnak. Készíts programot, ami megnézi, hogy az
#„e” és „é” betűk száma a magánhangzók számához képes hány százalék!
#Bemenet
#A bemeneten egy tetszőleges hosszúságú szöveg szerepeljen.
#Kimenet
#A kimenet egészre kerekítve szerepeljen az „e” és „é” betűk számának aránya.
#Példa
#Be:
#Ez egy nagyon elegáns feladat!
#Ki:
#50%


szoveg=input("Ez egy nagyon elegáns feladat! ")

maganhangzok = "aáeéiíoóöőuúüű"
maganhazok_szama=0
e_szama=0

for betu in szoveg.lower():
    if betu in maganhangzok:
        maganhangzok_szama += 1
        if betu== 'e' or betu == 'é':
            e_szamaq  += 1


if maganhangzok_szama == 0:
    arany=0
else:
    arany= round((e_szama / maganhangzok_szama) * 100)

    print(f"{arany}%")


