from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', utc_dt = datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')