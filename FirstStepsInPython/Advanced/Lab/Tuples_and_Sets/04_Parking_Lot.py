num_inputs = int(input())
parking = []
while num_inputs:
    command = input().split(', ')
    act = command[0]
    registration = command[1]

    if act == 'IN':
        if registration not in parking:
            parking.append(registration)
    elif registration in parking:
        parking.remove(registration)
    num_inputs -= 1
if parking:
    print(* parking, sep='\n')
else:
    print('Parking Lot is Empty')

