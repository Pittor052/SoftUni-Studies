incoming_dragons = int(input())

dragons_den = {}

while incoming_dragons:
    dragon_spawn = input()
    # {type} {name} {damage} {health} {armor}
    rarity, name, damage, health, armor = dragon_spawn.split(" ")
    # default values: health 250, damage 45, and armor 10
    if damage == "null":
        damage = "45"
    damage = int(damage)

    if health == "null":
        health = "250"
    health = int(health)

    if armor == "null":
        armor = "10"
    armor = int(armor)

    if rarity not in dragons_den:
        dragons_den[rarity] = [{"name": name, "damage": damage, "health": health, "armor": armor}]
    else:
        new = True
        for check in dragons_den[rarity]:
            if check["name"] == name:
                check.update({'name': name, 'damage': damage, 'health': health, 'armor': armor})
                new = False
                break
        if new:
            dragons_den[rarity].append({"name": name, "damage": damage, "health": health, "armor": armor})

    incoming_dragons -= 1

# print(dragons_den)
for x, y in dragons_den.items():
    # {Type}::({damage}/{health}/{armor})
    average = {"damage": 0, "health": 0, "armor": 0}
    for rec in y:
        average["damage"] += rec["damage"]
        average["health"] += rec["health"]
        average["armor"] += rec["armor"]
    print(f"{x}::({average['damage'] / len(y):.2f}/{average['health'] / len(y):.2f}/{average['armor'] / len(y):.2f})")
    for dragon in sorted(y, key=lambda r: r["name"]):
        print(f"-{dragon['name']} -> damage: {dragon['damage']}, health: {dragon['health']}, armor: {dragon['armor']}")

# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50
# # TEST
# 2
# Red Bazgargal 100 2500 25
# Red Bazgargal 100 2500 24