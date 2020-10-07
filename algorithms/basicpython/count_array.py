from array import *
arr = array('i',[1,2,3,4,5,0,6,8,9,0,9,25])
aco=0
for i in arr:
    if i == 0:
        aco +=1
print("The Number of 0's in array is:", aco)