#3

# osszeg=0
# for i in range(len(t)):
#     osszeg+=t[i]
    
# maxi=0
# for i in range(len(t)):
#     if t[i]>t[maxi]:
#         maxi=i

t=[]
maxi=0
osszeg=t[maxi]
maxosszeg=t[maxi]
for i in range(len(t)):
    osszeg+=t[i]
    if (osszeg>t[maxi]):
        maxi=i
        maxosszeg=osszeg

        print()