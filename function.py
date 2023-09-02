#LAMBDA
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))
# Add 10 to argument a, and return the result:

# Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#ARRAYS
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]


# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


