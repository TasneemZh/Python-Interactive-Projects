from menu import Menu
from coin import Coin
from resource import Resource

menu = Menu()
coin = Coin()
resource = Resource()


def run_the_shop():
    while True:
        user_drink = menu.handle_menu_question()
        if user_drink:
            not_enough = resource.check_shop_resources(user_drink)
            if not not_enough:
                user_coins = coin.handle_coins_question()
                in_dollars = coin.convert_coins_to_dollars(user_coins)
                operation_cancelled = coin.check_paid_price(in_dollars, user_drink)
                if not operation_cancelled:
                    resource.consume_shop_resources(user_drink)
                    print(f"Here is your {user_drink} 🍵. Enjoy!")


run_the_shop()
