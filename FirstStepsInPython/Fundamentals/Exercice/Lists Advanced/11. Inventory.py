backpack = input().split(", ")
command = input().split(" - ")
while not command[0] == "Craft!":
    if command[0] == "Collect" and command[1] not in backpack:
        backpack.append(command[1])
    if command[0] == "Renew" and (command[1] in backpack):
        backpack.remove(command[1])
        backpack.append(command[1])
    if command[0] == "Combine Items":
        items = command[1].split(":")
        if items[0] in backpack:
            item_index = backpack.index(items[0])
            backpack.insert(item_index + 1, items[1])
    if command[0] == "Drop" and (command[1] in backpack):
        backpack.remove(command[1])
    command = input().split(" - ")
print(", ".join(list(filter((lambda x: x), backpack))))

# Iron, Sword
# Drop - Bronze
# Combine Items - Sword:Bow
# Renew - Iron
# Craft!
