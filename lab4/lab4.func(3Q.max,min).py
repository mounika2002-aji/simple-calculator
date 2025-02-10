#3Q.Using max() and min() functions display the maximum and minimum of 5 random numbers

import random

# Generating 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Displaying the random numbers
print(f"Random numbers: {random_numbers}")

# Using max() and min() to find the maximum and minimum values
max_num = max(random_numbers)
min_num = min(random_numbers)

# Displaying the results
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
