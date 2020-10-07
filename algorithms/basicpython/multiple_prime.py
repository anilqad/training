from prime import prime

for i in range(5, 10):
    if prime(i):
        print(i, " is Prime")
    else:
        print(i, "is not prime")
