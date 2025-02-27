def nStarTriangle(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*n-(2*i+1)):
            print("*", end="")
        print()
n = int(input("Enter the value of n: "))
nStarTriangle(n)