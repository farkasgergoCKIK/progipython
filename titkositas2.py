karakter=input("Adj meg egy karaktert: ")
elteres=int(input("Add meg az eltolás mértékét: "))

kod=ord(karakter)

titkositott_kod=(kod - 97 + elteres) % 26 + 97

titkositott_karakter=chr(titkositott_kod)

print("Titkosított karakter:", titkositott_karakter)
