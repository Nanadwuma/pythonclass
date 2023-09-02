# SET
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}

#print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry"}
myset = {"apple", "banana", "cherry"}
print(len(thisset))
print(type(myset))

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("apple")

print(thisset)
#pop
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Clear
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#del
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# Loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Keep only duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

#Intersections
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)