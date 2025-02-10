#3Q.Write a Program to Convert Kilometers to Miles

# Function to convert kilometers to miles
def kilometers_to_miles(km):
    """
    Converts kilometers to miles.
    Formula: 1 kilometer = 0.621371 miles
    """
    miles = km * 0.621371  # Conversion formula
    return miles

# Taking user input for distance in kilometers
kilometers = float(input("Enter the distance in kilometers: "))

# Converting to miles
miles = kilometers_to_miles(kilometers)

# Displaying the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
