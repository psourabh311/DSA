def alphaHill(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")  # Print leading spaces
        ch = ord('A')  # Start with 'A'
        breakpoint = (2 * i + 1) // 2  # Correct integer breakpoint
        for j in range(2 * i + 1):  # Full row width
            print(chr(ch), end="")   
            if j < breakpoint:
                ch += 1  # Increment until the middle
            else:
                ch -= 1  # Decrement after the middle
        print()  # Move to the next line
n = int(input("Enter the value of n: "))
alphaHill(n)