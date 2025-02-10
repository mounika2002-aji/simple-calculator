#3Q.Python Program to Check if a Number is Positive, Negative or 0 

# Function to check if a number is positive, negative, or zero
def check_number_type(num):
    """
    This function checks if the given number is positive, negative, or zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Taking user input
num = float(input("Enter a number: "))

# Checking the type of the number
result = check_number_type(num)

# Displaying the result
print(f"The number {num} is {result}.")
