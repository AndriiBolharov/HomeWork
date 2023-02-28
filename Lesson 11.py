print("Task 1")
"""
Write a Python program to detect the number of local variables declared in a function.
"""
def func():
    a = 5
    b = 6
    c = 7
    print("Змінні")

print(func.__code__.co_nlocals)
print("\n")

print("Task 2")
"""
Write a Python program to access a function inside a function 
(Tips: use function, which returns another function)
"""
def add(a):
    def abc(b):
        nonlocal a
        a += 1
        return a+b
    return abc

ok = add(1)
print(ok(2))
print("\n")

print("Task 3")
"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one
"""

def choose_func(nums: list, positive_func, negative_func):
    if all(num > 0 for num in nums):
        return positive_func(nums)
    else:
        return negative_func(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 0, -7, -10, 5]
nums2 = [1, 2, -5, -4, 8]

result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)

assert choose_func(nums1, square_nums, remove_negatives) == [1, 5]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 2, 8]







