# The find() method finds the first occurrence of the specified value.
# Syntax: string.find(value, start, end)
herd = input()
sheep_count = 0
if herd.find("wolf") == len(herd) - 4:
    print("Please go away and stop eating my sheep")
else:
    for sheep in range(herd.find("wolf"), len(herd)):
        if herd[sheep] == "s":
            sheep_count += 1
    print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
# wolf, sheep, sheep, sheep, sheep, sheep
# sheep, sheep, sheep, wolf, sheep, sheep
# sheep, sheep, wolf
