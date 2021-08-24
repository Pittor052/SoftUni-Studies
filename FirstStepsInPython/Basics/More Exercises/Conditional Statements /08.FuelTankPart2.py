fuel_type = str(input())
fuel_litres = float(input())
card = str(input())

gas_price = fuel_litres * 0.93
gasoline_price = fuel_litres * 2.22
diesel_price = fuel_litres * 2.33
small_discount = fuel_litres * 0.08
big_discount = fuel_litres * 0.1
card_gas = fuel_litres * (0.93 - 0.08)
card_gasoline = fuel_litres * (2.22 - 0.18)
card_diesel = fuel_litres * (2.33 - 0.12)

if card == "No":

    if fuel_litres < 20:

        if fuel_type == "Gas":
            print(f"{gas_price:.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{gasoline_price:.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{diesel_price:.2f} lv.")

    elif 20 <= fuel_litres <= 25:

        if fuel_type == "Gas":
            print(f"{gas_price - (gas_price * 0.08):.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{gasoline_price - (gasoline_price * 0.08):.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{diesel_price - (diesel_price * 0.08):.2f} lv.")

    elif fuel_litres > 25:

        if fuel_type == "Gas":
            print(f"{gas_price - (gas_price * 0.1):.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{gasoline_price - (gasoline_price * 0.1):.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{diesel_price - (diesel_price * 0.1):.2f} lv.")
elif card == "Yes":

    if fuel_litres < 20:
        if fuel_type == "Gas":
            print(f"{card_gas:.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{card_gasoline:.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{card_diesel:.2f} lv.")

    elif 20 <= fuel_litres <= 25:
        if fuel_type == "Gas":
            print(f"{card_gas - (card_gas * 0.08):.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{card_gasoline - (card_gasoline * 0.08):.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{card_diesel - (card_diesel * 0.08):.2f} lv.")

    elif fuel_litres > 25:
        if fuel_type == "Gas":

            print(f"{card_gas - (card_gas * 0.1):.2f} lv.")

        elif fuel_type == "Gasoline":
            print(f"{card_gasoline - (card_gasoline * 0.1):.2f} lv.")

        elif fuel_type == "Diesel":
            print(f"{card_diesel - (card_diesel * 0.1):.2f} lv.")
