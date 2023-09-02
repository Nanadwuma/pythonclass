# Number Guessing Game
# Create a code to pick a random number between 1 and 100
# The user will try and guess it, each time they guess;
# Give a clue on the guess for example Hey!, You've got to guess higher or lower or give them a clue
# Introducing timimg to pause the sequene to bring life to the game



import random
import time 

#print("Hi! Welcome to the guessing game. Please guess a number between 1 and 100.")
print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(2)

print("Picking a number...")
time.sleep(2)

guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
     guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
    else:
     guess = int(input("Wrong. You need to guess lower. What is your guess?: "))
time.sleep(1)

print(f"Congrats!!! The right answer was {correct_number}. It took you {guess_count} guesses. ")
