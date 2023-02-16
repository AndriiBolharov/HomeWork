print("task 1")
""" Make a program that has some sentence (a string) on input and returns a dict containing 
    all unique words as keys and the number of occurrences as values. 
"""
fruit_dic = {
    'apple': 10,
    'orange': 7,
    'banana': 6,
    'grape': 5
}
#Додаємо в словник lemon і отримуємо результат
fruit_dic.update({'lemon': 8})
print(fruit_dic)
print("\n")

print("task 2")
""" Compute the total price of the stock where the total price is 
    the sum of the price of an item multiplied by the quantity of this exact item.
"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#Обчислюємо кожну змінну
banana = 6 * 4
apple = 0 * 2
orange = 32 * 1.5
pear = 15 * 3
#Виводимо результат за допомогою print(складаємо результат обчислення кожної змінної)
print(banana + apple + orange + pear)
print("\n")

print("task 3")
""" Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j`
    is corresponding to `i` squared.
"""
#Знаходимо спочатку змінну i_tuple
i_tuple = []
for i in range(1, 11):
    i_tuple.append(i)
print(i_tuple)
#За допомогою i_tuple знаходимо j_tuple
j_tuple = []
for i in range(1, 11):
    j_tuple.append(i ** 2)  #Приводимо до ступіня
print(j_tuple)

print('\n')
#Після того як знайшли усі змінні, прінтимо ij_list
ij_list = (i_tuple, j_tuple)
print(ij_list)

print("\n")

print("task 4")
"""Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""
days_list = [':Monday', ':Tuesday', ':Wednesday', ':Thursday', ':Friday', ':Saturday', ':Sunday']
#Проводимо нумерацію кожного дня в day_list, після кожної ітерації додаємо +1 і потім print
for i, day in enumerate(days_list):
    days_list[i] = {day, i+1}
print(days_list)






