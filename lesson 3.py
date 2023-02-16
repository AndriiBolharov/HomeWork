#Task1
name = 'cloudysky'
if (len(name)) >= 2:
    print(name[0:2] + name[-2:]) #Якщо 2 або більше символи - друкує перші 2 та останні 2 літери
elif (len(name)) < 2:
    print('')                   #Якщо менше 2х літер - нічого не друкує

print('\n')

#Task2

#Перевіряємо, чи є у змінній літери
number = '0983420130'
if number.isdigit():
    print('contains only numbers')
else:
    print('contains not only numbers')

#Перевіряємо, cкільки символів у рядку
long = '1732449910'
if len(long) <= 10:
    print("true")
elif len(long)  > 10:
    print('false')
print('\n')

#Task3

#Перевіряємо правильність математичного виразу
expression = input("number: ")
if int(expression) < 15:
    print('false')
elif int(expression) >= 15:
    print('true')


print('\n')

#Task4
name = 'Andrii'
name1 = input("correct name: ")
if name.lower() == name1.lower() :    #Andrii == andriI
    print('That is correct')
else:
    print('that is not correct')

print('\n')

#Task5

#I was born in December
month = input("number of month: ")
if(int(month) <= 2 or int(month) == 12):     #1й, 2й та 12й місяці
    print("I was born in winter")
elif(int(month) >= 3 and int(month) <=5 ):   #3й, 4й та 5й місяці
    print('I was born in spring')
elif(int(month) >=6 and int(month) <=8):     #6й, 7й та 8й місяці
    print("I was born in summer")
elif(int(month) >=9 and int(month) <=11 ):   #9й, 10й та 11й місяці
    print("I was born in autumn")



