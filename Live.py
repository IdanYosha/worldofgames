from MemoryGame import play1
from GuessGame import play2
from CurrencyRouletteGame import play3

game = ["You choose the Memory Game \n", "You choose the Guess Game \n", "You choose the Currency Roulette Game \n"]
diff = ["Difficulty chosen: Very easy \n", "Difficulty chosen: Easy \n", "Difficulty chosen: Normal \n",
        "Difficulty chosen: Hard \n", "Difficulty chosen: Very hard \n"]


def between(a, b, c):
    if a <= c <= b:
        return True
    else:
        print(f"Please enter a number between {a} and {b}. \n")


def welcome(name):
    name = str(input("Enter your name: "))
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play \n"


def load_game():
    while True:
        try:
            choose = int(input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear "
                               "for 1 second and you have to  guess it back \n 2. Guess Game - guess a number and see "
                               "if you chose like the computer \n 3. Currency Roulette - try and guess the value of a "
                               "random amount of USD in ILS \n Enter your choice here: "))
            range1 = between(1, 3, choose)
            if range1:
                print(game[int(choose) - 1])
                break
            raise ValueError()
        except ValueError:
            return load_game()
    while True:
        try:
            difficulty = int(input("Choose your difficulty: \n 1 - Very easy \n 2 - Easy \n 3 - Normal \n 4 - hard \n "
                                   "5 - Very hard \n Enter your choice here: "))
            range2 = between(1, 5, difficulty)
            if range2:
                print(diff[int(difficulty) - 1])
                if choose == 1:
                    play1(difficulty)
                if choose == 2:
                    play2(difficulty)
                if choose == 3:
                    play3(difficulty)
                break
            raise ValueError()
        except ValueError:
            continue
