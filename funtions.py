# funtion/method: is a block of code that run when it is called
# all functions have a name
# a funtion can be delcared with arguments
# a function can receive data called parametes
# a function can return a result or no result: a funtion returns result(data) with the the keyword return

def function_name():
    "actions to perform"
    pass

def show_message():
    print("I am called to show message")

# show_message()

def add_numbers():
    result = 2+5
    return result
    # print(result)

# declaring a funtion with arguments
# number1 is the argument of this funtion
def add(number1):
    pass

#  a funtion with many arguments
def add(number1, number2, number3):
    pass

# eg funtion to buy bread
def buy_bread(money, change):
    print(f"Kofi, buy a {money} cedis bread and bring a change of {change}")

buy_bread(20, 5)

# print(add_numbers() - 2)




#PRACTICE
#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


#Return Values
def my_function(x):
  return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print(5/0)

def subtract(num1, num2):
   return num1-num2