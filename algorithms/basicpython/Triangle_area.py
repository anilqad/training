import math
def triangle():
    A = int(input("Enter The Triangle side A:"))
    B = int(input("Enter The Triangle side B:"))
    C = int(input("Enter The Triangle side C:"))
    p= (A + B + C) / 2
    print("The area of the triangle is :",math.sqrt(p*((p-A) * (p-B) * (p-C))))


print("Calculate Triangle Area :\n Enter the A , B , C area sides of Triangle ")
triangle()
