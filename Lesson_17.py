print("Task 1")
"""
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""
def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

animals = ["dog", "cat", "lion", "pig", "cock"]
for index, animal in with_index(animals, start=1):
    print(f"{index}: {animal}")


print("\n")
print("Task 2")
"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""
def in_range(start, end, step=1):
    index = start
    while index < end:
        yield index
        index += step

for index in range(0, 10, 2):
    print(index)


print("\n")
print("Task 3")
"""
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
"""
class MyIterable:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

iterable = MyIterable(10)
for index in iterable:
    print(index)
