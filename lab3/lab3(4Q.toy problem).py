#4Q.A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount. 

# Function to calculate net amount after discount
def calculate_discount(product_code, order_amount):
    """
    This function calculates the net amount after applying discount based on product type and order value.
    """
    if product_code == 1:  # Battery-Based Toys
        if order_amount > 1000:
            discount = 0.10  # 10% discount for orders above Rs. 1000
        else:
            discount = 0
    elif product_code == 2:  # Key-Based Toys
        if order_amount > 100:
            discount = 0.05  # 5% discount for orders above Rs. 100
        else:
            discount = 0
    elif product_code == 3:  # Electrical Charging Based Toys
        if order_amount > 500:
            discount = 0.10  # 10% discount for orders above Rs. 500
        else:
            discount = 0
    else:
        return "Invalid product code!"

    # Calculate net amount after applying discount
    discount_amount = order_amount * discount
    net_amount = order_amount - discount_amount
    return net_amount

# Taking user input for product code and order amount
product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging): "))
order_amount = float(input("Enter the order amount: "))

# Calculating the net amount after discount
net_amount = calculate_discount(product_code, order_amount)

# Displaying the result
print(f"The net amount to be paid is Rs. {net_amount:.2f}") 
