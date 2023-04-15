print("Task 1")
"""
A Person class

Make a class called Person. 
Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
"""
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and my age is {self.age}")

person = Person("Andrii", "Bolharov", 23)
person.talk()

print("\n")
print("Task 2")
"""
Doggy age
Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""
class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor

if __name__ == "__main__":
    dog = Dog(5)
    print(dog.human_age())

print("\n")
print("Task 3")
"""
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.
 

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, N):
        self.current_channel_index = N - 1
        return self.current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, channel):
        return "Yes" if channel in self.channels else "No"


if __name__ == "__main__":
    channels = ['Stb', 'NoviiKanal', 'Inter', 'Rada']
    controller = TVController(channels)

controller.first_channel()
print("First chanel:", controller.first_channel())
controller.last_channel()
print("Last channel:", controller.last_channel())
controller.turn_channel(3)
print("Turn channel:", controller.turn_channel(3))
controller.next_channel()
print("Next channel:", controller.next_channel())
controller.previous_channel()
print("Previous channel:", controller.previous_channel())
controller.current_channel()
print("Current channel:", controller.current_channel())
controller.is_exist(6)
print(controller.is_exist(6))
controller.is_exist("Rada")
print(controller.is_exist("Rada"))

