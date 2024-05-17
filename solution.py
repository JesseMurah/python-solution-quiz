def calculateTax(price):
    tax = 0.07
    return price * tax

def calculateAfterTax(price):
    return price + calculateTax(price)

def calculatePricebeforeTax(price, quantity):
    return price * quantity

"""
def calculatePriceafterTax(price, quantity):
    return calculateTotal(price) * quantity

a = input("Enter the name of the item: ")
b = float(input("Enter the price per unit of the item: "))
c = float(input("Enter the quantity of the item: "))

items = 3
for i in range(items):
    name = input("Enter the naem of the item: ")
    pricePerUnit = float(input("Enter the price per unit of the item: "))
    quantity = float(input("Enter the quantity of the item: "))

    total = calculatePricebeforeTax(pricePerUnit, quantity)
    print(f"The total price for {name} is: ", total)

    print(f"The tax for {name} is : ", "{:.2f}".format(calculateTax(total)))
    print(f"The final total for {name} is: ","{:.2f}".format(calculateAfterTax(total)))
"""




items = 3
total_before_tax = 0
total_tax = 0
final_total = 0

for i in range(items):
    name = input("Enter the name of the item: ")
    price_per_unit = float(input("Enter the price per unit of the item: "))
    quantity = int(input("Enter the quantity of the item: "))

    total = calculatePricebeforeTax(price_per_unit, quantity)
    total_before_tax += total
    tax = calculateTax(total)
    total_tax += tax
    final_total += total + tax

    print(f"The subtotal for {name} is: ", "{:.2f}".format(total))

print(f"The total before tax for all items is: ", "{:.2f}".format(total_before_tax))
print(f"The total tax for all items is : ", "{:.2f}".format(total_tax))
print(f"The final total for all items is: ","{:.2f}".format(final_total))