from turtle import Screen


def get_mouse_click_dimensions(x, y):
    print(f"x: {x}, y: {y}")


screen = Screen()
screen.onscreenclick(get_mouse_click_dimensions)
