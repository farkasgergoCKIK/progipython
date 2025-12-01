a=int(input())
b=int(input())

if (a > 0 and b > 0):
    print("egy")
elif (a < 0 and b > 0):
    print("ketto")
elif (a > 0 and b < 0):
    print("harom")
elif (a < 0 and b < 0):
    print("negy")
elif (a == 0 and b != 0):
    print("x tengely")
elif (a != 0 and b == 0):
    print("y tengely")
else:
    print("origó")
