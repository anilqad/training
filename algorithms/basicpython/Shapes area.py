def areacal(name):
    if name == "1":
        a=int(input("enter the square area "))
        square_area=(a *a)
        print("The area of Square is ",square_area)

    elif name == "2":
        l = int(input("Enter rectangle length: "))
        b = int(input("Enter rectangle breadth: "))
        rectangle_area = l * b
        print("The area of rectangle is ",rectangle_area)

    elif name == "3":
        r = int(input("Enter radious length: "))
        pi=3.14
        circle_area = pi * r *r
        print("The area of Circle is ",circle_area)

    elif name == "4":
        b = int(input("Enter radious length: "))
        h = int(input("Enter radious height: "))
        triangle_area = 1/2 * b *h
        print("The area of Triangle is ",triangle_area)

    elif name == "5":
        a = int(input("Enter  length: "))
        b = int(input("Enter  length: "))
        rightangle_area = 0.5*(a * b)
        print("The area of right rectangle is ",rightangle_area)
    else:
        print("entered a wrong input")


if __name__ == "__main__":
    print("Calculate Shape Area : \n 1 is a Sequre  \n 2 is rectangle \n 3 is Circle \n 4 is Triangle \n 5 is Right Angle ")
    shape_name = input("Enter the name of shape: ")
    areacal(shape_name)