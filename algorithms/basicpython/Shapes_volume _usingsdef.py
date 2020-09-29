def cylinder(p,x,y):
    return p * (r * r) * h
def sphare(p,r):
    return 4/3 *p * (r *r * r)
def cone(p,r,h):
    return  p * (r * r ) * (h/3)
def cube(a):
    return a * a * a


print("Calculate surface and volume : \n 1 is a Cylinder \n 2 is a Sphere \n 3 is a CONE \n 4 is CUBE")
select = int(input("Select operations form 1, 2, 3, 4 :"))

if select == 1:
    r = int(input("enter the cylinder area "))
    h = int(input("enter the cylinder  area "))
    print("share value is ", cylinder(3.14,r,h))

elif select == 2:
    r = int(input("enter the Spahare radius area "))
    print("The surface  of Sphere is ",sphare(3.14,r))

if select == 3:
    r = int(input("enter the CONE Radius "))
    h = int(input("enter the CONE Height "))
    print("The surface  of CONE  is ", cone(3.14,r,h))

if select == 4:
    a = int(input("enter the CUBE Edge "))
    print("The surface  of CUBE  is ",cube(a))

else:
    print("enter the correct number")

