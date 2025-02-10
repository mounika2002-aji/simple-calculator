#2Q.Python Program to Find the Largest Among Three Numbers 

# Function to find the largest number among three
def find_largest(num1, num2, num3):
    """
    This function takes three numbers as input and returns the largest one.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Taking user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
largest = find_largest(num1, num2, num3)

# Displaying the result
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
