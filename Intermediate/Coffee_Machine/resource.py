from constants import MENU


class Resource:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }

    @staticmethod
    def check_shop_resources(user_drink):
        ingredients = MENU[user_drink]["ingredients"]
        for key in ingredients:
            if Resource.resources[key] - ingredients[key] < 0:
                print(f"Sorry there is not enough {key}.")
                return True
        return False

    @staticmethod
    def consume_shop_resources(user_drink):
        ingredients = MENU[user_drink]["ingredients"]
        for key in ingredients:
            Resource.resources[key] = Resource.resources[key] - ingredients[key]
