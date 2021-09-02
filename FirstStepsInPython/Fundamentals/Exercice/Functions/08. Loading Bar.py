def loading(num):
    num = int(num / 10)
    bar = ".........."
    for i in range(num):
        bar = bar.replace('.', '%', 1)
    if 0 < num < 10:
        print(f"{num}0% [{bar}]")
        print("Still loading...")
    else:
        print(f"100% Complete!")
        print(f"[{bar}]")


loading(int(input()))