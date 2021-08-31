# After you have successfully completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you have to answer customers
#   if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space). On the next line
# you will be given products to search for. Check for each product, you have 2 possibilities:
#    If you have the product, print "We have {quantity} of {product} left"
#    Otherwise, print "Sorry, we don't have {product}"
line_input = input().split()
bakery = {}
for i in range(0, len(line_input), 2):
    item = line_input[i]
    quantity_in_stock = int(line_input[i + 1])
    bakery[item] = quantity_in_stock
search_for_product = input().split()
for item in search_for_product:
    if item not in bakery:
        print(f"Sorry, we don't have {item}")
    else:
        print(f"We have {bakery[item]} of {item} left")

# # INPUT
# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes
# # OUTPUT
# # Sorry, we don&#39;t have jam
# # We have 10 of cheese left
# # We have 10 of ham left
# # Sorry, we don&#39;t have tomatoes