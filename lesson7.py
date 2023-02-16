print("task 1")
"""A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
The function should then print “My favorite movie is named {name}”.
"""
#Створили функцію favorite_movie
def favorite_movie(movie):
    print("My favorite movie is named" + " " + movie)
#Через прінт виводимо назву улюбленого фільму
favorite_movie("Home Alone")
print("\n")

print("task 2")
"""Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""
#Створили функцію make_country і виводимо назву країни і її столицю
def make_country(country, capital):
    print(f"{country} - name of country, {capital} - capital in this country")
make_country("Ukraine", "Kyiv")
#Створили словник, в якому назва країни(ключ), а столиця(параметр) і виводимо
make_capital = {
    "Ukraine": "Kyiv"
}
print(make_capital)
print("\n")

print("task 3")
"""Create a function called make_operation, which takes in a simple arithmetic operator 
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. 
For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
"""
#Створили функцію і нам потрібно повернути число 16, використовуючі дані, які в нас є
def make_operation1(a, x, y, z):
    return  x + y + z
print(make_operation1('+', 7, 7, 2))
#Створили функцію і нам потрібно повернути число 30, використовуючі дані, які в нас є
def make_operation2(b, c, d, e, f):
    return c - d - e - f
print(make_operation2('-', 5, 5, -10, -20))
#Створили функцію і нам потрібно повернути число 42, використовуючі дані, які в нас є
def make_operation3(g, i, k):
    return i * k
print(make_operation3('*', 7, 6))
print("\n")





