from Utils import scores_file_name
points_of_winning = 0

def read_score_from_file():
    """
    Try to read from scores file
    :return: file object and current score if file exists
    """
    file = open(scores_file_name, 'r+')
    first_line = file.readline()
    current_score = int(first_line)
    return file, current_score


def add_score(difficulty):
    """
    The function’s input is a variable called difficulty. The function will try to read
    the current score in the scores file, if it fails it will create a new one and will use it to save
    the current score.
    :return:
    """
    global points_of_winning

    # Write score to file
    try:
        file, current_score = read_score_from_file()
        new_score = current_score + (difficulty * 3) + 5
        file.seek(0)
        file.write(str(new_score))
        file.truncate()
    except FileNotFoundError:
        # Create file
        file = open(scores_file_name, 'w+')
        new_score = (difficulty * 3) + 5
        file.write(str(new_score))
    except:
        print(f'Failed to create scores file - {scores_file_name}')
        exit()
    points_of_winning = new_score
    print(f'Score updated to {new_score}')