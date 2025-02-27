def nTriangle(n):
    for i in range(n):  # Start i from 0 to n-1
        for j in range(i+1):  # Start j from 0 to i
            print(f"{j+1} ", end="")  # Add 1 to j for 1-based output
        print()  # Move to the next line after each row
n = int(input("Enter the value of n: "))
nTriangle(n)