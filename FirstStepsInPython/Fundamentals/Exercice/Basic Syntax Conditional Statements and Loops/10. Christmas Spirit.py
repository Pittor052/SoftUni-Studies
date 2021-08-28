quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
money_spent = 0
count = 0
spirit = 0
while days > 0:
    days -= 1
    count += 1
    if count % 11 == 0:
        quantity += 2
    if count % 2 == 0:
        money_spent += ornament_set * quantity
        spirit += 5
    if count % 3 == 0:
        money_spent += (tree_skirt * quantity) + (tree_garlands * quantity)
        spirit += 13
    if count % 5 == 0:
        money_spent += tree_lights * quantity
        spirit += 17
        if count % 3 == 0:
            spirit += 30
    if count % 10 == 0:
        spirit -= 20
        money_spent += tree_skirt + tree_lights + tree_garlands

if count % 10 == 0:
    spirit -= 30
print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit}")
