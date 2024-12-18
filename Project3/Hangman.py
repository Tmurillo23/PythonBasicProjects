import random

HANGMAN_WORDS = ['Jackdaws', 'love', 'my', 'big', 'sphinx', 'of', 'quartz.']
FIGURA = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
          |
          |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ========''',

    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========'''
]


def select_word():
    return random.choice(HANGMAN_WORDS).upper()


def input_letter(guessed_letters):
    while True:
        letter = input("Enter a letter: ").upper()
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
        elif letter in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return letter


def main():
    print("Welcome to Hangman!")
    hangman_word = select_word()
    guessed_letters = set()
    correct_letters = set(hangman_word)
    tries_left = len(FIGURA) - 1
    current_state = ["_"] * len(hangman_word)

    while tries_left >= 0:
        print(FIGURA[len(FIGURA) - 1 - tries_left])
        print(" ".join(current_state))
        print(f"Tries left: {tries_left}")

        if "_" not in current_state:
            print("Congratulations! You guessed the word!")
            break

        letter = input_letter(guessed_letters)
        guessed_letters.add(letter)

        if letter in correct_letters:
            print(f"Good guess! '{letter}' is in the word.")
            for i, char in enumerate(hangman_word):
                if char == letter:
                    current_state[i] = letter
        else:
            print(f"Wrong guess! '{letter}' is not in the word.")
            tries_left -= 1

        if tries_left < 0:
            print(FIGURA[-1])
            print(f"You've been hanged! The word was '{hangman_word}'.")
            break


main()
