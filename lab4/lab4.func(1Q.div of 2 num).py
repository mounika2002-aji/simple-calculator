#1Q.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

# Function to perform division of two numbers
def div(num1, num2):
    """
    This function takes two numbers and returns their division result.
    """
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2

# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the div function to calculate the division
result = div(num1, num2)

# Displaying the result
print(f"The division of {num1} by {num2} is: {result}")


