#1. Calculate the multiplication and sum of two numbers
def calculate_multiplication_and_sum(num1,num2):
    """
    This function takes two numbers as input'
    returns their multiplication and sum.
    """
    multiplication = num1 * num2 # Calculate multiplication
    addition = num1 + num2 # Calculate sum
    return multiplication,addition

# Example usage
number1 = 5  # First number
number2 = 3  # Second number

# Calling function and storing results
multiplication_result, sum_result = calculate_multiplication_and_sum(number1, number2)
# Displaying output
print(f"Multiplication: {multiplication_result}")
print(f"Sum: {sum_result}")
