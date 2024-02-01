from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello, world"


@app.route("/first_page")
def render_first_page():
    return render_template("first_page.html")

@app.route("/second_page")
def render_second_page():
    return render_template("second_page.html")

@app.route("/jinja2")
def render_jinja2_intro():
    return render_template(
        "jinja2-intro.html", name = "John Doe",
        template_name = "Jinja2")