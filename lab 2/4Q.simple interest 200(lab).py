#4Q.Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    """
    This function calculates Simple Interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Given values
principal = 200  # Principal amount in Rs.
rate = 5         # Rate of interest per year in percentage
time = 5         # Time in years

# Calculating Simple Interest
interest = calculate_simple_interest(principal, rate, time)

# Displaying the result
print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% per year is Rs. {interest}.")
