from collections import deque
line_up = deque(input().split())
throws = int(input())
turns = throws

while len(line_up) > 1:
    line_up.append(line_up.popleft())
    turns -= 1
    if turns == 0:
        print(f'Removed {line_up.pop()}')
        turns = throws

print(f'Last is {line_up.pop()}')

# George Peter Michael William Thomas Mitio
# 27
