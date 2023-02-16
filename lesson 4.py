print('Task in classroom')
N = int(input('enter number: '))
A = int(input('enter number: '))
B = int(input('enter number: '))
for i in range(1, N):

 if i % A == 0 and i % B == 0:
    print('Бінго')
    break 
 if i % A == 0:
     print(f'кратне {i}  лише А')
 if i % B == 0:
     print(f'кратне {i} лише B')


print('\n')
print('Task 1')
print('\n')

import random
x = int(input('Choose number from 1 to 10: '))
if x > 10:
    print('not correct')
elif x <= 10:
    print('correct')


print('\n')

print('Task 2')
print('\n')
name  = input('Whats your name?: ')
age  = int(input('How old are you?: '))
print(f"Hello, {name}. On your next birthday you will be {age+1} years")

print('\n')
print('Task 3')
print('\n')
import random
random_word = input('Please enter a word with 5 or more letters: ')

i = 0
new_word1 = ''
new_word2 = ''
new_word3 = ''
new_word4 = ''
new_word5 = ''

if len(random_word) >= 5:
 while i != len(random_word):
    i += 1
    new_word1 = new_word1 + random.choice(random_word)
    new_word2 = new_word2 + random.choice(random_word)
    new_word3 = new_word3 + random.choice(random_word)
    new_word4 = new_word4 + random.choice(random_word)
    new_word5 = new_word5 + random.choice(random_word)
 print('"' + new_word1, new_word2, new_word3, new_word4, new_word5, sep='","', end='"')
else:
     print('5 or more letters')
