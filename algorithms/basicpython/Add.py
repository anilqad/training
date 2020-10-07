# x=int(input("enter the first number"))
# y=int(input("enter the second number"))
# print("your entered values are ", "X: ",x , "Y: ",y)
# z=x+y
# print("The sum of number is ",z)


def sum10(a, b):
    if sum([a, b]) % 10 == 0: return True; return False

print(sum10(7, 3))
print (sum10(5, 15))

def is_greater(x, y):
    if x > y:
       return True
    else:
       return False
print(is_greater(5,7))