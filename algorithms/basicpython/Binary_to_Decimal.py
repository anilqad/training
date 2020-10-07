b_num = list(input("Enter a binary number: "))

dec = 0

for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == "1":
        dec = dec + pow(2, i)
print("The decimal value of the number is",dec)

