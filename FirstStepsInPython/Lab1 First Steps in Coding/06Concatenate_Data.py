# Напишете програма, която прочита от конзолата име, фамилия, възраст и град и печата съобщение от
# следния вид: &quot;You are {first_name} {last_name}, a {age}-years old person from {town}.&quot;

first_name = input()
last_name = input()
age = int(input())
town = input()
print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")