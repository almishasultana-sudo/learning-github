import random

secret_number = random.randint(1, 10)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Enter your guess: "))

print("Congratulations! You guessed correctly!")