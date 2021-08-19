number = float(input())
convert_from = input()
convert_to = input()
mm = str("mm")
cm = str("cm")
m = str("m")
if convert_from == mm and convert_to == m:
    print(f"{number / 1000:.3f}")
elif convert_from == m and convert_to == cm:
    print(f"{number * 100:.3f}")
elif convert_from == cm and convert_to == m:
    print(f"{number / 100:.3f}")
elif convert_from == cm and convert_to == mm:
    print(f"{number * 10:.3f}")
elif convert_from == mm and convert_to == cm:
    print(f"{number / 10:.3f}")
elif convert_from == m and convert_to == mm:
    print(f"{number * 1000:.3f}")