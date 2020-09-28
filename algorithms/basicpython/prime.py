x=int(input("enter the number"))
if x>1:
    for i in range(2,x):
        if (x % i )== 0:
            print("This is NOT A Prime Number")
            break
    else:
        print("This Is a Prime")
else:
    print("this is Not a prime")

######

lower = int(input("enter The starting number"))
upper = int(input("enter last number"))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
print("done")


