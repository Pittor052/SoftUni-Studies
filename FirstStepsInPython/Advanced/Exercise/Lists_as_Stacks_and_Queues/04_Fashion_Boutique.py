pile_clothes = [int(x) for x in input().split()]
capacity = int(input())
clothes_capacity = 0
boxes = 1

while pile_clothes:
    item = pile_clothes.pop()
    clothes_capacity += item

    if clothes_capacity > capacity:
        clothes_capacity = item
        boxes += 1

print(boxes)
