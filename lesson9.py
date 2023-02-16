print("task 1")
"""
    Write a function called oops that explicitly raises an IndexError exception when called.
    Then write another function that calls oops inside a try/except statement to catch the error. 
    What happens if you change oops to raise KeyError instead of IndexError?
"""
def oops():
    raise IndexError
def catch():
    try:
        oops()
    except IndexError:
        print('Find IndexError')

catch()
#Якщо ми змінимо oops() на KeyError замість IndexError, def catch() буде виводити KeyError
print("\n")
print("Task 2")
def int_input():
    a = int(input("Введіть число: "))
    b = int(input("Введіть число: "))
    result = a ** 2 / b
    return print(result)

try:
    int_input()
except ValueError as v:
    print("Немає числа у рядку")
except ZeroDivisionError:
    print("На нуль ділите не можна")
