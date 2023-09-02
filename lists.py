#Access list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

#This will return the items from position 2 to 5.
#the first item is position 0,
#and note that the item in position 5 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# define lists

'''
print( 10 + int('10'))
print(float(2.3), int(2.3))
'''

fruits = ["apple", "orange"]
quantity = [10, "10", True]

# print(len(fruits)) # count items in the list
# print(fruits[1]) # Access elements in the list using index i.e. thier positions 0 1 2 3 etc

# print(fruits)
# fruits.append("banana")
# print(fruits)

salaries = [100, 110, 20, 35]
year_bonus = 16
VAT = 4.5 # CONSTANT
# add 10 cedis to all staff salary
# for loop
# for element in list:
#     expression or statement

# For each employee salary, add a bonus of 10
# 1. get each salary -> loop over the list
# 2. add 10 to each salary and call it bonus_salaray
# 3. print the each salary - the bonus_salary using f-string


# print(f"Work --> {salaries} no good! boss")
for salary in salaries:
    # print(salary)
    bonus_salary = salary + year_bonus
    print(f"{salary} + {year_bonus} = {bonus_salary}")


# Assignment 2 
# In this mix list, print string or type of number, or Condition if identified
mix_list = ['apple', 'fish', 1, 5, 2.5,True]
print(type(mix_list))
print(str(mix_list))
print(bool(mix_list))
print(mix_list[2:5])
print(mix_list[-1])
print(mix_list[0:2])
if "fish" in mix_list:
   print("yes, fish is part of the list")

if 5 in mix_list:
    print("yes, 5 is part of the list and its an integer")

for apple in mix_list:
    print("aplle")

#for i in range(len(mix_list)): Not Callable
 #   print(mix_list(i))



library = ["Abat", "Basetet", "Dansey"]
print(len(library))
print(library[2])
print(library[-2])
print(type(library))
#library[0] = "Solo"

print(library[0:1])
print(library)
#library.append("Solo")
print(library)
#library.insert(2, "Terminator")
print(library)
new = ["Grounds", "Delete", "Surrogacy" ]
library.extend(new)
print(library)
#library.remove("Delete")
print(library)
library.pop(1)
#library.clear()
#print(library)
#library.sort(reverse = True)
#print(library)
library.sort()
print(library)
library_two = library.copy()
print(library_two)




# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

