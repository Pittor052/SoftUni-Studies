price_vegetables = float(input())
price_fruit = float(input())
vegetable_kg = float(input())
fruit_kg = float(input())

income_vegetables = price_vegetables * vegetable_kg
income_fruits = price_fruit * fruit_kg
total_income = income_vegetables + income_fruits
total_income /= 1.94
print(f"{total_income:.2f}")
