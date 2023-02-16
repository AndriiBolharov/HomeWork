"""Write a Python program to get the largest number from a list of random numbers with
 the length of 10.
 Constraints: use only while loop and random module to generate numbers
"""
print('task 1')
import random

a = []
while len(a) < 10:
    c = random.randint(0, 10)
    a.append(c)
s = max(a)
print(a, s)

print('\n')
"""Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list 
 containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers

"""
print('task 2')
import random

#Генеруємо a_list
a_list = []
while len(a_list) < 10:
    c = random.randint(0, 10)
    a_list.append(c)

#Генеруємо b_list
b_list = []
while len(b_list) < 10:
    c = random.randint(0, 10)
    b_list.append(c)

#Знаходимо set(a_list + b_list)
s = list(set(a_list + b_list))
print(s)

print('\n')
"""Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible 
by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
"""

print('task 3')

numbers = list(range(1, 101))
print(numbers)

results = []
for number in numbers:
    if number % 7 == 0 and number % 5 != 0:
        print(number)
        results.append(number)
    print(results)

