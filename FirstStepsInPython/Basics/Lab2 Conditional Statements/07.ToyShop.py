trip_price = float ( input () )
puzzles = int ( input () )
dolls = int ( input () )
bears = int ( input () )
minions = int ( input () )
trucks = int ( input () )
money = (puzzles * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)
num_toys = puzzles + dolls + bears + minions + trucks
money = 0.9 * money      # dediction of rent

if num_toys >= 50:
    money = 0.75 * money # dediction of discount
if money >= trip_price:
    print ( f"Yes! {money - trip_price:.2f} lv left." )
else:
    print ( f"Not enough money! {trip_price - money:.2f} lv needed." )