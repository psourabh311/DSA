def alphaTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{chr(65+n-j-1)} ",end="")
        print()
n = int(input("Enter the value of n: "))
alphaTriangle(n)
