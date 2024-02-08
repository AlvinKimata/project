import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='postgres',
                            password='root')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books');

    books = cur.fetchall()
    print(f"Books are: {books}")
    cur.close()
    conn.close()
    return render_template('index.html', books = books)

@app.route('/create/', methods = ('GET', 'POST'))
def create():
    return render_template('create.html')
