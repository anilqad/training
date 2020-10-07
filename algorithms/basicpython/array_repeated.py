import array as arr
a = arr.array('i',[1, 2, 3, 4, 2, 7, 8, 8, 3])
# print("Duplicate elements in given array: ")
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        # print(i,j)
        if (a[i] == a[j]):
            print(a[i])
print("Done")
