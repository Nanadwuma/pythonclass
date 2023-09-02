    # Fortune Number
# 1. create a fortune statement for the user and give the user a lucky number
# 2. lucky number is a random number (lucky number changes anytime you run the code) --->import a module  ---> random
# 3. create 3 different fortunes
'''first fortune: You will have a great day!
second fortune: Today will be tough...but worth it
third fortune: You will graduate this year'''
# 4. use f string to print the outcomeimport random



import random 
lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = " "

if fortune_number == 1:
    fortune_text = "You will have a great day!"
if fortune_number == 2:
    fortune_text = "Today will be tough...but it is worth it!"
if fortune_number == 3:
    fortune_text = "You will graduate this year!"
print(f"{fortune_text} Your lucky number is:{lucky_number}")


