import array as ar
a=ar.array('i',[1,2,4,9,1,258,87,-1])

for i in range(len(a)):
    for j in range(i + 1, len(a)):

        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]
print(a)
print("Minimam valis is ",a[0])
print("Maxima Value is ",a[-1])
