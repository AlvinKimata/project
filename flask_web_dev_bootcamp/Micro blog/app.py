import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///weather.db"

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)

@app.route("/", methods = ["GET", "POST"])
def index():
    api_key = "1325dd373f3a1565484ec02597270807"
    lat = "36.8219"
    lon = "1.2921"
    url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"

    r = requests.get(url).json()
    weather = {
        "latitude": lat,
        'longitude': lon,
        "Temperature": r['main']['temp'],
        "description": r['weather'][0]['description'],
        "icon": r['weather'][0]['icon']
    }
    print(weather)
    # return render_template("weather.html")
