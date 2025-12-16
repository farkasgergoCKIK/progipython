t=[90, 100, 170, 350, 550, 550, 890, 1000, 1100]

legkisebb=999999
index=0

for i in range(len(t)-1):
    emelkedes=t[i+1] - t[i]
    if emelkedes > 0 and emelkedes < legkisebb:
        legkisebb=emelkedes
        index=i

print("Az", index + 1, ". mérési ponton volt a legkisebb emelkedési szög.")
