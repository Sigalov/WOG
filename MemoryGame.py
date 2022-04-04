import random, sys, time, Live

memory_game_difficulty = -1
user_list_input = []
random_list = []

def generate_sequence():
    random_list.clear()
    user_list_input.clear()
    """Will generate a list of random numbers between 1 and 101. The list length will be difficulty"""
    for i in range(0, memory_game_difficulty):
        n = random.randint(1, 101)
        random_list.append(n)

    print(random_list)
    # Remove the line after 0.7 sec
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    time.sleep(0.7)
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    return

def get_list_from_user():
    """Will return a list of numbers prompted from the user. The list length will be in the size of difficulty."""
    for i in range(0, memory_game_difficulty):
        user_number_input = Live.get_integer_input(1, 101, f'Get the {i} of {memory_game_difficulty} number between 1 and 101\n')
        user_list_input.append(user_number_input)
    print(f'Your numbers are: {user_list_input}')
    return

def is_list_equal():
    """A function to compare two lists if they are equal. The function will return True / False."""
    return sorted(random_list) == sorted(user_list_input)

def play():
    """Will call the functions above and play the game. Will return True / False if the user lost or won."""
    generate_sequence()
    get_list_from_user()
    if is_list_equal():
        print(f'You WON! You have remembered all the numbers')
        return True
    print(f'You LOST! You have not remembered all the numbers')
    print(f'The correct numbers are: {random_list}')
    return False