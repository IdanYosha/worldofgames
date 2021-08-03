import random
import time
from Score import add_score


randomlist = []
userlist = []


def play1(difficulty):
    print("Welcome to the Memory Game \n")

    def generate_sequence():
        for i in range(0, difficulty):
            n = random.randint(1, 101)
            randomlist.append(n)
            randomlist.sort()
        print(randomlist, end="")
        time.sleep(0.7)
        print("\r"" ")

    def get_list_from_user():
        print(f"Enter the right numbers of the list ")
        for i in range(0, difficulty):
            userenter = int(input(f"Enter your next number: "))
            userlist.append(userenter)

    def is_list_equal():
        if randomlist == userlist:
            return True
        else:
            return False

    generate_sequence()
    get_list_from_user()
    game = is_list_equal()
    if game:
        print(f"correct! the list was {randomlist}")
        add_score(difficulty)
    else:
        print(f"You lost! the list was {randomlist}")
