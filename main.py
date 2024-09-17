"""THE HANGMAN PROJECT"""
'''
Pseudocode:
    0. Creating word bank, defining the HP number, and making the hangman ASCII.
    1. Defining the chosen word from word bank
        1.a. Changing every letter to '_' for display purpose
    2. Asking for user input
    3. Loop through for every letter in the word:
        3.a. Check if any letter are the same:
            3.a.a. If yes: replace the '_' to the letter guessed
                3.a.a.a. If there's no '_' remaining, player WINS
            3.a.b. If no: reduce the hit points.
                3.a.b.a. If there's no hit points left, plater LOSE
'''
import random
from game_data import word_bank, HANGMAN

# TODO 0: Define the chosen word from the word bank
keyword = random.choice(word_bank)
correct_letter = []
incorrect_guesses = []
hp = 6

game_is_on = True
while game_is_on:
    # TODO 1: Display the current word with underscores and guessed letters
    display = ''
    for letter in keyword:
        if letter in correct_letter:
            display += letter
        else:
            display += '_'

    # TODO 5: Check for win/lose conditions
    if '_' not in display:
        print('******************** You Won ********************')
        break
    elif hp == 0:
        print(f'******************** You Lose ********************')
        print(f'The correct word was: {keyword}')
        break

    # TODO 6: Print the current state of the game (with underscores)
    print(f"Correct Letter:\t\t{correct_letter}")
    print(f"Incorrect Letter:\t{incorrect_guesses}")
    print(display.strip())

    # TODO 2: Ask for user input
    guess = input("Guess a letter:\t").lower()

    # TODO 3: Check if the guessed letter is in the word
    if guess in keyword:
        correct_letter.append(guess)
    else:
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
            hp -= 1
            print(f"Incorrect! {hp} guesses left.")
        else:
            print(f"You've already guessed '{guess}'. Try another letter.")

    # TODO 4: Display hangman figure
    print(f"\n========= You Have {hp} Lives ==========")
    print(HANGMAN[6 - hp])
