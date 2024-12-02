import random
from math import log2
def UserInput():
    print("Welcome to Number Guessing Game!")
    print("Please enter a number, this will be the lower bound.")
    lower_bound = int(input("Lower bound: "))
    print("Please enter a number, this will be the upper bound.")
    upper_bound = int(input("Upper bound: "))
    return lower_bound, upper_bound

def GuessNumber(lower_bound, upper_bound):
    guess = random.randint(lower_bound, upper_bound)
    return guess

def UserGuess(lower_bound, upper_bound,guess):
    min_of_guessing = log2(upper_bound- lower_bound + 1)
    counter_of_guessing = 0
    while counter_of_guessing < min_of_guessing:
        counter_of_guessing += 1
        user_guess = int(input("Guess a number: "))
        if user_guess == guess:
            print("You win! Correct!")
            break
        elif counter_of_guessing >= min_of_guessing:
            print(f"You lose! the correct number is {guess}")
            break
        elif user_guess not in range(lower_bound, upper_bound+1):
            raise(ValueError("Guess not valid!"))
        elif user_guess < guess:
            print("Too low!")
        elif user_guess > guess:
            print("Too high!")




def main():
    lower_bound, upper_bound = UserInput()
    guess = GuessNumber(lower_bound, upper_bound)
    UserGuess(lower_bound, upper_bound, guess)


main()