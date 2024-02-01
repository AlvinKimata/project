from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello, world"


@app.route("/first_page")
def render_first_page():
    return render_template("first_page.html")

@app.route("/second_page")
def render_first_page():
    return render_template("second_page.html")