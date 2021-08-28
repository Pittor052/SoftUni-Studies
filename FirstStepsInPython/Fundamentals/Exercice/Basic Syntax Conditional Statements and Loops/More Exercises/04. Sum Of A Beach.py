import re
# # 01 solution with re.findall() with multiple values: findall(value|value|value, str) module is used to search for
# # “all” occurrences that match a given pattern
# # This solution may cause time limit penalty!
command = input()
# # | is used for separation between words. For more on separators go to file re.py line 59 for more info
print(len(re.findall(r"fish|sun|water|sand", command, flags=re.IGNORECASE)))

# # # 02 solution with re.findall() for each word searched
# command = input()
# lower_command = command.lower()
# ls1 = re.findall("fish", lower_command)
# ls2 = re.findall("sun", lower_command)
# ls3 = re.findall("water", lower_command)
# ls4 = re.findall("sand", lower_command)
# print(len(ls1 + ls2 + ls3 + ls4))
