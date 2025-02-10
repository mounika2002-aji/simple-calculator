#3Q.Python program to convert the temperature in degree centigrade to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

def celsius_to_fahrenheit(celsius):
    """
    This function converts temperature from Celsius to Fahrenheit.
    Formula: (C × 9/5) + 32 = F
    """
    fahrenheit = (celsius * 9/5) + 32  # Conversion formula
    return fahrenheit
# user input
celsius_temp = float(input("Enter temperature in Celsius: "))# Temperature in Celsius
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)  # Convert to Fahrenheit

# Displaying output
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
