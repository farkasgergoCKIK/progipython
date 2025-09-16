ido=input()
eltelt=int(input())
ora=int(ido.split(':')[0])
perc=int(ido.split(':')[1])
mindenPerc=ora*60+perc
aktIdo=mindenPerc+eltelt
print(f"{aktIdo//60}:{aktIdo%60}")