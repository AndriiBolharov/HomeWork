print("Task 1")
"""
Make a class structure in python representing people at school. 
Make a base class called Person, a class called Student, and another one called Teacher. 
Try to find as many methods and attributes as you can which belong to different classes, 
and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available to the teacher. 
"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender


class Student(Person):
    def __init__(self, name, age, gender, student_, grade):
        super().__init__(name, age, gender)
        self.student_ = student_
        self.grade = grade
    def get_student(self):
        return self.student_
    def get_grade(self):
        return self.grade


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_, subject, salary):
        super().__init__(name, age, gender)
        self.teacher_ = teacher_
        self.subject = subject
        self.salary = salary
    def get_teacher_(self):
        return self.teacher_
    def get_subject(self):
        return self.subject
    def get_salary(self):
        return self.salary

person1 = Person("John Doe", 25, "male")
print(person1.get_name())
print(person1.get_age())
print(person1.get_gender())
print("\n")

student1 = Student("Jane Smith", 18, "female", "12345", 11)
print(student1.get_name())
print(student1.get_age())
print(student1.get_gender())
print(student1.get_grade())
print("\n")

teacher1 = Teacher("Mr. Johnson", 40, "male", "98765", "Math", 50000)
print(teacher1.get_name())
print(teacher1.get_age())
print(teacher1.get_salary())
print(teacher1.get_subject())
print("\n")



print("Task 2")
"""
Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""
class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(dates):
        return [date for date in dates if (date % 4 == 0 and date % 100 != 0)]


if __name__ == "__main__":
    m = Mathematician()
    assert m.square_nums([1, 2, 3, -4, 5]) == [1, 4, 9, 16, 25]
    assert m.remove_positives([5, 7, 12, -15, 2]) == [-15]
    assert m.filter_leaps([1996, 1995, 2000, 2002, 2008]) == [2000]

print("\n")
print("Task 3")
"""
Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product
 with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - 
 adds a discount for all products specified by input identifiers (type or name). 
 The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, 
 in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""

