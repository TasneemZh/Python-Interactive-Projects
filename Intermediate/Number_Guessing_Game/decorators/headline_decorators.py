from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def make_text_bold():
        return f"<b>{function()}</b>"
    return make_text_bold


def make_emphasis(function):
    def make_text_emphasis():
        return f"<em>{function()}</em>"
    return make_text_emphasis


def make_underlined(function):
    def make_text_underlined():
        return f"<u>{function()}</u>"
    return make_text_underlined


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def homepage():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
