def symmetry(n):
    for i in range(n):
        for j in range(n-i):
            print("* ",end="")
        for j in range(2*i):
            print("  ",end="")
        for j in range(n-i):
            print("* ",end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        for j in range(2*(n-i-1)):
            print("  ",end="")
        for j in range(i+1):
            print("* ",end="")
        print()
n = int(input("Enter the value of n: "))
symmetry(n)
