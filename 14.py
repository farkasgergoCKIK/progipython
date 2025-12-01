#14 Rajz, háromszög 
# Feladat 
# A  felhasználó  megadja  a  négyzet  oldalát.  Készíts  egy  programot,  ami  kirajzolja  az 
# összes  lehetséges  módon  az  oldalak  és  átlók  által  megadott  egyenlőszárú  derékszögű 
# háromszegeket illetve kirajzol egy 2n hosszúságú piramist.  
# Bemenet 
# Bemenet egyetlen sorában az N (0 ≤ N ) szám kerül. 
# Kimenet 
# Kimenet a csillagokkal megrajzolt alakzatok kerüljenek.  
# Példa 
# Be: 
# 4 
# Ki: 
# * 
# ** 
# *** 
# **** 
 
 
#    * 
#   ** 
#  *** 
# **** 
 
# **** 
#  *** 
#   ** 
#    * 
 
# **** 
# *** 
# ** 
# * 
 
#    * 
#   *** 
#  ***** 
# ******* 
 
 
n=int(input(""))
for i in range(0,n,1):
    for j in range(0,n,1):
        print("*",end="")
else:
    print("",end="")

