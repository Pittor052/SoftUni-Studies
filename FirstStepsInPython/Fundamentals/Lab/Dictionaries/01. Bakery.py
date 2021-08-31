# This is your first task in your new job. You were tasked to create a list of the stock in a bakery
# and you really don't want to fail at you first day at work.
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – the value and so on).
# Create a dictionary with all the keys and values and print it on the console
line_input = input().split()
bakery = {}
for i in range(0, len(line_input), 2):
    item = line_input[i]
    quantity_in_stock = int(line_input[i + 1])
    bakery[item] = quantity_in_stock
print(bakery)

# # INPUT
# bread 10 butter 4 sugar 9 jam 12
# # OUTPUT
# # {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
