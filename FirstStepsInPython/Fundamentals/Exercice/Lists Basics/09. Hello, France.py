line_input = input().split("|")
budget = float(input())
new_prices = []
old_sum = 0
new_sum = 0
for i in range(len(line_input)):
    test = line_input[i].split("->")
    if (test[0] == "Clothes" and float(test[1]) <= 50) or (test[0] == "Shoes" and float(test[1]) <= 35) or (
            test[0] == "Accessories" and float(test[1]) <= 20.50):
        if float(test[1]) <= budget:
            old_sum += float(test[1])
            new_prices.append((float(test[1]) * 1.4))
            new_sum += (float(test[1]) * 1.4)
            budget -= float(test[1])

for i in range(len(new_prices)):
    print(f"{(float(new_prices[i])):.2f}", end=" ")
profit = new_sum - old_sum
print(f"\nProfit: {profit:.2f}")
if budget + new_sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
# # INPUT 1
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
# # INPUT 2
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
# # INPUT END
