def prime_or_not(x):
    if x>1:
        for i in range(2,x):
            if (x % i )== 0:
                print(x,"This is NOT A Prime Number")
                break
        else:
            print(x,"This Is a Prime")
prime_or_not(7)
prime_or_not(97)


x= int(input("enter start value"))
b= int(input("enter end value"))
for i in range(x,b+1):
    prime_or_not(i)
print("done")