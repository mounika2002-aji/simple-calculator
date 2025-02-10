#1Q.Python program to check leap year 

# Function to check if a year is a leap year
def is_leap_year(year):
    """
    A year is a leap year if:
    - It is divisible by 4,
    - If divisible by 100, it must also be divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Taking user input for the year
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
