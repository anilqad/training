def printPairs(arr, arr_size, sum):
    s = set()
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if temp in s:
            print("Pair with given sum " + str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
        s.add(arr[i])
A = [1, 2, 3, 9, 10, 8]
n = 12
printPairs(A, len(A), n)
