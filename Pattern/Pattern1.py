def nForest(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        print()
n = int(input("Enter the value of n: "))
nForest(n)