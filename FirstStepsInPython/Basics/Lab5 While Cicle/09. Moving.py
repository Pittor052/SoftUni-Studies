width = int(input())
depth = int(input())
height = int(input())
# Size of available space
available_space = int(width * depth * height)
no_space = bool(False)
# String we input
boxInput = str
# value for parsing
box = int()
while not no_space:
    boxInput = input()
    # Using Try-Catch exceptions to see if box can be parsed into INT
    try:
        box = int(boxInput)
        available_space -= box
    # If input cannot be parsed, throw exception to see if string says "Done"
    except:
        break
    if available_space < 0:
        no_space = True
        break
if no_space:
    print(f"No more free space! You need {abs(available_space)} Cubic meters more.")
else:
    print(f"{available_space} Cubic meters left.")
