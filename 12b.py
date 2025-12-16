import random

n=int(input())
t=[]

utasokszama=0

for i in range(n-1):
    felszall=random.randint(0,100)
    t.append(felszall)
    t.append(random.randint(0,utasokszama))
    utasokszama+=felszall
t.append(0)
t.append(utasokszama)

for i in range(len(t)):
               print(f'{t[i]} fel {t[i]} le')