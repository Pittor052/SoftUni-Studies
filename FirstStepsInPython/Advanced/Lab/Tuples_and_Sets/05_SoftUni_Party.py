num_guests = int(input())
guest_list = []
who_did_not_came = []
while num_guests:
    guest_list.append(input())
    num_guests -= 1

while True:
    name = input()
    if name == 'END':
        break
    elif name in guest_list:
        guest_list.remove(name)

print(len(guest_list))
print(*sorted(guest_list), sep='\n')
