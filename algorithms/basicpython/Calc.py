x=int(input("enter the Number for calc"))
if x<0:
    print("enter the correct number")
y = int(input("enter First Number"))
z = int(input("enter Second Number"))
if x==1:
    print("1 Is sum of numbers", y+z)
elif x==2:
    print("1 Is SUB of numbers", y - z)
elif x==3:
    print("1 Is Multiplication of numbers", y * z)
elif x==4:
    print("1 Is Division of numbers", y / z)
else:
    print("enter the correct number")


