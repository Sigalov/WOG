import platform, os

# A string representing a file name. By default, “Scores.txt”
scores_file_name    = 'Scores.txt'
# A number representing a bad return code for a function.
bad_return_code     = None

def screen_cleaner():
    """
    A function to clear the screen (useful when playing memory game or
    before a new game starts).
    :return: None
    """
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')