#be: a=5 b=3 c=5
#ki: 3<5=5

a=int(input())
b=int(input())
c=int(input())

if (a<b and a<c and b<c):
    print(f"{a}<{b}<{c}")

elif (a<b and a<c and c<b):
    print(f"{a}<{c}<{b}")   
elif (b<a and b<c and a<c):
    print(f"{b}<{a}<{c}") 
elif (b<a and b<c and c<a):
    print(f"{b}<{c}<{a}")       
elif (c<a and c<b and a<b):
    print(f"{c}<{a}<{b}")
elif (c<a and c<b and b<a):
    print(f"{c}<{b}<{a}")
elif (a==b and a<c):
    print(f"{a}={b}<{c}")
elif (a==b and a>c):
    print(f"{a}={b}>{c}")               
elif (a==c and a<b):
    print(f"{a}={c}<{b}")
elif (a==c and a>b):
    print(f"{a}={c}>{b}")



elif (b==c and b<a):
    print(f"{b}={c}<{a}")                                               

elif (b==c and b>a):    








    print(f"{b}={c}>{a}")                                   