sor=input().split(" ")
a=int(sor[0])
b=int(sor[1])

kisebb=b
if a < b:
    kisebb=a
    nagyobb=b

while (kisebb>1 and not (a%kisebb==0 and b%kisebb==0)):
    kisebb-=1

print(kisebb,a*b/kisebb)

novekmeny=nagyobb

while nagyobb%a!=0 or nagyobb%b!=0:
    nagyobb+=novekmeny
print(nagyobb)

