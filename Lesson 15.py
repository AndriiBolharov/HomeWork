print("Task 1")
"""
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, 
and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, 
while Cat’s can be to print ‘meow’.

Also, create a simple generic function, 
which takes as input instance of a Cat or Dog classes and performs talk method on input parameter. 
"""
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("woof woof")

class Cat(Animal):
    def talk(self):
        print("meow")

def animal_talk(Animal):
    Animal.talk()

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

animal_talk(dog)
animal_talk(cat)

print("\n")
print("Task 2")
"""
Library

Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - 
returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""

class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"(Author {self.name})"

    def __str__(self):
        return self.name

class Book:
    total_book = 0
    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_book += 1

    def __repr__(self):
        return f"Book {self.name}, {self.year}, {self.author}"

    def __str__(self):
        return f"{self.name}, {self.year}, {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library {self.name}"

    def __str__(self):
        return {self.name}

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author) -> list:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]


library = Library("Golovna Biblioteka")

author1 = Author("Andrii", "Ukraine", "04.12.1999")
author2 = Author("Arthur", "England", "15.11.1998")
library.authors.extend([author1, author2])

book1 = Book("Daddy D", 2020, author1)
book2 = Book("Main country", 2020, author2)
library.books.extend([book1, book2])

print(library.group_by_author(author1))
print(library.group_by_author(author2))


print(library.group_by_year(2020))


print("\n")
print("Task 3")
"""
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) 
з належною перевіркою й обробкою помилок. 
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
"""
