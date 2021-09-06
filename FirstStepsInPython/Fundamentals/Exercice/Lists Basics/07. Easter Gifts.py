# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space,
# in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#  "OutOfStock {gift}"
# oFind the gifts with this name in your collection, if there are any, and change their values to "None".
#  "Required {gift} {index}"
# oReplace the value of the current gift on the given index with this gift if the index is valid.
#  "JustInCase {gift}"
# oReplace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
#   On the 1st line you are going to receive the names of the gifts, separated by a single space.
#   On the next lines, until the "No Money" command is received, you will be receiving commands.
#   The input will always be valid.
# Output
#   Print the gifts in the format described above.
# 01 solution


line_gifts = input().split()
command = input()
while "No Money" not in command:
    command = command.split(" ")
    if "OutOfStock" in command:
        test_gift = command[1]
        for j in range(len(line_gifts)):
            if test_gift == line_gifts[j]:
                line_gifts[j] = "None"
    if "Required" in command:
        if 0 <= int(command[2]) < len(line_gifts):
            line_gifts[int(command[2])] = command[1]
    if "JustInCase" in command:
        line_gifts[len(line_gifts) - 1] = command[1]

    command = input()

line_gifts[:] = (value for value in line_gifts if value != "None")
print(" ".join([x for x in line_gifts]))

# # INPUT 1
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
# # INPUT 2
# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
# # INPUT END
