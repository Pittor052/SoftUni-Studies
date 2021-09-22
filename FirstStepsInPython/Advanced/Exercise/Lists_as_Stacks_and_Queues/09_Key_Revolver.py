from collections import deque

#  On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
#  On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
#  On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
#  On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
#  On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
bullet_price = int(input())
chambers = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
loot = int(input())
output = []
shots = 0
total_shots = 0
while True:

    if shots == chambers and not (len(bullets) == bullets.count(None)):
        output.append('Reloading!')
        total_shots += shots
        shots = 0

    if (len(locks) == locks.count(None)) or (len(bullets) == bullets.count(None)):
        break

    load = bullets.pop()
    bullets.appendleft(None)
    current_lock = locks[0]
    shots += 1

    if load <= current_lock:
        output.append('Bang!')
        locks.popleft()
        locks.append(None)
    else:
        output.append('Ping!')

bullets_left = len(bullets) - bullets.count(None)
locks_left = len(locks) - locks.count(None)
bullets_cost = bullets.count(None) * bullet_price
money_earned = loot - bullets_cost

print(*output, sep='\n')

if len(locks) == locks.count(None):
    print(f'{bullets_left} bullets left. Earned ${money_earned}')
else:
    print(f"Couldn't get through. Locks left: {locks_left}")

# #
# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500
