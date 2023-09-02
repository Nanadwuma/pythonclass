#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Upper case
a = "Hello, World!"
print(a.upper())

# Lower case
a = "Hello, World!"
print(a.lower())

#remove whitespace - strip
a = " Hello, World! "
print(a.strip())

#Replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split string
a = "Hello, World!"
print(a.split(","))

# Cant combine string and number.
# Use format to combine a string to a number
#string format
age = 33
txt =  "My name is Alex, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#indexing format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Boolean Values
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33

if b < a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Access list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.
#the first item is position 0,
#and note that the item in position 5 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.
#index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included


'''
language = "Python"
school = "freeCodeCamp"
print(f"I am learning {language} from {school}.")

num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")

num_one = 45
num_two = 53
print(f"The product of {num_one} and {num_two} is {num_one * num_two}.")

num = 87;
print(f"Is num even? {True if num%2==0 else False}")

num_three = 90
print(f"Is num_three even? {True if num_three%2 ==0 else False}")

age = 17
print(f"Is age even? {True if age%2 ==0 else False}")

author = "jane smith"
a_name = author.title()
print(f"This is a book by {a_name}.")

partner = "roland adjetu"
a_name = partner.title()
print(f"The Blue Skies account was qualified by partner {a_name} because they refused to pass the adjustments.")

partner = "roland adjetu"
print(f"The Blue Skies  acoount was qualified by partner {partner.title()} because they refused to pass the adjustments.")

tax = " seth kusi"
print(f"{tax.title()} is the tax consultant at Mazars")
'''   

# Dictionaries
cats = {"Tom":4, "Jerry":6, "TJ":1}

cats["Jack"] = 3
#print(cats)
#print(len(cats))
#del(cats["Tom"])
print(cats)


# Create a dictionary with Ints for keys and Boolean for values
ints_bools = {3:True, 5:False, 55:False, 18:True}


#FUNCTIONS
def bark():
  print("Woof woof!!!")
  print("Hey!! Becareful. That is a dog")
#bark()

for x in range(10):
  bark()

#Parameters
def numbers_cal(num1, num2):
  #print(num1 / num2)
   print(num1 * num2) 
   print(num2 + num1)
   print(num2 * num1)

numbers_cal(5,2)


# Create a function called dog_info that takes a dog's age and name and prints out a sentence about the dog

def dog_info(age, name):
  print(f"Hi, my name is {name} and I am {age} years old.")

dog_info(7,"Jack")



#TUPLES
'''
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets.
'''

#MODULE

import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)


import mymodule as mx

a = mx.person1["age"]
print(a)
