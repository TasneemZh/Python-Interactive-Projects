from constants import COINS, MENU
from resource import Resource

class Coin:
    @staticmethod
    def handle_coins_question():
        print("Please insert the coins.")
        user_coins = []
        for key in COINS:
            user_coins.append(float(input(f"How many {key}? ")))
        return user_coins

    @staticmethod
    def convert_coins_to_dollars(user_coins):
        in_dollars = 0
        index = 0
        for key in COINS:
            in_dollars += COINS[key] * user_coins[index]
            index += 1
        return in_dollars

    @staticmethod
    def check_paid_price(in_dollars, user_drink):
        if MENU[user_drink]["cost"] > in_dollars:
            print("Sorry that's not enough money. Money refunded.")
            return True
        Resource.resources["money"] += MENU[user_drink]["cost"]
        user_change = round(in_dollars - MENU[user_drink]["cost"], 2)
        print(f"Here's ${user_change} in change.")
        return False
