def func(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{chr(65+i)}",end="")
        print()
n = int(input("Enter the value of n: "))
func(n)