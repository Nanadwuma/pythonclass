#def add(x, y):
# Write my functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by 0, enter another number."
    return num1 / num2

# Prompt the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#your_number = int(input("What do you want to do? Select your operation from option 1 to 4: "))
your_number = int(input("Select operation from  1 to 4: "))

#num1 = (input("Enter first number: "))
#num2 = (input("Enter second number: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# trying writing the coswe below using match patern
if your_number == 1:
    result = add(num1, num2)
elif your_number == 2:
    result = subtract(num1, num2)
elif your_number == 3:
    result = multiply(num1, num2)
elif your_number == 4:
    result = divide(num1, num2)
else:
    result = "Invalid input"

print("Result:", result)