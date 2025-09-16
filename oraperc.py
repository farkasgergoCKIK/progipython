#be 12:15, 45perc
#ki: 13:00

import math

ora=int(input())
perc=int(input())

hozzaadottperc=int(input())

osszesperc=perc+hozzaadottperc

ujora=ora+math.floor(osszesperc/60)

ujora=ujora%24

ujperc=osszesperc%60

print(f"Új idő: {ujora}:{ujperc:02d}")
