#variables are of types
#string: str
#numbers: int, float, complex
#Boolean: bool (true/false)
#sequence type: list, tuple, range


holiday = "25 july"
name = "Nana Daniel"
print(holiday)
print(name)

#numbers
int
one = 1
two_float  = 1.2
print(one+two_float)    
name = ("nana", "joe", " emma", "joy", "mary")
age = (5,18,23,12,56)
print(name + age)
x, y, z = ("nana", "john", "eric")
print(x)
print(y)
print(z)
x = y = z = ("Nana")
print(x)
print(y)
print(z)
            #Unpacking
fruits = ["apple", "banana", "orange"]
print(fruits)
#One value to many variables
x = y = z = 'orange'
print(x)
print(y)
print(z)
#Many variables to multiple values
x = y = z = 'apple', 'grapes', 'orange'
print(x)
print(y)
print(z)
#Global keyword
def myfunc():
    global x
x = "Nana"
# myfunc()
print("----->  My name is",  myfunc())
#Data types
x = 5
print(type(x))
x = "Hello World"
x = 20
x = 2.5
x = ['apple', 'ball', 'pearl']
print(type(x))
y = 13.7
print(type(y))
b = range (6)
print(type(b))
k = {'apple', 'ball', 'pearl'}
print("---->", type(k))
#looping in strings
#for x in "nana":
 #   print(x)

"""
t = '''The company is affiliated to a Foundation (Blue Skies Foundation)
    that implements corporate social responsibility activities on behalf 
    of the group of companies in Ghana.'''
#"""
t ='''The company is affiliated to a Foundation (Blue Skies Foundation)
    that implements corporate social responsibility activities on behalf 
    of the group of companies in Ghana.'''
print(t)

list = [1, 2, "d", 1.2]
tuple = (1, 2, "d", 1.2)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

name = "Mawulorm Yao"
account_number = "1023 1245 1256 3256"
if "Yao" in name:
    print("Login")  
print(len(name))
print(name[2:3])
print(account_number[:4])

user_input = "1254"

'''
1, get account number
2. get user input
3. compare user input to 1st 4 character of the account bumber 
4. print login if true
5. print try again if false
'''
# slicing
account_number = "1122 1245 1256 3256"
user_input = "1122"
print("---------", user_input==account_number[:4])

# if (condition) esle ... stattement
if (user_input==account_number[:4]):
   print("Login")
else:
   print("try again!!")


# print(list(range(4)))


