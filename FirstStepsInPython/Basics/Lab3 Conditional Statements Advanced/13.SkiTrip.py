days = int(input())
room_type = str(input())
score = str(input())

one = False
apt = False
pr = False

if room_type == "room for one person":
    one = True
elif room_type == "apartment":
    apt = True
elif room_type == "president apartment":
    pr = True

a = False
b = False
c = False

if days < 10:
    a = True
elif 10 <= days <= 15:
    b = True
elif days > 15:
    c = True
days = days - 1
sc = False

if score == "positive":
    sc = True

final_price = 0

if one:
    final_price = days * 18
    if sc:
        final_price = (final_price * 0.25) + final_price
        print(f"{final_price:.2f}")
    else:
        final_price = final_price - (final_price * 0.1)
        print(f"{final_price:.2f}")

elif apt:
    if a:
        final_price = (days * 25) * 0.7
        if sc:
            final_price += (final_price * 0.25)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")

    elif b:
        final_price = (days * 25) * 0.65
        print(final_price)
        if sc:
            final_price += (final_price * 0.25)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")

    elif c:
        final_price = (days * 25) * 0.5
        if sc:
            final_price += (final_price * 0.25)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")
elif pr:
    if a:
        final_price = (days * 35) * 0.9
        if sc:
            final_price += (final_price * 0.25)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")

    elif b:
        final_price = (days * 35) * 0.85
        if sc:
            final_price += (final_price * 0.25)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")

    elif c:
        final_price = (days * 35) * 0.80
        if sc:
            final_price += (0.25 * final_price)
            print(f"{final_price:.2f}")
        else:
            final_price -= (final_price * 0.1)
            print(f"{final_price:.2f}")
