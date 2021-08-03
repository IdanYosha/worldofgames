from currency_converter import CurrencyConverter
import random
from Score import add_score


def play3(difficulty):
    def get_money_interval():
        global current
        global number
        currency = CurrencyConverter()
        current = currency.convert(1, 'USD', 'ILS')
        number = random.randint(1, 100)

    def get_guess_from_user():
        user_number = float(input(f"How much is {number} in USD? "))
        a = between(difficulty, user_number)
        print(a)

    def between(difficulty, user_number):
        total = number * current
        print(f"${number} in ILS is {total} \n")
        if (total - (5 - difficulty)) <= user_number <= total + (5 - difficulty):
            add_score(difficulty)
            return True
        else:
            return False

    get_money_interval()
    get_guess_from_user()
