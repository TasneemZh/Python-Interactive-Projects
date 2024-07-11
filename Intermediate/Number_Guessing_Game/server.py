from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)


def decorate_result(function):
    def decorate_random_result(*args):
        return (f'<h1 style="color:{args[0]};">{args[1]}</h1>'
                f'<iframe src={args[2]} width="30%" height="30%" '
                'style="position:absolute" frameBorder="0"></iframe>')

    return decorate_random_result


@decorate_result
def format_response(text_color, text_resp, gift_img):
    pass


@app.route("/reset")
def homepage():
    global random_number
    text_color = "purple"
    text_resp = "Guess a number from 0 to 9"
    gift_img = "https://giphy.com/embed/z1HdiobjzYIrm"
    random_number = random.randint(0, 9)
    return format_response(text_color, text_resp, gift_img)


@app.route("/<int:user_number>")
def user_guess(user_number):
    if user_number == random_number:
        text_color = "green"
        text_resp = "You guessed the right number!"
        gift_img = "https://giphy.com/embed/1YeLBMkZojP2ESn5eb"
    elif user_number < random_number:
        text_color = "blue"
        text_resp = "Too low! Try again..."
        gift_img = "https://giphy.com/embed/w89ak63KNl0nJl80ig"
    else:
        text_color = "red"
        text_resp = "Too high! Try again..."
        gift_img = "https://giphy.com/embed/KpSrCxhoZQWjJVVnrd"
    return format_response(text_color, text_resp, gift_img)


if __name__ == "__main__":
    app.run(debug=True)
