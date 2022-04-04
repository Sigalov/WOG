import random
import Live

guess_game_difficulty = -1
secret_number = -1

def generate_number():
    """Will generate number between 1 to difficulty and save it to secret_number."""
    global secret_number
    secret_number = random.randint(1, guess_game_difficulty)
    return

def get_guess_from_user():
    """Will prompt the user for a number between 1 to difficulty and return the number."""
    return Live.get_integer_input(1, guess_game_difficulty, f'Guess a number between 1 to {guess_game_difficulty}\n')

def compare_results():
    """Will compare the secret generated number to the one prompted by the get_guess_from_user."""
    if secret_number == get_guess_from_user():
        print(f'You WON!')
        return True
    print(f'You LOST! The secret number was {secret_number}')
    return False

def play():
    """Will call the functions above and play the game. Will return True / False if the user lost or won."""
    generate_number()
    return compare_results()