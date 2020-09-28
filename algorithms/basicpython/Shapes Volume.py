def volumee(name):
    if name == "1":
        r=int(input("enter the Cylinder Radius "))
        h=int(input("enter the Cylinder Height "))
        p=3.14
        cylinder_surare=2 *p *r * h + 2* p* (r*r)
        cylinder_Vol= p * (r *r) * h
        print("The surface  of Cylinder is ",cylinder_surare, "\n" "Cylinder volume:",cylinder_Vol)
    if name == "2":
        r=int(input("enter the Sphere Radius "))
        p=3.14
        sphere_surare=4* p* (r*r)
        sphere_Vol= 4/3 *p * (r *r * r)
        print("The surface  of Sphere is ",sphere_surare, "\n" "Sphere volume:",sphere_Vol)
    if name == "3":
        r = int(input("enter the CONE Radius "))
        h = int(input("enter the CONE Height "))
        p = 3.14
        cone_surare =  p * r * (r + (h + r))
        cone_Vol =   p * (r * r ) * (h/3)
        print("The surface  of CONE  is ", cone_surare, "\n" "CONE volume:", cone_Vol)


if __name__ == "__main__":
    print("Calculate surface and volume : \n 1 is a Cylinder \n 2 is a Sphere \n 3 is a CONE")
    shape_name = input("Enter the name of shape: ")
    volumee(shape_name)