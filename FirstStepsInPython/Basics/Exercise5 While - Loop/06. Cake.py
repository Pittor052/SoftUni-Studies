width = int(input())
length = int(input())
area = width * length
num_pieces = int()
no_more_cake = False
while area > 0:
    pieces = input()
    try:
        num_pieces = int(pieces)
        area -= num_pieces
    except:
        no_more_cake = True
        break

if no_more_cake:
    print(f"{area} pieces are left.")
else:
    print(f"No more cake left! You need {abs(area)} pieces more.")