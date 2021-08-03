import random
from Score import add_score


def play2(difficulty):
    print("Welcome to the Guess Game \n")
    secret_number = random.randint(1, difficulty)
    promt_number = int(input(f"Guess a number between 1 and {difficulty + 1}: "))

    def between(promt_number, difficulty):
        if 1 <= promt_number <= difficulty:
            return True
        else:
            print(f"Please enter a number between 1 and {difficulty + 1}. \n")

    def get_guess_from_user():
        while True:
            try:
                range1 = between(promt_number, difficulty + 1)
                if range1 == True:
                    return promt_number
                raise ValueError()
            except ValueError:
                return get_guess_from_user()

    def compare_results():
        if secret_number == promt_number:
            return True
        else:
            return False

    get_guess_from_user()
    c = compare_results()
    if c == True:
        print("You guessed right!")
        add_score(difficulty)
    else:
        print("You guessed wrong")
