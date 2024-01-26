from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name="Kimata")

@app.route('/your_url', methods=['GET', 'POST'])
def your_url():
    
    if request.method == 'POST':
        urls = {}
        urls[request.form['code']] == {'url': request.form['url']}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        code = request.form['code']
        return render_template('your_url.html', code=code)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
