def prime(x):
    if x == 1:
        return False

    for i in range(2,x):
        if (x % i) == 0:
            return False
    else:
        return True

def main():
    if prime(10):
        print("Is Prime")
    else:
        print("Not prime")


if __name__ == "__main__":
    main()

