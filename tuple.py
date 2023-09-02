# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# # Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
#print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
#print(len(thistuple))

#One item
thistuple = ("apple",)
#print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
#print(type(thistuple))

#The tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
#print(thistuple)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Change tuple values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#print(x)

#Add items to a tuple
#1
#Step 1:Convert the tuple into a list:
fruits = ("apple", "banana", "cherry")
y = list(fruits)

#Step 2: Add "orange" to the list
y.append("orange")

#Step 3: And convert it back into a tuple
fruits = tuple(y)

print(fruits)

#2
#Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)