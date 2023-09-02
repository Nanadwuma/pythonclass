# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:
def greeting(name):
  print("Hello, " + name)

# Use a Module
# Now we can use the module we just created, by using the import statement:


# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
# Example
# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)


# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

import platform

x = dir(platform)
print(x)
