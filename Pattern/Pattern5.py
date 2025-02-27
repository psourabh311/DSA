def seeding(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print("* ",end="")
        print()
n = int(input("Enter the value of n: "))
seeding(n)