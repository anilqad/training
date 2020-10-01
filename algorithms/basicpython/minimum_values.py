import array as ar
a=ar.array('i',[1,2,4,9,1,258,87,-8,-52])
minn=a[0]
maxe=a[0]
for i in range(0,len(a)):
    if a[i] < minn :
        minn=a[i]
    if a[i] > maxe:
        maxe = a[i]
print(maxe)
print(minn)
