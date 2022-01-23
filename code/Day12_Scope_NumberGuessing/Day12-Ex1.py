# Guessing game
from random import randint


EASY_LEVEL = 10
HARD_LEVEL = 5


def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL
    else:
        print("Wrong difficulty name.")
        return -1


def check_guess(guess, answer):
    if guess < answer:
        print("Too low.\nGuess again.")
        return -1
    elif guess > answer:
        print("Too high.\nGuess again.")
        return 1
    else:
        print(f"You got it the answer was: {answer}")
        print("You Win!")
        return 0


def guess_number():
    game_continues = True
    attempts = 0
    answer = randint(1, 100)

    welcome()

    attempts = set_difficulty()
    if attempts == -1:
        return

    while game_continues:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result_guess = check_guess(guess, answer)
        if result_guess == 1 or result_guess == -1:
            attempts -= 1
        else:
            return
        if attempts == 0:
            print("You have no more attempts.")
            print("You Lose!")
            game_continues = False


guess_number()
