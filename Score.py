from Utils import *
from os import path


# calculate the score before adding it to file
def calculate_score(difficulty):
    global new_score
    point_of_winning = int((difficulty * 3) + 5)
    scores_file = open(SCORES_FILE_NAME, "r")
    current_score = int(float(scores_file.readline()))
    scores_file.close()
    new_score = current_score + point_of_winning
    return new_score


# add the current score to the file
def add_score(difficulty):
    if path.exists(SCORES_FILE_NAME):
        new_score = calculate_score(difficulty)
        scores_file = open(SCORES_FILE_NAME, "w")
        scores_file.write(str(new_score))
    else:
        scores_file = open(SCORES_FILE_NAME, "w+")
        scores_file.write("0")
    scores_file.close()
