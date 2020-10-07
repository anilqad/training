import math
import array as arr
# def dtoB(n):
#     if n > 1:
#         dtoB(n // 2)
#     print(n % 2, end=' ')
# dnum=int(input("enter the Decimal number:"))
# dtoB(dnum)

num = int(input("enter the number"))
re=""
while num >=1:
    re= re + str(num % 2)
    num=math.floor(num / 2)
bina=""
for i in range(len(re)-1,-1,-1):
    bina=bina+re[i]
print("the binary number is:",bina)


## using reverse ###
for s in reversed(re):
    print(s, end="")






