import requests, Live

roulette_game_difficulty = -1
user_number_input = -1
generated_interval = -1
curr_value = -1

def get_money_interval():
    """Will get the current currency rate from USD to ILS and will generate an interval as follows:
        a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d)"""

    global generated_interval
    global curr_value
    try:
        # Where USD is the base currency you want to use
        url = 'https://v6.exchangerate-api.com/v6/2345b5f4a35e7eb2963f7801/latest/USD'
        # Making our request
        response = requests.get(url)
        data = response.json()
        curr_value = data['conversion_rates']['ILS'].__round__(2)
        generated_interval = ((curr_value - (5 - roulette_game_difficulty)).__round__(2), (curr_value + (5 - roulette_game_difficulty)).__round__(2))
    except:
        print('Failed to get the current currency rate from USD to ILS')
        exit()
    return

def get_guess_from_user():
    global user_number_input
    """A method to prompt a guess from the user to enter a guess of value to a given amount of USD"""
    user_number_input = Live.get_float_input(1, 100, f'Guess the current currency rate from USD to ILS from 1 to 100\n')
    return

def play():
    """Will call the functions above and play the game. Will return True / False if the user lost or won."""
    get_money_interval()
    get_guess_from_user()
    if generated_interval[0] <= user_number_input <= generated_interval[1]:
        print(f'You WON! You guessed right, the exact current currency rate from USD to ILS is {curr_value}')
        return True
    print(f'You LOST! You have not guessed right, the exact current currency rate from USD to ILS is {curr_value}')
    return False