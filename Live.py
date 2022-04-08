from flask import render_template

import MemoryGame, GuessGame, CurrencyRouletteGame, Score

choose_game_output = 'Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and ' \
                   'you have to\nguess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. ' \
                   'Currency Roulette - try and guess the value of a random amount of USD in ILS\n' \
                   'Type "-1" to exit game\n'
select_difficulty_output = 'Please choose game difficulty from 1 to 5:\n'
game_id = 0
game_difficulty = 0

def welcome(name):
    return render_template('welcome.html')
    # print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')
    # return

def load_game_web(game_id_=None,game_difficulty_=None):
    is_won = False
    print(f'Selected game id: {game_id_} and game difficulty: {game_difficulty_}')
    if game_id_ == 1:
        MemoryGame.memory_game_difficulty = game_difficulty_
        is_won = MemoryGame.play()
    elif game_id_ == 2:
        GuessGame.guess_game_difficulty = game_difficulty_
        is_won = GuessGame.play()
    elif game_id_ == 3:
        CurrencyRouletteGame.roulette_game_difficulty = game_difficulty_
        is_won = CurrencyRouletteGame.play()
    if is_won:
        Score.add_score(game_difficulty_)
    return

# def load_game(game_id_=None,game_difficulty_=None):
#     global game_id, game_difficulty
#     is_won = False
#     while True:
#         if not game_id_:
#             game_id = get_integer_input(-1, 3, choose_game_output)
#         if not game_difficulty_:
#             game_difficulty = get_integer_input(1, 5, select_difficulty_output)
#         print(f'Selected game id: {game_id} and game difficulty: {game_difficulty}')
#         if game_id == 1:
#             MemoryGame.memory_game_difficulty = game_difficulty
#             is_won = MemoryGame.play()
#         elif game_id == 2:
#             GuessGame.guess_game_difficulty = game_difficulty
#             is_won = GuessGame.play()
#         elif game_id == 3:
#             CurrencyRouletteGame.roulette_game_difficulty = game_difficulty
#             is_won = CurrencyRouletteGame.play()
#         if is_won:
#             Score.add_score(game_difficulty)
#     return

def get_integer_input(from_number, to_number, message):
    while True:
        try:
            number = int(input(message))
            if number == -1:
                exit()
            elif number > to_number or number < from_number:
                raise Exception()
            break
        except SystemExit:
            exit()
        except Exception as e:
            print(f"That's not a valid option! Choose a number between {from_number} and {to_number}\n")
    return number

def get_float_input(from_number, to_number, message):
    while True:
        try:
            number = float(input(message))
            if number == -1:
                exit()
            elif number > to_number or number < from_number:
                raise Exception()
            break
        except SystemExit:
            exit()
        except:
            print(f"That's not a valid option! Choose a number between {from_number} and {to_number}\n")
    return number