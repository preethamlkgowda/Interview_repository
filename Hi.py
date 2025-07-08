def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b != 0:
# Define a function to add two numbers and return the result.
        return a / b
    return None
# Define a function to subtract the second number from the first and return the result.

def main():
# Define a function to multiply two numbers and return the result.
    x = 10
    y = 5
# Define a function to divide the first number by the second. Returns None if the divisor is zero.
    # Check if the divisor is not zero before performing the division to avoid a runtime error.
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    # Define the main function to demonstrate the usage of arithmetic operations.
    # Initialize variable x with the value 10.
    # Initialize variable y with the value 5.
    # Call the add function with x and y, and print the result.
    # Call the subtract function with x and y, and print the result. Note: 'subtract' is incorrectly named; it should be 'sub'.
    # Call the multiply function with x and y, and print the result. Note: 'multiply' is incorrectly named; it should be 'mul'.
# Call the divide function with x and y, and print the result.

main()
