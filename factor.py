def factorial_calculation(n):
    if n == 0:
        return 1
    else:
        return n * factorial_calculation(n - 1)

# Get the number from the user
number = float(input("Enter a number: "))

# Calculate the factorial of the entered number
result = factorial_calculation(number)

print(f"The factorial of {number} is {result}")