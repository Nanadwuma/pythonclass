#Python Classes 
#Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. 
#A Class is like an object constructor, or a "blueprint" for creating objects.

''''
class Cat:
    info = "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."

print(Cat.info)
'''
# Excercise
# Create a class for something around your daily work
# Create a class variable inside the class


#class Data:
#   info = "A data lake is a centralized repository designed to store, process, and secure large amounts of structured, semistructured, and unstructured data. It can store data in its native format and process any variety of it, ignoring size limits."

#    def __init__(self): 
#     print("Its difference from data warehouse") 
#print(Data.info)

#class Square:
#    sides = 4

#print(Square.sides)




# INSTANCES or OBJECTS
#Data()
import random

class Cat:
    info = "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."

    def __init__(self, name):
        print("I am alive!!!")
        #print(random.randint(1,10))
        # create an instance variable
        self.lucky_number = random.randint(1,10)
        self.name = name

cat1 = Cat("Sash Miaw")
cat2 = Cat("Micky Miaw")

print(cat1.lucky_number)
print(cat2.lucky_number)

print(cat1.name)
print(cat2.name)



#Exercise
#What ever your class was in the first exercise,
#make an instance of it and and add an instance variable to it.
 

 #sample 1

import random

class Data:
   
   lake = "A data lake is a centralized repository designed to store, process, and secure large amounts of structured, semistructured, and unstructured data. It can store data in its native format and process any variety of it, ignoring size limits."
   
   def __init__(self, name): 
     print("Its difference from data warehouse") 
     self.lucky_number = random.randint(1,10)
     self.name = name


data1 = Data("Mart")
data2 = Data("Warehouse")

print(data1.lucky_number)
print(data2.lucky_number)

print(data1.name)
print(data2.name)

#sample 2
class Square:
   sides = 4

my_shape= Square()
my_shape.height = 10
my_shape.lenght = 34


print(my_shape.height)
print(my_shape.lenght)


#METHODS
# A method is a function inside a class

 # INHERITANCE

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


# Add Properties
# Example
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
#Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


# Add Methods
# Example. Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
