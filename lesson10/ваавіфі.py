# a = "Andrii"
# b = "Wednesday"
# print(f"Good day, {a}! {b} is a good day to learn Python")
#
#
# c = "Andrii "
# d = "Bolharov"
# f = c + d
# print(f"Hello, {f}")
# a = 1
# b = 2
# add = a + b
# print(add)
# a1 = 2
# b1 = 1
# sub = a1 - b1
# print(sub)
# a2 = 5
# b2 = 5
# div = a2 - b2
# print(div)
# a3 = 2
# b3 = 2
# mul = a3 + b3
# print(mul)
# a4 = 10
# b4 = 4
# mod = a4 % b4
# print(mod)
# a5 = 11
# b5 = 3
# floor = a5 // b5
# print(floor)

# name = "expensive"
# if len(name) > 2:
#     print(name[0:2] + name[-2:])
# elif len(name) < 2:
# #     print("")


# long = "1732449910"
# number = "9834201300"
# if len(long) or number.isdigit() >= 10:
#     print("Правильна довжина")
# else:
#     print("Помилка")

# a = input("Назвіть число: ")
# # if int(a) >= 10:
# #     print("True")
# # elif int(a) < 10:
# #     print("False")

# a = "andrii"
# b = "aNDRii"
# if a.lower() == b.lower():
#     print("Andrii")
# else:
#     print("Error")

def add_five(x):
    return x + 5

def do_twice(f):
    def resulting_func(x):
        return f(f(x))
    return resulting_func

result = do_twice(add_five)
print(result(1))