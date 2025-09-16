karakter=input()
eltolas=int(input())
print(karakter)
print(chr(ord(karakter)-ord("a")+eltolas%26+ord("a")))
