import random

def guess_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)
    return word

def main():
    name = input("What is your name? ")
    print(f"Hello {name}. Good luck!")
    max_guesses = 5
    failed = 0
    word = guess_word()
    print(f"You have {max_guesses} guesses left.")
    while failed < max_guesses:
        guess = input("Guess the word: ")
        if guess == word:
            print("Good job! You got it!")
            break
        else:
            failed += 1
            print(f"Sorry, that's wrong. Try again.")
        if failed == max_guesses:
            print("You lose! The word was", word)
            input("Want to play again?. Write Yes or No:  ")
            if input() == "Yes":
                failed = 0
                continue
            else:
                print("Thank you for playing!")
                break

main()