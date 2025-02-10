#2Q.two variables and print that which variable is largest using ternary operato

# Define two variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Using ternary operator to find the largest number
largest = num1 if num1 > num2 else num2

# Print the result
print(f"The largest number is: {largest}")
