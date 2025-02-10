#2Q.Using input function take two number and then swap the number 

# Taking user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swapping the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Displaying the swapped numbers
print(f"After swapping, first number: {num1}, second number: {num2}")
