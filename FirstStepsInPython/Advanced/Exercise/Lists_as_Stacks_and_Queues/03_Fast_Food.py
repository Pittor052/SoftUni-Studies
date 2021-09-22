from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))

while not food == 0:
    if len(orders) == 0:
        break

    elif orders[0] <= food:
        food -= orders[0]
        orders.popleft()

    else:
        break

if len(orders) == 0:
    print('Orders complete')

else:
    print(f'Orders left: ', end='')
    print(*orders, sep=" ")
# # 02 Solution
# quantity_food = int(input())
# orders_input = list(map(lambda x: int(x), input().split()))
# print(max(orders_input))
# stopped = False
#
# for order in orders_input:
#
#     if quantity_food - order < 0:
#         index = orders_input.index(order)
#         print(f"Orders left: ", end="")
#         print(*orders_input[index:], sep=" ")
#         stopped = True
#         break
#
#     else:
#         quantity_food -= order
#
# if not stopped:
#     print("Orders complete")
