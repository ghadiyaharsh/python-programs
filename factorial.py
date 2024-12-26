 # Factorial of a number
def factorial():
    n = int(input("Enter the number: "))
    
    if n < 0:
        print("Factorial is not possible for negative numbers.")
    elif n == 0:
        print("Factorial of 0 is 1.")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Factorial of {n} is {factorial}.")
