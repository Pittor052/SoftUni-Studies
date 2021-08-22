user_name = str(input())
password = str(input())

while True:
    line = input()
    if line == password:
        print(f"Welcome {user_name}!")
        break