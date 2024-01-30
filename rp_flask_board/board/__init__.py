from flask import Flask
from board import pages

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)
    return app