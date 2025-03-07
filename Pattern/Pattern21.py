def getStarPattern(n):
    print("*"*n,end="")
    print()
    if(n>1):
        for j in range(n-2):
            print("*",end="")
            for j in range(n-2):
                print(" ",end="")
            print("*",end="")
            print()
        print("*"*n,end="")
        
n=int(input("Enter the value of n: "))
getStarPattern(n)