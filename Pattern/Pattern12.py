def numberCrown(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1} ",end="")
        for j in range(2*(n-i-1)):
            print("  ",end="")
        for j in range(i+1,0,-1):
            print(f"{j} ",end="") 
        print()            
            
n = int(input("n = "))
numberCrown(n)
