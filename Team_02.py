"""
CSE 111 
Author: Tim Illguth
Instructor: 
File Team_02.py
"""

import datetime

# Get today's weekday as an integer (Monday is 0 and Sunday is 6)
today = datetime.datetime.today().weekday()

# Get the subtotal from the user
subtotal = float(input("Enter the subtotal: $"))

# Check if the subtotal is eligible for a discount
if subtotal >= 50 and today in [1, 2]:  # Tuesday is 1 and Wednesday is 2
    discount = subtotal * 0.1
    subtotal -= discount
    print(f"Discount: ${discount:.2f}")

# Calculate the sales tax and total amount due
tax_rate = 0.06
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

# Print the sales tax and total amount due
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Due: ${total:.2f}")


import datetime

# Get today's weekday as an integer (Monday is 0 and Sunday is 6)
today = datetime.datetime.today().weekday()

subtotal = 0
while True:
    price = float(input("Enter the price (or 0 to exit): $"))
    if price == 0:
        break
    quantity = int(input("Enter the quantity: "))
    subtotal += price * quantity

# Check if the subtotal is eligible for a discount
if subtotal >= 50 and today in [1, 2]:  # Tuesday is 1 and Wednesday is 2
    discount = subtotal * 0.1
    subtotal -= discount
    print(f"Discount: ${discount:.2f}")
elif subtotal < 50 and today in [1, 2]:  # Tuesday is 1 and Wednesday is 2
    additional_amount = 50 - subtotal
    print(f"Add ${additional_amount:.2f} to your purchase to get a discount.")

# Calculate the sales tax and total amount due
tax_rate = 0.06
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

# Print the sales tax and total amount due
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Due: ${total:.2f}")
