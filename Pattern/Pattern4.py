def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{i+1} ",end="")
        print()
n = int(input("Enter the value of n: "))
triangle(n)