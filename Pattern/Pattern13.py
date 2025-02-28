def nNumberTriangle(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(f"{num} ",end="")
            num+=1
        print()
n = int(input("Enter the value of n: "))
nNumberTriangle(n)