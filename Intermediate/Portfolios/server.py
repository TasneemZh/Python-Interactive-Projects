from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/formal")
def formal_cv():
    return render_template("formal.html")


@app.route("/informal")
def informal_cv():
    return render_template("informal.html")


if __name__ == "__main__":
    app.run(debug=True)
