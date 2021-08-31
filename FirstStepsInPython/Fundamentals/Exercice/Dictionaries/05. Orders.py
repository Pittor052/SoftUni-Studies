# Write a program that keeps information about products and their prices. Each product has a name,
# a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity and
# if its price is different, replace the price as well.
# You will receive products' names, prices and quantities on new lines. Until you receive the command "buy",
# keep adding items. When you do receive the command "buy", print the items with their names and
# total price of all the products with that name.
# Input
# Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
# "{productName} -> {totalPrice}"
# Format the total price to the 2nd digit after the decimal separator.

line_input = input()
result = {}
while not line_input == "buy":
    line_input = line_input.split()
    name = line_input[0]
    price = float(line_input[1])
    quantity = float(line_input[2])
    if name not in result:
        result[name] = {"price": price, "quantity": quantity}
    else:
        result[name].update({"price": price})
        result[name]["quantity"] += quantity

    line_input = input()

for order, nums in result.items():
    for price, quantity in nums.items():
        print(f"{order} -> {(result[order]['price'] * result[order]['quantity']):.2f}")
        break
# # INPUT 0
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
#
# # OUTPUT 0
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00
#
# # INPUT 1
# Beer 2.40 350
# Water 1.25 200
# IceTea 5.20 100
# Beer 1.20 200
# IceTea 0.50 120
# buy
#
# # OUTPUT 1
# Beer -> 660.00
# Water -> 250.00
# IceTea -> 110.00
#
# # INPUT 2
# CesarSalad 10.20 25
# SuperEnergy 0.80 400
# Beer 1.35 350
# IceCream 1.50 25
# buy
#
# # OUTPUT 2
# CesarSalad -> 255.00
# SuperEnergy -> 320.00
# Beer -> 472.50
# IceCream -> 37.50
