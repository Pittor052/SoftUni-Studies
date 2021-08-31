# # Dictionary Comprehension: https://www.programiz.com/python-programming/dictionary-comprehension
# # zip() Function: https://www.w3schools.com/python/ref_func_zip.asp
# # 01 solution
#
# k1 = input().split(", ")
# k2 = input().split(", ")
# dictionary = dict()
# for i in range(len(k1)):
#     dictionary[k1[i]] = k2[i]
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # 02 solution
#
# country, capitol = input().split(", "), input().split(", ")
# dictionary = {country[i]: capitol[i] for i in range(len(country))}
# for key, value in dictionary.items():
#     print(f"{key} -> {value}")
#
# # 03 solution
#
# country, capitol = input().split(", "), input().split(", ")
# for each in range(len(country)):
#     print(f"{country[each]} -> {capitol[each]}")
#
# # 04 solution
#
dictionary = dict(zip(input().split(", "), input().split(", ")))
for country, capitol in dictionary.items():
    print(f"{country} -> {capitol}")
