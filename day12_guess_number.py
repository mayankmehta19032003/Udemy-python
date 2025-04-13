import random

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.choice(range(1,100))
easy = 10
hard = 5


if dificulty == "easy":
    while easy > 0:
        print(f"You have {easy} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if number == guess:
            print(f"You got it! The answer was {number}.")
            break
        elif number > guess:
            print("Too Low.")
            easy -= 1
        else:
            print("Too High.")
            easy -= 1
else:
    while hard > 0:
        print(f"You have {hard} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if number == guess:
            print(f"You got it! The answer was {number}.")
            break
        elif number > guess:
            print("Too Low.")
            hard -= 1
        else:
            print("Too High.")
            hard -= 1