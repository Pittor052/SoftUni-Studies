from collections import deque

queue = deque([])

text = input()

while 'End' not in text:
    if 'Paid' not in text:
        queue.append(text)
    else:
        print(*queue, sep='\n')
        queue.clear()
    text = input()
print(f'{len(queue)} people remaining.')

