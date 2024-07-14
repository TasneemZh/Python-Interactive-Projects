import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_user_gender(name):
    params = {
        "name": name
    }
    response = requests.get("https://api.genderize.io", params=params)
    response.raise_for_status()
    return response.json()["gender"]


def get_user_age(name):
    params = {
        "name": name
    }
    response = requests.get("https://api.agify.io", params=params)
    response.raise_for_status()
    return response.json()["age"]


@app.route("/guess/<name>")
def root(name):
    gender = get_user_gender(name)
    age = get_user_age(name)
    return render_template("index.html", name=name.title(), gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
