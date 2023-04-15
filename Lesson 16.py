print("Task 1")
"""
Create a class method named `validate`, 
which should be called from the `__init__` method to validate parameter email, passed to the constructor. 
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
"""
import re

class Validate:

    def __init__(self, validate_email: str):
        if not isinstance(validate_email, str):
            raise TypeError('Error type email!!!')

        if not re.match('\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', validate_email):
            raise TypeError('Error type email!!!')

        self.validate_email = validate_email


print("\n")
print("Task 2")
"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. 
You should implement a method that allows you to add workers to a Boss. 
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!

You can refactor the existing code.
"""
class Boss:
    def __init__(self, name):
        self.name = name
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
            worker.boss = self
        else:
            raise ValueError("Worker instance required")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, name, boss=None):
        self.name = name
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if value is None or isinstance(value, Boss):
            if self._boss != value:
                old_boss = self._boss
                self._boss = value
                if old_boss is not None:
                    old_boss.workers.remove(self)
                if value is not None:
                    value.add_worker(self)
        else:
            raise ValueError("Boss instance or None required")



print("\n")
print("Task 3")
"""
Write a class TypeDecorators 
which has several methods for converting results of functions to a specified type (if it's possible):

methods:

to_int

to_str

to_bool

to_float

Don't forget to use @wraps
"""
from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper
