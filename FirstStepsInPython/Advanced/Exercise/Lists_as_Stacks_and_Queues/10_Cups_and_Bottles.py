# # 01 solution
# from collections import deque
# #  On the first line of input, you will receive the integers, representing the cups&#39; capacity, separated by a
# # single space.
# #  On the second line of input, you will receive the integers, representing the filled bottles, separated by a
# # single space.
#
# cups = deque(int(x) for x in input().split())  # popleft
# bottles = deque(int(x) for x in input().split())  # pop
# wasted_water = 0
#
# while True:
#     if not cups or not bottles:
#         break
#
#     current_cup = cups.popleft()
#     current_bottle = bottles.pop()
#     transfer = 0
#
#     while current_cup > 0:
#         current_cup -= current_bottle
#         transfer = current_cup
#
#         if transfer > 0:
#             current_bottle = bottles.pop()
#
#     wasted_water += abs(transfer)
#
# if cups:
#     remaining_cups = [str(x) for x in cups]
#     print(f'Cups: {" ".join(remaining_cups)}')
#
# elif bottles:
#     remaining_bottles = [str(x) for x in bottles]
#     print(f'Bottles: {" ".join(remaining_bottles)}')
#
# print(f'Wasted litters of water: {wasted_water}')
# # 02 solution
from collections import deque
#  On the first line of input, you will receive the integers, representing the cups&#39; capacity, separated by a
# single space.
#  On the second line of input, you will receive the integers, representing the filled bottles, separated by a
# single space.

cups = deque(int(x) for x in input().split())  # popleft
bottles = deque(int(x) for x in input().split())  # pop
wasted_water = 0
while True:
    if not cups or not bottles:
        break

    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    while current_cup > 0:
        current_bottle -= 1
        current_cup -= 1

        if current_bottle == 0 and not current_cup == 0:
            current_bottle = bottles.pop()

    wasted_water += current_bottle

if cups:
    remaining_cups = [str(x) for x in cups]
    print(f'Cups: {" ".join(remaining_cups)}')

elif bottles:
    remaining_bottles = [str(x) for x in bottles]
    print(f'Bottles: {" ".join(remaining_bottles)}')

print(f'Wasted litters of water: {wasted_water}')

