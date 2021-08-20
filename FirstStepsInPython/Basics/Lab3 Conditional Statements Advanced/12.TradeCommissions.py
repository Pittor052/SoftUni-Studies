city = str(input())
s = float(input())

sa = False
va = False
plo = False

if city == "Sofia":
    sa = True
elif city == "Varna":
    va = True
elif city == "Plovdiv":
    plo = True


a = False
b = False
c = False
d = False

if 0 <= s <= 500:
    a = True
elif 500 <= s <= 1000:
    b = True
elif 1000 < s <= 10000:
    c = True
elif s > 10000:
    d = True

if sa:
    if a:
        print(f"{s * 0.05:.2f}")
    elif b:
        print(f"{s * 0.07:.2f}")
    elif c:
        print(f"{s * 0.08:.2f}")
    elif d:
        print(f"{s * 0.12:.2f}")
    else:
        print("error")
elif va:
    if a:
        print(f"{s * 0.045:.2f}")
    elif b:
        print(f"{s * 0.075:.2f}")
    elif c:
        print(f"{s * 0.10:.2f}")
    elif d:
        print(f"{s * 0.13:.2f}")
    else:
        print("error")
elif plo:
    if a:
        print(f"{s * 0.055:.2f}")
    elif b:
        print(f"{s * 0.08:.2f}")
    elif c:
        print(f"{s * 0.12:.2f}")
    elif d:
        print(f"{s * 0.145:.2f}")
    else:
        print("error")
else:
    print("error")
