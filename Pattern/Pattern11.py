def nBinaryTriangle(n):
    for i in range(n):
        for j in range(i+1):
            k = i+j
            print("0 " if k%2!=0 else "1 ", end="")
        print()
n = int(input("n = "))
nBinaryTriangle(n)
