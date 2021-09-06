line_input = input().split("|")
energy = 100
coins = 100
stop = False
for i in range(len(line_input)):
    test = line_input[i].split("-")
    if test[0] == "rest":
        gain_energy = int(test[1])

        if energy + gain_energy > 100:
            gain_energy = 100 - energy

        energy += gain_energy

        print(f"You gained {gain_energy} energy.")
        print(f"Current energy: {energy}.")

    elif test[0] == "order":

        if energy >= 30:

            energy -= 30
            coins += int(test[1])
            print(f"You earned {int(test[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= int(test[1])
        if not coins <= 0:
            print(f"You bought {test[0]}.")
        else:
            stop = True
            print(f"Closed! Cannot afford {test[0]}.")
    if stop:
        break
if not stop:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

# # INPUT 1
# rest-2|order-10|eggs-100|rest-10
# # INPUT 2
# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
# # INPUT END
