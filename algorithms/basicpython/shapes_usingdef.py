def square(x):
    return x * x * x

def rectangle(l, b):
    return l * b

def circle(p, r):
    return p * r

def triangle(b, h):
    return 0.5 * b * h

def righttrainglr(a, b):
    return 0.5 * (a * b)


print("Calculate Shape Area : \n 1 is a Sequre  \n 2 is rectangle \n 3 is Circle \n 4 is Triangle \n 5 is Right Angle ")

select = int(input("Select operations form 1, 2, 3, 4, 5 :"))

if select == 1:
    a = int(input("enter the square area "))
    print("share valus is ", square(a))

elif select == 2:
    l = int(input("Enter rectangle length: "))
    b = int(input("Enter rectangle breadth: "))
    print("The area of Square is ", rectangle(l, b))
elif select == 3:
    r = int(input("Enter radious length: "))
    print("The area of Square is ", circle(3.14, r))
elif select == 4:
    b = int(input("Enter radious length: "))
    h = int(input("Enter radious height: "))
    print("The area of traingle is ", triangle(b, h))
elif select == 5:
    a = int(input("Enter  length: "))
    b = int(input("Enter  length: "))
    print("The area of right rectangle is ", righttrainglr(a, b))

else:
    print("Select the correct Number")
