print("Task 1")
"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!
"""
def arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@arguments
def add(a, b):
    return a + b

add(4, 5)

@arguments
def square_all(*args):
    return(arg ** 2 for arg in args)

square_all(4, 5)

print("\n")
print("Task 2")
"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def stop_words(words_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words_list:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(["and", "is", "not"])
def my_function():
    return "My name is Andrii and my name is not Serhii"

assert my_function() == "My name * Andrii * my name * * Serhii"

print("\n")
print("Task 3")
"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
"""
def arg_rules(max_length: int, type_: type, contains: list):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Аргумент {arg} не є типом {type_}")
                    return False
                if len(args) > max_length:
                    print(f"Довжина аргументу {arg} більше, ніж {max_length}")
                    return False
                for symbol in contains:
                    if symbol not in arg:
                        print(f"Аргумент {arg} не входить до {symbol}")
                        return False
            return func(*args)
        return wrapper
    return decorator

@arg_rules(max_length=15, type_=str, contains=['@', '.'])
def my_function(email: str):
    print(f"Received email: {email}")
    return True

my_function("john@example.com")
my_function("invalid_email")
my_function('123')
my_function("a" * 16)
