#Feladat 
# Írj programot, amely egy menürendszer segítségével 1-es menüpont választása esetén bekér 
# egy nevet; 2., 3. és 4. menü kiválasztása után három különböző módon üdvözli a felhasználót a 
# megadott név alapján; míg az 5. menüpont választása esetén kilép a programból.
# Bemenet
# A megfelelő menüpont száma. Egyes menüpont esetén egy nevet kell megadni.
# Kimenet
# Amennyiben helytelen menüpontot ad meg, újra kirajzolja a menüt, máskülönben a 
# megfelelő menüponthoz tartozó bekérés, illetve köszöntés jelenik meg. 
# Példa 1
# 1 – Add meg a nevet
# 2 – Üdv {0}!
# 3 – Helló {0}!
# 4 – Szia {0}!
# 5 – Kilépés. 
# Be:
# 1
# Emánuel
# Példa 2
# Be:
# 2
# Ki:
# Üdv Emánuel

menu=""
while (menu!="5"):
    print("1 – Add meg a nevet")
    print("2 – Üdv {0}!")
    print("3 – Helló {0}!")
    print("4 – Szia {0}!")
    print("5 – Kilépés.")
    menu=int(input("Kérem válasszon menüpontot: "))
    if (menu=="1"):
        nev=input("Kérem adja meg a nevét: ")
    elif (menu=="2"):
        print(f"Üdv {nev}!")
    elif (menu=="3"):
        print(f"Helló {nev}!")
    elif (menu=="4"):
        print(f"Szia {nev}!")
