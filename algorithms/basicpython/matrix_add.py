a = [[1, 2, 3],
     [9, 5, 1],
     [6, 2, 3]]
b=  [[1, 2, 6],
     [5, 1, 3],
     [3, 2, 7]]
c=  [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
for r in c:
    print(r)
