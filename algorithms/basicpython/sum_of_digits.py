n=int(input("Enter the number:"))
to=0
while n>0:
    dig=n % 10
    to=to+dig
    n=n//10
print("The total sum of digits is:",to)

# x=123
# x= x // 10
# print(x)