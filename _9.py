# calculate factorial 
def factorial(n):
    if n < 0:
        return "Not Exist"

    elif n == 0 or n == 1:
        return 1

    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i

        return fact

N = int(input("Enter the number: "))
print(f"The factorial of {N} is: {factorial(N)}")