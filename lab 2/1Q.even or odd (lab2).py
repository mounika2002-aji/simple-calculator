#Q1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

import math

def triangle_area(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.
    Formula: Area = √(s * (s - a) * (s - b) * (s - c))
    where s = (a + b + c) / 2 (semi-perimeter)
    """
    s = (a + b + c) / 2  # Calculate semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
    return area

# Taking user input for triangle sides
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Checking if the sides form a valid triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # Calculate area
    area = triangle_area(side1, side2, side3)
    print(f"The area of the triangle is: {area:.2f} square units")
else:
    print("Invalid triangle sides! The sum of any two sides must be greater than the third side.")
