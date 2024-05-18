from constants import MENU
from resource import Resource


class Menu:
    @staticmethod
    def handle_menu_question():
        shop_menu = ""
        for key in MENU:
            shop_menu += key + "/"
        user_drink = input(f"What would you like? ({shop_menu[:-1]}) ").lower()
        if user_drink == "report":
            front_unit = ""
            for key in Resource.resources:
                if key == 'water' or key == 'milk':
                    back_unit = "ml"
                elif key == "coffee":
                    back_unit = "g"
                else:
                    front_unit = "$"
                    back_unit = ""
                print(f"{key.title()}: {front_unit}{Resource.resources[key]}{back_unit}")
            return ""
        return user_drink

