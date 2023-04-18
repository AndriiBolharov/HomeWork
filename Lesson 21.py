print("task 1")
"""
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""
class Stack:
    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return len(self.item) == 0

sequence = input("Enter: ")

stack = Stack()

for it in sequence:
    stack.push(it)

print("Reversed sequence:", end=" ")
while not stack.is_empty():
    print(stack.pop(), end="")


print("\n")

print("task 2")
"""
Write a program that reads in a sequence of characters, 
and determines whether it's parentheses, braces, and curly brackets are "balanced."
"""
print("\n")

def is_balanced(sequence):
    stack = []
    for i in sequence:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            if i == '}' and stack[-1] == '{':
                stack.pop()
            if i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return not stack

sequence = input("Enter: ")
if is_balanced(sequence):
    print("Balanced")
else:
    print("Not balanced")

print("task 3")
"""
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. 
Consider the case in which the element is not found - raise ValueError with proper info Message
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_not_empty(self):
        return len(self.items)

    def get_stack(self, value):
        for i in range(len(self.items)):
            if self.items[i] == value:
                return self.items.pop(i)

        raise ValueError(f'{value} is not find')

stack = Stack()
stack.push(1)
stack.push(3)
stack.get_stack(3)
stack.get_stack(6)