# Напишете програма, която чете от конзолата цели числа, докато не се получи команда &quot;stop&quot;. Да се намери
# сумата на всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от
# математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да
# се изведе следното съобщение &quot;Number is negative.&quot;. В този случай въведено число се игнорира и не се
# прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на
# следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# &quot;Sum of all prime numbers is: {prime numbers sum}&quot;
# &quot;Sum of all non prime numbers is: {nonprime numbers sum}&quot;
num = input()
sum_prime = 0
sum_non_prime = 0
print()
while not num == "stop":
    num = int(num)
    if num >= 0:
        for i in range(2, num):
            if (num % i) == 0:
                sum_non_prime += num
                break
        else:
            sum_prime += num
    else:
        print("Number is negative.")

    num = input()
else:
    print(f"Sum of all prime numbers is: {sum_prime}")
    print(f"Sum of all non prime numbers is: {sum_non_prime}")

# 3
# 9
# 0
# 7
# 19
# 4
# stop

# 3
# 7
# 19
# stop

# 9
# stop

# 9
# 0
# 4
# stop

# -1
# stop

# 0
# stop

# -1
# -3
# 2
# 4
# stop
