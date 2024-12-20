'''Implement your solution in this file.
Make sure that you decompose your solution into appropriate 
functions and that you include appropriate documentation.'''

import random
import string

def load_words():
    """Load the list of words from the file 'words.txt'"""
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: words.txt file not found!")
        return []

def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)

def is_word_guessed(secret_word, letters_guessed):
    """Check if the word is completely guessed."""
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    """Return the guessed word with unguessed letters replaced by '_'."""
    return ''.join([letter if letter in letters_guessed else '_' for letter in secret_word])

def get_available_letters(letters_guessed):
    """Return the list of letters not yet guessed."""
    return ''.join([letter for letter in string.ascii_lowercase if letter not in letters_guessed])

def hangman():
    """Run the Hangman game."""
    word_list = load_words()
    if not word_list:
        return

    secret_word = choose_word(word_list)
    letters_guessed = []
    guesses_remaining = 10
    warnings_remaining = 3

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings.")

    while guesses_remaining > 0:
        print("-" * 20)
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha():
            warnings_remaining -= 1
            if warnings_remaining < 0:
                guesses_remaining -= 1
                print("Oops! That's not a valid letter. You have no warnings left, so you lose one guess.")
            else:
                print(f"Oops! That's not a valid letter. You have {warnings_remaining} warnings left.")
            continue

        if guess in letters_guessed:
            warnings_remaining -= 1
            if warnings_remaining < 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess.")
            else:
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if guess in 'aeiou':
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):
            print("-" * 20)
            print("Congratulations, you won!")
            score = guesses_remaining * len(secret_word)
            print(f"Your total score for this game is: {score}")
            return

    print("-" * 20)
    print(f"Sorry, you ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
