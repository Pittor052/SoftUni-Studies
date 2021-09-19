from collections import deque

quantity = int(input())
queue = deque([])
stop = False
output = []
while True:

    if stop:
        break

    text = input()

    if text == 'Start':
        litres = input().split()

        while True:

            if litres[0] == 'End':
                stop = True
                break

            elif len(litres) < 2:

                litres = int(litres[0])

                if litres <= quantity:
                    quantity -= litres
                    output.append(f'{queue.popleft()} got water')

                else:
                    output.append(f'{queue.popleft()} must wait')

            else:
                quantity += int(litres[1])

            litres = input().split()
    else:
        queue.append(text)

print(*output, sep="\n")
print(f'{quantity} liters left')
