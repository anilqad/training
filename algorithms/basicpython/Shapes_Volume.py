import math
p=math.pi
def cylinder():
    x = int(input("enter the cylinder area "))
    y = int(input("enter the cylinder  area "))
    print("Cyinder value is ", p * x *y)
    return
def sphare():
    r = int(input("enter the Spahare radius area "))
    print("The surface  of Sphere is ",4/3 *p * (r *r * r ))
    return
def cone():
    r = int(input("enter the CONE Radius "))
    h = int(input("enter the CONE Height "))
    print("The surface  of CONE  is ", p * (r * r ) * (h/3))
    return
def cube():
    a = int(input("enter the CUBE Edge "))
    print("The surface  of CUBE  is ",  a * a * a)
    return


print("Calculate surface and volume : \n 1 is a Cylinder \n 2 is a Sphere \n 3 is a CONE \n 4 is CUBE")
select = int(input("Select operations form 1, 2, 3, 4 :"))

if select == 1:
    cylinder()

elif select == 2:
    sphare()

elif select == 3:
    cone()

elif select == 4:

    cube()
else:
    print("enter the correct number")

