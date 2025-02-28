def nStarTriangle(n):
    for i in range(n):
        print("*" * (i+1))
    for i in range(n):
        print("*" * (n-i-1))
n = int(input("n = "))
nStarTriangle(n)