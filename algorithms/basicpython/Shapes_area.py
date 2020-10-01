import math
def square():
    x = int(input("enter the square area "))
    print("share valus is ",  x * x * x)


def rectangle( ):
    l = int(input("Enter rectangle length: "))
    b = int(input("Enter rectangle breadth: "))
    print("The area of rectangle is ", l * b)

def circle( ):
    p=math.pi
    r = int(input("Enter radious length: "))
    print("The area of circle is ", p * r * r)

def triangle( ):
    b = int(input("Enter Triangle Base: "))
    h = int(input("Enter Triangle Height: "))
    print("The area of traingle is ", 0.5 * (b * h))

def righttraingle( ):
    a = int(input("Enter RightTriangle A leg length : "))
    b = int(input("Enter RightTriangle B leg Length: "))
    print("The area of right rectangle is ", 0.5 * (a * b))

print("Calculate Shape Area : \n 1 is a Sequre  \n 2 is rectangle \n 3 is Circle \n 4 is Triangle \n 5 is Right Angle ")

select = int(input("Select operations form 1, 2, 3, 4, 5 :"))

if select == 1:
    square()

elif select == 2:
    rectangle()
elif select == 3:
   circle()
elif select == 4:
    triangle()
elif select == 5:
    righttraingle()

else:
    print("Select the correct Number")