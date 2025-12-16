import random

t=[]
n=int(input())

akt=0
for i in range(n):
    v=random.randint(-10,10)
    akt+=v
    if (akt<0):
        akt=0
        if (akt>20):
            akt=20

t.append(akt)
print(t)

for i in range(len(t)):

    if i%5==0:
        print(f"{t[i]} liter/100km")
    else:
        if (i==n-1):
            print(f"{t[i]} liter/100km,", end="")

maxi=0
for i in range(1,len(t)-1,1):
    if (t[i+1]-t[i]>t[maxi+1]-t[maxi]):
        maxi=i

print(f"{maxi}-{maxi-1} időegység között volt a maximalis fogyasztás: {t[maxi]} liter/100km")

